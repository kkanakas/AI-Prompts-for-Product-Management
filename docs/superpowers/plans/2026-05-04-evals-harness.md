# Evals Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a two-tier evaluation harness for the AI Prompts for Product Management library that runs structural checks in CI and LLM-as-judge scoring on demand.

**Architecture:** Pure-Python CLI (`python -m evals`) reuses `parse_prompt_file` from `mcp-server/server.py` to load prompts, fills them from JSON fixtures, runs Tier 1 structural checks (no API) and optionally Tier 2 LLM-judge scoring via the Anthropic SDK with prompt caching. Results output as a Rich terminal table, timestamped JSON, and `evals/results/latest-report.md`.

**Tech Stack:** Python 3.11+, `anthropic>=0.40.0`, `rich>=13.0.0`, `pytest` for tests.

---

## File Map

```
evals/
├── __init__.py
├── __main__.py                       # enables python -m evals
├── types.py                          # CheckResult, ScoreResult, EvalResult dataclasses
├── cli.py                            # argparse + command handlers
├── runner.py                         # orchestrates load → fill → evaluate → report
├── evaluators/
│   ├── __init__.py
│   ├── structural.py                 # Tier 1: 5 pure-Python checks
│   └── llm_judge.py                  # Tier 2: Claude-as-judge via Anthropic SDK
├── reporters/
│   ├── __init__.py
│   ├── terminal.py                   # Rich coloured table
│   ├── json_reporter.py              # evals/results/<timestamp>.json
│   └── markdown_reporter.py         # evals/results/latest-report.md
├── fixtures/
│   ├── __init__.py                   # load_fixture(prompt_id) → dict | None
│   ├── generator.py                  # auto-generates fixtures via Claude API
│   ├── prds/
│   │   ├── 04-given-when-then.json
│   │   └── 05-ai-prd.json
│   ├── metrics/
│   │   ├── 01-feature-success-metrics.json
│   │   └── 02-ai-product-metrics.json
│   ├── strategy/
│   │   ├── 01-product-strategy-canvas.json
│   │   ├── 02-team-okr-generator.json
│   │   └── 08-big-rock-decomposition.json
│   └── prototyping/
│       ├── 05-wizard-of-oz-protocol.json
│       └── 07-ai-feature-stub.json
├── rubrics/
│   ├── universal.md
│   ├── prds.md
│   ├── metrics.md
│   ├── prototyping.md
│   └── strategy.md
└── results/
    └── .gitkeep

tests/
└── evals/
    ├── __init__.py
    ├── test_types.py
    ├── test_structural.py
    ├── test_fixtures.py
    ├── test_runner.py
    ├── test_reporters.py
    └── test_llm_judge.py

.github/workflows/evals.yml
evals/requirements.txt
```

---

## Task 1: Project scaffold + data types

**Files:**
- Create: `evals/__init__.py`
- Create: `evals/__main__.py`
- Create: `evals/types.py`
- Create: `evals/evaluators/__init__.py`
- Create: `evals/reporters/__init__.py`
- Create: `evals/fixtures/__init__.py` (stub — full implementation in Task 3)
- Create: `evals/results/.gitkeep`
- Create: `evals/requirements.txt`
- Create: `tests/__init__.py`
- Create: `tests/evals/__init__.py`
- Create: `tests/evals/test_types.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/evals/test_types.py
from dataclasses import asdict
from evals.types import CheckResult, ScoreResult, EvalResult


def test_check_result_fields():
    r = CheckResult(name="placeholders_filled", passed=True, message="")
    assert r.name == "placeholders_filled"
    assert r.passed is True
    assert r.message == ""


def test_check_result_failed():
    r = CheckResult(name="placeholders_filled", passed=False, message="Unfilled: [FOO]")
    assert r.passed is False
    assert "FOO" in r.message


def test_score_result_fields():
    s = ScoreResult(dimension="completeness", score=4, rationale="All sections present", is_bonus=False)
    assert s.score == 4
    assert s.is_bonus is False


def test_eval_result_serializable():
    result = EvalResult(
        prompt_id="prds/01-prd-generation",
        prompt_title="PRD Generation",
        category="prds",
        fixture_path="fixtures/prds/01-prd-generation.json",
        filled_prompt="You are a PM...",
        structural_checks=[CheckResult("placeholders_filled", True, "")],
        llm_scores=None,
        structural_passed=True,
        overall_score=None,
        duration_ms=50,
        timestamp="2026-05-04T00:00:00+00:00",
    )
    d = asdict(result)
    assert d["prompt_id"] == "prds/01-prd-generation"
    assert d["llm_scores"] is None
    assert d["structural_checks"][0]["passed"] is True
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/stynger76/Documents/GitHub/AI-Prompts-for-Product-Management
pytest tests/evals/test_types.py -v
```

Expected: `ModuleNotFoundError: No module named 'evals'`

- [ ] **Step 3: Create directory structure and empty init files**

```bash
mkdir -p evals/evaluators evals/reporters evals/fixtures evals/results tests/evals
touch evals/__init__.py evals/evaluators/__init__.py evals/reporters/__init__.py
touch tests/__init__.py tests/evals/__init__.py
touch evals/results/.gitkeep
```

- [ ] **Step 4: Create `evals/requirements.txt`**

```
anthropic>=0.40.0
rich>=13.0.0
pytest>=7.0.0
```

- [ ] **Step 5: Create `evals/types.py`**

```python
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CheckResult:
    name: str
    passed: bool
    message: str


@dataclass
class ScoreResult:
    dimension: str
    score: int        # 1–5
    rationale: str
    is_bonus: bool    # True = category-specific bonus check


@dataclass
class EvalResult:
    prompt_id: str
    prompt_title: str
    category: str
    fixture_path: str
    filled_prompt: str
    structural_checks: list[CheckResult]
    llm_scores: list[ScoreResult] | None   # None if tier 1 only
    structural_passed: bool
    overall_score: float | None            # mean of llm_scores
    duration_ms: int
    timestamp: str
```

- [ ] **Step 6: Create `evals/__main__.py`**

```python
from evals.cli import main

if __name__ == "__main__":
    main()
```

- [ ] **Step 7: Create stub `evals/fixtures/__init__.py`** (full implementation in Task 3)

```python
# Full implementation added in Task 3
def load_fixture(prompt_id: str) -> dict | None:
    return None
```

- [ ] **Step 8: Run test to verify it passes**

```bash
pytest tests/evals/test_types.py -v
```

Expected: `4 passed`

- [ ] **Step 9: Commit**

```bash
git add evals/ tests/ 
git commit -m "feat: scaffold evals harness — directory structure and core data types"
```

---

## Task 2: Structural evaluator

**Files:**
- Create: `evals/evaluators/structural.py`
- Create: `tests/evals/test_structural.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_structural.py
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
    # _meta key is not a placeholder
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_structural.py -v
```

Expected: `ImportError: cannot import name 'check_placeholders_filled' from 'evals.evaluators.structural'`

- [ ] **Step 3: Create `evals/evaluators/structural.py`**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_structural.py -v
```

Expected: `22 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/evaluators/structural.py tests/evals/test_structural.py
git commit -m "feat: add Tier 1 structural evaluator with 5 checks"
```

---

## Task 3: Fixture loader

**Files:**
- Modify: `evals/fixtures/__init__.py` (replace stub)
- Create: `tests/evals/test_fixtures.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_fixtures.py
import json
from pathlib import Path
import pytest
from unittest.mock import patch
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_fixtures.py -v
```

Expected: `AttributeError` or assertion failure because `load_fixture` returns `None` (stub).

- [ ] **Step 3: Replace stub with full implementation in `evals/fixtures/__init__.py`**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_fixtures.py -v
```

Expected: `3 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/fixtures/__init__.py tests/evals/test_fixtures.py
git commit -m "feat: add fixture loader utility"
```

---

## Task 4: Rubric files

**Files:**
- Create: `evals/rubrics/universal.md`
- Create: `evals/rubrics/prds.md`
- Create: `evals/rubrics/metrics.md`
- Create: `evals/rubrics/prototyping.md`
- Create: `evals/rubrics/strategy.md`

No tests needed — these are plain Markdown consumed by the LLM judge.

- [ ] **Step 1: Create `evals/rubrics/universal.md`**

