from __future__ import annotations
import re
from evals.types import CheckResult

# Matches [UPPER_CASE], [UPPER_CASE_UNDERSCORE], [UPPER CASE SPACE], [UPPER/SLASH]
_PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z_\s/]*\]")
_SEP_ROW_RE = re.compile(r"^\|[-| :]+\|$")


def check_placeholders_filled(text: str) -> CheckResult:
    remaining = sorted(set(_PLACEHOLDER_RE.findall(text)))
    if remaining:
        return CheckResult(
            name="placeholders_filled",
            passed=False,
            message=f"Unfilled placeholders: {', '.join(remaining)}",
        )
    return CheckResult(name="placeholders_filled", passed=True, message="")


def check_sections_present(filled_text: str, expected_sections: list[str]) -> CheckResult:
    missing = [s for s in expected_sections if s not in filled_text]
    if missing:
        return CheckResult(
            name="sections_present",
            passed=False,
            message=f"Missing sections: {', '.join(missing)}",
        )
    return CheckResult(name="sections_present", passed=True, message="")


def check_tables_well_formed(text: str) -> CheckResult:
    lines = text.splitlines()
    tables: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|"):
            current.append(stripped)
        else:
            if current:
                tables.append(current)
                current = []
    if current:
        tables.append(current)

    errors: list[str] = []
    for table in tables:
        data_rows = [row for row in table if not _SEP_ROW_RE.match(row)]
        counts = [row.count("|") for row in data_rows]
        if counts and len(set(counts)) > 1:
            errors.append(f"Table at '{table[0][:40]}' has inconsistent column counts")

    if errors:
        return CheckResult(name="tables_well_formed", passed=False, message="; ".join(errors))
    return CheckResult(name="tables_well_formed", passed=True, message="")


def check_code_blocks_closed(text: str) -> CheckResult:
    count = sum(1 for line in text.splitlines() if line.strip().startswith("```"))
    if count % 2 != 0:
        return CheckResult(
            name="code_blocks_closed",
            passed=False,
            message=f"Odd number of ``` markers ({count}): at least one code block is unclosed",
        )
    return CheckResult(name="code_blocks_closed", passed=True, message="")


def check_required_fields(fixture_data: dict, prompt_placeholders: dict[str, str]) -> CheckResult:
    missing = [k for k in prompt_placeholders if k not in fixture_data]
    if missing:
        return CheckResult(
            name="required_fields",
            passed=False,
            message=f"Fixture missing values for: {', '.join(missing)}",
        )
    return CheckResult(name="required_fields", passed=True, message="")


def run_structural_checks(
    filled_text: str,
    template_sections: list[str],
    fixture_data: dict,
    prompt_placeholders: dict[str, str],
) -> list[CheckResult]:
    return [
        check_placeholders_filled(filled_text),
        check_sections_present(filled_text, template_sections),
        check_tables_well_formed(filled_text),
        check_code_blocks_closed(filled_text),
        check_required_fields(fixture_data, prompt_placeholders),
    ]
