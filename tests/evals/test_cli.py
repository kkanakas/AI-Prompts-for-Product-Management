"""Tests for evals/cli.py — run, status, generate-fixtures commands."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from evals.types import CheckResult, EvalResult


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_result(passed: bool = True) -> EvalResult:
    return EvalResult(
        prompt_id="prds/05-ai-prd",
        prompt_title="AI PRD",
        category="prds",
        fixture_path="fixtures/prds/05-ai-prd.json",
        filled_prompt="some filled text",
        structural_checks=[
            CheckResult("placeholders_filled", passed, "" if passed else "unfilled")
        ],
        llm_scores=None,
        structural_passed=passed,
        overall_score=None,
        duration_ms=100,
        timestamp="2026-05-04T00:00:00",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestRunCommand:
    def test_run_tier_structural_exit_zero(self, tmp_path):
        """Passing result -> exit code 0."""
        from evals.cli import main

        results = [_make_result(passed=True)]

        with (
            patch("evals.cli.run_evals", return_value=results),
            patch("evals.cli.terminal.render"),
            patch("evals.cli.json_reporter.write", return_value=tmp_path / "out.json"),
            patch("evals.cli.markdown_reporter.write", return_value=tmp_path / "latest-report.md"),
        ):
            # Should not raise SystemExit, or raise SystemExit(0)
            try:
                main(["run", "--tier", "structural"])
            except SystemExit as exc:
                assert exc.code == 0

    def test_run_tier_structural_exit_one(self, tmp_path):
        """Failing result (structural_passed=False) -> exit code 1."""
        from evals.cli import main

        results = [_make_result(passed=False)]

        with (
            patch("evals.cli.run_evals", return_value=results),
            patch("evals.cli.terminal.render"),
            patch("evals.cli.json_reporter.write", return_value=tmp_path / "out.json"),
            patch("evals.cli.markdown_reporter.write", return_value=tmp_path / "latest-report.md"),
        ):
            with pytest.raises(SystemExit) as exc_info:
                main(["run", "--tier", "structural"])
            assert exc_info.value.code == 1

    def test_run_tier_all_missing_api_key(self, monkeypatch, tmp_path):
        """--tier all without ANTHROPIC_API_KEY -> non-zero exit."""
        from evals.cli import main

        # Ensure the env var is absent
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

        with pytest.raises(SystemExit) as exc_info:
            main(["run", "--tier", "all"])
        assert exc_info.value.code != 0

    def test_run_calls_all_reporters(self, tmp_path):
        """All three reporters are called after run_evals."""
        from evals.cli import main

        results = [_make_result(passed=True)]

        mock_terminal_render = MagicMock()
        mock_json_write = MagicMock(return_value=tmp_path / "out.json")
        mock_md_write = MagicMock(return_value=tmp_path / "latest-report.md")

        with (
            patch("evals.cli.run_evals", return_value=results),
            patch("evals.cli.terminal.render", mock_terminal_render),
            patch("evals.cli.json_reporter.write", mock_json_write),
            patch("evals.cli.markdown_reporter.write", mock_md_write),
        ):
            try:
                main(["run"])
            except SystemExit as exc:
                # Exit 0 is fine
                assert exc.code == 0

        mock_terminal_render.assert_called_once()
        mock_json_write.assert_called_once()
        mock_md_write.assert_called_once()

    def test_run_passes_category_to_run_evals(self, tmp_path):
        """--category flag is forwarded to run_evals."""
        from evals.cli import main

        results = [_make_result(passed=True)]
        mock_run_evals = MagicMock(return_value=results)

        with (
            patch("evals.cli.run_evals", mock_run_evals),
            patch("evals.cli.terminal.render"),
            patch("evals.cli.json_reporter.write", return_value=tmp_path / "out.json"),
            patch("evals.cli.markdown_reporter.write", return_value=tmp_path / "latest-report.md"),
        ):
            try:
                main(["run", "--category", "prds"])
            except SystemExit as exc:
                assert exc.code == 0

        call_kwargs = mock_run_evals.call_args
        assert call_kwargs.kwargs.get("category") == "prds" or (
            call_kwargs.args and call_kwargs.args[0] == "prds"
        )

    def test_run_changed_only_flag(self, tmp_path):
        """--changed-only flag is forwarded to run_evals."""
        from evals.cli import main

        results = [_make_result(passed=True)]
        mock_run_evals = MagicMock(return_value=results)

        with (
            patch("evals.cli.run_evals", mock_run_evals),
            patch("evals.cli.terminal.render"),
            patch("evals.cli.json_reporter.write", return_value=tmp_path / "out.json"),
            patch("evals.cli.markdown_reporter.write", return_value=tmp_path / "latest-report.md"),
        ):
            try:
                main(["run", "--changed-only"])
            except SystemExit as exc:
                assert exc.code == 0

        call_kwargs = mock_run_evals.call_args
        assert call_kwargs.kwargs.get("changed_only") is True or (
            len(call_kwargs.args) >= 3 and call_kwargs.args[2] is True
        )


class TestStatusCommand:
    def test_status_command_runs(self):
        """Smoke test: status completes without unhandled exception."""
        from evals.cli import main

        try:
            main(["status"])
        except SystemExit as exc:
            # Any clean exit is acceptable
            assert exc.code in (None, 0)


class TestGenerateFixturesCommand:
    def test_generate_fixtures_no_generator(self):
        """If generator module is absent, exits 0 with informational message."""
        from evals.cli import main

        # Remove evals.fixtures.generator from sys.modules if present, and
        # ensure importing it fails so the "not yet implemented" path is taken.
        sys.modules.pop("evals.fixtures.generator", None)

        with patch.dict("sys.modules", {"evals.fixtures.generator": None}):
            try:
                main(["generate-fixtures"])
            except SystemExit as exc:
                assert exc.code in (None, 0)

    def test_generate_fixtures_with_generator(self, tmp_path):
        """If generator module IS present, generate_fixtures() is called."""
        from evals.cli import main

        mock_generator = MagicMock()
        mock_generator.generate_fixtures = MagicMock()

        sys.modules.pop("evals.fixtures.generator", None)

        with patch.dict("sys.modules", {"evals.fixtures.generator": mock_generator}):
            try:
                main(["generate-fixtures"])
            except SystemExit as exc:
                assert exc.code in (None, 0)

        mock_generator.generate_fixtures.assert_called_once()
