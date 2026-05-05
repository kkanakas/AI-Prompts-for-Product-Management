from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from evals.types import ScoreResult

RUBRICS_DIR = Path(__file__).parent.parent.parent / "evals" / "rubrics"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FIVE_UNIVERSAL_SCORES = [
    {"dimension": "completeness", "score": 4, "rationale": "All sections present.", "is_bonus": False},
    {"dimension": "placeholder_substitution", "score": 5, "rationale": "No placeholders remain.", "is_bonus": False},
    {"dimension": "format_compliance", "score": 4, "rationale": "Minor formatting issues.", "is_bonus": False},
    {"dimension": "actionability", "score": 4, "rationale": "Mostly actionable.", "is_bonus": False},
    {"dimension": "specificity", "score": 3, "rationale": "Mix of specific and generic.", "is_bonus": False},
]

ONE_BONUS_SCORE = [
    {"dimension": "prd_section_coverage", "score": 4, "rationale": "Most sections present.", "is_bonus": True},
]


def _make_mock_client(scores: list[dict]) -> MagicMock:
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_tool_use = MagicMock()
    mock_tool_use.type = "tool_use"
    mock_tool_use.name = "submit_scores"
    mock_tool_use.input = {"scores": scores}
    mock_response.content = [mock_tool_use]
    mock_client.messages.create.return_value = mock_response
    return mock_client


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_run_llm_judge_returns_score_results():
    """Well-formed response with 5 universal + 1 bonus → 6 ScoreResult objects."""
    from evals.evaluators.llm_judge import run_llm_judge

    mock_client = _make_mock_client(FIVE_UNIVERSAL_SCORES + ONE_BONUS_SCORE)

    with patch("evals.evaluators.llm_judge.anthropic.Anthropic", return_value=mock_client):
        results = run_llm_judge(
            filled_prompt="A well-filled prompt.",
            category="prds",
            api_key="fake-key",
            rubrics_dir=RUBRICS_DIR,
        )

    assert len(results) == 6
    assert all(isinstance(r, ScoreResult) for r in results)

    # Check fields on first result
    first = results[0]
    assert first.dimension == "completeness"
    assert first.score == 4
    assert first.rationale == "All sections present."
    assert first.is_bonus is False

    # Bonus result
    bonus = results[5]
    assert bonus.is_bonus is True
    assert bonus.dimension == "prd_section_coverage"


def test_run_llm_judge_no_category_rubric():
    """Category with no rubric file → only 5 results, no error."""
    from evals.evaluators.llm_judge import run_llm_judge

    mock_client = _make_mock_client(FIVE_UNIVERSAL_SCORES)

    with patch("evals.evaluators.llm_judge.anthropic.Anthropic", return_value=mock_client):
        results = run_llm_judge(
            filled_prompt="A well-filled prompt.",
            category="customer-discovery",
            api_key="fake-key",
            rubrics_dir=RUBRICS_DIR,
        )

    assert len(results) == 5
    assert all(not r.is_bonus for r in results)


def test_run_llm_judge_malformed_response():
    """Non-tool-use response → RuntimeError."""
    from evals.evaluators.llm_judge import run_llm_judge

    mock_client = MagicMock()
    mock_response = MagicMock()
    # content item is a text block, not tool_use
    mock_text_block = MagicMock()
    mock_text_block.type = "text"
    mock_text_block.text = "I cannot score this."
    mock_response.content = [mock_text_block]
    mock_client.messages.create.return_value = mock_response

    with patch("evals.evaluators.llm_judge.anthropic.Anthropic", return_value=mock_client):
        with pytest.raises(RuntimeError):
            run_llm_judge(
                filled_prompt="Some prompt.",
                category="prds",
                api_key="fake-key",
                rubrics_dir=RUBRICS_DIR,
            )


def test_system_prompt_includes_universal_rubric():
    """The create() call's system prompt contains content from universal.md."""
    from evals.evaluators.llm_judge import run_llm_judge

    mock_client = _make_mock_client(FIVE_UNIVERSAL_SCORES + ONE_BONUS_SCORE)

    with patch("evals.evaluators.llm_judge.anthropic.Anthropic", return_value=mock_client):
        run_llm_judge(
            filled_prompt="Some prompt.",
            category="prds",
            api_key="fake-key",
            rubrics_dir=RUBRICS_DIR,
        )

    call_kwargs = mock_client.messages.create.call_args
    system = call_kwargs.kwargs.get("system") or call_kwargs[1].get("system") or call_kwargs[0][0]

    # system should be a list of dicts
    assert isinstance(system, list)
    assert len(system) >= 1

    # First block text should contain universal rubric content
    first_block = system[0]
    assert "type" in first_block
    assert first_block["type"] == "text"
    assert "Completeness" in first_block["text"] or "completeness" in first_block["text"].lower()


def test_cache_control_on_universal_rubric():
    """The first system block has cache_control={'type': 'ephemeral'}."""
    from evals.evaluators.llm_judge import run_llm_judge

    mock_client = _make_mock_client(FIVE_UNIVERSAL_SCORES + ONE_BONUS_SCORE)

    with patch("evals.evaluators.llm_judge.anthropic.Anthropic", return_value=mock_client):
        run_llm_judge(
            filled_prompt="Some prompt.",
            category="prds",
            api_key="fake-key",
            rubrics_dir=RUBRICS_DIR,
        )

    call_kwargs = mock_client.messages.create.call_args
    system = call_kwargs.kwargs.get("system") or call_kwargs[1].get("system") or call_kwargs[0][0]

    first_block = system[0]
    assert "cache_control" in first_block
    assert first_block["cache_control"] == {"type": "ephemeral"}
