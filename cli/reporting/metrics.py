from __future__ import annotations

import os
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from collections import defaultdict


def unify_path(path: str | None) -> str:
    if not path:
        return "problem_statement.md"
    for prefix in (
        "solution_repository/",
        "template_repository/",
        "solution/",
        "template/",
    ):
        if path.startswith(prefix):
            return path[len(prefix) :]
    return path


def issue_to_tokens(issue: Dict[str, Any]) -> Set[Tuple[str, str, int]]:
    tokens: Set[Tuple[str, str, int]] = set()
    # Support both snake_case (internal/gold) and camelCase (API/prediction) keys
    locations = issue.get("related_locations") or issue.get("relatedLocations") or []
    for location in locations:
        if not isinstance(location, dict):
            continue
        artifact_type = str(location.get("type") or "UNKNOWN")
        file_path = unify_path(location.get("file_path") or location.get("filePath") or "")
        try:
            start_line = int(location.get("start_line") or location.get("startLine") or 0)
        except (TypeError, ValueError):
            start_line = 0
        try:
            end_line = int(location.get("end_line") or location.get("endLine") or start_line)
        except (TypeError, ValueError):
            end_line = start_line
        if end_line < start_line:
            end_line = start_line
        for line in range(start_line, end_line + 1):
            tokens.add((artifact_type, file_path or "problem_statement.md", line))
    if not tokens:
        tokens.add(("PROBLEM_STATEMENT", "problem_statement.md", 0))
    return tokens


def _issues_from_payload(payload: Any) -> List[Dict[str, Any]]:
    issues: List[Dict[str, Any]] = []
    if not isinstance(payload, list):
        return issues
    for entry in payload:
        if not isinstance(entry, dict):
            continue
        category = entry.get("category")
        if not category:
            continue
        tokens = issue_to_tokens(entry)
        issues.append({"category": category, "tokens": tokens})
    return issues


def load_gold_issues(course: str, exercise: str, variant: str, data_root: Path) -> Tuple[Optional[List[Dict[str, Any]]], Path]:
    gold_path = (
        data_root
        / course
        / exercise
        / "variants"
        / variant
        / f"{variant}.json"
    )
    if not gold_path.exists():
        return None, gold_path
    try:
        data = json.loads(gold_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, gold_path
    issues = _issues_from_payload(data.get("issues"))
    return issues, gold_path


def extract_prediction_issues(case_data: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], bool]:
    response = case_data.get("response")
    if isinstance(response, dict):
        issues = response.get("issues")
        if isinstance(issues, list):
            return _issues_from_payload(issues), False
    direct = case_data.get("issues")
    if isinstance(direct, list):
        return _issues_from_payload(direct), False
    return [], True


def compute_f1_iou(
    pred_tokens: Set[Tuple[str, str, int]],
    gold_tokens: Set[Tuple[str, str, int]],
) -> Tuple[float, float]:
    if not pred_tokens or not gold_tokens:
        return 0.0, 0.0
    intersection = pred_tokens & gold_tokens
    if not intersection:
        return 0.0, 0.0
    inter = len(intersection)
    precision = inter / len(pred_tokens)
    recall = inter / len(gold_tokens)
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0.0
    union = len(pred_tokens | gold_tokens)
    iou = inter / union if union else 0.0
    return f1, iou


def greedy_match(
    pred_issues: List[Dict[str, Any]],
    gold_issues: List[Dict[str, Any]],
) -> Tuple[List[Tuple[int, int, float, float]], Set[int], Set[int]]:
    candidates: List[Tuple[float, float, int, int]] = []
    for i, pred in enumerate(pred_issues):
        for j, gold in enumerate(gold_issues):
            if pred.get("category") != gold.get("category"):
                continue
            f1, iou = compute_f1_iou(pred["tokens"], gold["tokens"])
            if f1 > 0:
                candidates.append((f1, iou, i, j))
    candidates.sort(key=lambda item: (-item[0], -item[1]))

    matched_pred: Set[int] = set()
    matched_gold: Set[int] = set()
    matches: List[Tuple[int, int, float, float]] = []

    for f1, iou, i, j in candidates:
        if i in matched_pred or j in matched_gold:
            continue
        matched_pred.add(i)
        matched_gold.add(j)
        matches.append((i, j, f1, iou))

    return matches, matched_pred, matched_gold


def evaluate_case(
    gold_issues: List[Dict[str, Any]],
    pred_issues: List[Dict[str, Any]],
) -> Tuple[int, int, int, float, float, int]:
    matches, matched_pred, matched_gold = greedy_match(pred_issues, gold_issues)
    tp = len(matches)
    fp = len(pred_issues) - len(matched_pred)
    fn = len(gold_issues) - len(matched_gold)
    span_sum = sum(match[2] for match in matches)
    iou_sum = sum(match[3] for match in matches)
    return tp, fp, fn, span_sum, iou_sum, len(matches)


def unify_model_name(model_name: str) -> str:
    """Normalise provider-qualified model identifiers.

    The input model_name may contain provider prefixes and preview suffixes,
    e.g. "openrouter:google/gemini-2.5-flash-lite-preview-06-17". We return
    a concise key by stripping the provider, selecting the last path
    component, and collapsing Gemini Flash Lite preview versions into a
    single key (``gemini-2.5-flash-lite``).
    """
    if ":" in model_name:
        spec = model_name.split(":", 1)[1]
    else:
        spec = model_name
    short = spec.split("/")[-1]

    # Strip timestamp if present (e.g., -2025-12-13-...) in output json file, key: run_id
    short = re.sub(r"-\d{4}-\d{2}-\d{2}.*", "", short)

    # normalise Flash Lite preview identifiers
    if "flash-lite" in short:
        return "google-gemini-2.5-flash-lite"
    return short


