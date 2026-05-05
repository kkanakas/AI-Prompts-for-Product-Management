"""CLI for the evals harness.

Commands
--------
  run               Run evaluations (Tier 1 structural, optionally Tier 2 LLM)
  status            Show fixture/result status for every known prompt
  generate-fixtures Generate test fixtures from prompts
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Lazy imports — imported at module level so tests can monkeypatch them
# ---------------------------------------------------------------------------
from evals.runner import run_evals  # noqa: E402
from evals.reporters import terminal, json_reporter, markdown_reporter  # noqa: E402

# Results directory lives at <repo_root>/evals/results/
_RESULTS_DIR = Path(__file__).parent / "results"
_FIXTURES_DIR = Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _filter_desc(args: argparse.Namespace) -> str:
    """Build a human-readable filter description from parsed args."""
    if getattr(args, "changed_only", False):
        return "changed files"
    if getattr(args, "prompt", None):
        return f"prompt: {args.prompt}"
    if getattr(args, "category", None):
        return f"category: {args.category}"
    return "all prompts"


def _all_passed(results: list, tier: str) -> bool:
    """Return True only if every result passes all relevant checks."""
    for r in results:
        if not r.structural_passed:
            return False
        if tier == "all" and r.overall_score is not None and r.overall_score < 3.5:
            return False
    return True


# ---------------------------------------------------------------------------
# Sub-command handlers
# ---------------------------------------------------------------------------

def _cmd_run(args: argparse.Namespace) -> int:
    """Execute the `run` sub-command."""
    tier = args.tier

    # Tier 2 requires the Anthropic API key
    api_key: str | None = None
    if tier == "all":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print(
                "Error: --tier all requires ANTHROPIC_API_KEY to be set in the environment.",
                file=sys.stderr,
            )
            return 2

    results = run_evals(
        category=args.category,
        prompt_id=args.prompt,
        changed_only=args.changed_only,
        tier=tier,
        anthropic_api_key=api_key,
    )

    filter_desc = _filter_desc(args)

    # Render to terminal
    terminal.render(results, tier)

    # Write JSON and Markdown reports
    json_reporter.write(results, tier, filter_desc, _RESULTS_DIR)
    markdown_reporter.write(results, tier, filter_desc, _RESULTS_DIR)

    return 0 if _all_passed(results, tier) else 1


def _cmd_status(_args: argparse.Namespace) -> int:
    """Execute the `status` sub-command."""
    # Import here so the rest of the CLI doesn't depend on the mcp-server at
    # import time (makes monkeypatching in tests simpler).
    sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
    try:
        from server import load_all_prompts  # type: ignore[import-untyped]
    except Exception as exc:
        print(f"Warning: could not load prompts — {exc}", file=sys.stderr)
        prompts = []
    else:
        prompts = load_all_prompts()

    from rich.console import Console
    from rich.table import Table
    from rich import box

    console = Console()
    table = Table(box=box.SIMPLE_HEAVY, expand=False)
    table.add_column("Prompt ID", style="bold", no_wrap=True)
    table.add_column("Category", no_wrap=True)
    table.add_column("Has Fixture", justify="center")
    table.add_column("Last Result", justify="center")

    # Read last report once (if it exists)
    report_path = _RESULTS_DIR / "latest-report.md"
    last_results: dict[str, str] = {}
    if report_path.exists():
        for line in report_path.read_text().splitlines():
            # Rows look like: | prds/05-ai-prd | 5/5 | — | 123ms | PASS |
            if line.startswith("| ") and " | " in line:
                parts = [p.strip() for p in line.strip("|").split("|")]
                if len(parts) >= 5 and parts[4] in ("PASS", "FAIL"):
                    last_results[parts[0]] = parts[4]

    for prompt in prompts:
        pid = prompt.get("id", "")
        category = prompt.get("category", "")
        fixture_file = _FIXTURES_DIR / f"{pid}.json"
        has_fixture = "[green]Yes[/green]" if fixture_file.exists() else "[red]No[/red]"
        last = last_results.get(pid, "—")
        if last == "PASS":
            last = "[green]PASS[/green]"
        elif last == "FAIL":
            last = "[red]FAIL[/red]"
        table.add_row(pid, category, has_fixture, last)

    if not prompts:
        console.print("[yellow]No prompts found.[/yellow]")
    else:
        console.print(table)

    return 0


def _cmd_generate_fixtures(args: argparse.Namespace) -> int:
    """Execute the `generate-fixtures` sub-command."""
    category: str | None = getattr(args, "category", None)

    try:
        # Support the case where the module entry is set to None in sys.modules
        # (as test does) — treat that the same as missing.
        generator_mod = sys.modules.get("evals.fixtures.generator", "NOT_LOADED")
        if generator_mod is None:
            raise ImportError("evals.fixtures.generator is not available")
        if generator_mod == "NOT_LOADED":
            import importlib
            generator_mod = importlib.import_module("evals.fixtures.generator")
        generator_mod.generate_fixtures(category=category)
    except (ImportError, ModuleNotFoundError, AttributeError):
        print("Fixture generator not yet implemented.")
        return 0
    return 0


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m evals",
        description="Evals harness for AI Prompts for Product Management.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ── run ──────────────────────────────────────────────────────────────────
    run_p = sub.add_parser("run", help="Run evaluations.")
    run_p.add_argument(
        "--category",
        metavar="SLUG",
        default=None,
        help="Only evaluate prompts in this category.",
    )
    run_p.add_argument(
        "--prompt",
        metavar="ID",
        default=None,
        help="Only evaluate this specific prompt ID.",
    )
    run_p.add_argument(
        "--changed-only",
        action="store_true",
        default=False,
        help="Only evaluate prompts changed in the last commit.",
    )
    run_p.add_argument(
        "--tier",
        choices=["structural", "all"],
        default="structural",
        help="Evaluation tier: 'structural' (default) or 'all' (includes LLM judge).",
    )

    # ── status ───────────────────────────────────────────────────────────────
    sub.add_parser("status", help="Show fixture and result status for every prompt.")

    # ── generate-fixtures ────────────────────────────────────────────────────
    gen_p = sub.add_parser(
        "generate-fixtures", help="Generate evaluation fixtures from prompts."
    )
    gen_p.add_argument(
        "--category",
        metavar="SLUG",
        default=None,
        help="Only generate fixtures for prompts in this category.",
    )

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        exit_code = _cmd_run(args)
    elif args.command == "status":
        exit_code = _cmd_status(args)
    elif args.command == "generate-fixtures":
        exit_code = _cmd_generate_fixtures(args)
    else:  # pragma: no cover
        parser.print_help()
        exit_code = 1

    if exit_code != 0:
        sys.exit(exit_code)