```markdown
# Universal Evaluation Rubric

You are an expert product management coach evaluating a filled prompt template from the AI Prompts for Product Management library. A PM has filled the template with their specific context and will run this prompt through an AI assistant. Your job is to assess the quality of the filled prompt — not a hypothetical AI output.

Score each dimension 1–5 using the `record_scores` tool. For each score, provide a one-sentence rationale.

## Dimensions

### Completeness (1–5)
All sections and sub-sections the template requested are present. No required sections have been omitted or left as headings with no content.

- 5: Every section is present and substantively filled
- 4: All major sections present; minor sub-sections may be brief
- 3: Most sections present; one significant section missing or very thin
- 2: Multiple sections missing or only headers with no content
- 1: Fewer than half the sections have substantive content

**Pass threshold: ≥ 3**

### Placeholder Substitution (1–5)
All `[PLACEHOLDERS]` have been replaced with contextually appropriate, specific content. No bracket tokens remain.

- 5: All placeholders filled with rich, specific PM context — no generic filler
- 4: All placeholders filled; most are specific and contextually appropriate
- 3: All placeholders filled but some contain generic or vague values
- 2: One or two placeholders unfilled or filled with placeholder-style text (e.g., "your product name")
- 1: Multiple unfilled placeholders remain

**Pass threshold: ≥ 4**

### Format Compliance (1–5)
Tables, code blocks, headers, and lists match the structure the template specified. No malformed markdown.

- 5: All structural elements are well-formed and match the template's specified format
- 4: Minor formatting inconsistencies that do not affect readability
- 3: Some structural elements malformed or missing; template structure mostly preserved
- 2: Multiple structural issues; some sections unrecognizable from the template format
- 1: Format severely degraded; template structure lost

**Pass threshold: ≥ 3**

### Actionability (1–5)
A PM could hand this filled prompt to their team and act on it today. The context is specific enough that an AI assistant would produce useful, targeted output.

- 5: Immediately actionable — context is rich, decisions are clear, scope is defined
- 4: Actionable with minor clarifications needed
- 3: Mostly actionable; one or two vague areas that would produce generic AI output
- 2: Significant gaps that would cause the AI to produce generic or off-target output
- 1: Too vague to be useful; would require major rework before running

**Pass threshold: ≥ 3**

### Specificity (1–5)
Concrete details, no generic filler, no re-stated placeholder names. Context values feel like they come from a real product and a real PM's notes.

- 5: All values are concrete and specific — names, numbers, roles, timelines where appropriate
- 4: Most values specific; minor generic statements present
- 3: Mix of specific and generic content; the generic parts reduce output quality
- 2: Mostly generic; could apply to any product in any industry
- 1: All values are generic placeholders or example-style text

**Pass threshold: ≥ 3**

## Overall Pass Threshold
Average ≥ 3.5. Any individual dimension < 3 flags a warning regardless of average.
```

- [ ] **Step 2: Create `evals/rubrics/prds.md`**

```markdown
# PRD Category Bonus Checks

Score the following bonus dimensions for prompts in the `prds` category. Set `is_bonus: true` for all scores in this file.

### PRD Section Coverage (1–5)
For AI PRD prompts: all 11 sections are present (Executive Summary, Problem Statement, Objectives/Metrics, AI Features, Data Requirements, Model Requirements, UX & Human Interaction, Ethical Risk & Compliance, Milestones, Stakeholders, References). For standard PRD prompts: the core sections are substantively filled.

- 5: All required sections present and substantively filled
- 3: Most sections present; 1–2 minor sections thin
- 1: Multiple required sections missing

### GWT Criteria Quality (1–5)
For Given/When/Then prompts: criteria include Given/When/Then structure; And clauses chain preconditions and outcomes correctly; But clauses assert negative assertions where applicable. Happy path, error handling, and edge cases are covered.

- 5: Full GWT structure with And/But used correctly; happy path, errors, and edge cases covered
- 3: GWT structure present; And/But usage present but some scenarios missing
- 1: GWT structure missing or criteria do not follow Gherkin conventions
```

- [ ] **Step 3: Create `evals/rubrics/metrics.md`**

```markdown
# Metrics Category Bonus Checks

Score the following bonus dimension for prompts in the `metrics` category. Set `is_bonus: true`.

### Metric Row Completeness (1–5)
Every metric row in the output template includes: metric name, measurement method, target value, and baseline. No row has a metric with a target but no baseline.

- 5: All rows have metric name, measurement method, target, and baseline
- 3: Most rows complete; 1–2 rows missing measurement method or baseline
- 1: Majority of rows lack measurement method or baseline values
```

- [ ] **Step 4: Create `evals/rubrics/prototyping.md`**

```markdown
# Prototyping Category Bonus Checks

Score the following bonus dimension for prompts in the `prototyping` category. Set `is_bonus: true`.

### Prototype Type Alignment (1–5)
The output maps to the correct prototype type specified in the prompt (lo-fi wireframe, Wizard of Oz, AI feature stub, agent workflow, etc.). Checklists and protocol steps appropriate to that prototype type are present.

- 5: Output clearly matches the specified prototype type; all relevant checklists and protocol steps present
- 3: Output mostly matches the type; some type-specific elements thin or generic
- 1: Output does not match the specified prototype type or is missing key type-specific elements
```

- [ ] **Step 5: Create `evals/rubrics/strategy.md`**

```markdown
# Strategy Category Bonus Checks

Score the following bonus dimension for prompts in the `strategy` category. Set `is_bonus: true`.

### Success Criteria Measurability (1–5)
Success criteria are measurable. OKR key results include numeric targets. Goals reference baselines where applicable. No success criteria that cannot be objectively verified.

- 5: All success criteria measurable; OKR KRs have numeric targets and baselines; goals time-boxed
- 3: Most criteria measurable; 1–2 KRs lack numeric targets or baselines
- 1: Success criteria are qualitative or cannot be objectively verified
```

- [ ] **Step 6: Commit**

```bash
git add evals/rubrics/
git commit -m "feat: add universal and category-specific evaluation rubrics"
```

---

## Task 5: Hand-written fixtures

**Files:**
- Create: `evals/fixtures/prds/04-given-when-then.json`
- Create: `evals/fixtures/prds/05-ai-prd.json`
- Create: `evals/fixtures/metrics/01-feature-success-metrics.json`
- Create: `evals/fixtures/metrics/02-ai-product-metrics.json`
- Create: `evals/fixtures/strategy/01-product-strategy-canvas.json`
- Create: `evals/fixtures/strategy/02-team-okr-generator.json`
- Create: `evals/fixtures/strategy/08-big-rock-decomposition.json`
- Create: `evals/fixtures/prototyping/05-wizard-of-oz-protocol.json`
- Create: `evals/fixtures/prototyping/07-ai-feature-stub.json`

No tests for content files — the runner integration test in Task 6 validates fixture loading.

- [ ] **Step 1: Create directories**

```bash
mkdir -p evals/fixtures/prds evals/fixtures/metrics evals/fixtures/strategy evals/fixtures/prototyping
```

- [ ] **Step 2: Create `evals/fixtures/prds/04-given-when-then.json`**

Placeholder keys from `prompts/prds/04-given-when-then.md`: `[PASTE_DOCUMENT]`, `[FEATURE_NAME]`, `[ACTORS]`, `[PRODUCT]`, `[QA_TOOL]`.

```json
{
  "_meta": {
    "prompt_id": "prds/04-given-when-then",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[PASTE_DOCUMENT]": "## Feature: Saved Search Alerts\n\nRegistered users can save a search query and opt-in to receive email notifications when new results matching that query are added to the platform.\n\n### Functional Requirements\n- FR-01: Registered users can save up to 10 active search queries per account\n- FR-02: Users can enable or disable email notifications per saved search independently\n- FR-03: Notification emails are delivered within 15 minutes of new matching results appearing\n- FR-04: Users can delete a saved search; deletion immediately cancels all future notifications for that query\n- FR-05: Each notification email contains a deep link that opens the platform pre-filtered to the saved search results\n\n### Non-Functional Requirements\n- NFR-01: Notification delivery latency must be under 15 minutes at the 95th percentile under normal load\n- NFR-02: The notification pipeline must handle 10,000 concurrent active saved searches without throughput degradation\n\n### Business Rules\n- BR-01: Free-tier accounts are limited to 3 saved searches; paid-tier accounts have no limit\n- BR-02: Notifications for a given saved search must not be sent more than once per 24-hour window regardless of how many new results match",
  "[FEATURE_NAME]": "Saved Search Alerts",
  "[ACTORS]": "Registered user (free tier), registered user (paid tier), system notification service, platform administrator",
  "[PRODUCT]": "B2B SaaS market intelligence platform — web application used by research analysts and competitive intelligence teams",
  "[QA_TOOL]": "Cucumber / Gherkin"
}
```

- [ ] **Step 3: Create `evals/fixtures/prds/05-ai-prd.json`**

