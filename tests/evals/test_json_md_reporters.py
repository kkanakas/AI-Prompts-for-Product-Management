import json
from pathlib import Path
from evals.types import CheckResult, EvalResult
from evals.reporters.json_reporter import write as write_json
from evals.reporters.markdown_reporter import write as write_md


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


def test_json_reporter_creates_file(tmp_path):
    results = [_make_result("prds/01", True, score=4.2)]
    out_path = write_json(results, tier="structural", results_dir=tmp_path)
    assert out_path.exists()
    assert out_path.suffix == ".json"


def test_json_reporter_valid_structure(tmp_path):
    results = [_make_result("prds/01", True)]
    out_path = write_json(results, tier="structural", results_dir=tmp_path)
    data = json.loads(out_path.read_text())
    assert "run_id" in data
    assert "tier" in data
    assert "summary" in data
    assert "results" in data
    assert data["tier"] == "structural"
    assert data["summary"]["total"] == 1
    assert data["summary"]["passed"] == 1
    assert data["summary"]["failed"] == 0


def test_json_reporter_failed_result(tmp_path):
    results = [_make_result("prds/01", True), _make_result("prds/02", False)]
    out_path = write_json(results, tier="structural", results_dir=tmp_path)
    data = json.loads(out_path.read_text())
    assert data["summary"]["failed"] == 1
    assert len(data["results"]) == 2


def test_json_reporter_result_fields(tmp_path):
    results = [_make_result("prds/01", True)]
    out_path = write_json(results, tier="structural", results_dir=tmp_path)
    data = json.loads(out_path.read_text())
    r = data["results"][0]
    assert r["prompt_id"] == "prds/01"
    assert "structural_checks" in r
    assert isinstance(r["structural_checks"], list)


def test_markdown_reporter_creates_file(tmp_path):
    results = [_make_result("prds/01", True, score=4.2)]
    out_path = write_md(results, tier="structural", results_dir=tmp_path)
    assert out_path.exists()
    assert out_path.name == "latest-report.md"


def test_markdown_reporter_contains_summary(tmp_path):
    results = [_make_result("prds/01", True), _make_result("prds/02", False)]
    out_path = write_md(results, tier="structural", results_dir=tmp_path)
    content = out_path.read_text()
    assert "## Summary" in content
    assert "prds/01" in content
    assert "prds/02" in content


def test_markdown_reporter_contains_failures(tmp_path):
    results = [_make_result("prds/02", False)]
    out_path = write_md(results, tier="structural", results_dir=tmp_path)
    content = out_path.read_text()
    assert "## Failures" in content
    assert "Unfilled" in content


def test_markdown_reporter_overwrites_on_rerun(tmp_path):
    results1 = [_make_result("prds/01", True)]
    write_md(results1, tier="structural", results_dir=tmp_path)
    results2 = [_make_result("prds/99", False)]
    out_path = write_md(results2, tier="structural", results_dir=tmp_path)
    content = out_path.read_text()
    assert "prds/99" in content
    assert "prds/01" not in content
