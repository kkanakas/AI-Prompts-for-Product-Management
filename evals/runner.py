from __future__ import annotations
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Reuse parse_prompt_file from mcp-server — single source of truth for prompt parsing
sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
from server import parse_prompt_file, PROMPTS_DIR  # noqa: E402

from evals.evaluators.structural import run_structural_checks
from evals.fixtures import load_fixture
from evals.types import EvalResult


def _extract_template_sections(template_text: str) -> list[str]:
    return [
        line.strip()
        for line in template_text.splitlines()
        if line.strip().startswith("## ")
    ]


def _fill_template(template: str, fixture_data: dict) -> str:
    filled = template
    for key, value in fixture_data.items():
        if key.startswith("_"):
            continue
        placeholder = key if key.startswith("[") else f"[{key}]"
        filled = filled.replace(placeholder, str(value))
    return filled


def _get_changed_prompt_files() -> list[Path]:
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
        capture_output=True,
        text=True,
        cwd=str(PROMPTS_DIR.parent),
    )
    return [
        PROMPTS_DIR.parent / f
        for f in result.stdout.strip().split("\n")
        if f.startswith("prompts/") and f.endswith(".md")
    ]


def run_evals(
    category: str | None = None,
    prompt_id: str | None = None,
    changed_only: bool = False,
    tier: str = "structural",
    anthropic_api_key: str | None = None,
) -> list[EvalResult]:
    if changed_only:
        prompt_files = _get_changed_prompt_files()
    elif prompt_id:
        prompt_files = list(PROMPTS_DIR.rglob(f"{prompt_id}.md"))
    elif category:
        cat_dir = PROMPTS_DIR / category
        prompt_files = sorted(cat_dir.glob("*.md")) if cat_dir.exists() else []
    else:
        prompt_files = sorted(PROMPTS_DIR.rglob("*.md"))

    results: list[EvalResult] = []
    for prompt_file in prompt_files:
        if not prompt_file.exists():
            continue
        try:
            prompt = parse_prompt_file(prompt_file)
        except Exception as exc:
            print(f"Warning: could not parse {prompt_file}: {exc}")
            continue

        fixture = load_fixture(prompt["id"])
        if fixture is None:
            print(f"Warning: no fixture for {prompt['id']} — skipping")
            continue

        if not prompt["templates"]:
            print(f"Warning: no template block in {prompt['id']} — skipping")
            continue

        template_text = prompt["templates"][0]
        template_sections = _extract_template_sections(template_text)

        start = time.time()
        filled = _fill_template(template_text, fixture)

        structural_checks = run_structural_checks(
            filled_text=filled,
            template_sections=template_sections,
            fixture_data=fixture,
            prompt_placeholders=prompt["placeholders"],
        )

        llm_scores = None
        if tier == "all":
            from evals.evaluators.llm_judge import score_prompt
            llm_scores = score_prompt(
                prompt_id=prompt["id"],
                category=prompt["category"],
                filled_prompt=filled,
                api_key=anthropic_api_key,
            )

        duration_ms = int((time.time() - start) * 1000)
        structural_passed = all(c.passed for c in structural_checks)
        llm_score_values = [s.score for s in llm_scores] if llm_scores else []
        overall_score = (
            sum(llm_score_values) / len(llm_score_values) if llm_score_values else None
        )

        results.append(
            EvalResult(
                prompt_id=prompt["id"],
                prompt_title=prompt["title"],
                category=prompt["category"],
                fixture_path=str(
                    Path(__file__).parent / "fixtures" / f"{prompt['id']}.json"
                ),
                filled_prompt=filled,
                structural_checks=structural_checks,
                llm_scores=llm_scores,
                structural_passed=structural_passed,
                overall_score=overall_score,
                duration_ms=duration_ms,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        )

    return results
