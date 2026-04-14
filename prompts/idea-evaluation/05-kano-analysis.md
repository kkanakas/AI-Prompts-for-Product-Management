# Kano Analysis Generator

**Phase:** Idea Evaluation
**Purpose:** Classify product features or ideas using the Kano model to distinguish must-haves from delighters — and avoid wasting investment on features that won't move customer satisfaction.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager evaluating a set of features or capabilities for [PRODUCT NAME], a [PRODUCT DESCRIPTION] serving [TARGET CUSTOMER].

I need to run a Kano analysis to understand how each feature will affect customer satisfaction and where to prioritize investment.

Here are the features I want to evaluate:
1. [FEATURE 1]
2. [FEATURE 2]
3. [FEATURE 3]
4. [FEATURE 4]
5. [FEATURE 5]

Additional context about our customers and competitive landscape:
[ANY RELEVANT CONTEXT — e.g. customer segment, maturity of market, known complaints, competitor features]

For each feature, apply the Kano model and produce the following:

## 1. Kano Classification Table

| Feature | Kano Category | Rationale | Customer Reaction if Present | Customer Reaction if Absent |
|---|---|---|---|---|

Use these Kano categories:
- **Basic (Must-Have)** — Expected by default; absence causes strong dissatisfaction; presence goes unnoticed
- **Performance (Linear)** — More is better; directly proportional to satisfaction; customers notice and value improvements
- **Delighter (Excitement)** — Unexpected; creates strong positive reaction when present; no dissatisfaction if absent
- **Indifferent** — Customers do not care either way; presence or absence has no meaningful impact
- **Reverse** — Some customers actively dislike this feature; presence causes dissatisfaction for a segment

## 2. Investment Priority Recommendation

Based on the Kano classification, recommend investment priority:

| Priority Tier | Feature(s) | Reasoning |
|---|---|---|
| **Tier 1 — Fix first** | Basic gaps we are missing | Absence is actively harming satisfaction |
| **Tier 2 — Scale next** | Performance features with room to improve | Direct satisfaction ROI per unit of investment |
| **Tier 3 — Differentiate** | Delighters worth building | Highest potential to create memorable moments and word-of-mouth |
| **Tier 4 — Defer or drop** | Indifferent or Reverse features | Low or negative return on investment |

## 3. Satisfaction Risk Assessment
For any feature classified as Basic that we do not currently have, flag it as a satisfaction risk with:
- Estimated customer impact (High / Medium / Low)
- How quickly we need to address it (Urgent / This quarter / Backlog)

## 4. Delight Opportunity Spotlight
For the top 1–2 Delighter features, provide:
- Why this has outsized potential for this customer segment
- A suggested MVP scope to test the delight hypothesis cheaply
- A success signal to know if it is landing as a true Delighter vs. Indifferent

## 5. Executive Summary
3–4 sentences summarizing the overall feature portfolio health: what foundational gaps exist, where performance investment has the best return, and which one Delighter has the strongest case to build next.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT NAME]` | Your product's name | "Trello" |
| `[PRODUCT DESCRIPTION]` | One-line description | "visual project management tool for teams" |
| `[TARGET CUSTOMER]` | Primary customer segment | "SMB teams managing cross-functional projects" |
| `[FEATURE 1–5]` | Features or capabilities to evaluate | "Offline mode", "AI task suggestions", "Custom fields" |
| `[ANY RELEVANT CONTEXT]` | Competitive signals, known complaints, customer tier | "Enterprise customers frequently request SSO; competitors have it" |

## Tips

- Kano categories are not fixed — the same feature can shift from Delighter to Basic as market expectations mature (e.g. mobile apps were once a Delighter, now a Basic)
- If you have customer survey data or NPS verbatims, include excerpts — they sharpen the AI's classification significantly
- Run Kano analysis per customer segment separately if your product serves distinct personas; what delights SMBs may be Basic for Enterprise
- The most common mistake is over-investing in Performance features while ignoring Basic gaps — use this output to pressure-test your roadmap balance
