# Evals Harness — Design Spec

**Date:** 2026-05-02
**Status:** Approved
**Author:** PM team

---

## Overview

A two-tier evaluation harness for the AI Prompts for Product Management library. Tier 1 runs fast structural checks in CI on every push. Tier 2 runs Claude-as-judge scoring on demand, targeted to a category, prompt ID, or git-changed files. All runs produce terminal output, a JSON artifact, and a Markdown report.

---

## Directory Layout

```
evals/
├── __init__.py
├── cli.py                        # Entry point: python -m evals <command>
├── runner.py                     # Orchestrates: load → fill → evaluate → report
├── evaluators/
│   ├── __init__.py
│   ├── structural.py             # Tier 1 — pure Python, no API
│   └── llm_judge.py              # Tier 2 — Claude-as-judge via Anthropic SDK
├── reporters/
│   ├── __init__.py
│   ├── terminal.py               # Coloured table via Rich
│   ├── json_reporter.py          # evals/results/<timestamp>.json
│   └── markdown_reporter.py      # evals/results/latest-report.md
├── fixtures/
│   ├── __init__.py               # Fixture loading utility
│   ├── generator.py              # Auto-generates fixtures via Claude API
│   ├── prds/
│   │   ├── 01-prd-generation.json
│   │   ├── 02-use-case-documentation.json
│   │   ├── 03-features-and-user-stories.json
│   │   ├── 04-given-when-then.json        # hand-written
│   │   └── 05-ai-prd.json                 # hand-written
│   ├── metrics/
│   │   ├── 01-feature-success-metrics.json  # hand-written
│   │   └── 02-ai-product-metrics.json       # hand-written
│   ├── strategy/                  # hand-written for key prompts
│   └── <category>/                # auto-generated for the rest
├── rubrics/
│   ├── universal.md               # Core 5-dimension rubric
│   ├── prds.md                    # Category bonus checks
│   ├── metrics.md
│   └── prototyping.md
└── results/
    └── .gitkeep
```

**Key constraint:** `runner.py` imports `parse_prompt_file` directly from `mcp-server/server.py`. Prompt parsing logic lives in exactly one place.

---

## Data Flow

```
CLI args
  → runner resolves prompt list:
      --category <slug>     filter by category
      --prompt <id>         single prompt
      --changed-only        git diff HEAD^ to find changed prompt files
      (default: all prompts with fixtures)

  → for each prompt:
      parse_prompt_file()         ← reused from mcp-server/server.py
      load fixture JSON
      fill [PLACEHOLDERS] → filled_prompt string

      ── Tier 1: structural (always) ──────────────────────
      structural.py:
        • placeholders_filled    — no [BRACKET] tokens remain
        • sections_present       — all ## headers from template exist in output
        • tables_well_formed     — markdown table rows have matching column count
        • code_blocks_closed     — every ``` opener has a closer
        • required_fields        — prompt-specific required keys present

      ── Tier 2: llm_judge (--tier all) ──────────────────
      llm_judge.py:
        • system prompt = universal rubric + category rubric (cached)
        • user message  = filled_prompt
        • response via tool_use → structured ScoreResult list

  → reporters (after all prompts complete):
      terminal.py         → stdout coloured table + failure details
      json_reporter       → evals/results/<timestamp>.json
      markdown_reporter   → evals/results/latest-report.md
```

---

## Core Data Types

```python
@dataclass
class CheckResult:
    name: str       # e.g. "placeholders_filled"
    passed: bool
    message: str    # detail on failure; empty on pass

@dataclass
class ScoreResult:
    dimension: str  # e.g. "completeness"
    score: int      # 1–5
    rationale: str  # one sentence from judge
    is_bonus: bool  # True = category-specific check

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

---

## CLI Interface

```bash
# Tier 1 only — CI default
python -m evals run --tier structural

# Both tiers, scoped to category
python -m evals run --category prds --tier all

# Both tiers, single prompt
python -m evals run --prompt prds/05-ai-prd --tier all

# CI mode — git-changed prompt files only
python -m evals run --changed-only --tier structural

# Generate fixtures for prompts missing one
python -m evals generate-fixtures --category prototyping

# Show all prompts with fixture + last eval status
python -m evals status
```

Default `--tier` is `structural`. `--tier all` requires `ANTHROPIC_API_KEY` in environment.

---

## Rubrics

### Universal (all prompts, 5 dimensions, scored 1–5)

| Dimension | Definition | Pass threshold |
|---|---|---|
| Completeness | All sections and sub-sections the template requested are present | ≥ 3 |
| Placeholder substitution | All `[PLACEHOLDERS]` replaced with contextually appropriate content | ≥ 4 |
| Format compliance | Tables, code blocks, headers match the template's specified structure | ≥ 3 |
| Actionability | A PM could hand this to their team and act on it today | ≥ 3 |
| Specificity | Concrete details; no generic filler or re-stated placeholders | ≥ 3 |

