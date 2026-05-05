"""End-to-end integration tests for the evals CLI.

These tests invoke the CLI with real fixture files and real prompt files — no mocking.
They are smoke tests verifying that the full pipeline runs without error.
"""
from __future__ import annotations


def test_e2e_run_structural_exits_zero():
    """Smoke test: full run with structural tier should succeed with real fixtures."""
    from evals.cli import main
    try:
        main(["run", "--tier", "structural"])
    except SystemExit as e:
        assert e.code == 0, f"CLI exited with code {e.code}"


def test_e2e_status_runs():
    """Status command should run without error."""
    from evals.cli import main
    try:
        main(["status"])
    except SystemExit as e:
        assert e.code in (0, None), f"CLI exited with code {e.code}"
