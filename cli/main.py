from __future__ import annotations

import argparse
import sys
from importlib import import_module
from typing import Callable

CommandRegistrar = Callable[[argparse.ArgumentParser], None]


def _load_command(module_path: str) -> CommandRegistrar:
    module = import_module(module_path)
    if not hasattr(module, "register_subcommand"):
        raise RuntimeError(f"Command module {module_path} missing register_subcommand")
    return getattr(module, "register_subcommand")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unified CLI for PECV benchmark dataset management, execution and evaluation.",
    )
    subparsers = parser.add_subparsers(dest="command")

    commands = {
        "variants": "cli.commands.variants",
        "run-benchmark": "cli.commands.run",
        "report": "cli.commands.report",
    }

    for command, module_path in commands.items():
        registrar = _load_command(module_path)
        registrar(subparsers.add_parser(command))

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args, unknown = parser.parse_known_args(argv)

    handler: Callable[[argparse.Namespace], int] | None = getattr(args, "handler", None)

    if handler is None:
        if unknown:
            parser.error(f"Unrecognized arguments: {' '.join(unknown)}")
        parser.print_help()
        return 0

    if unknown:
        command = getattr(args, "command", None)
        if command != "run-benchmark":
            parser.error(f"Unrecognized arguments: {' '.join(unknown)}")
        setattr(args, "_extra_args", unknown)

    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
