from __future__ import annotations

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


def ensure_data_root() -> Path:
    if not DATA_ROOT.exists():
        raise FileNotFoundError(f"Dataset directory not found: {DATA_ROOT}")
    return DATA_ROOT


def ensure_results_root() -> Path:
    RESULTS_ROOT.mkdir(parents=True, exist_ok=True)
    return RESULTS_ROOT


def ensure_runs_root() -> Path:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    return RUNS_ROOT


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
        if len(parts) < 2:
            raise ValueError(
                "Exercise path must include course and exercise, e.g. "
                "ITP2425/H01E01-Lectures"
            )
        return cls(course=parts[0], exercise=parts[1])


def iter_exercises(data_root: Path | None = None) -> Iterable[ExerciseIdentifier]:
    root = data_root or ensure_data_root()
    for course_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for exercise_dir in sorted(p for p in course_dir.iterdir() if p.is_dir()):
            yield ExerciseIdentifier(course=course_dir.name, exercise=exercise_dir.name)