Placeholder keys from `prompts/prds/05-ai-prd.md`: `[PRODUCT_NAME]`, `[ONE_LINE_DESCRIPTION]`, `[STAGE]`, `[AUTHOR]`, `[DATE]`, `[OBJECTIVE]`, `[BUSINESS_PROBLEM]`, `[TARGET_USERS]`, `[BUSINESS_IMPACT]`, `[STAGE_MILESTONES]`.

```json
{
  "_meta": {
    "prompt_id": "prds/05-ai-prd",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[PRODUCT_NAME]": "Aria — AI Support Assistant",
  "[ONE_LINE_DESCRIPTION]": "Drafts replies to inbound support tickets and surfaces the most relevant knowledge base articles for Tier-1 support agents",
  "[STAGE]": "Discovery",
  "[AUTHOR]": "Kartik K., Senior PM — Platform",
  "[DATE]": "2026-05-04",
  "[OBJECTIVE]": "Reduce average handle time for Tier-1 support agents by 40% through AI-assisted response drafting",
  "[BUSINESS_PROBLEM]": "Support agents spend 60% of their time on ticket types that follow predictable resolution patterns — password resets, billing inquiries, shipping status — driving high operational cost and slow response times despite low required judgment",
  "[TARGET_USERS]": "Tier-1 support agents handling 80+ tickets per day; secondary audience is end customers on the self-serve plan who interact with the AI-suggested responses",
  "[BUSINESS_IMPACT]": "$2.4M annual cost reduction from reduced handle time; 40% reduction in average handle time from 8 min to 4.8 min; 15-point CSAT improvement driven by faster, more consistent responses",
  "[STAGE_MILESTONES]": "Discovery complete: 2026-05-30 / Model selection and data audit: 2026-07-15 / Internal validation with 10 agents: 2026-08-31 / Staged production deployment: 2026-09-30"
}
```

- [ ] **Step 4: Create `evals/fixtures/metrics/01-feature-success-metrics.json`**

Placeholder keys from `prompts/metrics/01-feature-success-metrics.md`: `[FEATURE_NAME]`, `[FEATURE_DESCRIPTION]`, `[TARGET_USERS]`, `[FEATURE_GOAL]`.

```json
{
  "_meta": {
    "prompt_id": "metrics/01-feature-success-metrics",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[FEATURE_NAME]": "Saved Search Alerts",
  "[FEATURE_DESCRIPTION]": "Allows registered users to save up to 10 search queries and receive email notifications when new results matching those queries are published to the platform",
  "[TARGET_USERS]": "Power users and research analysts who monitor specific topics continuously; primarily paid-tier subscribers running competitive intelligence programs",
  "[FEATURE_GOAL]": "Increase weekly active usage by 20% and reduce churn among research-heavy users by surfacing relevant content without requiring daily manual login and search"
}
```

- [ ] **Step 5: Create `evals/fixtures/metrics/02-ai-product-metrics.json`**

Placeholder keys from `prompts/metrics/02-ai-product-metrics.md`: `[PRODUCT_NAME]`, `[PRODUCT_DESCRIPTION]`, `[TARGET_USERS]`, `[AI_MODALITY]`, `[BUSINESS_OUTCOME]`, `[CURRENT_INSTRUMENTATION]`, `[KNOWN_RISKS]`.

```json
{
  "_meta": {
    "prompt_id": "metrics/02-ai-product-metrics",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[PRODUCT_NAME]": "Aria — AI Support Assistant",
  "[PRODUCT_DESCRIPTION]": "LLM-powered assistant that drafts replies to inbound support tickets by retrieving relevant knowledge base articles and generating natural-language responses for Tier-1 agents to review and send",
  "[TARGET_USERS]": "Tier-1 support agents handling 80+ tickets per day; secondary audience is end customers who receive the AI-assisted responses",
  "[AI_MODALITY]": "RAG pipeline with claude-sonnet-4-6, retrieval from Confluence knowledge base via embedding search, streamed responses displayed in the support agent UI with a one-click accept or edit workflow",
  "[BUSINESS_OUTCOME]": "Reduce average handle time for support tickets by 40% (from 8 min to 4.8 min) and deflect 25% of inbound tickets to self-serve within 6 months of launch",
  "[CURRENT_INSTRUMENTATION]": "Basic API error rate and uptime via Datadog; ticket volume and handle time tracked in Zendesk; no product-level AI-specific metrics currently instrumented",
  "[KNOWN_RISKS]": "Hallucinations in responses about billing terms and legal commitments; latency spikes during peak hours (9–11am EST) causing agent frustration; agents over-trusting AI for complex escalation cases that require human judgment"
}
```

- [ ] **Step 6: Create `evals/fixtures/strategy/01-product-strategy-canvas.json`**

Placeholder keys from `prompts/strategy/01-product-strategy-canvas.md` Placeholders table: `[PRODUCT NAME]`, `[PRODUCT DESCRIPTION]`, `[COMPANY STAGE / REVENUE MODEL]`, `[TARGET CUSTOMER]`, `[PROBLEM WE ARE SOLVING]`, `[CURRENT SOLUTION LANDSCAPE]`, `[OUR DIFFERENTIATORS]`, `[STRATEGIC CONSTRAINTS]`, `[12-MONTH GOAL]`.

```json
{
  "_meta": {
    "prompt_id": "strategy/01-product-strategy-canvas",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[PRODUCT NAME]": "Clearpath",
  "[PRODUCT DESCRIPTION]": "contract management platform for in-house legal teams at mid-market companies",
  "[COMPANY STAGE / REVENUE MODEL]": "Series B SaaS, $12M ARR, 18-month path to profitability, transitioning from SMB to mid-market accounts ($20K–$80K ACV)",
  "[TARGET CUSTOMER]": "In-house general counsel and legal operations managers at companies with 500–5,000 employees and 3–15 person legal teams",
  "[PROBLEM WE ARE SOLVING]": "In-house legal teams spend 60% of their time chasing contract status across email threads and shared drives — not doing legal work — because incumbent CLM tools were built for large law firms, not lean in-house teams",
  "[CURRENT SOLUTION LANDSCAPE]": "Email + Google Drive (most common), legacy CLM tools (Ironclad, DocuSign CLM) that require 6-month implementation, or no system at all — teams rely on a paralegal as the single source of truth",
  "[OUR DIFFERENTIATORS]": "AI-native contract review that surfaces risks in under 60 seconds, deploys in one day with no IT involvement, priced for mid-market not enterprise, built specifically for in-house legal workflow not law firm workflow",
  "[STRATEGIC CONSTRAINTS]": "24-month runway, team of 18, no enterprise sales motion yet — limited to self-serve and inside sales; GDPR and SOC 2 Type II compliance required for EU expansion in Q3",
  "[12-MONTH GOAL]": "Sign 75 new mid-market accounts and reach $2.2M ARR from that segment, establishing Clearpath as the default CLM for in-house legal teams under 20 people"
}
```

- [ ] **Step 7: Create `evals/fixtures/strategy/02-team-okr-generator.json`**

Placeholder keys: `[COMPANY OKRS]`, `[TEAM NAME]`, `[PRODUCT AREA OR DOMAIN]`, `[TEAM SIZE AND ROLES]`, `[CURRENT QUARTER]`, `[INITIATIVES ALREADY PLANNED]`, `[KEY CONSTRAINTS]`, `[BASELINE METRICS]`.

```json
{
  "_meta": {
    "prompt_id": "strategy/02-team-okr-generator",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[COMPANY OKRS]": "O1: Become the default contract management platform for mid-market in-house legal teams. KR1: Grow ARR from $12M to $18M by end of Q4. KR2: Achieve NPS of 50+ across mid-market segment. KR3: Reach 85% of customers actively using AI review feature within 60 days of activation.",
  "[TEAM NAME]": "Activation & Adoption Squad",
  "[PRODUCT AREA OR DOMAIN]": "User onboarding, first-contract-uploaded workflow, AI review feature activation, in-product education and empty states",
  "[TEAM SIZE AND ROLES]": "1 PM (me), 3 engineers, 1 designer, 0.5 data analyst (shared with Growth team)",
  "[CURRENT QUARTER]": "Q3 2026",
  "[INITIATIVES ALREADY PLANNED]": "Redesigning the first-run experience for new accounts; shipping in-app contract template library (20 templates); A/B testing the AI review feature placement in the upload flow",
  "[KEY CONSTRAINTS]": "Dependent on Platform team for SSO integration (ETA: week 4 of Q3); designer on parental leave weeks 8–12; cannot change the Stripe billing integration until Q4",
  "[BASELINE METRICS]": "Time-to-first-contract-uploaded: 4.2 days; AI review feature activation rate: 31% within 60 days; 30-day retention: 67%; free-to-paid conversion: 5.8%"
}
```

