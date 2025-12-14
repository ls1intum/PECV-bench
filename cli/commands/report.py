from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple

try:
    import yaml  # type: ignore[import]
except ImportError:  # pragma: no cover - optional dependency
    yaml = None  # type: ignore[assignment]

from cli.reporting import (
    evaluate_case,
    extract_prediction_issues,
    load_gold_issues,
    summarise_dataset,
)
from cli.utils import DATA_ROOT, PROJECT_ROOT, RESULTS_ROOT, RUNS_ROOT


MetricValue = Optional[float]


def _resolve_path(candidate: str | Path | None, default: Path) -> Path:
    if candidate is None:
        return default
    path = Path(candidate).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _log_warning(message: str) -> None:
    print(f"[report] {message}", file=sys.stderr)

def _simple_yaml_parse(text: str) -> dict[str, Any]:
    """Fallback parser for the minimal run metadata structure."""

    result: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, result)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        while stack and indent < stack[-1][0]:
            stack.pop()

        parent = stack[-1][1] if stack else result

        if value == "" or value == "|":
            container: dict[str, Any] = {}
            parent[key] = container
            stack.append((indent + 2, container))
            continue

        if value.startswith("'") and value.endswith("'"):
            value = value.strip("'")
        elif value.startswith('"') and value.endswith('"'):
            value = value.strip('"')

        if value.lower() in {"true", "false"}:
            parent[key] = value.lower() == "true"
            continue

        try:
            parent[key] = int(value)
            continue
        except ValueError:
            pass

        try:
            parent[key] = float(value)
            continue
        except ValueError:
            pass

        parent[key] = value

    return result


def _display_config_key(config_key: str, benchmark: str) -> str:
    prefix = f"{benchmark} :: "
    if config_key.startswith(prefix):
        return config_key[len(prefix) :]
    return config_key


