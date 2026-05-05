import pytest
from evals.evaluators.structural import (
    check_placeholders_filled,
    check_sections_present,
    check_tables_well_formed,
    check_code_blocks_closed,
    check_required_fields,
    run_structural_checks,
)


# ── placeholders_filled ─────────────────────────────────────────────────────

def test_placeholders_filled_clean_text():
    result = check_placeholders_filled("You are a PM building Aria.")
    assert result.passed is True
    assert result.message == ""


def test_placeholders_filled_single_remaining():
    result = check_placeholders_filled("Build a product for [PRODUCT_NAME].")
    assert result.passed is False
    assert "[PRODUCT_NAME]" in result.message


def test_placeholders_filled_multiple_remaining():
    result = check_placeholders_filled("[PRODUCT_NAME] solves [PROBLEM].")
    assert result.passed is False
    assert "[PRODUCT_NAME]" in result.message
    assert "[PROBLEM]" in result.message


def test_placeholders_filled_ignores_lowercase():
    result = check_placeholders_filled("See [example] and [note: details].")
    assert result.passed is True


def test_placeholders_filled_space_separated():
    result = check_placeholders_filled("For [PRODUCT NAME] and [TARGET CUSTOMER].")
    assert result.passed is False
    assert "[PRODUCT NAME]" in result.message


def test_placeholders_filled_with_slash():
    result = check_placeholders_filled("Context: [COMPANY STAGE / REVENUE MODEL].")
    assert result.passed is False


# ── sections_present ─────────────────────────────────────────────────────────

def test_sections_present_all_found():
    text = "## Section One\ncontent\n## Section Two\ncontent"
    result = check_sections_present(text, ["## Section One", "## Section Two"])
    assert result.passed is True


def test_sections_present_missing_one():
    text = "## Section One\ncontent"
    result = check_sections_present(text, ["## Section One", "## Section Two"])
    assert result.passed is False
    assert "## Section Two" in result.message


def test_sections_present_empty_expected():
    result = check_sections_present("any text", [])
    assert result.passed is True


def test_sections_present_all_missing():
    result = check_sections_present("no headers here", ["## A", "## B"])
    assert result.passed is False
    assert "## A" in result.message
    assert "## B" in result.message


# ── tables_well_formed ───────────────────────────────────────────────────────

def test_tables_well_formed_valid():
    text = "| A | B |\n|---|---|\n| 1 | 2 |"
    result = check_tables_well_formed(text)
    assert result.passed is True


def test_tables_well_formed_mismatched_columns():
    text = "| A | B |\n|---|---|\n| 1 | 2 | 3 |"
    result = check_tables_well_formed(text)
    assert result.passed is False


def test_tables_well_formed_no_tables():
    result = check_tables_well_formed("just some text with no tables")
    assert result.passed is True


def test_tables_well_formed_multiple_valid_tables():
    text = "| X | Y |\n|---|---|\n| a | b |\n\n| P | Q | R |\n|---|---|---|\n| 1 | 2 | 3 |"
    result = check_tables_well_formed(text)
    assert result.passed is True


# ── code_blocks_closed ───────────────────────────────────────────────────────

def test_code_blocks_closed_pair():
    text = "```\ncode here\n```"
    result = check_code_blocks_closed(text)
    assert result.passed is True


def test_code_blocks_closed_unclosed():
    text = "```\nunclosed block"
    result = check_code_blocks_closed(text)
    assert result.passed is False


def test_code_blocks_closed_multiple_pairs():
    text = "```python\ncode\n```\n```\nmore\n```"
    result = check_code_blocks_closed(text)
    assert result.passed is True


def test_code_blocks_closed_no_blocks():
    result = check_code_blocks_closed("just plain text")
    assert result.passed is True


# ── required_fields ──────────────────────────────────────────────────────────

def test_required_fields_all_present():
    fixture = {"[FOO]": "bar", "[BAZ]": "qux"}
    placeholders = {"[FOO]": "desc", "[BAZ]": "desc2"}
    result = check_required_fields(fixture, placeholders)
    assert result.passed is True


def test_required_fields_missing_key():
    fixture = {"[FOO]": "bar"}
    placeholders = {"[FOO]": "desc", "[BAZ]": "desc2"}
    result = check_required_fields(fixture, placeholders)
    assert result.passed is False
    assert "[BAZ]" in result.message


def test_required_fields_no_placeholders():
    result = check_required_fields({}, {})
    assert result.passed is True


def test_required_fields_meta_ignored():
    fixture = {"_meta": {"generated": "handwritten"}, "[FOO]": "bar"}
    placeholders = {"[FOO]": "desc"}
    result = check_required_fields(fixture, placeholders)
    assert result.passed is True


# ── run_structural_checks ────────────────────────────────────────────────────

def test_run_structural_checks_returns_five_results():
    checks = run_structural_checks(
        filled_text="## Section\ncontent",
        template_sections=["## Section"],
        fixture_data={"[NAME]": "Aria"},
        prompt_placeholders={"[NAME]": "product name"},
    )
    assert len(checks) == 5
    assert all(hasattr(c, "passed") for c in checks)
