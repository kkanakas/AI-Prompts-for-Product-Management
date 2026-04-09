# MECE Analysis

**Phase:** Ideation
**Purpose:** Decompose a complex product problem or strategic challenge into a set of categories that are Mutually Exclusive and Collectively Exhaustive (MECE), then diagnose each category by identifying the key issue, root cause, and proposed solution — all cited back to the uploaded source document.

## Before You Begin

Upload the document you want to analyze (e.g., a research report, strategy deck, PRD, competitive brief, or discovery synthesis). The model will use it as the primary source and cite specific sections, page numbers, or passages in its output.

## Prompt Template

```
You are a senior product manager and strategist. I am uploading a document for you to analyze.

[UPLOAD YOUR DOCUMENT HERE]

Using the uploaded document as your primary source, conduct a MECE analysis on the following challenge:

Topic / Challenge: [TOPIC_OR_CHALLENGE]
Scope: [SCOPE]
Audience for this analysis: [AUDIENCE]

Follow these steps:

Step 1 — Define the MECE structure
Break the topic into [3–6] categories that together cover the full problem space (Collectively Exhaustive) with no meaningful overlap between them (Mutually Exclusive). State each category name and a one-sentence definition of what it includes and explicitly excludes.

Step 2 — Analyze each category
For each category, provide:
1. Key issue — the specific problem or gap within this category, as evidenced by the document
2. Root cause — the underlying reason this issue exists (not a symptom)
3. Proposed solution — a concrete, actionable recommendation to address the root cause
4. Source citation — the exact section, page, quote, or data point from the uploaded document that supports this analysis

Step 3 — Validate MECE integrity
After completing all categories, confirm:
- No issue or theme appears in more than one category (Mutually Exclusive check)
- Together, the categories account for the full scope of the challenge (Collectively Exhaustive check)
- If any gaps or overlaps are found, revise the structure and explain what changed

Step 4 — Executive summary
Provide a 3–5 sentence summary of the most critical finding across all categories and the single highest-priority recommendation for the team to act on first.
```

## Placeholders

| Variable | Description |
|---|---|
| `[UPLOAD YOUR DOCUMENT HERE]` | The source document to analyze — research report, strategy memo, PRD, competitive brief, discovery synthesis, etc. |
| `[TOPIC_OR_CHALLENGE]` | The specific problem, decision, or question you want the MECE analysis to address |
| `[SCOPE]` | The boundaries of the analysis — what is in and out of scope (e.g., "North America market only", "mobile app experience only") |
| `[AUDIENCE]` | Who will consume this analysis (e.g., executive team, engineering leads, design partners) — shapes the depth and tone of recommendations |
| `[3–6]` | The number of top-level MECE categories to generate — use 3–4 for focused problems, 5–6 for broad strategic challenges |

## Tips

- The quality of the MECE structure depends on how clearly you define the topic and scope — vague inputs produce categories that are hard to separate cleanly.
- If the document covers multiple user segments or markets, ask for a MECE breakdown per segment to avoid aggregation hiding segment-specific issues.
- Use the "Validate MECE integrity" step as a forcing function — asking the model to self-check often catches category drift that would otherwise weaken the analysis.
- For strategic planning, run this prompt on competing documents (e.g., two market research reports) and compare the resulting MECE structures to surface where sources agree and disagree.
- Cite-heavy outputs are easier to pressure-test in a review — if a recommendation cannot be traced back to the document, it is an assumption, not a finding.