**Overall pass threshold:** average ≥ 3.5. Any individual dimension < 3 flags a warning regardless of average.

### Category bonus checks (scored 1–5, appended to LLM call)

| Category | Bonus check |
|---|---|
| `prds` | All 11 AI PRD sections present; GWT criteria include Given/When/Then/And/But |
| `metrics` | Every metric row has measurement method, target, and baseline |
| `prototyping` | Output maps to the correct prototype type; checklists present |
| `strategy` | Success criteria measurable; OKR key results have numeric targets |

Rubric files are plain Markdown so PMs can edit them without touching Python.

---

## Fixture Format

```json
{
  "_meta": {
    "prompt_id": "prds/05-ai-prd",
    "generated": "handwritten",
    "author": "PM team",
    "date": "2026-05-02"
  },
  "[PRODUCT_NAME]": "Aria — AI Support Assistant",
  "[ONE_LINE_DESCRIPTION]": "Drafts replies to inbound support tickets and surfaces the most relevant knowledge base articles",
  "[STAGE]": "Discovery",
  "[OBJECTIVE]": "Reduce average handle time for Tier-1 support agents by 40% through AI-assisted response drafting"
}
```

- Keys match the placeholder names exactly as they appear in the prompt (`[BRACKET_FORMAT]`)
- `_meta.generated`: `"handwritten"` or `"auto"` — allows filtering fixtures that need human review
- Fixture path mirrors prompt path: `fixtures/prds/05-ai-prd.json` → `prompts/prds/05-ai-prd.md`
- Missing fixture → prompt is skipped with a warning, not a failure

### Hand-written fixtures (priority set)

The following fixtures are hand-written with realistic PM context:

- `prds/04-given-when-then.json`
- `prds/05-ai-prd.json`
- `metrics/01-feature-success-metrics.json`
- `metrics/02-ai-product-metrics.json`
- `strategy/01-product-strategy-canvas.json`
- `strategy/02-team-okr-generator.json`
- `strategy/08-big-rock-decomposition.json`
- `prototyping/05-wizard-of-oz-protocol.json`
- `prototyping/07-ai-feature-stub.json`

All remaining fixtures are auto-generated via `generate-fixtures` and tagged `"generated": "auto"`.

---

## Reporting

### Terminal (Rich)

```
╭─ Evals Run ── 2026-05-02 14:31 ── tier: all ── 12 prompts ───────────────╮
│  Prompt                        Structural   Score   Duration   Status     │
│  prds/05-ai-prd                6/6 ✓        4.6/5   8.2s       PASS ✓   │
│  metrics/02-ai-product-metrics 5/6 ✗        3.1/5   6.8s       FAIL ✗   │
│  Summary  11 passed · 1 failed · avg 4.1/5 · 94s                         │
│  Failures                                                                  │
│    metrics/02-ai-product-metrics                                           │
│      ✗ structural: unfilled placeholder [CURRENT_INSTRUMENTATION]         │
│      ✗ judge specificity 2/5: metrics lack measurement methods            │
╰───────────────────────────────────────────────────────────────────────────╯
```

### JSON (`evals/results/<timestamp>.json`)

Top-level keys: `run_id`, `tier`, `filter`, `summary`, `results`. Each result contains the full `EvalResult` serialised. Used for CI artifact upload and score diffing across runs.

### Markdown (`evals/results/latest-report.md`)

Overwritten on every run. Contains: run metadata, summary table, per-prompt results table, failure detail section. Designed to be committed to the repo or attached to a PR comment.

---

## Prompt Caching

The universal rubric is identical across every LLM call in a batch run. It is placed in the system prompt with `cache_control={"type": "ephemeral"}` so the first call in a run writes the cache and all subsequent calls are cache hits. Estimated token cost reduction: ~80% on the system prompt portion of each judge call.

---

## Dependencies

Added to `evals/requirements.txt` (separate from mcp-server):

```
anthropic>=0.40.0
rich>=13.0.0
```

`ANTHROPIC_API_KEY` environment variable required for `--tier all` and `generate-fixtures`. Structural tier runs with no API key.

---

## CI Integration

`.github/workflows/evals.yml` (or equivalent):

```yaml
on: [push]
jobs:
  evals:
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 2 }
      - run: pip install -r evals/requirements.txt
      - run: python -m evals run --changed-only --tier structural
      - uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: evals/results/
```

LLM-judge tier is not run in CI to avoid API cost on every push. It is run manually before merging prompt additions.

---

## Out of Scope

- Web UI for browsing eval results
- Automatic PR comments from eval output
- Fine-tuning or RLHF pipelines from eval scores
- Per-prompt custom rubrics (category bonus checks are the granularity floor)
