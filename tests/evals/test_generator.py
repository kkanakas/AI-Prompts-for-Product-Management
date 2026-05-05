"""Tests for evals/fixtures/generator.py — all tests mock the Anthropic API."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_mock_client(response_text: str) -> MagicMock:
    """Return a mock Anthropic client whose messages.create returns response_text."""
    mock_client = MagicMock()
    mock_message = MagicMock()
    mock_message.content = [MagicMock(text=response_text)]
    mock_client.messages.create.return_value = mock_message
    return mock_client


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGenerateFixturesCreatesFile:
    """generate_fixtures() writes a JSON fixture file for a prompt without one."""

    def test_generate_fixtures_creates_file(self, tmp_path, monkeypatch):
        """A missing fixture is created when the API returns valid JSON."""
        import evals.fixtures.generator as gen

        # Redirect output dir to tmp_path
        monkeypatch.setattr(gen, "_FIXTURES_DIR", tmp_path)

        mock_client = _make_mock_client('{"[PRODUCT_NAME]": "Acme CRM"}')

        with patch("evals.fixtures.generator.anthropic") as mock_anthropic:
            mock_anthropic.Anthropic.return_value = mock_client
            result = gen.generate_fixtures(category="prds", api_key="fake")

        # At least one file should have been created
        assert len(result) > 0
        for path in result:
            assert path.exists()
            data = json.loads(path.read_text())
            assert "_meta" in data
            assert data["_meta"]["generated"] == "auto"


class TestGenerateFixturesSkipsExisting:
    """With force=False, prompts that already have a fixture are skipped."""

    def test_generate_fixtures_skips_existing(self, tmp_path, monkeypatch):
        """When a fixture already exists, the API must not be called."""
        import evals.fixtures.generator as gen

        monkeypatch.setattr(gen, "_FIXTURES_DIR", tmp_path)

        # Pre-create a fixture for every prds prompt so all are "existing"
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mcp-server"))
        from server import PROMPTS_DIR  # noqa: E402

        prds_dir = PROMPTS_DIR / "prds"
        for prompt_file in sorted(prds_dir.glob("*.md")):
            fixture_path = tmp_path / "prds" / (prompt_file.stem + ".json")
            fixture_path.parent.mkdir(parents=True, exist_ok=True)
            fixture_path.write_text(json.dumps({"_meta": {"generated": "handwritten"}}))

        mock_client = _make_mock_client('{"[PRODUCT_NAME]": "Acme CRM"}')

        with patch("evals.fixtures.generator.anthropic") as mock_anthropic:
            mock_anthropic.Anthropic.return_value = mock_client
            result = gen.generate_fixtures(category="prds", api_key="fake", force=False)

        # Nothing generated — all skipped
        assert result == []
        mock_client.messages.create.assert_not_called()


class TestGenerateFixturesForceRegenerates:
    """With force=True, even existing fixtures are regenerated."""

    def test_generate_fixtures_force_regenerates(self, tmp_path, monkeypatch):
        """force=True causes the API to be called even when fixture exists."""
        import evals.fixtures.generator as gen

        monkeypatch.setattr(gen, "_FIXTURES_DIR", tmp_path)

        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mcp-server"))
        from server import PROMPTS_DIR  # noqa: E402

        prds_dir = PROMPTS_DIR / "prds"
        prompt_files = sorted(prds_dir.glob("*.md"))
        # Pre-create fixtures for all prds prompts
        for pf in prompt_files:
            fixture_path = tmp_path / "prds" / (pf.stem + ".json")
            fixture_path.parent.mkdir(parents=True, exist_ok=True)
            fixture_path.write_text(json.dumps({"_meta": {"generated": "handwritten"}}))

        mock_client = _make_mock_client('{"[PRODUCT_NAME]": "Acme CRM"}')

        with patch("evals.fixtures.generator.anthropic") as mock_anthropic:
            mock_anthropic.Anthropic.return_value = mock_client
            result = gen.generate_fixtures(category="prds", api_key="fake", force=True)

        # API should have been called for prompts that have placeholders
        assert mock_client.messages.create.call_count > 0


class TestGenerateFixturesBadJsonContinues:
    """A garbled API response doesn't abort the batch — it logs a warning."""

    def test_generate_fixtures_bad_json_continues(self, tmp_path, monkeypatch):
        """When the API returns garbage, no exception is raised."""
        import evals.fixtures.generator as gen

        monkeypatch.setattr(gen, "_FIXTURES_DIR", tmp_path)

        mock_client = _make_mock_client("NOT VALID JSON AT ALL!!!!")

        with patch("evals.fixtures.generator.anthropic") as mock_anthropic:
            mock_anthropic.Anthropic.return_value = mock_client
            # Should NOT raise
            result = gen.generate_fixtures(category="prds", api_key="fake")

        # No fixture should have been written for the garbled response
        assert isinstance(result, list)


class TestGenerateFixturesReturnsPaths:
    """generate_fixtures() returns a list of Path objects."""

    def test_generate_fixtures_returns_paths(self, tmp_path, monkeypatch):
        """Return value is a list of Path objects pointing to created files."""
        import evals.fixtures.generator as gen

        monkeypatch.setattr(gen, "_FIXTURES_DIR", tmp_path)

        mock_client = _make_mock_client('{"[PRODUCT_NAME]": "Acme CRM", "[TARGET_USERS]": "PMs"}')

        with patch("evals.fixtures.generator.anthropic") as mock_anthropic:
            mock_anthropic.Anthropic.return_value = mock_client
            result = gen.generate_fixtures(category="prds", api_key="fake")

        assert isinstance(result, list)
        for item in result:
            assert isinstance(item, Path)
            assert item.suffix == ".json"
