import sys
from pathlib import Path
from unittest.mock import patch
import pytest

from evals.runner import _extract_template_sections, _fill_template, run_evals
from evals.types import ScoreResult


def test_extract_template_sections_finds_headers():
    template = "## Step 1 — Extract\ncontent\n## Step 2 — Write\nmore content"
    sections = _extract_template_sections(template)
    assert "## Step 1 — Extract" in sections
    assert "## Step 2 — Write" in sections


def test_extract_template_sections_empty_template():
    assert _extract_template_sections("no headers here") == []


def test_fill_template_replaces_placeholders():
    template = "Build a product for [PRODUCT_NAME] targeting [TARGET_USERS]."
    fixture = {"[PRODUCT_NAME]": "Aria", "[TARGET_USERS]": "support agents"}
    result = _fill_template(template, fixture)
    assert result == "Build a product for Aria targeting support agents."


def test_fill_template_skips_meta_keys():
    template = "Build [PRODUCT_NAME]."
    fixture = {"_meta": {"generated": "handwritten"}, "[PRODUCT_NAME]": "Aria"}
    result = _fill_template(template, fixture)
    assert result == "Build Aria."
    assert "_meta" not in result


def test_fill_template_leaves_unfilled_placeholders():
    template = "Build [PRODUCT_NAME] for [UNFILLED]."
    fixture = {"[PRODUCT_NAME]": "Aria"}
    result = _fill_template(template, fixture)
    assert "[PRODUCT_NAME]" not in result
    assert "[UNFILLED]" in result


def test_run_evals_structural_returns_results_for_fixtures():
    # Uses real prompt files and the hand-written fixture for prds/05-ai-prd
    results = run_evals(prompt_id="prds/05-ai-prd", tier="structural")
    assert len(results) == 1
    result = results[0]
    assert result.prompt_id == "prds/05-ai-prd"
    assert len(result.structural_checks) == 5
    assert result.llm_scores is None
    assert result.duration_ms >= 0


def test_run_evals_skips_prompts_without_fixtures():
    # prds/01-prd-generation has no hand-written fixture
    results = run_evals(prompt_id="prds/01-prd-generation", tier="structural")
    assert isinstance(results, list)
    # Either empty (skipped) or has result — just must not raise


def test_run_evals_category_filter():
    results = run_evals(category="metrics", tier="structural")
    for r in results:
        assert r.category == "metrics"


def test_run_evals_tier_all_calls_llm_judge(monkeypatch):
    """tier='all' should call run_llm_judge and populate llm_scores + overall_score."""
    mock_scores = [
        ScoreResult(dimension="completeness", score=4, rationale="Good.", is_bonus=False),
        ScoreResult(dimension="placeholder_substitution", score=5, rationale="Clean.", is_bonus=False),
        ScoreResult(dimension="format_compliance", score=4, rationale="Fine.", is_bonus=False),
        ScoreResult(dimension="actionability", score=3, rationale="Mostly.", is_bonus=False),
        ScoreResult(dimension="specificity", score=4, rationale="Specific.", is_bonus=False),
    ]

    import evals.evaluators.llm_judge as llm_judge_module

    monkeypatch.setattr(llm_judge_module, "run_llm_judge", lambda **kwargs: mock_scores)

    results = run_evals(prompt_id="prds/05-ai-prd", tier="all", anthropic_api_key="fake")
    assert len(results) == 1
    result = results[0]

    assert result.llm_scores is not None
    assert len(result.llm_scores) == 5
    assert result.overall_score is not None
    # mean of [4, 5, 4, 3, 4] = 20/5 = 4.0
    assert abs(result.overall_score - 4.0) < 1e-9