- [ ] **Step 8: Create `evals/fixtures/strategy/08-big-rock-decomposition.json`**

Placeholder keys: `[INITIATIVE_NAME]`, `[STRATEGIC_INTENT]`, `[TARGET_USER]`, `[TEAM_TYPE]`, `[CONSTRAINTS]`, `[DEPENDENCIES]`, `[CURRENT_STATE]`.

```json
{
  "_meta": {
    "prompt_id": "strategy/08-big-rock-decomposition",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[INITIATIVE_NAME]": "AI-Powered Contract Intelligence Platform",
  "[STRATEGIC_INTENT]": "Transform Clearpath from a contract storage and routing tool into an intelligent risk advisor — enabling in-house legal teams to review contracts 10x faster while catching risks that currently slip through manual review",
  "[TARGET_USER]": "In-house legal counsel and legal operations managers at mid-market companies; secondary audience is the non-legal business stakeholders (sales, procurement, HR) who initiate contract requests",
  "[TEAM_TYPE]": "Two product squads (Contract Review Squad, Workflow Automation Squad) plus one shared Platform team for ML infrastructure",
  "[CONSTRAINTS]": "Must not break existing contract storage and e-signature integrations; board demo required at end of Q4 2026; ML infrastructure team has a 6-engineer cap; SOC 2 Type II audit in October cannot be disrupted",
  "[DEPENDENCIES]": "ML infrastructure platform (Platform team — parallel track); legal data labeling partnership with external vendor (contract signed, onboarding Q3); GDPR legal review of AI processing (Legal — ETA: August 2026)",
  "[CURRENT_STATE]": "Contracts are uploaded, routed for signatures, and stored — but no AI analysis exists today. Legal teams extract risks manually by reading contracts in full, a process that takes 45–90 minutes per contract and misses non-obvious clause interactions"
}
```

- [ ] **Step 9: Create `evals/fixtures/prototyping/05-wizard-of-oz-protocol.json`**

Placeholder keys: `[FEATURE_NAME]`, `[PRODUCT_CONTEXT]`, `[USER_TASK]`, `[PARTICIPANT_PROFILE]`, `[HYPOTHESIS]`, `[AI_BEHAVIOR]`, `[TEST_FORMAT]`, `[PARTICIPANT_COUNT]`.

```json
{
  "_meta": {
    "prompt_id": "prototyping/05-wizard-of-oz-protocol",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[FEATURE_NAME]": "AI Contract Risk Highlighter — surfaces high-risk clauses with a one-sentence plain-English explanation and a recommended action",
  "[PRODUCT_CONTEXT]": "Clearpath — B2B SaaS contract management platform used by in-house legal teams at mid-market companies. Agents are legal ops managers and junior lawyers, not technical users.",
  "[USER_TASK]": "Review an NDA sent by a new enterprise vendor, identify any clauses that pose risk to Clearpath, and decide whether to sign, request changes, or escalate to senior counsel",
  "[PARTICIPANT_PROFILE]": "In-house legal operations managers with 2–6 years of experience, accustomed to reviewing contracts manually, no prior experience with AI contract review tools, working at companies with 500–2,000 employees",
  "[HYPOTHESIS]": "Legal ops managers will act on AI risk highlights for standard clause types (IP ownership, indemnification cap, governing law) without independent verification, but will escalate AI-flagged custom clauses to senior counsel",
  "[AI_BEHAVIOR]": "For each clause flagged as high-risk: display a yellow highlight on the clause text, a one-sentence plain-English risk summary, a confidence score (High / Medium / Low), and a suggested action (Accept / Request modification / Escalate). Wizard selects from a prepared playbook of 8 response types based on which clause the participant hovers over.",
  "[TEST_FORMAT]": "Moderated remote session via Zoom with screen share; wizard operates from a separate hidden browser tab with a pre-loaded response playbook; facilitator and wizard are different people",
  "[PARTICIPANT_COUNT]": "8"
}
```

- [ ] **Step 10: Create `evals/fixtures/prototyping/07-ai-feature-stub.json`**

Placeholder keys: `[FEATURE_NAME]`, `[PRODUCT_CONTEXT]`, `[TRIGGER_ACTION]`, `[OUTPUT_FORMAT]`, `[PROTOTYPE_TYPE]`, `[TRUST_HYPOTHESIS]`.

```json
{
  "_meta": {
    "prompt_id": "prototyping/07-ai-feature-stub",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-04"
  },
  "[FEATURE_NAME]": "AI Contract Risk Highlighter — flags high-risk clauses with plain-English explanations and recommended actions",
  "[PRODUCT_CONTEXT]": "Clearpath — B2B SaaS contract management platform; users are legal ops managers and junior lawyers reviewing vendor NDAs, MSAs, and SOWs; typically 45–90 minutes per contract today",
  "[TRIGGER_ACTION]": "User uploads a contract PDF or pastes contract text into the review workspace and clicks 'Analyze contract'",
  "[OUTPUT_FORMAT]": "Inline yellow highlights on the clause text, a right-hand panel listing all flagged clauses with: clause type, risk level badge (High/Medium/Low), one-sentence plain-English risk description, confidence score percentage, and a recommended action button (Accept / Request changes / Escalate to senior counsel)",
  "[PROTOTYPE_TYPE]": "Wizard of Oz session with 8 legal ops managers — wizard selects pre-written stub responses from a playbook based on which clause the participant hovers over",
  "[TRUST_HYPOTHESIS]": "Legal ops managers will accept AI recommendations for standard clause types (IP ownership, indemnification cap, governing law) without reading the full clause, but will escalate AI-flagged non-standard or custom clauses regardless of AI confidence score"
}
```

- [ ] **Step 11: Commit**

```bash
git add evals/fixtures/
git commit -m "feat: add 9 hand-written fixtures for priority prompts"
```

---

## Task 6: Runner (structural path)

**Files:**
- Create: `evals/runner.py`
- Create: `tests/evals/test_runner.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_runner.py
import sys
from pathlib import Path
import pytest

# Make sure the evals package is importable
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from evals.runner import _extract_template_sections, _fill_template, run_evals


def test_extract_template_sections_finds_headers():
    template = "## Step 1 — Extract\ncontent\n## Step 2 — Write\nmore content"
    sections = _extract_template_sections(template)
    assert "## Step 1 — Extract" in sections
    assert "## Step 2 — Write" in sections


def test_extract_template_sections_empty_template():
    assert _extract_template_sections("no headers here") == []


def test_fill_template_replaces_placeholders():
    template = "Build a product for [PRODUCT_NAME] targeting [TARGET_USERS]."
    fixture = {"[PRODUCT_NAME]": "Aria", "[TARGET_USERS]": "support agents"}
    result = _fill_template(template, fixture)
    assert result == "Build a product for Aria targeting support agents."


def test_fill_template_skips_meta_keys():
    template = "Build [PRODUCT_NAME]."
    fixture = {"_meta": {"generated": "handwritten"}, "[PRODUCT_NAME]": "Aria"}
    result = _fill_template(template, fixture)
    assert result == "Build Aria."
    assert "_meta" not in result


def test_fill_template_leaves_unfilled_placeholders():
    template = "Build [PRODUCT_NAME] for [UNFILLED]."
    fixture = {"[PRODUCT_NAME]": "Aria"}
    result = _fill_template(template, fixture)
    assert "[PRODUCT_NAME]" not in result
    assert "[UNFILLED]" in result


def test_run_evals_structural_returns_results_for_fixtures():
    # Uses real prompt files and the hand-written fixture for prds/05-ai-prd
    results = run_evals(prompt_id="prds/05-ai-prd", tier="structural")
    assert len(results) == 1
    result = results[0]
    assert result.prompt_id == "prds/05-ai-prd"
    assert result.structural_passed is True
    assert len(result.structural_checks) == 5
    assert result.llm_scores is None
    assert result.duration_ms >= 0


def test_run_evals_skips_prompts_without_fixtures():
    # prds/01-prd-generation has no hand-written fixture yet
    results = run_evals(prompt_id="prds/01-prd-generation", tier="structural")
    # Should return empty (skipped with warning) not raise
    assert isinstance(results, list)


def test_run_evals_category_filter():
    results = run_evals(category="metrics", tier="structural")
    for r in results:
        assert r.category == "metrics"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_runner.py -v
```

Expected: `ImportError: cannot import name '_extract_template_sections' from 'evals.runner'`

- [ ] **Step 3: Create `evals/runner.py`**

