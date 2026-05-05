from __future__ import annotations
import json
from pathlib import Path

_FIXTURES_DIR = Path(__file__).parent


def load_fixture(prompt_id: str) -> dict | None:
    """Load a fixture JSON for the given prompt_id, or return None if not found."""
    fixture_path = _FIXTURES_DIR / f"{prompt_id}.json"
    if not fixture_path.exists():
        return None
    return json.loads(fixture_path.read_text())
