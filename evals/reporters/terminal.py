from __future__ import annotations
from datetime import datetime

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from evals.types import EvalResult

_console = Console()


def render(results: list[EvalResult], tier: str) -> None:
    if not results:
        _console.print("[yellow]No results to display.[/yellow]")
        return

    table = Table(box=box.SIMPLE_HEAVY, show_footer=False, expand=True)
    table.add_column("Prompt", style="bold", no_wrap=True)
    table.add_column("Structural", justify="center")
    table.add_column("Score", justify="center")
    table.add_column("Duration", justify="right")
    table.add_column("Status", justify="center")

    passed_count = 0
    for r in results:
        n_passed = sum(1 for c in r.structural_checks if c.passed)
        n_total = len(r.structural_checks)
        structural_str = f"{n_passed}/{n_total} {'✓' if n_passed == n_total else '✗'}"
        score_str = f"{r.overall_score:.1f}/5" if r.overall_score is not None else "—"
        duration_str = f"{r.duration_ms / 1000:.1f}s"
        if r.structural_passed:
            status = "[green]PASS ✓[/green]"
            passed_count += 1
        else:
            status = "[red]FAIL ✗[/red]"
        table.add_row(r.prompt_id, structural_str, score_str, duration_str, status)

    failed_count = len(results) - passed_count
    scores = [r.overall_score for r in results if r.overall_score is not None]
    avg_score = sum(scores) / len(scores) if scores else None

    summary_parts = [f"{passed_count} passed · {failed_count} failed"]
    if avg_score is not None:
        summary_parts.append(f"avg {avg_score:.1f}/5")
    total_ms = sum(r.duration_ms for r in results)
    summary_parts.append(f"{total_ms / 1000:.0f}s")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = f"Evals Run ── {timestamp} ── tier: {tier} ── {len(results)} prompts"

    _console.print(Panel(table, title=title, subtitle=" · ".join(summary_parts)))

    failures = [r for r in results if not r.structural_passed]
    if failures:
        _console.print("\n[bold]Failures[/bold]")
        for r in failures:
            _console.print(f"  {r.prompt_id}")
            for c in r.structural_checks:
                if not c.passed:
                    _console.print(f"    [red]✗ structural: {c.message}[/red]")
            if r.llm_scores:
                for s in r.llm_scores:
                    if s.score < 3:
                        _console.print(
                            f"    [red]✗ judge {s.dimension} {s.score}/5: {s.rationale}[/red]"
                        )