```python
from __future__ import annotations
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Reuse parse_prompt_file from mcp-server — single source of truth for prompt parsing
sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
from server import parse_prompt_file, PROMPTS_DIR  # noqa: E402

from evals.evaluators.structural import run_structural_checks
from evals.fixtures import load_fixture
from evals.types import EvalResult


def _extract_template_sections(template_text: str) -> list[str]:
    return [
        line.strip()
        for line in template_text.splitlines()
        if line.strip().startswith("## ")
    ]


def _fill_template(template: str, fixture_data: dict) -> str:
    filled = template
    for key, value in fixture_data.items():
        if key.startswith("_"):
            continue
        placeholder = key if key.startswith("[") else f"[{key}]"
        filled = filled.replace(placeholder, str(value))
    return filled


def _get_changed_prompt_files() -> list[Path]:
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
        capture_output=True,
        text=True,
        cwd=str(PROMPTS_DIR.parent),
    )
    return [
        PROMPTS_DIR.parent / f
        for f in result.stdout.strip().split("\n")
        if f.startswith("prompts/") and f.endswith(".md")
    ]


def run_evals(
    category: str | None = None,
    prompt_id: str | None = None,
    changed_only: bool = False,
    tier: str = "structural",
    anthropic_api_key: str | None = None,
) -> list[EvalResult]:
    if changed_only:
        prompt_files = _get_changed_prompt_files()
    elif prompt_id:
        prompt_files = list(PROMPTS_DIR.rglob(f"{prompt_id}.md"))
    elif category:
        cat_dir = PROMPTS_DIR / category
        prompt_files = sorted(cat_dir.glob("*.md")) if cat_dir.exists() else []
    else:
        prompt_files = sorted(PROMPTS_DIR.rglob("*.md"))

    results: list[EvalResult] = []
    for prompt_file in prompt_files:
        if not prompt_file.exists():
            continue
        try:
            prompt = parse_prompt_file(prompt_file)
        except Exception as exc:
            print(f"Warning: could not parse {prompt_file}: {exc}")
            continue

        fixture = load_fixture(prompt["id"])
        if fixture is None:
            print(f"Warning: no fixture for {prompt['id']} — skipping")
            continue

        if not prompt["templates"]:
            print(f"Warning: no template block in {prompt['id']} — skipping")
            continue

        template_text = prompt["templates"][0]
        template_sections = _extract_template_sections(template_text)

        start = time.time()
        filled = _fill_template(template_text, fixture)

        structural_checks = run_structural_checks(
            filled_text=filled,
            template_sections=template_sections,
            fixture_data=fixture,
            prompt_placeholders=prompt["placeholders"],
        )

        llm_scores = None
        if tier == "all":
            from evals.evaluators.llm_judge import score_prompt
            llm_scores = score_prompt(
                prompt_id=prompt["id"],
                category=prompt["category"],
                filled_prompt=filled,
                api_key=anthropic_api_key,
            )

        duration_ms = int((time.time() - start) * 1000)
        structural_passed = all(c.passed for c in structural_checks)
        llm_score_values = [s.score for s in llm_scores] if llm_scores else []
        overall_score = (
            sum(llm_score_values) / len(llm_score_values) if llm_score_values else None
        )

        results.append(
            EvalResult(
                prompt_id=prompt["id"],
                prompt_title=prompt["title"],
                category=prompt["category"],
                fixture_path=str(
                    Path(__file__).parent / "fixtures" / f"{prompt['id']}.json"
                ),
                filled_prompt=filled,
                structural_checks=structural_checks,
                llm_scores=llm_scores,
                structural_passed=structural_passed,
                overall_score=overall_score,
                duration_ms=duration_ms,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        )

    return results
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_runner.py -v
```

Expected: `8 passed` (the `run_evals` tests require that `evals/fixtures/prds/05-ai-prd.json` exists from Task 5)

- [ ] **Step 5: Commit**

```bash
git add evals/runner.py tests/evals/test_runner.py
git commit -m "feat: add runner — loads prompts, fills fixtures, runs structural checks"
```

---

## Task 7: Terminal reporter

**Files:**
- Create: `evals/reporters/terminal.py`
- Create: `tests/evals/test_reporters.py` (stub — extended in Tasks 8 and 9)

- [ ] **Step 1: Write the failing smoke test**

```python
# tests/evals/test_reporters.py
from io import StringIO
from evals.types import CheckResult, EvalResult
from evals.reporters.terminal import render


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


def test_render_does_not_raise_on_all_passed():
    results = [_make_result("prds/01", True), _make_result("prds/02", True)]
    render(results, tier="structural")  # must not raise


def test_render_does_not_raise_on_failures():
    results = [_make_result("prds/01", True), _make_result("prds/02", False)]
    render(results, tier="structural")  # must not raise


def test_render_does_not_raise_empty():
    render([], tier="structural")  # must not raise
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_reporters.py::test_render_does_not_raise_on_all_passed -v
```

Expected: `ImportError: cannot import name 'render' from 'evals.reporters.terminal'`

- [ ] **Step 3: Create `evals/reporters/terminal.py`**

```python
from __future__ import annotations
from datetime import datetime

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from evals.types import EvalResult

_console = Console()


def render(results: list[EvalResult], tier: str) -> None:
    if not results:
        _console.print("[yellow]No results to display.[/yellow]")
        return

    table = Table(box=box.SIMPLE_HEAVY, show_footer=False, expand=True)
    table.add_column("Prompt", style="bold", no_wrap=True)
    table.add_column("Structural", justify="center")
    table.add_column("Score", justify="center")
    table.add_column("Duration", justify="right")
    table.add_column("Status", justify="center")

    passed_count = 0
    for r in results:
        n_passed = sum(1 for c in r.structural_checks if c.passed)
        n_total = len(r.structural_checks)
        structural_str = f"{n_passed}/{n_total} {'✓' if n_passed == n_total else '✗'}"
        score_str = f"{r.overall_score:.1f}/5" if r.overall_score is not None else "—"
        duration_str = f"{r.duration_ms / 1000:.1f}s"
        if r.structural_passed:
            status = "[green]PASS ✓[/green]"
            passed_count += 1
        else:
            status = "[red]FAIL ✗[/red]"
        table.add_row(r.prompt_id, structural_str, score_str, duration_str, status)

    failed_count = len(results) - passed_count
    scores = [r.overall_score for r in results if r.overall_score is not None]
    avg_score = sum(scores) / len(scores) if scores else None

    summary_parts = [f"{passed_count} passed · {failed_count} failed"]
    if avg_score is not None:
        summary_parts.append(f"avg {avg_score:.1f}/5")
    total_ms = sum(r.duration_ms for r in results)
    summary_parts.append(f"{total_ms / 1000:.0f}s")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = f"Evals Run ── {timestamp} ── tier: {tier} ── {len(results)} prompts"

    _console.print(Panel(table, title=title, subtitle=" · ".join(summary_parts)))

    failures = [r for r in results if not r.structural_passed]
    if failures:
        _console.print("\n[bold]Failures[/bold]")
        for r in failures:
            _console.print(f"  {r.prompt_id}")
            for c in r.structural_checks:
                if not c.passed:
                    _console.print(f"    [red]✗ structural: {c.message}[/red]")
            if r.llm_scores:
                for s in r.llm_scores:
                    if s.score < 3:
                        _console.print(
                            f"    [red]✗ judge {s.dimension} {s.score}/5: {s.rationale}[/red]"
                        )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_reporters.py::test_render_does_not_raise_on_all_passed tests/evals/test_reporters.py::test_render_does_not_raise_on_failures tests/evals/test_reporters.py::test_render_does_not_raise_empty -v
```

Expected: `3 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/reporters/terminal.py tests/evals/test_reporters.py
git commit -m "feat: add Rich terminal reporter"
```

---

## Task 8: JSON reporter

**Files:**
- Modify: `tests/evals/test_reporters.py` (add JSON reporter tests)
- Create: `evals/reporters/json_reporter.py`

- [ ] **Step 1: Write the failing tests** (append to `tests/evals/test_reporters.py`)

```python
import json
import tempfile
from pathlib import Path
from evals.reporters.json_reporter import write


def test_json_reporter_creates_file(tmp_path):
    results = [_make_result("prds/01", True, score=4.2)]
    out_path = write(results, tier="structural", results_dir=tmp_path)
    assert out_path.exists()
    assert out_path.suffix == ".json"


def test_json_reporter_valid_json(tmp_path):
    results = [_make_result("prds/01", True)]
    out_path = write(results, tier="structural", results_dir=tmp_path)
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
    out_path = write(results, tier="structural", results_dir=tmp_path)
    data = json.loads(out_path.read_text())
    assert data["summary"]["failed"] == 1
    assert len(data["results"]) == 2


def test_json_reporter_result_fields(tmp_path):
    results = [_make_result("prds/01", True)]
    out_path = write(results, tier="structural", results_dir=tmp_path)
    data = json.loads(out_path.read_text())
    r = data["results"][0]
    assert r["prompt_id"] == "prds/01"
    assert "structural_checks" in r
    assert isinstance(r["structural_checks"], list)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_reporters.py -k "json" -v
```

