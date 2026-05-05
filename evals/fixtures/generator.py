"""Auto-generate test fixtures for PM prompt templates via the Claude API."""
from __future__ import annotations

import json
import logging
import os
import sys
from datetime import date
from pathlib import Path

import anthropic

# Reuse parse_prompt_file from mcp-server — single source of truth for prompt parsing
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mcp-server"))
from server import parse_prompt_file, PROMPTS_DIR  # noqa: E402

_FIXTURES_DIR = Path(__file__).parent

_MODEL = "claude-haiku-4-5-20251001"
_SYSTEM_PROMPT = (
    "You are generating test fixture data for a PM prompt template evaluator. "
    "Return only a JSON object mapping placeholder names to realistic values. "
    "No explanation."
)

log = logging.getLogger(__name__)


def _build_user_prompt(placeholders: dict) -> str:
    return (
        "Generate realistic values for these placeholders in the context of a B2B SaaS product:\n\n"
        + json.dumps(placeholders, indent=2)
    )


def _strip_fences(text: str) -> str:
    """Remove markdown code fences (```json ... ``` or ``` ... ```) from text."""
    text = text.strip()
    if text.startswith("```"):
        # Remove the opening fence line
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]
        else:
            text = text[3:]
    if text.endswith("```"):
        text = text[: text.rfind("```")]
    return text.strip()


def _call_claude(client: anthropic.Anthropic, placeholders: dict) -> dict:
    """Ask Claude to fill in values for the given placeholders dict."""
    message = client.messages.create(
        model=_MODEL,
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_user_prompt(placeholders)}],
    )
    raw_text = message.content[0].text
    clean = _strip_fences(raw_text)
    return json.loads(clean)


def _write_fixture(fixture_path: Path, prompt_id: str, values: dict) -> None:
    """Write the fixture JSON file, creating parent directories as needed."""
    fixture_path.parent.mkdir(parents=True, exist_ok=True)
    payload: dict = {
        "_meta": {
            "prompt_id": prompt_id,
            "generated": "auto",
            "author": "fixture-generator",
            "date": date.today().isoformat(),
        }
    }
    payload.update(values)
    fixture_path.write_text(json.dumps(payload, indent=2))


def generate_fixtures(
    category: str | None = None,
    api_key: str | None = None,
    force: bool = False,
) -> list[Path]:
    """Generate fixture JSON files for prompts that are missing one.

    Parameters
    ----------
    category:
        If given, only generate fixtures for prompts in that category directory.
    api_key:
        Anthropic API key.  Falls back to the ``ANTHROPIC_API_KEY`` environment
        variable when *None*.
    force:
        When *True*, regenerate fixtures even if one already exists.

    Returns
    -------
    list[Path]
        Paths to newly created (or overwritten) fixture files.
    """
    resolved_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=resolved_key)

    # Collect prompt files
    if category:
        cat_dir = PROMPTS_DIR / category
        prompt_files = sorted(cat_dir.glob("*.md")) if cat_dir.exists() else []
    else:
        prompt_files = sorted(PROMPTS_DIR.rglob("*.md"))

    created: list[Path] = []

    for prompt_file in prompt_files:
        if not prompt_file.exists():
            continue

        # Derive fixture path
        relative = prompt_file.relative_to(PROMPTS_DIR)
        fixture_path = _FIXTURES_DIR / relative.with_suffix(".json")

        # Skip if fixture already exists and force=False
        if fixture_path.exists() and not force:
            continue

        # Parse prompt
        try:
            prompt = parse_prompt_file(prompt_file)
        except Exception as exc:
            log.warning("Could not parse %s: %s", prompt_file, exc)
            continue

        placeholders = prompt.get("placeholders", {})
        if not placeholders:
            # Nothing to fill — skip silently
            continue

        # Generate values via Claude
        try:
            values = _call_claude(client, placeholders)
        except Exception as exc:
            log.warning("Fixture generation failed for %s: %s", prompt["id"], exc)
            continue

        # Write fixture
        try:
            _write_fixture(fixture_path, prompt["id"], values)
            created.append(fixture_path)
        except Exception as exc:
            log.warning("Could not write fixture for %s: %s", prompt["id"], exc)
            continue

    return created
