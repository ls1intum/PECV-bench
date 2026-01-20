from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List

from cli.utils import (
	DATA_ROOT,
	ExerciseIdentifier,
	iter_exercises,
)

from pecv_reference.consistency_check.models import (  # type: ignore[import]
	SemanticConsistencyIssueCategory,
	StructuralConsistencyIssueCategory,
)


BASE_ARTIFACTS = [
	"problem-statement.md",
	"solution",
	"template",
	"tests",
	"exercise-details.json",
]

ALL_CATEGORIES = {
	"METHOD_RETURN_TYPE_MISMATCH": StructuralConsistencyIssueCategory.METHOD_RETURN_TYPE_MISMATCH,
	"METHOD_PARAMETER_MISMATCH": StructuralConsistencyIssueCategory.METHOD_PARAMETER_MISMATCH,
	"CONSTRUCTOR_PARAMETER_MISMATCH": StructuralConsistencyIssueCategory.CONSTRUCTOR_PARAMETER_MISMATCH,
	"ATTRIBUTE_TYPE_MISMATCH": StructuralConsistencyIssueCategory.ATTRIBUTE_TYPE_MISMATCH,
	"VISIBILITY_MISMATCH": StructuralConsistencyIssueCategory.VISIBILITY_MISMATCH,
	"IDENTIFIER_NAMING_INCONSISTENCY": SemanticConsistencyIssueCategory.IDENTIFIER_NAMING_INCONSISTENCY,
}


@dataclass
class VariantStatus:
	variant_id: str
	category: str | None
	description: str | None
	has_patch: bool
	has_annotation: bool
	is_materialized: bool
	outputs_count: int