Expected: `ImportError: cannot import name 'write' from 'evals.reporters.json_reporter'`

- [ ] **Step 3: Create `evals/reporters/json_reporter.py`**

```python
from __future__ import annotations
import json
import uuid
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from evals.types import EvalResult

_DEFAULT_RESULTS_DIR = Path(__file__).parent.parent / "results"


def write(
    results: list[EvalResult],
    tier: str,
    filter_desc: str | None = None,
    results_dir: Path | None = None,
) -> Path:
    out_dir = results_dir or _DEFAULT_RESULTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    run_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now(timezone.utc).isoformat()
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{run_id}.json"
    out_path = out_dir / filename

    passed = sum(1 for r in results if r.structural_passed)
    scores = [r.overall_score for r in results if r.overall_score is not None]

    payload = {
        "run_id": run_id,
        "timestamp": timestamp,
        "tier": tier,
        "filter": filter_desc,
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": len(results) - passed,
            "avg_score": round(sum(scores) / len(scores), 2) if scores else None,
        },
        "results": [asdict(r) for r in results],
    }

    out_path.write_text(json.dumps(payload, indent=2))
    return out_path
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_reporters.py -k "json" -v
```

Expected: `4 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/reporters/json_reporter.py tests/evals/test_reporters.py
git commit -m "feat: add JSON reporter — writes timestamped artifact to evals/results/"
```

---

## Task 9: Markdown reporter

**Files:**
- Modify: `tests/evals/test_reporters.py` (add Markdown reporter tests)
- Create: `evals/reporters/markdown_reporter.py`

- [ ] **Step 1: Write the failing tests** (append to `tests/evals/test_reporters.py`)

```python
from evals.reporters.markdown_reporter import write as write_md


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
    assert "prds/01" not in content  # previous run overwritten
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_reporters.py -k "markdown" -v
```

Expected: `ImportError: cannot import name 'write' from 'evals.reporters.markdown_reporter'`

- [ ] **Step 3: Create `evals/reporters/markdown_reporter.py`**

```python
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path

from evals.types import EvalResult

_DEFAULT_RESULTS_DIR = Path(__file__).parent.parent / "results"


def write(
    results: list[EvalResult],
    tier: str,
    filter_desc: str | None = None,
    results_dir: Path | None = None,
) -> Path:
    out_dir = results_dir or _DEFAULT_RESULTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "latest-report.md"

    passed = sum(1 for r in results if r.structural_passed)
    scores = [r.overall_score for r in results if r.overall_score is not None]
    avg_score = round(sum(scores) / len(scores), 2) if scores else None
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Evals Report",
        "",
        f"**Date:** {timestamp}  ",
        f"**Tier:** {tier}  ",
        f"**Filter:** {filter_desc or 'all'}  ",
        "",
        "## Summary",
        "",
        f"| Total | Passed | Failed | Avg Score |",
        f"|---|---|---|---|",
        f"| {len(results)} | {passed} | {len(results) - passed} | {avg_score or '—'} |",
        "",
        "## Results",
        "",
        "| Prompt | Structural | Score | Duration | Status |",
        "|---|---|---|---|---|",
    ]

    for r in results:
        n_passed = sum(1 for c in r.structural_checks if c.passed)
        n_total = len(r.structural_checks)
        score_str = f"{r.overall_score:.1f}" if r.overall_score is not None else "—"
        status = "PASS" if r.structural_passed else "FAIL"
        lines.append(
            f"| {r.prompt_id} | {n_passed}/{n_total} | {score_str} | {r.duration_ms}ms | {status} |"
        )

    failures = [r for r in results if not r.structural_passed]
    if failures:
        lines += ["", "## Failures", ""]
        for r in failures:
            lines.append(f"### {r.prompt_id}")
            lines.append("")
            for c in r.structural_checks:
                if not c.passed:
                    lines.append(f"- **{c.name}**: {c.message}")
            if r.llm_scores:
                for s in r.llm_scores:
                    if s.score < 3:
                        lines.append(f"- **judge {s.dimension}** {s.score}/5: {s.rationale}")
            lines.append("")

    out_path.write_text("\n".join(lines))
    return out_path
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_reporters.py -k "markdown" -v
```

Expected: `4 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/reporters/markdown_reporter.py tests/evals/test_reporters.py
git commit -m "feat: add Markdown reporter — writes evals/results/latest-report.md"
```

---

## Task 10: CLI

**Files:**
- Create: `evals/cli.py`
- Modify: `evals/__main__.py` (update to call `main`)
- Create: `tests/evals/test_cli.py`

The CLI wires together `runner.run_evals` with all three reporters. It also implements the `status` and `generate-fixtures` commands.

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_cli.py
import sys
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
from evals.cli import parse_args, main


def test_parse_args_run_structural_defaults():
    args = parse_args(["run"])
    assert args.command == "run"
    assert args.tier == "structural"
    assert args.category is None
    assert args.prompt is None
    assert args.changed_only is False


def test_parse_args_run_tier_all():
    args = parse_args(["run", "--tier", "all", "--category", "prds"])
    assert args.tier == "all"
    assert args.category == "prds"


def test_parse_args_run_single_prompt():
    args = parse_args(["run", "--prompt", "prds/05-ai-prd"])
    assert args.prompt == "prds/05-ai-prd"


def test_parse_args_run_changed_only():
    args = parse_args(["run", "--changed-only"])
    assert args.changed_only is True


def test_parse_args_status():
    args = parse_args(["status"])
    assert args.command == "status"


def test_parse_args_generate_fixtures():
    args = parse_args(["generate-fixtures", "--category", "prototyping"])
    assert args.command == "generate-fixtures"
    assert args.category == "prototyping"


def test_main_run_structural_calls_runner(tmp_path):
    with patch("evals.cli.run_evals") as mock_runner, \
         patch("evals.cli.render_terminal"), \
         patch("evals.cli.write_json"), \
         patch("evals.cli.write_markdown"):
        mock_runner.return_value = []
        main(["run", "--tier", "structural"])
        mock_runner.assert_called_once_with(
            category=None,
            prompt_id=None,
            changed_only=False,
            tier="structural",
            anthropic_api_key=None,
        )


def test_main_run_passes_category(tmp_path):
    with patch("evals.cli.run_evals") as mock_runner, \
         patch("evals.cli.render_terminal"), \
         patch("evals.cli.write_json"), \
         patch("evals.cli.write_markdown"):
        mock_runner.return_value = []
        main(["run", "--category", "metrics"])
        mock_runner.assert_called_once_with(
            category="metrics",
            prompt_id=None,
            changed_only=False,
            tier="structural",
            anthropic_api_key=None,
        )
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_cli.py -v
```

Expected: `ImportError: cannot import name 'parse_args' from 'evals.cli'`

- [ ] **Step 3: Create `evals/cli.py`**

```python
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path

from evals.runner import run_evals
from evals.reporters.terminal import render as render_terminal
from evals.reporters.json_reporter import write as write_json
from evals.reporters.markdown_reporter import write as write_markdown


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="evals",
        description="Evaluate AI Prompts for Product Management library",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run evaluations")
    run_p.add_argument("--tier", choices=["structural", "all"], default="structural")
    run_p.add_argument("--category", default=None, help="Filter by category slug")
    run_p.add_argument("--prompt", default=None, help="Single prompt ID")
    run_p.add_argument("--changed-only", action="store_true", help="Only changed prompt files")

    status_p = sub.add_parser("status", help="Show prompts with fixture + last eval status")

    gen_p = sub.add_parser("generate-fixtures", help="Auto-generate missing fixtures")
    gen_p.add_argument("--category", default=None)
    gen_p.add_argument("--prompt", default=None)

    return parser.parse_args(argv)


def _cmd_run(args: argparse.Namespace) -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY") if args.tier == "all" else None

    filter_desc_parts = []
    if args.category:
        filter_desc_parts.append(f"category={args.category}")
    if args.prompt:
        filter_desc_parts.append(f"prompt={args.prompt}")
    if args.changed_only:
        filter_desc_parts.append("changed-only")
    filter_desc = ", ".join(filter_desc_parts) or "all"

    results = run_evals(
        category=args.category,
        prompt_id=args.prompt,
        changed_only=args.changed_only,
        tier=args.tier,
        anthropic_api_key=api_key,
    )

    render_terminal(results, tier=args.tier)
    json_path = write_json(results, tier=args.tier, filter_desc=filter_desc)
    md_path = write_markdown(results, tier=args.tier, filter_desc=filter_desc)

    print(f"\nArtifacts: {json_path.name}  |  {md_path.name}")

    failed = [r for r in results if not r.structural_passed]
    if failed:
        sys.exit(1)


