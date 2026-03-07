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


def get_data_root(version: str = "V1") -> Path:
    """Resolve the data root for a specific version (V1, V2, ...)."""
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


def infer_version_from_path(path: Path) -> str:
    """Extract a version token (V1, V2, ...) from any component of the path.

    Falls back to 'V1' if none is found.
    """
    for part in path.parts:
        if part.startswith("V") and part[1:].isdigit():
            return part
    return "V1"


@dataclass
class ExerciseIdentifier:
    version: str
    course: str
    exercise: str

    @property
    def relative(self) -> str:
        """Course/exercise path without version. Used for case_id construction."""
        return f"{self.course}/{self.exercise}"

    @property
    def full_path(self) -> str:
        """Version/course/exercise path. Used for display."""
        return f"{self.version}/{self.course}/{self.exercise}"

    @classmethod
    def parse(cls, exercise_path: str) -> "ExerciseIdentifier":
        parts = [part for part in Path(exercise_path).parts if part]
        if len(parts) == 3:
            return cls(version=parts[0], course=parts[1], exercise=parts[2])
        if len(parts) == 2:
            # Backward-compat: COURSE/EXERCISE with no version defaults to V1
            return cls(version="V1", course=parts[0], exercise=parts[1])
        raise ValueError(
            "Exercise path must be VERSION/COURSE/EXERCISE or COURSE/EXERCISE, "
            "e.g. V2/IOS26/TC1-Bookstore or ITP2425/H01E01-Lectures"
        )


def iter_exercises(version: str | None = None) -> Iterable[ExerciseIdentifier]:
    """Iterate over all exercise directories.

    If *version* is given, only that version is scanned.
    If *version* is None, all version directories (V1, V2, …) are scanned.
    """
    if version:
        versions = [version]
    else:
        versions = sorted(
            p.name
            for p in DATA_ROOT.iterdir()
            if p.is_dir() and p.name.startswith("V") and p.name[1:].isdigit()
        )
    for ver in versions:
        root = DATA_ROOT / ver
        if not root.exists():
            continue
        for course_dir in sorted(p for p in root.iterdir() if p.is_dir()):
            for exercise_dir in sorted(p for p in course_dir.iterdir() if p.is_dir()):
                yield ExerciseIdentifier(
                    version=ver,
                    course=course_dir.name,
                    exercise=exercise_dir.name,
                )
