import json
from pathlib import Path
import pytest
from evals.fixtures import load_fixture, _FIXTURES_DIR


def test_load_fixture_returns_dict_when_file_exists(tmp_path, monkeypatch):
    fixture_data = {
        "_meta": {"prompt_id": "prds/01", "generated": "handwritten"},
        "[PRODUCT_NAME]": "Aria",
    }
    fixture_file = tmp_path / "prds" / "01.json"
    fixture_file.parent.mkdir(parents=True)
    fixture_file.write_text(json.dumps(fixture_data))

    monkeypatch.setattr("evals.fixtures._FIXTURES_DIR", tmp_path)

    result = load_fixture("prds/01")
    assert result is not None
    assert result["[PRODUCT_NAME]"] == "Aria"
    assert result["_meta"]["generated"] == "handwritten"


def test_load_fixture_returns_none_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr("evals.fixtures._FIXTURES_DIR", tmp_path)
    result = load_fixture("prds/99-nonexistent")
    assert result is None


def test_load_fixture_parses_valid_json(tmp_path, monkeypatch):
    fixture_data = {"_meta": {"prompt_id": "metrics/01"}, "[FEATURE_NAME]": "Search Alerts"}
    path = tmp_path / "metrics" / "01.json"
    path.parent.mkdir()
    path.write_text(json.dumps(fixture_data))
    monkeypatch.setattr("evals.fixtures._FIXTURES_DIR", tmp_path)

    result = load_fixture("metrics/01")
    assert result["[FEATURE_NAME]"] == "Search Alerts"
