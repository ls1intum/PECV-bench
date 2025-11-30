from __future__ import annotations

import argparse
import shutil
import textwrap
from pathlib import Path

from cli.reporting.metrics import analyse_variants_runs
from cli.reporting.variants_report_plotter import generate_plots
from cli.utils import PROJECT_ROOT, RESULTS_ROOT

class RawAndDefaults(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
    pass


def variants_analysis_command(args: argparse.Namespace) -> int:
    """Run variants analysis to generate reports grouped by model."""


    # Resolve results directory
    if args.results_dir:
        results_dir = Path(args.results_dir).expanduser()
        if not results_dir.is_absolute():
            results_dir = PROJECT_ROOT / results_dir
    else:
        results_dir = RESULTS_ROOT / "pecv-reference"

    # Ensure directory exists
    if not results_dir.exists():
        print(f"Error: Results directory does not exist: {results_dir}")
        return 1

    json_file = results_dir / "variants_report.json"
    plots_dir = results_dir / "variants_report_plots"

    # Handle --clear flag (only clear, don't run analysis)
    if args.clear:
        print("\n=== Cleaning Previous Results ===")
        removed_items = []

        if json_file.exists():
            json_file.unlink()
            removed_items.append(str(json_file))
            print(f"Removed: {json_file}")

        if plots_dir.exists():
            shutil.rmtree(plots_dir)
            removed_items.append(str(plots_dir))
            print(f"Removed: {plots_dir}")

        if not removed_items:
            print("No previous results found to clear.")

        return 0

    # Run the analysis (always when not just clearing)
    print("\n=== Running Variants Analysis ===")
    analyse_variants_runs(str(results_dir))

    # Optionally generate plots
    if args.plot:
        if not json_file.exists():
            print(f"\nWarning: Cannot generate plots - {json_file} not found")
            return 1
    
        output_dir = f"{args.plot_output}/variants_report_plots" or str(plots_dir)

        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"\n=== Generating Plots ===")
        try:
            generate_plots(str(json_file), output_dir)
            print(f"\nPlots saved to: {output_dir}")
        except Exception as e:
            print(f"Error generating plots: {e}")
            return 1

    return 0


def register_subcommand(parser: argparse.ArgumentParser) -> None:
    """Register the variants-analysis subcommand."""
    parser.formatter_class = RawAndDefaults
    parser.set_defaults(handler=variants_analysis_command)
    parser.add_argument(
        "--results-dir",
        default=None,
        help=textwrap.dedent(
            """Path to results directory (default: results/pecv-reference)
JSON file created at: RESULTS_DIR/variants_report.json`
    {
    "model-name-1": [
        {
        "variant": "001",
        "exercise": "ITP2425/H01E01-Lectures",
        ... other fields ...
        }
    ],
    "model-name-2": [...],
    ...
    }
        """,
        )
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Remove previous results (variants_report.json and variants_report_plots folder\n in results/pecv-reference) before running analysis",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help=textwrap.dedent(
            """Runs the analysis and generates plots after analysis\nExpected structure:
    results/
    └── pecv-reference/
        ├── <timestamped-run-id>/
        │   ├── cases/
        │   └── run_report.json
        ├── variants_report_plots
        │   ├── per_mode.png - Scatter plots with one subplot per model, 
        |   |      showing relationship between prompt tokens (x-axis) and F1 score (y-axis)
        │   └── per_model_per_exercise.png - Grid of scatter plots, grouped by model (rows) and exercise (columns)
        ├── variants_report.json
        ├── summary.json
        ├── summary.md
        └── summary.tex
            """,
        )
    )
    parser.add_argument(
        "--plot-output",
        default=None,
        help="Output directory for plots\n(default: results_dir/variants_report_plots)"
    )