def analyse_variants_runs(results_dir: str) -> None:
    """
    Iterate through all result files in results_dir

    DEFAULT: results/pecv-reference
    and extract required information.

    New structure:
    results/pecv-reference/<run-id>/cases/<course>/<exercise>/<variant>.json

    Each JSON contains:
    - case_id: "ITP2425/H01E01-Lectures/003" (course/exercise/variant)
    - run_id: the full run identifier
    - issues: array of detected issues
    - [OPTIONAL] tokens: {prompt, completion, total}
    - [OPTIONAL] cost: {total_usd}
    - [OPTIONAL] timing: {duration_s}
    """

    if not os.path.isdir(results_dir):
        raise ValueError(
            f"Results directory {results_dir} does not exist or is not a directory."
        )

    total_analysed_files = 0
    results_by_model = defaultdict(list)

    # Iterate over run directories in results_dir
    for run_id in sorted(os.listdir(results_dir)):
        run_dir = os.path.join(results_dir, run_id)
        if not os.path.isdir(run_dir):
            continue

        cases_dir = os.path.join(run_dir, "cases")
        if not os.path.isdir(cases_dir):
            print(f"Warning: No cases directory in {run_dir}")
            continue

        print(f"\nProcessing run: {run_id}")
        for root, _, files in os.walk(cases_dir):
            for filename in files:
                if not filename.endswith(".json"):
                    print("No json files found.")
                    continue

                result_file_path = os.path.join(root, filename)

                try:
                    with open(result_file_path, "r", encoding="utf-8") as file:
                        result_data = json.load(file)

                    case_id = result_data.get("case_id")
                    if not case_id:
                        print(f"Warning: No case_id found in {result_file_path}")
                        continue

                    # Extract course, exercise, variant from case_id
                    # case_id format: "ITP2425/H01E01-Lectures/003"
                    parts = case_id.split("/")
                    if len(parts) != 3:
                        print(f"Warning: Unexpected case_id format: {case_id}")
                        continue
                    course, exercise, variant = parts

                    # Extract model name from run_id or file structure
                    # run_id format: "openai-o4-mini-medium-2025-10-20-1207-e8aa62"
                    # Use the directory name (run_id) as the source of truth for the model identifier
                    # to ensure we capture differences like reasoning effort (medium/high) that might
                    # be missing from the internal JSON run_id.
                    model_name = run_id

                    unified_model_name = unify_model_name(model_name)                    # Find corresponding gold standard file
                    # Assume gold standard is in data/<course>/<exercise>/variants/<variant>/<variant>.json
                    project_root = Path(__file__).resolve().parents[2]
                    gold_standard_path = project_root / "data" / course / exercise / "variants" / variant / f"{variant}.json"

                    if not os.path.isfile(gold_standard_path):
                        print(f"Warning: Gold standard not found for {case_id}: {gold_standard_path}")
                        continue

                    # Load gold issues using the metrics function
                    gold_issues, gold_path = load_gold_issues(
                        course=course,
                        exercise=exercise,
                        variant=variant,
                        data_root=project_root / "data"
                    )

                    if gold_issues is None:
                        print(f"Warning: Gold standard not found: {gold_path}")
                        continue

                    # Extract predicted issues using the metrics function
                    pred_issues, is_empty = extract_prediction_issues(result_data)

                    if is_empty:
                        print(f"Warning: No issues found in {result_file_path}")
                        continue



                    # Evaluate the run
                    try:
                        tp, fp, fn, span_sum, iou_sum, match_count = evaluate_case(gold_issues, pred_issues)
                        #tp, fp, fn, span_sum, iou_sum, match_count = evaluate_run(gold_issues, pred_issues)

                        # Calculate metrics
                        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

                        # Calculate average span F1 and IoU
                        avg_span_f1 = span_sum / match_count if match_count > 0 else 0.0
                        avg_iou = iou_sum / match_count if match_count > 0 else 0.0



                        # Extract tokens/timing/cost
                        tokens_data = result_data.get("tokens", {})
                        prompt_tokens = tokens_data.get("prompt", 0)

                        timing_data = result_data.get("timing", {})
                        duration_s = timing_data.get("duration_s") or timing_data.get("durationS") or 0

                        cost_data = result_data.get("cost") or result_data.get("costs") or {}
                        total_cost = cost_data.get("total_usd") or cost_data.get("totalUsd") or 0

                        # Store result grouped by model
                        results_by_model[unified_model_name].append({
                            "variant": variant,
                            "exercise": f"{course}/{exercise}",
                            "case_id": case_id,
                            "run_id": result_data.get("run_id"),
                            "prompt_tokens": prompt_tokens,
                            "f1": f1,
                            "precision": precision,
                            "recall": recall,
                            "span_f1": avg_span_f1,
                            "iou": avg_iou,
                            "duration_s": duration_s,
                            "cost_usd": total_cost,
                            "tp": tp,
                            "fp": fp,
                            "fn": fn
                        })

                        total_analysed_files += 1

                    except Exception as e:
                        print(f"Error evaluating {case_id}: {e}")
                        continue
                except Exception as e:
                    print(f"Error loading {result_file_path}: {e}")
                    continue


    # Sort results by case_id within each model
    sorted_results_by_model = {}
    for model_name, results in results_by_model.items():
        sorted_results_by_model[model_name] = sorted(
            results,
            key=lambda x: x["case_id"]
        )

    # Save results
    output_file = f"{results_dir}/variants_report.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(sorted_results_by_model, file, indent=2)

    print(f"\n=== Summary ===")
    print(f"Total result files processed: {total_analysed_files}")
    print(f"Models analyzed: {list(results_by_model.keys())}")
    print(f"Results saved to: {output_file}")