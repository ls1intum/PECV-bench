from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Tuple

from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import yaml  # type: ignore[import]
except ImportError:  # pragma: no cover - optional dependency
    yaml = None  # type: ignore[assignment]

from cli.commands.variants import VariantManager
from cli.utils import (
    CONFIGS_ROOT,
    ExerciseIdentifier,
    REFERENCE_ROOT,
    RESULTS_ROOT,
    RUNS_ROOT,
    iter_exercises,
)


DEFAULT_CONFIG = CONFIGS_ROOT / "pecv-reference.yaml"


def slugify(text: str) -> str:
    cleaned = re.sub(r"[\s/:]+", "-", text)
    cleaned = re.sub(r"[^A-Za-z0-9\-]+", "-", cleaned)
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "run"


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to parse approach configuration. "
            "Please install PyYAML."
        )
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def parse_bool(value: str) -> bool:
    normalised = value.strip().lower()
    if normalised in {"true", "1", "yes", "on"}:
        return True
    if normalised in {"false", "0", "no", "off"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected boolean value, got '{value}'")


def load_resume_metadata(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Run metadata file not found: {path}")
    if path.suffix in {".yaml", ".yml"} and yaml is not None:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return json.loads(path.read_text(encoding="utf-8"))


def _forward_stream(
    stream: Any, sink: Any, buffer: list[str], *, prefix: str | None = None
) -> None:
    if stream is None:
        return
    try:
        for line in iter(stream.readline, ""):
            if prefix and line:
                formatted = f"{prefix}{line}"
            else:
                formatted = line
            sink.write(formatted)
            sink.flush()
            buffer.append(line)
    finally:
        stream.close()


def parse_approach_arguments(
    config: dict,
    extra_args: list[str] | None,
    extra_defaults: dict[str, Any] | None = None,
) -> Tuple[dict[str, Any], dict[str, dict[str, Any] | None]]:
    arguments_spec = config.get("arguments", {}) or {}
    if not arguments_spec:
        if extra_args:
            extras = " ".join(extra_args)
            raise ValueError(
                "Approach config defines no arguments, but received extras: "
                f"{extras}"
            )
        return {}, {}

    parser = argparse.ArgumentParser(add_help=False)
    choice_metadata: dict[str, dict[str, Any]] = {}
    defaults = extra_defaults or {}

    for name, spec in arguments_spec.items():
        flag = f"--{name.replace('_', '-')}"
        type_name = (spec.get("type") or "str").lower()
        if type_name == "int":
            arg_type = int
        elif type_name == "float":
            arg_type = float
        elif type_name == "bool":
            arg_type = parse_bool
        else:
            arg_type = str

        choices_spec = spec.get("choices") or []
        choices: list[Any] | None = None
        meta_for_arg: dict[str, Any] = {}
        if choices_spec:
            choices = []
            for entry in choices_spec:
                if isinstance(entry, dict):
                    choice_id = entry.get("id")
                    if choice_id is None:
                        continue
                    choices.append(choice_id)
                    meta_for_arg[choice_id] = entry
                else:
                    choices.append(entry)
            choice_metadata[name] = meta_for_arg

        default = defaults.get(name, spec.get("default"))
        parser.add_argument(
            flag,
            dest=name,
            help=spec.get("help"),
            type=arg_type,
            choices=choices,
            default=default,
        )

    namespace, unknown = parser.parse_known_args(extra_args or [])
    if unknown:
        extras = " ".join(unknown)
        raise ValueError(f"Unrecognised approach arguments: {extras}")

    values: dict[str, Any] = {}
    selection_metadata: dict[str, dict[str, Any] | None] = {}
    for name in arguments_spec:
        value = getattr(namespace, name)
        values[name] = value
        selection_metadata[name] = choice_metadata.get(name, {}).get(value)

    return values, selection_metadata


def run_entrypoint(
    command: str,
    *,
    input_path: Path | None = None,
    output_path: Path | None = None,
    case_id: str | None = None,
    approach_args: dict[str, Any] | None = None,
    extra_flags: dict[str, Any] | None = None,
) -> None:
    if not command:
        raise ValueError("Approach configuration is missing an executable entrypoint")

    cmd = shlex.split(command)
    if input_path is not None:
        cmd.extend(["--input-path", str(input_path)])
    if output_path is not None:
        cmd.extend(["--output-path", str(output_path)])
    if case_id is not None:
        cmd.extend(["--case-id", case_id])

    def emit_flags(values: dict[str, Any]) -> list[str]:
        result: list[str] = []
        for key, raw_value in values.items():
            if raw_value is None:
                continue
            flag = f"--{key.replace('_', '-')}"
            if isinstance(raw_value, bool):
                if raw_value:
                    result.append(flag)
            elif isinstance(raw_value, (list, tuple)):
                for item in raw_value:
                    result.extend([flag, str(item)])
            else:
                result.extend([flag, str(raw_value)])
        return result

    if approach_args:
        cmd.extend(emit_flags(approach_args))
    if extra_flags:
        cmd.extend(emit_flags(extra_flags))

    if cmd and cmd[0] in {"python", "python3"}:
        cmd[0] = sys.executable

    env = os.environ.copy()
    pythonpath_parts = [str(REFERENCE_ROOT)]
    if existing := env.get("PYTHONPATH"):
        pythonpath_parts.append(existing)
    env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)

    stdout_lines: list[str] = []
    stderr_lines: list[str] = []
    process = subprocess.Popen(  # noqa: S603,B404 - intentional execution
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
    )

    threads = [
        threading.Thread(
            target=_forward_stream,
            args=(process.stdout, sys.stdout, stdout_lines),
        ),
        threading.Thread(
            target=_forward_stream,
            args=(process.stderr, sys.stderr, stderr_lines),
        ),
    ]
    for thread in threads:
        thread.daemon = True
        thread.start()

    try:
        returncode = process.wait()
    except KeyboardInterrupt:  # pragma: no cover - interactive flow
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        raise
    finally:
        for thread in threads:
            thread.join()

    if returncode != 0:
        raise RuntimeError(
            "\n".join(
                [
                    f"Command failed: {' '.join(cmd)}",
                    "--- stdout ---",
                    "".join(stdout_lines).strip(),
                    "--- stderr ---",
                    "".join(stderr_lines).strip(),
                ]
            )
        )


def resolve_exercises(values: list[str] | None) -> Iterable[ExerciseIdentifier]:
    if values:
        seen: set[str] = set()
        for value in values:
            identifier = ExerciseIdentifier.parse(value)
            key = identifier.relative
            if key in seen:
                continue
            seen.add(key)
            yield identifier
        return
    yield from iter_exercises()


def determine_variants(
    manager: VariantManager, variants: list[str] | None
) -> list[str]:
    if variants:
        return variants
    return [status.variant_id for status in manager.list_variants()]


@dataclass
class RunStats:
    executed: int = 0
    skipped: int = 0
    failed: int = 0


@dataclass
class CaseTask:
    exercise: ExerciseIdentifier
    variant_id: str
    case_id: str
    target_path: Path


def write_run_metadata(
    approach_id: str,
    run_id: str,
    approach_args: dict[str, Any],
    config_path: Path,
    stats: RunStats | None = None,
) -> Path:
    runs_dir = RUNS_ROOT / approach_id
    runs_dir.mkdir(parents=True, exist_ok=True)
    target = runs_dir / f"{run_id}.yaml"

    try:
        relative_config = str(config_path.relative_to(CONFIGS_ROOT.parent))
    except ValueError:
        relative_config = str(config_path)

    payload: dict[str, Any] = {
        "approach_id": approach_id,
        "run_id": run_id,
        "args": {**approach_args},
        "config_path": relative_config,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    if stats is not None:
        payload["cases_executed"] = stats.executed
        payload["cases_failed"] = stats.failed

    if yaml is None:
        target.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    else:
        target.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    return target


def run_benchmark(args: argparse.Namespace) -> int:
    config_path = Path(args.config)
    config = load_config(config_path)

    default_approach = config.get("approach_id", "pecv-reference")

    resume_path: Path | None = None
    resume_run_id = args.resume_run_id
    if args.resume_run:
        candidate = Path(args.resume_run)
        if candidate.is_file():
            resume_path = candidate
        else:
            inferred = (
                RUNS_ROOT
                / (
                    args.approach
                    or getattr(args, "approach_name", None)
                    or default_approach
                )
                / f"{args.resume_run}.yaml"
            )
            if inferred.exists():
                resume_path = inferred
            else:
                raise FileNotFoundError(
                    f"Unable to locate resume metadata at {candidate} or {inferred}"
                )
    elif resume_run_id:
        resume_dir = (
            args.approach or getattr(args, "approach_name", None) or default_approach
        )
        candidate = RUNS_ROOT / resume_dir / f"{resume_run_id}.yaml"
        if candidate.exists():
            resume_path = candidate
        else:
            resume_path = None

    resume_metadata = load_resume_metadata(resume_path) if resume_path else None

    if (
        resume_metadata
        and args.approach
        and args.approach != resume_metadata.get("approach_id")
    ):
        raise ValueError(
            "--approach conflicts with the approach recorded in the run metadata"
        )

    if resume_metadata:
        config_hint = resume_metadata.get("config_path")
        if config_hint:
            config_candidate = Path(config_hint)
            if not config_candidate.is_absolute():
                config_candidate = CONFIGS_ROOT.parent / config_candidate
            if config_candidate.exists():
                config_path = config_candidate
                config = load_config(config_path)

    approach_id = (
        args.approach
        or getattr(args, "approach_name", None)
        or (resume_metadata or {}).get("approach_id")
        or config.get("approach_id", "pecv-reference")
    )

    stored_args = (resume_metadata or {}).get("args", {})
    defaults_from_resume = {
        key: value for key, value in stored_args.items() if key != "exercises"
    }
    extra_args = getattr(args, "_extra_args", [])
    approach_args, selection_metadata = parse_approach_arguments(
        config,
        extra_args,
        extra_defaults=defaults_from_resume,
    )

    entrypoints = config.get("entrypoints", {}) or {}
    run_case_entrypoint = entrypoints.get("run_case")
    if not run_case_entrypoint:
        raise ValueError(
            "Approach configuration must provide an 'entrypoints.run_case'"
        )

    prepare_entrypoint = entrypoints.get("prepare")
    if prepare_entrypoint:
        try:
            run_entrypoint(
                prepare_entrypoint,
                approach_args=approach_args,
                extra_flags={"config": str(config_path)},
            )
        except Exception as exc:  # noqa: BLE001 - preparation errors for visibility
            raise RuntimeError(f"Failed to run prepare entrypoint: {exc}") from exc

    slug_components: list[str] = []
    for key, value in approach_args.items():
        meta = selection_metadata.get(key)
        if isinstance(value, bool):
            if value:
                slug_components.append(slugify(key))
            continue
        if value in (None, ""):
            continue
        if meta and meta.get("run_id"):
            slug_components.append(slugify(str(meta["run_id"])))
        else:
            slug_components.append(slugify(str(value)))
    if not slug_components:
        slug_components.append(slugify(approach_id))
    slug_base = "-".join(slug_components)

    if resume_metadata and "run_id" in resume_metadata:
        default_run_id = resume_metadata["run_id"]
    elif resume_run_id:
        default_run_id = resume_run_id
    else:
        time_slug = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M")
        suffix = uuid.uuid4().hex[:6]
        parts: list[str] = []
        if slug_base:
            parts.append(slug_base)
        parts.extend([time_slug, suffix])
        default_run_id = "-".join(parts)

    run_id = args.run_id or default_run_id

    results_dir = RESULTS_ROOT / approach_id / run_id / "cases"
    results_dir.mkdir(parents=True, exist_ok=True)

    stats = RunStats()
    if resume_metadata:
        stats.executed = int(resume_metadata.get("cases_executed", 0))
        stats.skipped = int(resume_metadata.get("cases_skipped", 0))
        # Always recompute failures for the current run to avoid carrying over past state
        stats.failed = 0

    metadata_path = write_run_metadata(
        approach_id=approach_id,
        run_id=run_id,
        approach_args=approach_args,
        config_path=config_path,
    )

    errors: list[str] = []

    requested_exercises = args.exercise
    if not requested_exercises and stored_args.get("exercises"):
        requested_exercises = list(stored_args["exercises"])

    variant_filter = args.variant or None
    if variant_filter and len(requested_exercises or []) != 1:
        raise ValueError("--variant requires exactly one --exercise to be specified")

    skip_existing = args.skip_existing or bool(resume_metadata) or bool(resume_run_id)

    tasks: list[CaseTask] = []

    for exercise in resolve_exercises(requested_exercises):
        manager = VariantManager(exercise)
        variants_to_run = determine_variants(manager, variant_filter)
        if not variants_to_run:
            continue

        for variant_id in variants_to_run:
            case_id = f"{exercise.relative}/{variant_id}"
            target_path = (
                results_dir / exercise.course / exercise.exercise / f"{variant_id}.json"
            )
            target_path.parent.mkdir(parents=True, exist_ok=True)

            if skip_existing and target_path.exists():
                stats.skipped += 1
                continue

            tasks.append(
                CaseTask(
                    exercise=exercise,
                    variant_id=variant_id,
                    case_id=case_id,
                    target_path=target_path,
                )
            )

    max_concurrency = args.max_concurrency or 1
    if max_concurrency < 1:
        raise ValueError("--max-concurrency must be at least 1")

    def execute_case(task: CaseTask) -> tuple[bool, str | None]:
        manager = VariantManager(task.exercise)
        try:
            materialized_dir = manager.materialize_variant(
                task.variant_id,
                force=args.force_materialize,
            )
        except Exception as exc:  # noqa: BLE001 - CLI reporting
            message = f"{task.case_id}: materialize failed ({exc})"
            return False, message

        try:
            run_entrypoint(
                run_case_entrypoint,
                input_path=materialized_dir,
                output_path=task.target_path,
                case_id=task.case_id,
                approach_args=approach_args,
            )
            success = True
            error_message: str | None = None
        except Exception as exc:  # noqa: BLE001 - CLI reporting
            success = False
            error_message = f"{task.case_id}: run failed ({exc})"
            if task.target_path.exists():
                task.target_path.unlink()
        finally:
            if args.clean_after:
                manager.clean_variant(
                    task.variant_id,
                    keep_outputs=args.keep_outputs,
                )

        return success, error_message

    run_interrupted = False
    try:
        if tasks:
            with ThreadPoolExecutor(max_workers=max_concurrency) as executor:
                future_to_task = {
                    executor.submit(execute_case, task): task for task in tasks
                }
                for future in as_completed(future_to_task):
                    success, error_message = future.result()
                    if success:
                        stats.executed += 1
                    else:
                        stats.failed += 1
                        if error_message:
                            errors.append(error_message)
    except KeyboardInterrupt:
        run_interrupted = True
        errors.append("Run interrupted by user")
    finally:
        metadata_path = write_run_metadata(
            approach_id=approach_id,
            run_id=run_id,
            approach_args=approach_args,
            config_path=config_path,
            stats=stats,
        )

    print(f"Run metadata written to {metadata_path}")
    print(
        f"Executed {stats.executed} case(s), skipped {stats.skipped}, "
        f"failed {stats.failed}."
    )

    if errors:
        print("Encountered issues:")
        for err in errors:
            print(f"  - {err}")
        if run_interrupted:
            return 130
        return 1

    return 0


def register_subcommand(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(handler=run_benchmark)
    parser.add_argument(
        "approach_name",
        nargs="?",
        help="Approach identifier (e.g. pecv-reference). Overrides config default.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="Approach configuration file (YAML)",
    )
    parser.add_argument(
        "--approach",
        help="Override approach identifier from config",
    )
    parser.add_argument(
        "--exercise",
        action="append",
        help="Exercise path (course/exercise). Repeatable.",
    )
    parser.add_argument(
        "--variant",
        action="append",
        help="Variant identifier (requires exactly one --exercise)",
    )
    parser.add_argument(
        "--run-id",
        help="Explicit run identifier (if omitted, one is generated)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip cases whose result file already exists",
    )
    parser.add_argument(
        "--force-materialize",
        action="store_true",
        help="Re-materialize variants before running",
    )
    parser.add_argument(
        "--clean-after",
        action="store_true",
        help="Clean materialised artefacts after each case",
    )
    parser.add_argument(
        "--keep-outputs",
        action="store_true",
        help="Preserve per-variant outputs directory when cleaning",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=1,
        help=(
            "Maximum number of cases to execute in parallel (default: 1). "
            "Increase to speed up runs on machines with sufficient capacity."
        ),
    )
    parser.add_argument(
        "--resume-run",
        help="Path to an existing run metadata YAML/JSON file to resume",
    )
    parser.add_argument(
        "--resume-run-id",
        help=(
            "Identifier of a previous run recorded under runs/<approach>/<run_id>.yaml "
            "to resume"
        ),
    )
