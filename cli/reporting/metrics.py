from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


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
    for location in issue.get("related_locations", []) or []:
        if not isinstance(location, dict):
            continue
        artifact_type = str(location.get("type") or "UNKNOWN")
        file_path = unify_path(location.get("file_path") or "")
        try:
            start_line = int(location.get("start_line", 0))
        except (TypeError, ValueError):
            start_line = 0
        try:
            end_line = int(location.get("end_line", start_line))
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

