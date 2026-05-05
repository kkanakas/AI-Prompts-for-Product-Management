from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path

from evals.types import EvalResult

_DEFAULT_RESULTS_DIR = Path(__file__).parent.parent / "results"


def write(
    results: list[EvalResult],
    tier: str,
    filter_desc: str | None = None,
    results_dir: Path | None = None,
) -> Path:
    out_dir = results_dir or _DEFAULT_RESULTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "latest-report.md"

    passed = sum(1 for r in results if r.structural_passed)
    scores = [r.overall_score for r in results if r.overall_score is not None]
    avg_score = round(sum(scores) / len(scores), 2) if scores else None
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Evals Report",
        "",
        f"**Date:** {timestamp}  ",
        f"**Tier:** {tier}  ",
        f"**Filter:** {filter_desc or 'all'}  ",
        "",
        "## Summary",
        "",
        "| Total | Passed | Failed | Avg Score |",
        "|---|---|---|---|",
        f"| {len(results)} | {passed} | {len(results) - passed} | {avg_score or '—'} |",
        "",
        "## Results",
        "",
        "| Prompt | Structural | Score | Duration | Status |",
        "|---|---|---|---|---|",
    ]

    for r in results:
        n_passed = sum(1 for c in r.structural_checks if c.passed)
        n_total = len(r.structural_checks)
        score_str = f"{r.overall_score:.1f}" if r.overall_score is not None else "—"
        status = "PASS" if r.structural_passed else "FAIL"
        lines.append(
            f"| {r.prompt_id} | {n_passed}/{n_total} | {score_str} | {r.duration_ms}ms | {status} |"
        )

    failures = [r for r in results if not r.structural_passed]
    if failures:
        lines += ["", "## Failures", ""]
        for r in failures:
            lines.append(f"### {r.prompt_id}")
            lines.append("")
            for c in r.structural_checks:
                if not c.passed:
                    lines.append(f"- **{c.name}**: {c.message}")
            if r.llm_scores:
                for s in r.llm_scores:
                    if s.score < 3:
                        lines.append(f"- **judge {s.dimension}** {s.score}/5: {s.rationale}")
            lines.append("")

    out_path.write_text("\n".join(lines))
    return out_path