def _cmd_status(args: argparse.Namespace) -> None:
    sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
    from server import load_all_prompts  # noqa: E402
    from evals.fixtures import load_fixture

    prompts = load_all_prompts()
    print(f"\n{'Prompt ID':<45} {'Has Fixture':<14} {'Category'}")
    print("-" * 80)
    for p in prompts:
        has_fixture = "✓" if load_fixture(p["id"]) is not None else "✗ missing"
        print(f"{p['id']:<45} {has_fixture:<14} {p['category']}")


def _cmd_generate_fixtures(args: argparse.Namespace) -> None:
    from evals.fixtures.generator import generate_and_save_fixture
    sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
    from server import load_all_prompts  # noqa: E402
    from evals.fixtures import load_fixture

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable required for generate-fixtures")
        sys.exit(1)

    prompts = load_all_prompts()
    if args.category:
        prompts = [p for p in prompts if p["category"] == args.category]
    if args.prompt:
        prompts = [p for p in prompts if p["id"] == args.prompt]

    for p in prompts:
        if load_fixture(p["id"]) is not None:
            print(f"  skip {p['id']} (fixture exists)")
            continue
        print(f"  generating {p['id']} ...", end="", flush=True)
        path = generate_and_save_fixture(p["id"], api_key=api_key)
        print(f" → {path}")


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    if args.command == "run":
        _cmd_run(args)
    elif args.command == "status":
        _cmd_status(args)
    elif args.command == "generate-fixtures":
        _cmd_generate_fixtures(args)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_cli.py -v
```

Expected: `10 passed`

- [ ] **Step 5: Verify `python -m evals` works**

```bash
cd /Users/stynger76/Documents/GitHub/AI-Prompts-for-Product-Management
pip install -r evals/requirements.txt
python -m evals run --tier structural --category prds
```

Expected: Rich table showing results for prds prompts that have fixtures (05-ai-prd and 04-given-when-then).

- [ ] **Step 6: Commit**

```bash
git add evals/cli.py evals/__main__.py tests/evals/test_cli.py
git commit -m "feat: add CLI — run, status, generate-fixtures commands"
```

---

## Task 11: LLM judge evaluator

**Files:**
- Create: `evals/evaluators/llm_judge.py`
- Create: `tests/evals/test_llm_judge.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_llm_judge.py
from unittest.mock import MagicMock, patch
import pytest
from evals.evaluators.llm_judge import score_prompt, _load_rubric
from evals.types import ScoreResult


def test_load_rubric_universal():
    rubric = _load_rubric("unknown-category")
    assert "Universal Evaluation Rubric" in rubric
    assert "Completeness" in rubric


def test_load_rubric_appends_category_rubric():
    rubric = _load_rubric("prds")
    assert "Universal Evaluation Rubric" in rubric
    assert "PRD Category Bonus Checks" in rubric


def test_load_rubric_category_without_file():
    # Category with no rubric file falls back to universal only
    rubric = _load_rubric("customer-discovery")
    assert "Universal Evaluation Rubric" in rubric
    # Should not raise even if customer-discovery.md doesn't exist


def _make_mock_anthropic_response(scores: list[dict]) -> MagicMock:
    tool_block = MagicMock()
    tool_block.type = "tool_use"
    tool_block.name = "record_scores"
    tool_block.input = {"scores": scores}
    response = MagicMock()
    response.content = [tool_block]
    return response


def test_score_prompt_returns_score_results():
    mock_scores = [
        {"dimension": "completeness", "score": 4, "rationale": "All sections present", "is_bonus": False},
        {"dimension": "placeholder_substitution", "score": 5, "rationale": "No unfilled placeholders", "is_bonus": False},
        {"dimension": "format_compliance", "score": 4, "rationale": "Tables well-formed", "is_bonus": False},
        {"dimension": "actionability", "score": 4, "rationale": "Specific context provided", "is_bonus": False},
        {"dimension": "specificity", "score": 3, "rationale": "Some generic values", "is_bonus": False},
    ]

    with patch("evals.evaluators.llm_judge.anthropic") as mock_anthropic_module:
        mock_client = MagicMock()
        mock_anthropic_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_anthropic_response(mock_scores)

        results = score_prompt(
            prompt_id="prds/05-ai-prd",
            category="prds",
            filled_prompt="You are a PM building Aria...",
            api_key="test-key",
        )

    assert len(results) == 5
    assert all(isinstance(r, ScoreResult) for r in results)
    assert results[0].dimension == "completeness"
    assert results[0].score == 4
    assert results[0].is_bonus is False


def test_score_prompt_returns_empty_on_no_tool_call():
    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = "Here is my assessment..."
    response = MagicMock()
    response.content = [text_block]

    with patch("evals.evaluators.llm_judge.anthropic") as mock_anthropic_module:
        mock_client = MagicMock()
        mock_anthropic_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = response

        results = score_prompt(
            prompt_id="prds/01",
            category="prds",
            filled_prompt="test prompt",
            api_key="test-key",
        )

    assert results == []


def test_score_prompt_passes_cache_control():
    with patch("evals.evaluators.llm_judge.anthropic") as mock_anthropic_module:
        mock_client = MagicMock()
        mock_anthropic_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_anthropic_response([])

        score_prompt("prds/01", "prds", "test prompt", api_key="test-key")

        call_kwargs = mock_client.messages.create.call_args.kwargs
        system = call_kwargs["system"]
        assert isinstance(system, list)
        assert system[0]["cache_control"] == {"type": "ephemeral"}
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_llm_judge.py -v
```

Expected: `ImportError: cannot import name 'score_prompt' from 'evals.evaluators.llm_judge'`

- [ ] **Step 3: Create `evals/evaluators/llm_judge.py`**

```python
from __future__ import annotations
from pathlib import Path

import anthropic

from evals.types import ScoreResult

_RUBRICS_DIR = Path(__file__).parent.parent / "rubrics"

_SCORE_TOOL: dict = {
    "name": "record_scores",
    "description": "Record the evaluation scores for each rubric dimension",
    "input_schema": {
        "type": "object",
        "properties": {
            "scores": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "dimension": {"type": "string"},
                        "score": {"type": "integer", "minimum": 1, "maximum": 5},
                        "rationale": {"type": "string"},
                        "is_bonus": {"type": "boolean"},
                    },
                    "required": ["dimension", "score", "rationale", "is_bonus"],
                },
            }
        },
        "required": ["scores"],
    },
}


def _load_rubric(category: str) -> str:
    universal = (_RUBRICS_DIR / "universal.md").read_text()
    category_path = _RUBRICS_DIR / f"{category}.md"
    if category_path.exists():
        return universal + "\n\n" + category_path.read_text()
    return universal


def score_prompt(
    prompt_id: str,
    category: str,
    filled_prompt: str,
    api_key: str | None = None,
) -> list[ScoreResult]:
    client = anthropic.Anthropic(api_key=api_key)
    rubric = _load_rubric(category)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": rubric,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": (
                    f"Evaluate this filled PM prompt template (prompt ID: {prompt_id}):\n\n"
                    f"{filled_prompt}"
                ),
            }
        ],
        tools=[_SCORE_TOOL],
        tool_choice={"type": "any"},
    )

    for block in response.content:
        if block.type == "tool_use" and block.name == "record_scores":
            return [
                ScoreResult(
                    dimension=s["dimension"],
                    score=s["score"],
                    rationale=s["rationale"],
                    is_bonus=s["is_bonus"],
                )
                for s in block.input["scores"]
            ]

    return []
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_llm_judge.py -v
```

Expected: `7 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/evaluators/llm_judge.py tests/evals/test_llm_judge.py
git commit -m "feat: add Tier 2 LLM judge evaluator with prompt caching"
```

---

## Task 12: Fixture generator

**Files:**
- Create: `evals/fixtures/generator.py`
- Create: `tests/evals/test_generator.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/evals/test_generator.py
import json
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
from evals.fixtures.generator import generate_fixture, generate_and_save_fixture


def _mock_claude_response(values: dict) -> MagicMock:
    content_block = MagicMock()
    content_block.text = json.dumps(values)
    response = MagicMock()
    response.content = [content_block]
    return response