class VariantManager:
	def __init__(self, exercise: ExerciseIdentifier) -> None:
		self.exercise = exercise
		self.exercise_path = DATA_ROOT / exercise.relative
		if not self.exercise_path.exists():
			raise FileNotFoundError(f"Exercise not found: {exercise.relative}")
		self.variants_path = self.exercise_path / "variants"
		self.variants_path.mkdir(parents=True, exist_ok=True)

	def _variant_dir(self, variant_id: str) -> Path:
		path = self.variants_path / variant_id
		if not path.exists():
			raise FileNotFoundError(
				f"Variant {variant_id} missing under {self.exercise.relative}"
			)
		return path

	def list_variants(self) -> List[VariantStatus]:
		statuses: list[VariantStatus] = []
		for variant_dir in sorted(
			(p for p in self.variants_path.iterdir() if p.is_dir()),
			key=lambda p: p.name,
		):
			variant_id = variant_dir.name
			patch_path = variant_dir / f"{variant_id}.patch"
			annotation_path = variant_dir / f"{variant_id}.json"
			outputs_dir = variant_dir / "outputs"

			desc_file = next(variant_dir.glob(f"{variant_id}.*.md"), None)
			category = None
			description = None
			if desc_file:
				parts = desc_file.stem.split(".")
				if len(parts) >= 2:
					category = parts[1]
				try:
					first_line = desc_file.read_text(encoding="utf-8").strip().splitlines()[0]
				except (IndexError, OSError):
					first_line = None
				description = first_line

			statuses.append(
				VariantStatus(
					variant_id=variant_id,
					category=category,
					description=description,
					has_patch=patch_path.exists() and patch_path.stat().st_size > 0,
					has_annotation=annotation_path.exists(),
					is_materialized=(variant_dir / "template").exists(),
					outputs_count=len(list(outputs_dir.glob("*_result.json"))) if outputs_dir.exists() else 0,
				)
			)
		return statuses

	def get_next_variant_number(self) -> str:
		numbers = [
			int(p.name)
			for p in self.variants_path.iterdir()
			if p.is_dir() and p.name.isdigit()
		]
		if not numbers:
			return "001"
		return f"{max(numbers) + 1:03d}"

	def init_variant(
		self,
		category: str,
		description: str,
		variant_id: str | None = None,
	) -> str:
		if category not in ALL_CATEGORIES:
			raise ValueError(f"Unknown category '{category}'.")

		resolved_variant_id = variant_id or self.get_next_variant_number()
		target_dir = self.variants_path / resolved_variant_id
		if target_dir.exists():
			raise FileExistsError(f"Variant {resolved_variant_id} already exists")

		target_dir.mkdir(parents=True)

		for artefact in BASE_ARTIFACTS:
			src = self.exercise_path / artefact
			dst = target_dir / artefact
			if not src.exists():
				continue
			if src.is_dir():
				shutil.copytree(src, dst, dirs_exist_ok=True)
			else:
				shutil.copy2(src, dst)

		desc_file = target_dir / f"{resolved_variant_id}.{category}.md"
		desc_file.write_text(f"{description}\n", encoding="utf-8")

		return resolved_variant_id

	def create_patch(self, variant_id: str) -> Path:
		variant_dir = self._variant_dir(variant_id)
		patch_path = variant_dir / f"{variant_id}.patch"

		with tempfile.TemporaryDirectory() as tmp:
			tmp_root = Path(tmp)
			base_tmp = tmp_root / "base"
			variant_tmp = tmp_root / "variant"
			base_tmp.mkdir()
			variant_tmp.mkdir()

			for artefact in BASE_ARTIFACTS:
				src = self.exercise_path / artefact
				if not src.exists():
					continue
				dst = base_tmp / artefact
				if src.is_dir():
					shutil.copytree(src, dst)
				else:
					dst.parent.mkdir(parents=True, exist_ok=True)
					shutil.copy2(src, dst)

			for artefact in BASE_ARTIFACTS:
				src = variant_dir / artefact
				if not src.exists():
					continue
				dst = variant_tmp / artefact
				if src.is_dir():
					shutil.copytree(src, dst)
				else:
					dst.parent.mkdir(parents=True, exist_ok=True)
					shutil.copy2(src, dst)

			diff = subprocess.run(
				["diff", "-ruN", str(base_tmp), str(variant_tmp)],
				text=True,
				capture_output=True,
				check=False,
			)

		if diff.stdout:
			content = diff.stdout.replace(str(base_tmp), "a").replace(str(variant_tmp), "b")
			patch_path.write_text(content, encoding="utf-8")
		else:
			patch_path.write_text("", encoding="utf-8")

		return patch_path

	def materialize_variant(self, variant_id: str, force: bool = False) -> Path:
		variant_dir = self._variant_dir(variant_id)

		if force:
			self.clean_variant(variant_id, keep_outputs=True)

		copied_any = False
		for artefact in BASE_ARTIFACTS:
			src = self.exercise_path / artefact
			dst = variant_dir / artefact
			if dst.exists() or not src.exists():
				continue
			if src.is_dir():
				shutil.copytree(src, dst, dirs_exist_ok=True)
			else:
				dst.parent.mkdir(parents=True, exist_ok=True)
				shutil.copy2(src, dst)
			copied_any = True

		patch_file = variant_dir / f"{variant_id}.patch"
		if copied_any and patch_file.exists() and patch_file.stat().st_size > 0:
			result = subprocess.run(
				["patch", "-p1", "--forward", "--batch"],
				cwd=variant_dir,
				text=True,
				input=patch_file.read_text(encoding="utf-8"),
				capture_output=True,
			)
			if result.returncode != 0:
				self.clean_variant(variant_id, keep_outputs=True)
				raise RuntimeError(
					f"Failed to apply patch for {variant_id}: {result.stderr or result.stdout}"
				)

		return variant_dir

	def clean_variant(self, variant_id: str, keep_outputs: bool = False) -> None:
		variant_dir = self._variant_dir(variant_id)
		for artefact in BASE_ARTIFACTS:
			target = variant_dir / artefact
			if target.is_dir():
				shutil.rmtree(target, ignore_errors=True)
			elif target.exists():
				target.unlink()

		if not keep_outputs:
			outputs_dir = variant_dir / "outputs"
			if outputs_dir.exists():
				shutil.rmtree(outputs_dir, ignore_errors=True)

		for extra in variant_dir.glob("*.rej"):
			extra.unlink()
		for extra in variant_dir.glob("*.orig"):
			extra.unlink()

	def generate_annotation(
		self,
		variant_id: str,
		model: str,
		reasoning_effort: str,
		force_materialize: bool = False,
	) -> Path:
		from pecv_reference.runner import (  # type: ignore[import]
			run_consistency_check,
		)

		variant_dir = self.materialize_variant(variant_id, force=force_materialize)
		case_id = f"{self.exercise.relative}/{variant_id}"

		with tempfile.TemporaryDirectory() as tmp:
			tmp_output = Path(tmp) / f"{variant_id}_result.json"

			run_consistency_check(
				input_path=variant_dir,
				output_path=tmp_output,
				model_name=model,
				reasoning_effort=reasoning_effort,
				case_id=case_id,
			)

			data = json.loads(tmp_output.read_text(encoding="utf-8"))

		residual_outputs = variant_dir / "outputs"
		if residual_outputs.exists():
			shutil.rmtree(residual_outputs, ignore_errors=True)

		annotation = {
			"case_id": case_id,
			"issues": data.get("issues", []),
		}

		annotation_path = variant_dir / f"{variant_id}.json"
		annotation_path.write_text(
			json.dumps(annotation, indent=2, ensure_ascii=False) + "\n",
			encoding="utf-8",
		)

		return annotation_path


