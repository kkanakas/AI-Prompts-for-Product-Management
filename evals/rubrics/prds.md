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
