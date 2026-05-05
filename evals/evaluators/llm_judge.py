from __future__ import annotations

import json
from pathlib import Path

import anthropic

from evals.types import ScoreResult

_MODEL = "claude-haiku-4-5-20251001"

_SUBMIT_SCORES_TOOL = {
    "name": "submit_scores",
    "description": "Submit evaluation scores for the filled prompt.",
    "input_schema": {
        "type": "object",
        "properties": {
            "scores": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "dimension": {"type": "string", "description": "Name of the dimension being scored"},
                        "score": {"type": "integer", "description": "Score from 1 to 5", "minimum": 1, "maximum": 5},
                        "rationale": {"type": "string", "description": "One-sentence rationale for the score"},
                        "is_bonus": {"type": "boolean", "description": "True if this is a category-specific bonus check"},
                    },
                    "required": ["dimension", "score", "rationale", "is_bonus"],
                },
            }
        },
        "required": ["scores"],
    },
}


def _load_rubric(rubrics_dir: Path, filename: str) -> str | None:
    path = rubrics_dir / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def _build_system_prompt(universal_text: str, category_text: str | None) -> list[dict]:
    blocks: list[dict] = [
        {
            "type": "text",
            "text": universal_text,
            "cache_control": {"type": "ephemeral"},
        }
    ]
    if category_text:
        blocks.append({"type": "text", "text": category_text})
    return blocks


def run_llm_judge(
    filled_prompt: str,
    category: str,
    api_key: str,
    rubrics_dir: Path | None = None,
) -> list[ScoreResult]:
    """Call Claude as an LLM judge and return structured ScoreResult objects.

    Args:
        filled_prompt: The filled template text to evaluate.
        category: The prompt category (e.g. "prds", "metrics").
        api_key: Anthropic API key.
        rubrics_dir: Directory containing rubric .md files; defaults to
            ``evals/rubrics/`` relative to this file.

    Returns:
        A list of ScoreResult objects (5 universal + optional bonus scores).

    Raises:
        RuntimeError: If the API call fails or the response is malformed.
    """
    if rubrics_dir is None:
        rubrics_dir = Path(__file__).parent.parent / "rubrics"

    universal_text = _load_rubric(rubrics_dir, "universal.md")
    if universal_text is None:
        raise RuntimeError(f"universal.md not found in {rubrics_dir}")

    category_text = _load_rubric(rubrics_dir, f"{category}.md")

    system_prompt = _build_system_prompt(universal_text, category_text)

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model=_MODEL,
            max_tokens=2048,
            system=system_prompt,
            tools=[_SUBMIT_SCORES_TOOL],
            tool_choice={"type": "any"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Please evaluate the following filled prompt and submit your scores "
                        "using the submit_scores tool.\n\n"
                        f"<filled_prompt>\n{filled_prompt}\n</filled_prompt>"
                    ),
                }
            ],
        )
    except Exception as exc:
        raise RuntimeError(f"Anthropic API call failed: {exc}") from exc

    # Find the submit_scores tool_use block in the response
    tool_use_block = None
    for block in response.content:
        if getattr(block, "type", None) == "tool_use" and getattr(block, "name", None) == "submit_scores":
            tool_use_block = block
            break

    if tool_use_block is None:
        raise RuntimeError(
            "LLM judge did not return a submit_scores tool call. "
            f"Response content types: {[getattr(b, 'type', type(b).__name__) for b in response.content]}"
        )

    raw_input = tool_use_block.input
    if not isinstance(raw_input, dict) or "scores" not in raw_input:
        raise RuntimeError(
            f"submit_scores tool input is malformed: {raw_input!r}"
        )

    scores_data = raw_input["scores"]
    if not isinstance(scores_data, list):
        raise RuntimeError(
            f"'scores' field is not a list: {scores_data!r}"
        )

    results: list[ScoreResult] = []
    for i, item in enumerate(scores_data):
        if not isinstance(item, dict):
            raise RuntimeError(f"Score item {i} is not a dict: {item!r}")
        try:
            results.append(
                ScoreResult(
                    dimension=str(item["dimension"]),
                    score=int(item["score"]),
                    rationale=str(item["rationale"]),
                    is_bonus=bool(item["is_bonus"]),
                )
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(f"Could not parse score item {i} ({item!r}): {exc}") from exc

    return results
