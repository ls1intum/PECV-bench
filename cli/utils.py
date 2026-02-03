from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_ROOT = PROJECT_ROOT / "pecv-reference"

if str(REFERENCE_ROOT) not in sys.path:
    sys.path.insert(0, str(REFERENCE_ROOT))
DATA_ROOT = PROJECT_ROOT / "data"
RESULTS_ROOT = PROJECT_ROOT / "results"
RUNS_ROOT = PROJECT_ROOT / "runs"
CONFIGS_ROOT = PROJECT_ROOT / "configs"


def timestamp_slug(dt: datetime | None = None) -> str:
    """Return a compact UTC timestamp slug helpful for run identifiers."""
    current = dt.astimezone(timezone.utc) if dt else datetime.now(timezone.utc)
    return current.strftime("%Y-%m-%d-%H%M-%S%f")


def get_data_root(version: str = "V1") -> Path:
    """Resolve the data root for a specific version (V1, V2)."""
    return DATA_ROOT / version


def ensure_data_root(version: str = "V1") -> Path:
    root = get_data_root(version)
    if not root.exists():
        raise FileNotFoundError(f"Dataset directory not found for version {version}: {root}")
    return root


def ensure_results_root() -> Path:
    RESULTS_ROOT.mkdir(parents=True, exist_ok=True)
    return RESULTS_ROOT


def ensure_runs_root() -> Path:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    return RUNS_ROOT


def add_version_flags(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--V1", action="store_true", help="Use V1 dataset (default)")
    group.add_argument("--V2", action="store_true", help="Use V2 dataset")


def get_version(args: argparse.Namespace) -> str:
    if hasattr(args, "V2") and args.V2:
        return "V2"
    return "V1"


@dataclass
class ExerciseIdentifier:
    course: str
    exercise: str

    @property
    def relative(self) -> str:
        return f"{self.course}/{self.exercise}"

    @classmethod
    def parse(cls, exercise_path: str) -> "ExerciseIdentifier":
        parts = [part for part in Path(exercise_path).parts if part]
        # Remove empty parts or parts that might be "V1"/"V2" if mistakenly passed
        # But generally we expect COURSE/EXERCISE here.
        if len(parts) < 2:
            raise ValueError(
                "Exercise path must include course and exercise, e.g. "
                "ITP2425/H01E01-Lectures"
            )
        # If the path happens to be absolute or relative to something else, we just take the last two parts
        # This handles cases like "data/V1/COURSE/EXERCISE" passed in by mistake, though we should encourage relative paths.
        return cls(course=parts[-2], exercise=parts[-1])


def iter_exercises(version: str = "V1") -> Iterable[ExerciseIdentifier]:
    root = ensure_data_root(version)
    for course_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for exercise_dir in sorted(p for p in course_dir.iterdir() if p.is_dir()):
            yield ExerciseIdentifier(course=course_dir.name, exercise=exercise_dir.name)