def _load_run_metadata(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            return yaml.safe_load(text) or {}
        except Exception:
            pass
    try:
        return _simple_yaml_parse(text)
    except Exception:
        return {}


def _flatten_args(args: dict[str, Any]) -> dict[str, Any]:
    flattened: dict[str, Any] = {}
    for key, value in args.items():
        if isinstance(value, (str, int, float, bool)):
            flattened[key] = value
        elif value is None:
            continue
        else:
            flattened[key] = json.dumps(value, sort_keys=True)
    return flattened


def _build_config_key(benchmark: str, args: dict[str, Any]) -> str:
    flattened = _flatten_args(args)
    if not flattened:
        return f"{benchmark} :: default"
    parts = [f"{key}={flattened[key]}" for key in sorted(flattened)]
    return f"{benchmark} :: " + ", ".join(parts)


def _safe_number(value: Any) -> MetricValue:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


@dataclass
class StatsAccumulator:
    cases: int = 0
    evaluated_cases: int = 0
    tp: int = 0
    fp: int = 0
    fn: int = 0
    span_sum: float = 0.0
    iou_sum: float = 0.0
    matches: int = 0
    time_sum: float = 0.0
    time_count: int = 0
    cost_sum: float = 0.0
    cost_count: int = 0

    def add_case(
        self,
        *,
        has_metrics: bool,
        tp: int = 0,
        fp: int = 0,
        fn: int = 0,
        span_sum: float = 0.0,
        iou_sum: float = 0.0,
        matches: int = 0,
        duration: MetricValue,
        cost: MetricValue,
    ) -> None:
        self.cases += 1
        if duration is not None:
            self.time_sum += duration
            self.time_count += 1
        if cost is not None:
            self.cost_sum += cost
            self.cost_count += 1
        if has_metrics:
            self.evaluated_cases += 1
            self.tp += tp
            self.fp += fp
            self.fn += fn
            self.span_sum += span_sum
            self.iou_sum += iou_sum
            self.matches += matches

    def totals(self) -> dict[str, Any]:
        precision = self.tp / (self.tp + self.fp) if (self.tp + self.fp) else 0.0
        recall = self.tp / (self.tp + self.fn) if (self.tp + self.fn) else 0.0
        f1 = (
            (2 * precision * recall) / (precision + recall)
            if (precision + recall)
            else 0.0
        )
        return {
            "cases": self.cases,
            "evaluated_cases": self.evaluated_cases,
            "tp": self.tp,
            "fp": self.fp,
            "fn": self.fn,
            "matches": self.matches,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    def averages(self) -> dict[str, Any]:
        span_avg = self.span_sum / self.matches if self.matches else None
        iou_avg = self.iou_sum / self.matches if self.matches else None
        time_avg = self.time_sum / self.time_count if self.time_count else None
        cost_avg = self.cost_sum / self.cost_count if self.cost_count else None
        return {
            "span_f1": span_avg,
            "iou": iou_avg,
            "time_s": time_avg,
            "cost_usd": cost_avg,
        }

    def merge(self, other: "StatsAccumulator") -> None:
        self.cases += other.cases
        self.evaluated_cases += other.evaluated_cases
        self.tp += other.tp
        self.fp += other.fp
        self.fn += other.fn
        self.span_sum += other.span_sum
        self.iou_sum += other.iou_sum
        self.matches += other.matches
        self.time_sum += other.time_sum
        self.time_count += other.time_count
        self.cost_sum += other.cost_sum
        self.cost_count += other.cost_count


def _iter_case_files(cases_dir: Path) -> Iterator[Path]:
    yield from sorted(cases_dir.rglob("*.json"))


def _derive_exercise(case_data: dict[str, Any], case_path: Path, cases_dir: Path) -> str | None:
    case_id = case_data.get("case_id")
    if isinstance(case_id, str):
        parts = [part for part in case_id.split("/") if part]
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"
    try:
        relative = case_path.relative_to(cases_dir)
    except ValueError:
        return None
    parts = list(relative.parts)
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return None


def _resolve_case_parts(cases_dir: Path, case_path: Path) -> Optional[Tuple[str, str, str]]:
    try:
        relative = case_path.relative_to(cases_dir)
    except ValueError:
        return None
    parts = list(relative.parts)
    if len(parts) < 3:
        return None
    course, exercise = parts[0], parts[1]
    variant = case_path.stem
    return course, exercise, variant


def _collect_run_stats(cases_dir: Path) -> tuple[StatsAccumulator, dict[str, StatsAccumulator]]:
    overall = StatsAccumulator()
    per_exercise: dict[str, StatsAccumulator] = defaultdict(StatsAccumulator)

    for case_path in _iter_case_files(cases_dir):
        try:
            case_data = json.loads(case_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue

        timing_data = case_data.get("timing") or {}
        duration = _safe_number(timing_data.get("duration_s") or timing_data.get("durationS"))

        cost_data = case_data.get("cost") or case_data.get("costs") or {}
        cost = _safe_number(cost_data.get("total_usd") or cost_data.get("totalUsd"))

        case_relative = None
        try:
            case_relative = str(case_path.relative_to(cases_dir))
        except ValueError:
            case_relative = case_path.name

        exercise_key = _derive_exercise(case_data, case_path, cases_dir)
        accumulator_targets = [overall]
        if exercise_key:
            accumulator_targets.append(per_exercise[exercise_key])

        course_exercise_variant = _resolve_case_parts(cases_dir, case_path)
        gold_issues: Optional[List[Dict[str, Any]]] = None
        gold_path: Optional[Path] = None
        if course_exercise_variant is not None:
            course, exercise, variant = course_exercise_variant
            gold_issues, gold_path = load_gold_issues(
                course, exercise, variant, DATA_ROOT
            )
            if gold_issues is None:
                _log_warning(
                    f"Gold annotations missing for {course}/{exercise}/{variant} at {gold_path}"
                )
        else:
            _log_warning(
                f"Could not resolve course/exercise/variant for case {case_relative}; metrics skipped"
            )

        predictions, missing_predictions = extract_prediction_issues(case_data)
        if missing_predictions:
            _log_warning(f"No predictions found for case {case_relative}; metrics skipped")

        has_metrics = (
            gold_issues is not None and not missing_predictions
        )

        tp = fp = fn = matches = 0
        span_sum = iou_sum = 0.0

        if has_metrics and gold_issues is not None:
            tp, fp, fn, span_sum, iou_sum, matches = evaluate_case(gold_issues, predictions)

        for target in accumulator_targets:
            target.add_case(
                has_metrics=has_metrics,
                tp=tp,
                fp=fp,
                fn=fn,
                span_sum=span_sum,
                iou_sum=iou_sum,
                matches=matches,
                duration=duration,
                cost=cost,
            )

    return overall, per_exercise


def _render_per_exercise(per_ex: dict[str, StatsAccumulator]) -> dict[str, Any]:
    rendered: dict[str, Any] = {}
    for exercise, stats in sorted(per_ex.items()):
        rendered[exercise] = {
            "totals": stats.totals(),
            "averages": stats.averages(),
        }
    return rendered


def _latex_escape(value: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
    }
    escaped = value
    for target, repl in replacements.items():
        escaped = escaped.replace(target, repl)
    return escaped


def _format_number(value: Any, precision: int = 4) -> str:
    if value is None:
        return "—"
    if isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
        return str(int(value))
    try:
        return f"{float(value):.{precision}f}"
    except (TypeError, ValueError):
        return str(value)


@dataclass
class GroupAccumulator:
    benchmark: str
    config_key: str
    model_values: set[str] = field(default_factory=set)
    run_count: int = 0
    overall: StatsAccumulator = field(default_factory=StatsAccumulator)
    per_exercise: Dict[str, StatsAccumulator] = field(default_factory=dict)

    def add_run(
        self,
        *,
        args_meta: Dict[str, Any],
        overall_stats: StatsAccumulator,
        per_exercise_stats: Dict[str, StatsAccumulator],
    ) -> None:
        self.run_count += 1
        model = args_meta.get("model")
        if isinstance(model, str):
            self.model_values.add(model)

        self.overall.merge(overall_stats)
        for exercise, stats in per_exercise_stats.items():
            bucket = self.per_exercise.get(exercise)
            if bucket is None:
                bucket = StatsAccumulator()
                self.per_exercise[exercise] = bucket
            bucket.merge(stats)

    def row(self) -> dict[str, Any]:
        totals = self.overall.totals()
        averages = self.overall.averages()
        tp = totals.get("tp", 0)
        fp = totals.get("fp", 0)
        fn = totals.get("fn", 0)
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (
            (2 * precision * recall) / (precision + recall)
            if (precision + recall)
            else 0.0
        )

        model = sorted(self.model_values)
        model_repr = ", ".join(model) if model else "—"

        return {
            "benchmark": self.benchmark,
            "model": model_repr,
            "config_key": self.config_key,
            "n_runs": self.run_count,
            "totals": {
                **totals,
                "precision": precision,
                "recall": recall,
                "f1": f1,
            },
            "averages": averages,
        }

    def per_exercise_summary(self) -> List[Dict[str, Any]]:
        entries: List[Dict[str, Any]] = []
        for exercise in sorted(self.per_exercise):
            stats = self.per_exercise[exercise]
            entries.append(
                {
                    "exercise": exercise,
                    "totals": stats.totals(),
                    "averages": stats.averages(),
                }
            )
        return entries


def report_command(args: argparse.Namespace) -> int:
    benchmark = args.benchmark
    results_root = _resolve_path(args.results_dir, RESULTS_ROOT)
    runs_root = _resolve_path(args.runs_dir, RUNS_ROOT)

    benchmark_root = results_root / benchmark
    if not benchmark_root.exists():
        raise FileNotFoundError(f"Benchmark results not found: {benchmark_root}")

    aggregate_dir_name = args.aggregate_dir
    aggregate_root: Optional[Path] = None
    if aggregate_dir_name:
        aggregate_root = benchmark_root / aggregate_dir_name
        aggregate_root.mkdir(parents=True, exist_ok=True)

    group_accumulators: dict[str, GroupAccumulator] = {}
    run_reports: list[dict[str, Any]] = []

    dataset_summary = summarise_dataset(DATA_ROOT)

    for run_dir in sorted(p for p in benchmark_root.iterdir() if p.is_dir()):
        if aggregate_root is not None and run_dir == aggregate_root:
            continue

        cases_dir = run_dir / "cases"
        if not cases_dir.exists():
            continue

        case_files = list(_iter_case_files(cases_dir))
        if not case_files:
            continue

        overall_stats, per_exercise_stats = _collect_run_stats(cases_dir)

        run_id = run_dir.name
        metadata_path = runs_root / benchmark / f"{run_id}.yaml"
        metadata = _load_run_metadata(metadata_path)
        args_meta = metadata.get("args") if isinstance(metadata, dict) else {}
        if not isinstance(args_meta, dict):
            args_meta = {}

        config_key = _build_config_key(benchmark, args_meta)

        accumulator = group_accumulators.setdefault(
            config_key, GroupAccumulator(benchmark=benchmark, config_key=config_key)
        )
        accumulator.add_run(
            args_meta=args_meta,
            overall_stats=overall_stats,
            per_exercise_stats=per_exercise_stats,
        )

        run_report = {
            "run_id": run_id,
            "benchmark": benchmark,
            "config": {
                "approach_id": metadata.get("approach_id"),
                "config_key": config_key,
                "args": args_meta,
                "generated_at": metadata.get("generated_at"),
                "cases_executed": metadata.get("cases_executed"),
                "cases_failed": metadata.get("cases_failed"),
            },
            "totals": overall_stats.totals(),
            "averages": overall_stats.averages(),
        }

        per_exercise_rendered = _render_per_exercise(per_exercise_stats)
        if per_exercise_rendered:
            run_report["per_exercise"] = per_exercise_rendered

        report_path = run_dir / "run_report.json"
        report_path.write_text(json.dumps(run_report, indent=2), encoding="utf-8")

        run_reports.append(run_report)

    summary_rows: List[dict[str, Any]] = []
    config_rows: Dict[str, dict[str, Any]] = {}
    for key, accumulator in group_accumulators.items():
        row = accumulator.row()
        config_rows[key] = row
        summary_rows.append(row)
    summary_rows.sort(key=lambda row: row["config_key"])

    per_exercise_tables = {
        key: {
            "model": config_rows[key]["model"],
            "exercises": group_accumulators[key].per_exercise_summary(),
        }
        for key in group_accumulators
    }

    summary_payload = {
        "benchmark": benchmark,
        "generated_at": _now_iso(),
        "dataset_summary": dataset_summary,
        "runs": summary_rows,
        "per_exercise": per_exercise_tables,
    }

    summary_json_path = benchmark_root / "summary.json"
    summary_json_path.write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")

    variants_per_exercise = dataset_summary.get("variants_per_exercise", {})
    issues_per_category = dataset_summary.get("issues_per_category", {})
    issues_per_artifact = dataset_summary.get("issues_per_artifact", {})

    markdown_lines = ["## Dataset Summary", ""]
    markdown_lines.append(
        f"- Total annotated variants: {dataset_summary.get('total_annotated_variants', 0)}"
    )
    markdown_lines.append(
        f"- Total gold issues: {dataset_summary.get('total_issues', 0)}"
    )

    variants_per_exercise = dataset_summary.get("variants_per_exercise", {})
    if variants_per_exercise:
        markdown_lines.append("")
        markdown_lines.append("| Exercise | Variants |")
        markdown_lines.append("| --- | --- |")
        for exercise, count in sorted(variants_per_exercise.items()):
            markdown_lines.append(f"| {exercise} | {count} |")

    issues_per_category = dataset_summary.get("issues_per_category", {})
    if issues_per_category:
        markdown_lines.append("")
        markdown_lines.append("| Issue Category | Count |")
        markdown_lines.append("| --- | --- |")
        for category, count in sorted(issues_per_category.items()):
            markdown_lines.append(f"| {category} | {count} |")

    issues_per_artifact = dataset_summary.get("issues_per_artifact", {})
    if issues_per_artifact:
        markdown_lines.append("")
        markdown_lines.append("| Artifact Type | Count |")
        markdown_lines.append("| --- | --- |")
        for artifact, count in sorted(issues_per_artifact.items()):
            markdown_lines.append(f"| {artifact} | {count} |")

    markdown_lines.append("")
    markdown_lines.append("## Aggregate Results")

    headers = [
        "Benchmark",
        "Config Key",
        "N runs",
        "TP",
        "FP",
        "FN",
        "Precision",
        "Recall",
        "F1",
        "Span F1",
        "IoU",
        "Avg Time (s)",
        "Avg Cost ($)",
    ]

    markdown_lines.extend(
        [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |",
        ]
    )

    for row in summary_rows:
        totals = row["totals"]
        averages = row["averages"]
        display_key = _display_config_key(row["config_key"], row["benchmark"])
        markdown_lines.append(
            "| "
            + " | ".join(
                [
                    row["benchmark"],
                    display_key,
                    str(row["n_runs"]),
                    _format_number(totals["tp"], 0),
                    _format_number(totals["fp"], 0),
                    _format_number(totals["fn"], 0),
                    _format_number(totals["precision"], 3),
                    _format_number(totals["recall"], 3),
                    _format_number(totals["f1"], 3),
                    _format_number(averages["span_f1"], 3),
                    _format_number(averages["iou"], 3),
                    _format_number(averages["time_s"], 3),
                    _format_number(averages["cost_usd"], 4),
                ]
            )
            + " |"
        )

    markdown_lines.append("")
    markdown_lines.append("## Per Exercise Breakdown")

    for row in summary_rows:
        config_key = row["config_key"]
        display_key = _display_config_key(config_key, row["benchmark"])
        per_ex = per_exercise_tables.get(config_key, {}).get("exercises") or []
        if not per_ex:
            continue
        markdown_lines.append("")
        markdown_lines.append(f"### {row['benchmark']} :: {display_key}")
        markdown_lines.append(
            "| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |"
        )
        markdown_lines.append(
            "| " + " | ".join(["---"] * 11) + " |"
        )
        for entry in per_ex:
            totals = entry["totals"]
            averages = entry["averages"]
            markdown_lines.append(
                "| "
                + " | ".join(
                    [
                        entry["exercise"],
                        _format_number(totals.get("tp"), 0),
                        _format_number(totals.get("fp"), 0),
                        _format_number(totals.get("fn"), 0),
                        _format_number(totals.get("precision"), 3),
                        _format_number(totals.get("recall"), 3),
                        _format_number(totals.get("f1"), 3),
                        _format_number(averages.get("span_f1"), 3),
                        _format_number(averages.get("iou"), 3),
                        _format_number(averages.get("time_s"), 3),
                        _format_number(averages.get("cost_usd"), 4),
                    ]
                )
                + " |"
            )

    markdown_lines.append("")
    markdown_lines.append(
        "*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*"
    )

    summary_md_path = benchmark_root / "summary.md"
    summary_md_path.write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    column_spec = "".join(["l" for _ in range(2)] + ["r" for _ in range(len(headers) - 2)])
    latex_blocks: List[str] = []

    ds_metric_lines = [
        "\\begin{tabular}{lr}",
        "Metric & Value \\",
        "\\hline",
        f"Total annotated variants & {dataset_summary.get('total_annotated_variants', 0)} \\",
        f"Total gold issues & {dataset_summary.get('total_issues', 0)} \\",
        "\\end{tabular}",
    ]
    latex_blocks.append("\n".join(ds_metric_lines))

    if variants_per_exercise:
        latex_ex_lines = [
            "\\begin{tabular}{lr}",
            "Exercise & Variants \\",
            "\\hline",
        ]
        for exercise, count in sorted(variants_per_exercise.items()):
            latex_ex_lines.append(
                f"{_latex_escape(exercise)} & {count} \\")
        latex_ex_lines.append("\\end{tabular}")
        latex_blocks.append("\n".join(latex_ex_lines))

    if issues_per_category:
        latex_cat_lines = [
            "\\begin{tabular}{lr}",
            "Issue Category & Count \\",
            "\\hline",
        ]
        for category, count in sorted(issues_per_category.items()):
            latex_cat_lines.append(
                f"{_latex_escape(category)} & {count} \\")
        latex_cat_lines.append("\\end{tabular}")
        latex_blocks.append("\n".join(latex_cat_lines))

    if issues_per_artifact:
        latex_art_lines = [
            "\\begin{tabular}{lr}",
            "Artifact Type & Count \\",
            "\\hline",
        ]
        for artifact, count in sorted(issues_per_artifact.items()):
            latex_art_lines.append(
                f"{_latex_escape(artifact)} & {count} \\")
        latex_art_lines.append("\\end{tabular}")
        latex_blocks.append("\n".join(latex_art_lines))

    latex_main_lines = [
        f"\\begin{{tabular}}{{{column_spec}}}",
        "Benchmark & Config Key & N runs & TP & FP & FN & Precision & Recall & F1 & Span F1 & IoU & Avg Time (s) & Avg Cost ($) "
        + "\\\\",
        "\\hline",
    ]
    for row in summary_rows:
        totals = row["totals"]
        averages = row["averages"]
        display_key = _display_config_key(row["config_key"], row["benchmark"])
        latex_values = [
            _latex_escape(row["benchmark"]),
            _latex_escape(display_key),
            str(row["n_runs"]),
            _format_number(totals["tp"], 0),
            _format_number(totals["fp"], 0),
            _format_number(totals["fn"], 0),
            _format_number(totals["precision"], 3),
            _format_number(totals["recall"], 3),
            _format_number(totals["f1"], 3),
            _format_number(averages["span_f1"], 3),
            _format_number(averages["iou"], 3),
            _format_number(averages["time_s"], 3),
            _format_number(averages["cost_usd"], 4),
        ]
        latex_main_lines.append(" & ".join(latex_values) + " " + "\\\\")

    latex_main_lines.append("\\end{tabular}")
    latex_blocks.append("\n".join(latex_main_lines))

    exercise_column_spec = "l" + "r" * 10
    for row in summary_rows:
        config_key = row["config_key"]
        display_key = _display_config_key(config_key, row["benchmark"])
        per_ex = per_exercise_tables.get(config_key, {}).get("exercises") or []
        if not per_ex:
            continue
        latex_lines = [
            f"% Per-exercise breakdown for {row['benchmark']} :: {display_key}",
            f"\\begin{{tabular}}{{{exercise_column_spec}}}",
            "Exercise & TP & FP & FN & Precision & Recall & F1 & Span F1 & IoU & Avg Time (s) & Avg Cost ($) "
            + "\\\\",
            "\\hline",
        ]
        for entry in per_ex:
            totals = entry["totals"]
            averages = entry["averages"]
            latex_values = [
                _latex_escape(entry["exercise"]),
                _format_number(totals.get("tp"), 0),
                _format_number(totals.get("fp"), 0),
                _format_number(totals.get("fn"), 0),
                _format_number(totals.get("precision"), 3),
                _format_number(totals.get("recall"), 3),
                _format_number(totals.get("f1"), 3),
                _format_number(averages.get("span_f1"), 3),
                _format_number(averages.get("iou"), 3),
                _format_number(averages.get("time_s"), 3),
                _format_number(averages.get("cost_usd"), 4),
            ]
            latex_lines.append(" & ".join(latex_values) + " " + "\\\\")
        latex_lines.append("\\end{tabular}")
        latex_blocks.append("\n".join(latex_lines))

    summary_tex_path = benchmark_root / "summary.tex"
    summary_tex_path.write_text("\n\n".join(latex_blocks) + "\n", encoding="utf-8")

    print(f"Generated {len(run_reports)} run reports.")
    print(f"Summary JSON: {summary_json_path}")
    print(f"Summary Markdown: {summary_md_path}")
    print(f"Summary LaTeX: {summary_tex_path}")

    return 0


def register_subcommand(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(handler=report_command)
    parser.add_argument(
        "--benchmark",
        default="pecv-reference",
        help="Benchmark name under results/ (default: pecv-reference)",
    )
    parser.add_argument(
        "--results-dir",
        default="results",
        help="Root directory that holds benchmark results (default: results)",
    )
    parser.add_argument(
        "--runs-dir",
        default="runs",
        help="Directory containing run metadata (default: runs)",
    )
    parser.add_argument(
        "--aggregate-dir",
        default=None,
        help=(
            "Optional subdirectory (within the benchmark results directory) for "
            "additional aggregate artifacts; when omitted, summaries are written "
            "directly to the benchmark root"
        ),
    )
