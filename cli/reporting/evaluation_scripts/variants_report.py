#!/usr/bin/env python3
"""
Evaluation script for variant tests. Purpose is
to iterate through all the variants and calculate the
accuracy aka F1 Value for each test, combine it with
input token size and save in a dictionary, grouped by
model type.

Plot the result in a graph and calculate Pearson
correlation between input token size and F1 Value.
"""

import os
import json
from pathlib import Path
import re
from cli.reporting.metrics import (
    extract_prediction_issues,
    load_gold_issues,
    issue_to_tokens,
    greedy_match,
    evaluate_case
)

from collections import defaultdict
from typing import Dict, List, Tuple, Set

# TODO: we dont have run_id in filename, now it 
def get_run_id_from_filename(filename) -> str | None:
    """Extract run ID from filename.
    '20250727_091546_65d45dbb_result.json' -> '65d45dbb'
    """
    match = re.search(r"_(\w+)_result\.json$", filename)
    if match:
        return match.group(1)
    else:
        return None


def get_stats_file_with_run_id(result_file_path, run_id) -> str | None:
    """
    Get the corresponding stats file for a given result
    file and run ID.
    """
    dir = os.path.dirname(result_file_path)
    expected_stat_file = f"{run_id}_stats.json"

    for file in os.listdir(dir):
        if file.endswith(expected_stat_file):
            stats_file_path = os.path.join(dir, file)
            return stats_file_path
    return None


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
    # normalise Flash Lite preview identifiers
    if "flash-lite" in short:
        return "gemini-2.5-flash-lite"
    return short

def process_variant(gt_path: str, pred_path: str) -> Tuple[List[Dict], List[Dict]]:
    """Load and prepare gold and predicted issues for a single variant run."""
    gold = json.load(open(gt_path, "r", encoding="utf-8"))
    gold_issues = []
    for issue in gold.get("issues", []):
        tokens = issue_to_tokens(issue)
        gold_issues.append(
            {"category": issue["category"], "tokens": tokens, "raw": issue}
        )
    pred = json.load(open(pred_path, "r", encoding="utf-8"))
    response = pred.get("response", {})
    pred_issues = []
    for issue in response.get("issues", []):
        tokens = issue_to_tokens(issue)
        pred_issues.append(
            {"category": issue.get("category"), "tokens": tokens, "raw": issue}
        )
    return gold_issues, pred_issues


def evaluate_run(gold_issues: List[Dict], pred_issues: List[Dict]) -> Tuple[
    int,
    int,
    int,
    List[Tuple[int, int, float, float]],
    Dict[str, Tuple[int, int, int, float, float, int]],
]:
    """Evaluate a single model run on one variant.

    Returns overall TP, FP, FN counts, the list of matches, and per‑category
    statistics capturing TP, FP, FN and sums of span F1 and IoU.
    """
    matches, matched_pred, matched_gold = greedy_match(pred_issues, gold_issues)
    tp = len(matches)
    fp = len(pred_issues) - tp
    fn = len(gold_issues) - tp
    per_cat: Dict[str, List] = defaultdict(lambda: [0, 0, 0, 0.0, 0.0, 0])
    for pred_idx, _, f1, iou in matches:
        cat = pred_issues[pred_idx]["category"]
        stats = per_cat[cat]
        stats[0] += 1  # TP
        stats[3] += f1
        stats[4] += iou
        stats[5] += 1
    for i, p in enumerate(pred_issues):
        if i not in matched_pred:
            stats = per_cat[p["category"]]
            stats[1] += 1  # FP
    for j, g in enumerate(gold_issues):
        if j not in matched_gold:
            stats = per_cat[g["category"]]
            stats[2] += 1  # FN
    return tp, fp, fn, matches, per_cat


# ---------------------------------------------------


def iterate_test_files(results_dir: str) -> None:
    """
    Iterate through all result files in results/pecv-reference/<run-id>/cases/
    and extract required information.
    
    New structure:
    results/pecv-reference/<run-id>/cases/<course>/<exercise>/<variant>.json
    
    Each JSON contains:
    - case_id: "ITP2425/H01E01-Lectures/003" (course/exercise/variant)
    - run_id: the full run identifier
    - issues: array of detected issues
    - tokens: {prompt, completion, total}
    - cost: {total_usd}
    - timing: {duration_s}
    """

    #results_dir = project_root / "results" / "pecv-reference"

    if not os.path.isdir(results_dir):
        raise ValueError(
            f"Results directory {results_dir} does not exist or is not a directory."
        )

    total_analysed_files = 0
    results_by_model = defaultdict(list)

    # Iterate over run directories in results_dir: "results/pecv-reference/"
    for run_id in sorted(os.listdir(results_dir)):
        run_dir = os.path.join(results_dir, run_id)
        if not os.path.isdir(run_dir):
            continue
        
        cases_dir = os.path.join(run_dir, "cases")
        if not os.path.isdir(cases_dir):
            print(f"Warning: No cases directory in {run_dir}")
            continue

        print(f"\nProcessing run: {run_id}")
        for root, dirs, files in os.walk(cases_dir):
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
                    # Extract model portion (everything before reasoning effort and timestamp)
                    model_name = result_data.get("run_id", run_id)
                    # Simple heuristic: take everything before "-medium-" or "-low-" or "-high-"
                    for effort in ["-medium-", "-low-", "-high-"]:
                        if effort in model_name:
                            model_name = model_name.split(effort)[0]
                            break
                    
                    unified_model_name = unify_model_name(model_name)

                    # Find corresponding gold standard file
                    # Assume gold standard is in data/<course>/<exercise>/variants/<variant>/<variant>.json
                    project_root = Path(__file__).resolve().parents[3]
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
                        print(f"Warning: No prediction issues found in {result_file_path}")
                        continue



                    # Evaluate the run
                    try:
                        tp, fp, fn, span_sum, iou_sum, match_count = evaluate_case(gold_issues, pred_issues)
                        
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
                        duration_s = timing_data.get("duration_s", 0)
                        
                        cost_data = result_data.get("cost", {})
                        total_cost = cost_data.get("total_usd", 0)
                        
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


    # Save results
    output_file = "cli/reporting/evaluation_scripts/variants_report.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(dict(results_by_model), file, indent=2)

    print(f"\n=== Summary ===")
    print(f"Total result files processed: {total_analysed_files}")
    print(f"Models analyzed: {list(results_by_model.keys())}")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    # Point to results directory
    project_root = Path(__file__).resolve().parents[3]
    results_dir = project_root / "results" / "pecv-reference"
    iterate_test_files(results_dir=str(results_dir))