def resolve_exercises(value: str | None) -> list[ExerciseIdentifier]:
	if value:
		identifier = ExerciseIdentifier.parse(value)
		if not (DATA_ROOT / identifier.relative).exists():
			raise FileNotFoundError(f"Exercise directory not found: {identifier.relative}")
		return [identifier]
	return list(iter_exercises())


def handle_list(args: argparse.Namespace) -> int:
	exercises = resolve_exercises(args.exercise)
	for idx, exercise in enumerate(exercises):
		manager = VariantManager(exercise)
		statuses = manager.list_variants()
		if idx or len(exercises) > 1:
			print(f"== {exercise.relative} ==")
		if not statuses:
			print("No variants yet.")
		for status in statuses:
			flags: list[str] = []
			flags.append("patch" if status.has_patch else "missing patch")
			flags.append("annotation" if status.has_annotation else "missing annotation")
			flags.append("materialized" if status.is_materialized else "not materialized")
			if status.outputs_count:
				flags.append(f"{status.outputs_count} outputs")
			category = status.category or "UNKNOWN"
			description = f" - {status.description}" if status.description else ""
			print(f"- {status.variant_id} [{category}]: {', '.join(flags)}{description}")
		if len(exercises) > 1 and idx < len(exercises) - 1:
			print()
	return 0


def handle_init(args: argparse.Namespace) -> int:
	exercise = ExerciseIdentifier.parse(args.exercise)
	manager = VariantManager(exercise)
	variant_id = manager.init_variant(args.category, args.description, args.variant)
	if not args.skip_materialize:
		manager.materialize_variant(variant_id, force=args.force_materialize)
		print(
			f"Initialized and materialized variant {variant_id} under {exercise.relative}"
		)
	else:
		print(f"Initialized variant {variant_id} under {exercise.relative}")
	return 0


def handle_create_patch(args: argparse.Namespace) -> int:
	exercise = ExerciseIdentifier.parse(args.exercise)
	manager = VariantManager(exercise)
	path = manager.create_patch(args.variant)
	if path.read_text(encoding="utf-8").strip():
		print(f"Generated patch at {path}")
	else:
		print(f"No differences detected; created empty patch at {path}")
	return 0


def handle_materialize(args: argparse.Namespace) -> int:
	exercise = ExerciseIdentifier.parse(args.exercise)
	manager = VariantManager(exercise)
	manager.materialize_variant(args.variant, force=args.force)
	print(f"Materialized variant {args.variant} under {exercise.relative}")
	return 0


def handle_materialize_all(args: argparse.Namespace) -> int:
	exercises = resolve_exercises(args.exercise)
	for exercise in exercises:
		manager = VariantManager(exercise)
		print(f"==> {exercise.relative}")
		for status in manager.list_variants():
			try:
				manager.materialize_variant(status.variant_id, force=args.force)
				print(f"  materialized {status.variant_id}")
			except Exception as exc:  # noqa: BLE001 - CLI reporting
				print(f"  {status.variant_id}: {exc}")
	return 0


def handle_clean(args: argparse.Namespace) -> int:
	exercise = ExerciseIdentifier.parse(args.exercise)
	manager = VariantManager(exercise)
	manager.clean_variant(args.variant, keep_outputs=args.keep_outputs)
	print(f"Cleaned materialized artefacts for variant {args.variant}")
	return 0