def test_generate_fixture_returns_dict():
    with patch("evals.fixtures.generator.anthropic") as mock_module:
        mock_client = MagicMock()
        mock_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _mock_claude_response(
            {"[FEATURE_NAME]": "Saved Search Alerts", "[FEATURE_GOAL]": "increase retention"}
        )
        result = generate_fixture("metrics/01-feature-success-metrics", api_key="test")

    assert "[FEATURE_NAME]" in result
    assert result["[FEATURE_NAME]"] == "Saved Search Alerts"


def test_generate_and_save_fixture_writes_file(tmp_path):
    with patch("evals.fixtures.generator.anthropic") as mock_module, \
         patch("evals.fixtures.generator._FIXTURES_DIR", tmp_path):
        mock_client = MagicMock()
        mock_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _mock_claude_response(
            {"[FEATURE_NAME]": "Alerts", "[FEATURE_DESCRIPTION]": "email notifications"}
        )
        path = generate_and_save_fixture("metrics/01-feature-success-metrics", api_key="test")

    assert path.exists()
    data = json.loads(path.read_text())
    assert data["_meta"]["generated"] == "auto"
    assert data["_meta"]["prompt_id"] == "metrics/01-feature-success-metrics"
    assert data["[FEATURE_NAME]"] == "Alerts"


def test_generate_and_save_fixture_creates_parent_dirs(tmp_path):
    with patch("evals.fixtures.generator.anthropic") as mock_module, \
         patch("evals.fixtures.generator._FIXTURES_DIR", tmp_path):
        mock_client = MagicMock()
        mock_module.Anthropic.return_value = mock_client
        mock_client.messages.create.return_value = _mock_claude_response({"[FOO]": "bar"})
        path = generate_and_save_fixture("some/new-category/01-prompt", api_key="test")

    assert (tmp_path / "some" / "new-category").is_dir()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/evals/test_generator.py -v
```

Expected: `ImportError: cannot import name 'generate_fixture' from 'evals.fixtures.generator'`

- [ ] **Step 3: Create `evals/fixtures/generator.py`**

```python
from __future__ import annotations
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import anthropic

from evals.fixtures import _FIXTURES_DIR

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mcp-server"))


def generate_fixture(prompt_id: str, api_key: str | None = None) -> dict:
    from server import parse_prompt_file, PROMPTS_DIR  # noqa: E402

    prompt_file = PROMPTS_DIR / f"{prompt_id}.md"
    if not prompt_file.exists():
        return {}

    prompt = parse_prompt_file(prompt_file)
    if not prompt["placeholders"]:
        return {}

    placeholder_list = "\n".join(
        f"- {k}: {v}" for k, v in prompt["placeholders"].items()
    )

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Generate realistic PM context values for this prompt template's placeholders.\n\n"
                    f"Prompt title: {prompt['title']}\n"
                    f"Purpose: {prompt['purpose']}\n\n"
                    f"Placeholders to fill:\n{placeholder_list}\n\n"
                    f"Return a JSON object where each key is exactly the placeholder name "
                    f"(including square brackets) and the value is a realistic, specific PM "
                    f"context value. Use a realistic B2B SaaS product as context. "
                    f"Be concrete — avoid generic placeholder-style values like 'your product name'."
                ),
            }
        ],
    )

    text = response.content[0].text
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if not json_match:
        return {}

    try:
        return json.loads(json_match.group())
    except json.JSONDecodeError:
        return {}


def generate_and_save_fixture(prompt_id: str, api_key: str | None = None) -> Path:
    values = generate_fixture(prompt_id, api_key=api_key)

    fixture = {
        "_meta": {
            "prompt_id": prompt_id,
            "generated": "auto",
            "author": "generator.py",
            "date": datetime.now().strftime("%Y-%m-%d"),
        },
        **values,
    }

    fixture_path = _FIXTURES_DIR / f"{prompt_id}.json"
    fixture_path.parent.mkdir(parents=True, exist_ok=True)
    fixture_path.write_text(json.dumps(fixture, indent=2))
    return fixture_path
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/evals/test_generator.py -v
```

Expected: `3 passed`

- [ ] **Step 5: Commit**

```bash
git add evals/fixtures/generator.py tests/evals/test_generator.py
git commit -m "feat: add fixture generator — auto-generates fixture JSON via Claude"
```

---

## Task 13: CI workflow

**Files:**
- Create: `.github/workflows/evals.yml`

No automated tests — verify by inspecting the YAML.

- [ ] **Step 1: Create `.github/workflows/evals.yml`**

```yaml
name: Evals — Structural Checks

on:
  push:
    paths:
      - "prompts/**"
      - "evals/**"

jobs:
  structural-evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install evals dependencies
        run: pip install -r evals/requirements.txt

      - name: Install mcp-server dependencies
        run: pip install -r mcp-server/requirements.txt

      - name: Run structural evals on changed prompts
        run: python -m evals run --changed-only --tier structural

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: eval-results
          path: evals/results/
```

- [ ] **Step 2: Verify mcp-server has a requirements.txt**

```bash
cat mcp-server/requirements.txt
```

Expected to contain `mcp` package. If the file doesn't exist:

```bash
echo "mcp" > mcp-server/requirements.txt
```

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/evals.yml
git commit -m "ci: add evals workflow — structural checks on changed prompts"
```

---

## Task 14: End-to-end smoke test

Run the full structural eval suite to verify everything wires together.

- [ ] **Step 1: Run full test suite**

```bash
cd /Users/stynger76/Documents/GitHub/AI-Prompts-for-Product-Management
pip install -r evals/requirements.txt
pytest tests/evals/ -v
```

Expected: All tests pass. Note any failures and fix before proceeding.

- [ ] **Step 2: Run structural evals for all prompts with fixtures**

```bash
python -m evals run --tier structural
```

Expected: Rich table showing results for the 9 hand-written fixtures. All 9 should PASS (structural checks pass for hand-written fixtures). Observe the `evals/results/` directory:

```bash
ls evals/results/
```

Expected: `<timestamp>.json` and `latest-report.md` files created.

- [ ] **Step 3: Run status command**

```bash
python -m evals status
```

Expected: Table showing all 70+ prompts, with ✓ for 9 fixtures and ✗ missing for the rest.

- [ ] **Step 4: Run category-filtered eval**

```bash
python -m evals run --tier structural --category metrics
```

Expected: 2 results (01-feature-success-metrics, 02-ai-product-metrics), both PASS.

- [ ] **Step 5: Commit final state**

```bash
git add evals/results/.gitkeep
git commit -m "test: verify end-to-end structural evals pass for all 9 hand-written fixtures"
```

---

## Self-Review

### Spec coverage check

| Spec section | Covered by task |
|---|---|
| Directory layout | Task 1 scaffold |
| `parse_prompt_file` reuse from mcp-server | Task 6 runner.py |
| Tier 1: all 5 structural checks | Task 2 |
| Tier 2: LLM judge with tool_use | Task 11 |
| CLI: `run --tier structural/all` | Task 10 |
| CLI: `run --category`, `--prompt`, `--changed-only` | Task 10 |
| CLI: `generate-fixtures` | Task 10 + Task 12 |
| CLI: `status` | Task 10 |
| Terminal reporter (Rich) | Task 7 |
| JSON reporter with timestamped filename | Task 8 |
| Markdown `latest-report.md` | Task 9 |
| Universal rubric (5 dimensions) | Task 4 |
| Category bonus rubrics (prds, metrics, prototyping, strategy) | Task 4 |
| Fixture format with `_meta.generated` | Tasks 5, 12 |
| 9 hand-written priority fixtures | Task 5 |
| Auto-generated fixtures via Claude | Task 12 |
| Prompt caching `cache_control=ephemeral` on rubric | Task 11 |
| `evals/requirements.txt` | Task 1 |
| CI workflow `--changed-only --tier structural` | Task 13 |
| `evals/results/.gitkeep` | Task 1 |

All spec sections covered. ✓

### Type consistency check

- `CheckResult`, `ScoreResult`, `EvalResult` defined in Task 1 (`types.py`), used unchanged in Tasks 2, 6, 7, 8, 9, 11.
- `run_structural_checks` signature in Task 2 matches calls in Task 6 runner.
- `score_prompt` signature in Task 11 matches calls in Task 6 runner.
- `load_fixture` in Task 3 matches calls in Tasks 6 and 12 (`load_fixture(prompt_id)` → `dict | None`).
- `_FIXTURES_DIR` exported from `evals/fixtures/__init__.py` and imported in Task 12 generator.
- `write` function in reporters Tasks 8 and 9 accept `results_dir: Path | None` for test isolation.
