from __future__ import annotations

import json
import os
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Optional


def _analyze_patch_file(patch_path: Path) -> dict:
    if not patch_path.is_file():
        return {}

    try:
        content = patch_path.read_text(encoding="utf-8")
    except OSError:
        return {}

    changes = {
        "repositories": set(),
        "file_types": Counter(),
        "changed_files": [],
        "total_additions": 0,
        "total_deletions": 0,
        "total_modifications": 0,
        "line_ranges": [],
    }

    current_file: Optional[str] = None
    in_hunk = False

    for line in content.splitlines():
        if line.startswith("diff -ruN"):
            parts = line.split()
            if len(parts) >= 4:
                new_path = parts[3][2:]
                current_file = new_path

                if current_file.startswith("solution/"):
                    changes["repositories"].add("solution")
                elif current_file.startswith("template/"):
                    changes["repositories"].add("template")
                elif current_file.startswith("tests/"):
                    changes["repositories"].add("tests")
                elif current_file == "problem-statement.md" or "problem-statement" in current_file:
                    changes["repositories"].add("problem_statement")

                if current_file.endswith(".java"):
                    changes["file_types"]["java"] += 1
                elif current_file.endswith(".py"):
                    changes["file_types"]["python"] += 1
                elif current_file.endswith(".md"):
                    changes["file_types"]["markdown"] += 1
                else:
                    changes["file_types"]["other"] += 1

                changes["changed_files"].append(current_file)

        elif line.startswith("@@"):
            import re

            match = re.match(r"@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@", line)
            if match:
                old_start = int(match.group(1))
                old_count = int(match.group(2)) if match.group(2) else 1
                new_start = int(match.group(3))
                new_count = int(match.group(4)) if match.group(4) else 1

                changes["line_ranges"].append(
                    {
                        "file": current_file,
                        "old_start": old_start,
                        "old_count": old_count,
                        "new_start": new_start,
                        "new_count": new_count,
                    }
                )
                in_hunk = True

        elif in_hunk and line:
            if line.startswith("+") and not line.startswith("+++"):
                changes["total_additions"] += 1
            elif line.startswith("-") and not line.startswith("---"):
                changes["total_deletions"] += 1

        elif not line.strip():
            in_hunk = False

    changes["total_modifications"] = min(
        changes["total_additions"], changes["total_deletions"]
    )
    changes["repositories"] = list(changes["repositories"])
    changes["file_types"] = dict(changes["file_types"])
    return changes


def summarise_dataset(data_root: Path | str, included_exercises: Optional[set[str]] = None) -> dict:
    root = Path(data_root)
    course_counts: Dict[str, Dict[str, int]] = {}
    ex_counts: Dict[str, int] = {}
    cat_counts: Counter[str] = Counter()
    artefact_counts: Counter[str] = Counter()

    injection_repos: Counter[str] = Counter()
    injection_file_types: Counter[str] = Counter()
    injection_patterns: Counter[str] = Counter()
    total_patch_changes = {
        "additions": 0,
        "deletions": 0,
        "modifications": 0,
        "files_changed": 0,
    }

    total_variants = 0
    total_issues = 0

    if not root.exists():
        raise FileNotFoundError(f"Dataset directory not found: {root}")

    for course_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        course_counts[course_dir.name] = {}
        for exercise_dir in sorted(p for p in course_dir.iterdir() if p.is_dir()):
            if included_exercises and exercise_dir.name not in included_exercises:
                continue

            variants_dir = exercise_dir / "variants"
            if not variants_dir.is_dir():
                continue

            exercise_key = f"{course_dir.name}/{exercise_dir.name}"

            for variant_dir in sorted(p for p in variants_dir.iterdir() if p.is_dir()):
                variant_id = variant_dir.name
                gold_path = variant_dir / f"{variant_id}.json"
                patch_path = variant_dir / f"{variant_id}.patch"

                if not gold_path.is_file():
                    continue

                total_variants += 1
                ex_counts[exercise_key] = ex_counts.get(exercise_key, 0) + 1
                course_counts[course_dir.name][exercise_dir.name] = (
                    course_counts[course_dir.name].get(exercise_dir.name, 0) + 1
                )

                try:
                    annotation = json.loads(gold_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    continue

                issues = annotation.get("issues", [])
                total_issues += len(issues)
                for issue in issues:
                    category = issue.get("category")
                    if category:
                        cat_counts[category] += 1
                    locations = issue.get("related_locations", [])
                    types = {loc.get("type") for loc in locations if loc.get("type")}
                    for loc_type in types:
                        artefact_counts[loc_type] += 1

                if patch_path.is_file():
                    patch_info = _analyze_patch_file(patch_path)

                    for repo in patch_info.get("repositories", []):
                        injection_repos[repo] += 1
                    for file_type, count in patch_info.get("file_types", {}).items():
                        injection_file_types[file_type] += count

                    total_patch_changes["additions"] += patch_info.get("total_additions", 0)
                    total_patch_changes["deletions"] += patch_info.get("total_deletions", 0)
                    total_patch_changes["modifications"] += patch_info.get("total_modifications", 0)
                    total_patch_changes["files_changed"] += len(
                        patch_info.get("changed_files", [])
                    )

                    repos = set(patch_info.get("repositories", []))
                    if len(repos) == 1:
                        repo = next(iter(repos))
                        injection_patterns[f"{repo}_only"] += 1
                    elif len(repos) == 2:
                        combo = "_".join(sorted(repos))
                        injection_patterns[combo] += 1
                    elif len(repos) >= 3:
                        injection_patterns["multi_repo"] += 1

    avg_changes = {
        key: (value / total_variants if total_variants else 0)
        for key, value in total_patch_changes.items()
    }

    return {
        "variants_per_course": course_counts,
        "variants_per_exercise": ex_counts,
        "total_annotated_variants": total_variants,
        "total_issues": total_issues,
        "issues_per_category": dict(cat_counts),
        "issues_per_artifact": dict(artefact_counts),
        "injection_analysis": {
            "repositories_affected": dict(injection_repos),
            "file_types_affected": dict(injection_file_types),
            "injection_patterns": dict(injection_patterns),
            "total_changes": total_patch_changes,
            "avg_changes_per_variant": avg_changes,
        },
    }