def handle_clean_all(args: argparse.Namespace) -> int:
	exercises = resolve_exercises(args.exercise)
	for exercise in exercises:
		manager = VariantManager(exercise)
		print(f"==> {exercise.relative}")
		for status in manager.list_variants():
			manager.clean_variant(status.variant_id, keep_outputs=args.keep_outputs)
			print(f"  cleaned {status.variant_id}")
	return 0


def handle_generate_annotation(args: argparse.Namespace) -> int:
	exercise = ExerciseIdentifier.parse(args.exercise)
	manager = VariantManager(exercise)
	annotation = manager.generate_annotation(
		args.variant,
		model=args.model,
		reasoning_effort=args.reasoning_effort,
		force_materialize=args.force_materialize,
	)
	print(f"Generated annotation at {annotation}")
	return 0


def register_subcommand(parser: argparse.ArgumentParser) -> None:
	parser.set_defaults(handler=lambda _args: parser.print_help() or 0)
	subparsers = parser.add_subparsers(dest="variants_command")

	list_parser = subparsers.add_parser("list", help="List variants and their status")
	list_parser.add_argument("--exercise", "-e", help="Course/exercise path")
	list_parser.set_defaults(handler=handle_list)

	init_parser = subparsers.add_parser("init", help="Initialise a new variant stub")
	init_parser.add_argument("--exercise", "-e", required=True)
	init_parser.add_argument("--category", "-c", required=True, choices=sorted(ALL_CATEGORIES))
	init_parser.add_argument("--description", "-d", required=True)
	init_parser.add_argument("--variant", "-v")
	init_parser.add_argument(
		"--skip-materialize",
		action="store_true",
		help="Create the variant but leave artefacts dematerialized",
	)
	init_parser.add_argument(
		"--force-materialize",
		action="store_true",
		help="Recreate artefacts even if they already exist",
	)
	init_parser.set_defaults(handler=handle_init)

	patch_parser = subparsers.add_parser("create-patch", help="Create a git-style patch for the variant")
	patch_parser.add_argument("--exercise", "-e", required=True)
	patch_parser.add_argument("--variant", "-v", required=True)
	patch_parser.set_defaults(handler=handle_create_patch)

	gen_parser = subparsers.add_parser("generate-annotation", help="Generate annotation via reference approach")
	gen_parser.add_argument("--exercise", "-e", required=True)
	gen_parser.add_argument("--variant", "-v", required=True)
	gen_parser.add_argument("--model", default="openai:gpt-5-mini")
	gen_parser.add_argument("--reasoning-effort", choices=["low", "medium", "high"], default="medium")
	gen_parser.add_argument("--force-materialize", action="store_true", help="Re-materialize variant before running")
	gen_parser.set_defaults(handler=handle_generate_annotation)

	materialize_parser = subparsers.add_parser("materialize", help="Materialize a single variant")
	materialize_parser.add_argument("--exercise", "-e", required=True)
	materialize_parser.add_argument("--variant", "-v", required=True)
	materialize_parser.add_argument("--force", action="store_true")
	materialize_parser.set_defaults(handler=handle_materialize)

	materialize_all_parser = subparsers.add_parser("materialize-all", help="Materialize all variants")
	materialize_all_parser.add_argument("--exercise", "-e", help="Restrict to a specific exercise")
	materialize_all_parser.add_argument("--force", action="store_true")
	materialize_all_parser.set_defaults(handler=handle_materialize_all)

	clean_parser = subparsers.add_parser("clean", help="Remove materialised artefacts for a variant")
	clean_parser.add_argument("--exercise", "-e", required=True)
	clean_parser.add_argument("--variant", "-v", required=True)
	clean_parser.add_argument("--keep-outputs", action="store_true", help="Preserve outputs directory")
	clean_parser.set_defaults(handler=handle_clean)

	clean_all_parser = subparsers.add_parser("clean-all", help="Remove materialised artefacts for all variants")
	clean_all_parser.add_argument("--exercise", "-e", help="Restrict to a specific exercise")
	clean_all_parser.add_argument("--keep-outputs", action="store_true")
	clean_all_parser.set_defaults(handler=handle_clean_all)
