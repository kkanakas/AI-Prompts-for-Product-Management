from dataclasses import asdict
from evals.types import CheckResult, ScoreResult, EvalResult


def test_check_result_fields():
    r = CheckResult(name="placeholders_filled", passed=True, message="")
    assert r.name == "placeholders_filled"
    assert r.passed is True
    assert r.message == ""


def test_check_result_failed():
    r = CheckResult(name="placeholders_filled", passed=False, message="Unfilled: [FOO]")
    assert r.passed is False
    assert "FOO" in r.message


def test_score_result_fields():
    s = ScoreResult(dimension="completeness", score=4, rationale="All sections present", is_bonus=False)
    assert s.score == 4
    assert s.is_bonus is False


def test_eval_result_serializable():
    result = EvalResult(
        prompt_id="prds/01-prd-generation",
        prompt_title="PRD Generation",
        category="prds",
        fixture_path="fixtures/prds/01-prd-generation.json",
        filled_prompt="You are a PM...",
        structural_checks=[CheckResult("placeholders_filled", True, "")],
        llm_scores=None,
        structural_passed=True,
        overall_score=None,
        duration_ms=50,
        timestamp="2026-05-04T00:00:00+00:00",
    )
    d = asdict(result)
    assert d["prompt_id"] == "prds/01-prd-generation"
    assert d["llm_scores"] is None
    assert d["structural_checks"][0]["passed"] is True
