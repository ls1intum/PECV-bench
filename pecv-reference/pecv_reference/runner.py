from __future__ import annotations

import argparse
import json
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

try:  # pragma: no cover - optional dependency
    from langsmith import Client as LangsmithClient  # type: ignore[import]
except ImportError:  # pragma: no cover - optional dependency
    LangsmithClient = None  # type: ignore[assignment]

from pecv_reference.consistency_check.handler import ConsistencyCheck
from pecv_reference.consistency_check.models import (
    ConsistencyCheckRequest,
    ProgrammingLanguage,
    Repository,
    RepositoryFile,
)
from pecv_reference.settings import settings


if settings.is_langsmith_enabled and LangsmithClient is not None:
    langsmith_client = LangsmithClient()
else:
    langsmith_client = None


LLM_RUN_TYPES = {"llm", "chat", "chat_model"}


def safe_decimal(value: object) -> Decimal:
    if value is None or value == "":
        return Decimal("0")
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return Decimal("0")


def decimal_to_float(value: Decimal) -> float:
    quantized = value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    return float(quantized)


def aggregate_usage(runs) -> tuple[dict[str, int], dict[str, float]]:
    prompt_tokens = 0
    completion_tokens = 0
    prompt_cost = Decimal("0")
    completion_cost = Decimal("0")
    total_cost = Decimal("0")

    for run in runs:
        run_type = getattr(run, "run_type", None)
        if run_type not in LLM_RUN_TYPES:
            continue

        prompt_tokens += int(getattr(run, "prompt_tokens", 0) or 0)
        completion_tokens += int(getattr(run, "completion_tokens", 0) or 0)

        prompt_cost += safe_decimal(getattr(run, "prompt_cost", 0))
        completion_cost += safe_decimal(getattr(run, "completion_cost", 0))
        raw_total_cost = getattr(run, "total_cost", None)
        if raw_total_cost not in (None, "", 0):
            total_cost += safe_decimal(raw_total_cost)
        else:
            total_cost += safe_decimal(getattr(run, "prompt_cost", 0)) + safe_decimal(
                getattr(run, "completion_cost", 0)
            )

    tokens = {
        "prompt": prompt_tokens,
        "completion": completion_tokens,
        "total": prompt_tokens + completion_tokens,
    }

    cost = {
        "prompt_usd": decimal_to_float(prompt_cost),
        "completion_usd": decimal_to_float(completion_cost),
        "total_usd": decimal_to_float(total_cost),
    }

    return tokens, cost


def fetch_langsmith_usage(
    trace_id: str,
    project_name: str | None,
    timeout_s: float = 60.0,
    poll_interval_s: float = 2.0,
) -> tuple[dict[str, int], dict[str, float]]:
    if langsmith_client is None:
        return None, None
    deadline = time.monotonic() + timeout_s
    filter_expr = f'eq(trace_id, "{trace_id}")'
    last_error: Exception | None = None

    while time.monotonic() < deadline:
        try:
            runs_iter = langsmith_client.list_runs(
                project_name=project_name,
                filter=filter_expr,
                select=[
                    "id",
                    "run_type",
                    "prompt_tokens",
                    "completion_tokens",
                    "total_tokens",
                    "prompt_cost",
                    "completion_cost",
                    "total_cost",
                ],
            )
            runs = list(runs_iter)
        except Exception as exc:  # pragma: no cover - network
            last_error = exc
            time.sleep(poll_interval_s)
            continue

        if runs:
            tokens, cost = aggregate_usage(runs)
            return tokens, cost
        time.sleep(poll_interval_s)

    if last_error:
        print(
            f"Warning: unable to fetch LangSmith usage for trace {trace_id}: {last_error}",
            file=sys.stderr,
        )

    return None, None


def load_problem_statement(base_path: Path) -> str:
    for candidate in ("problem-statement.md", "problem_statement.md"):
        candidate_path = base_path / candidate
        if candidate_path.exists():
            return candidate_path.read_text(encoding="utf-8")
    raise FileNotFoundError(
        "Could not locate problem statement in "
        f"{base_path}. Expected one of: problem-statement.md, problem_statement.md"
    )


def load_repository_files(repo_path: Path) -> list[RepositoryFile]:
    if not repo_path.exists():
        return []

    files: list[RepositoryFile] = []
    for file_path in sorted(repo_path.rglob("*")):
        if not file_path.is_file():
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative_path = file_path.relative_to(repo_path)
        if any(part.startswith(".") for part in relative_path.parts):
            continue
        files.append(
            RepositoryFile(
                path=str(relative_path).replace(os.sep, "/"), content=content
            )
        )
    return files


def read_programming_language(start_path: Path) -> ProgrammingLanguage:
    details_path = start_path / "exercise-details.json"
    if not details_path.exists():
        raise FileNotFoundError(f"exercise-details.json not found under {start_path}")

    try:
        payload = json.loads(details_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Failed to parse programming language from {details_path}: {exc}"
        ) from exc

    language_raw = payload.get("programmingLanguage")
    if not language_raw:
        raise ValueError(
            f"Programming language missing in {details_path}. Expected 'programmingLanguage' field."
        )

    normalized = str(language_raw).strip().lower()
    if normalized == ProgrammingLanguage.JAVA.value:
        return ProgrammingLanguage.JAVA
    if normalized == ProgrammingLanguage.PYTHON.value:
        return ProgrammingLanguage.PYTHON

    raise ValueError(
        f"Unsupported programming language '{language_raw}' in {details_path}"
    )


