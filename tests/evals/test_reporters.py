from evals.types import CheckResult, EvalResult
from evals.reporters.terminal import render


def _make_result(prompt_id: str, passed: bool, score: float | None = None) -> EvalResult:
    checks = [
        CheckResult("placeholders_filled", passed, "" if passed else "Unfilled: [FOO]"),
        CheckResult("sections_present", True, ""),
        CheckResult("tables_well_formed", True, ""),
        CheckResult("code_blocks_closed", True, ""),
        CheckResult("required_fields", True, ""),
    ]
    return EvalResult(
        prompt_id=prompt_id,
        prompt_title="Test Prompt",
        category="prds",
        fixture_path="fixtures/prds/test.json",
        filled_prompt="filled content",
        structural_checks=checks,
        llm_scores=None,
        structural_passed=passed,
        overall_score=score,
        duration_ms=100,
        timestamp="2026-05-04T00:00:00+00:00",
    )


def test_render_does_not_raise_on_all_passed():
    results = [_make_result("prds/01", True), _make_result("prds/02", True)]
    render(results, tier="structural")  # must not raise


def test_render_does_not_raise_on_failures():
    results = [_make_result("prds/01", True), _make_result("prds/02", False)]
    render(results, tier="structural")  # must not raise


def test_render_does_not_raise_empty():
    render([], tier="structural")  # must not raise