def derive_case_id(input_path: Path) -> str:
    parts = list(input_path.resolve().parts)
    if "data" in parts:
        data_idx = parts.index("data")
        parts = parts[data_idx + 1 :]
    if "variants" in parts:
        variants_idx = parts.index("variants")
        parts = parts[:variants_idx] + parts[variants_idx + 1 :]
    if not parts:
        return input_path.name
    return Path(*parts).as_posix()


def resolve_output_file(path: Path) -> Path:
    if path.is_dir() or str(path).endswith(os.sep):
        return path / "result.json"
    if path.suffix:
        return path
    return path / "result.json"


def build_run_id(
    model_name: str, case_id: str, timestamp: datetime, reasoning_effort: str | None = None
) -> str:
    model_slug = model_name.replace(":", "-").replace("/", "-")
    if reasoning_effort:
        model_slug = f"{model_slug}-{reasoning_effort}"
    time_slug = timestamp.strftime("%Y-%m-%d-%H%M%S")
    suffix = case_id.split("/")[-1]
    random_part = uuid.uuid4().hex[:6]
    return f"{model_slug}-{time_slug}-{suffix}-{random_part}"


def format_timestamp(dt: datetime) -> str:
    return (
        dt.astimezone(timezone.utc)
        .replace(tzinfo=None)
        .strftime("%Y-%m-%dT%H:%M:%S.%f")
    )


def run_consistency_check(
    input_path: Path,
    output_path: Path,
    model_name: str,
    reasoning_effort: str,
    case_id: str | None = None,
    run_id: str | None = None,
) -> None:
    start_time = datetime.now(timezone.utc)
    resolved_case_id = case_id or derive_case_id(input_path)
    resolved_run_id = run_id or build_run_id(
        model_name, resolved_case_id, start_time, reasoning_effort
    )

    problem_statement = load_problem_statement(input_path)
    template_files = load_repository_files(input_path / "template")
    solution_files = load_repository_files(input_path / "solution")
    test_files = load_repository_files(input_path / "tests")

    if not template_files:
        raise RuntimeError(f"No template files found under {input_path / 'template'}")

    programming_language = read_programming_language(input_path)

    request = ConsistencyCheckRequest(
        problem_statement=problem_statement,
        template_repository=Repository(files=template_files),
        programming_language=programming_language,
        solution_repository=(
            Repository(files=solution_files) if solution_files else None
        ),
        test_repository=Repository(files=test_files) if test_files else None,
    )

    os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
    os.environ.setdefault("LANGCHAIN_PROJECT", "pecv-reference")
    os.environ["LANGCHAIN_RUN_ID"] = resolved_run_id

    checker = ConsistencyCheck(model=model_name, reasoning_effort=reasoning_effort)
    response = checker.check(request)

    finished_at = datetime.now(timezone.utc)
    response_data = response.model_dump()
    metadata = response_data.get("metadata", {})
    issues_payload = response_data.get("issues", [])

    tokens_summary = {"prompt": 0, "completion": 0, "total": 0}
    cost_summary = {
        "prompt_usd": 0.0,
        "completion_usd": 0.0,
        "total_usd": 0.0,
    }

    trace_id = metadata.get("trace_id")
    if trace_id:
        project_name = os.environ.get("LANGCHAIN_PROJECT")
        try:
            tokens_summary, cost_summary = fetch_langsmith_usage(
                trace_id=trace_id,
                project_name=project_name,
            )
        except Exception as exc:  # pragma: no cover - network
            print(
                f"Warning: failed to fetch LangSmith usage for trace {trace_id}: {exc}",
                file=sys.stderr,
            )

    result = {
        "case_id": resolved_case_id,
        "run_id": resolved_run_id,
        "timestamp": format_timestamp(finished_at),
        "issues": issues_payload,
        "timing": {
            "start_time": format_timestamp(start_time),
            "end_time": format_timestamp(finished_at),
            "duration_s": (finished_at - start_time).total_seconds(),
        },
        "trace_id": trace_id or "",
    }
    if tokens_summary:
        result["tokens"] = tokens_summary
    if cost_summary:
        result["cost"] = cost_summary

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the PECV consistency checker on a prepared variant"
    )
    parser.add_argument(
        "--input-path",
        type=Path,
        required=True,
        help="Path to the exercise variant directory",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        required=True,
        help="File or directory for the result JSON",
    )
    parser.add_argument(
        "--model",
        dest="model_name",
        default=None,
        help="Model identifier to use (fallbacks to MODEL_NAME from environment)",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["low", "medium", "high"],
        default="medium",
        help="Reasoning effort setting for the model",
    )
    parser.add_argument(
        "--case-id",
        dest="case_id",
        default=None,
        help="Override the case identifier used in the output JSON",
    )
    parser.add_argument(
        "--run-id",
        dest="run_id",
        default=None,
        help="Override the run identifier used in the output JSON",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    model_name = args.model_name or settings.MODEL_NAME
    if not model_name:
        parser.error(
            "Model must be provided via --model or MODEL_NAME environment variable"
        )

    output_file = resolve_output_file(args.output_path)

    try:
        run_consistency_check(
            input_path=args.input_path,
            output_path=output_file,
            model_name=model_name,
            reasoning_effort=args.reasoning_effort,
            case_id=args.case_id,
            run_id=args.run_id,
        )
    except Exception as exc:  # pragma: no cover - CLI error reporting
        parser.error(str(exc))

    return 0


if __name__ == "__main__":
    sys.exit(main())
