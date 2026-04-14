# Team OKR Generator

**Phase:** Strategy
**Purpose:** Cascade company OKRs into well-formed, measurable team OKRs — ensuring every Objective is inspiring and time-bound, every Key Result is quantified and outcome-focused, and the team's work has a clear line of sight to company goals.

## Prompt Template

```
You are a senior OKR coach and product strategy advisor. I am a Product Management leader building team OKRs that cascade from our company-level OKRs.

**Company OKRs (this quarter/year):**
[PASTE COMPANY OKRS HERE — Objectives and their Key Results as written by leadership]

**My team context:**
- Team name: [TEAM NAME]
- What the team owns: [PRODUCT AREA, PLATFORM, OR DOMAIN — e.g. "user onboarding, activation flow, and the free-to-paid conversion funnel"]
- Team size: [NUMBER AND ROLES — e.g. "1 PM, 4 engineers, 1 designer, 1 data analyst"]
- Current quarter: [Q AND YEAR — e.g. "Q3 2025"]
- Initiatives or themes already planned: [ANY COMMITTED WORK OR KNOWN PRIORITIES — e.g. "redesigning the setup wizard, shipping SSO, reducing onboarding drop-off"]
- Key constraints: [DEPENDENCIES, HEADCOUNT LIMITS, TECH DEBT, OR EXTERNAL BLOCKERS]
- Baseline metrics (where known): [CURRENT NUMBERS FOR METRICS THE TEAM INFLUENCES — e.g. "activation rate: 38%, time-to-value: 6 days, free-to-paid conversion: 4.2%"]

---

Using this input, produce the following:

## 1. OKR Cascade Map
Show how each company Objective maps to the team's area of influence. For each company Objective, identify:
- Which part of it my team can meaningfully move
- The team's lever — what action or product change creates that movement
- The metric that would prove we moved it

Present as a table:
| Company Objective | Team's Area of Influence | Team Lever | Measurable Signal |
|---|---|---|---|

## 2. Recommended Team OKRs

Write 2–3 Objectives with 3–4 Key Results each. Apply these strict OKR quality rules:

**Objectives must:**
- Start with a verb (Accelerate, Establish, Transform, Deliver, Grow)
- Be qualitative and aspirational — describe a desired state, not a task
- Be achievable within the quarter
- Connect clearly to at least one company Objective

**Key Results must:**
- Be quantified — every KR must contain a number, percentage, or binary milestone
- Be outcome-focused — measure what changed for users or the business, not what the team shipped
- Follow the format: "[Metric] from [baseline] to [target] by [date]" or "Achieve [specific milestone] by [date]"
- Avoid output language like "launch", "build", "deliver", or "complete" unless paired with a measurable outcome
- Be independently trackable — the team should be able to report progress weekly without waiting for another team

**Format each OKR as:**

---
**Objective [N]: [OBJECTIVE STATEMENT]**
*Connects to company Objective: [COMPANY OBJECTIVE IT SUPPORTS]*

- KR1: [Metric] from [baseline] to [target] by [date]
- KR2: [Metric] from [baseline] to [target] by [date]
- KR3: [Metric] from [baseline] to [target] by [date]
- KR4 (optional): [Specific milestone achieved by date]

*Why this Objective matters: [1-sentence rationale linking team work to company impact]*
---

## 3. OKR Health Check

Review each proposed KR against these failure patterns and flag any issues:

| KR | Issue | Suggested Fix |
|---|---|---|
| Activity KR (measures output, not outcome) | Reframe around the change it creates | |
| Vanity metric (large number, no business impact) | Replace with a metric that reflects real value | |
| Missing baseline (no starting point) | Add current state so progress is measurable | |
| Binary without nuance (yes/no only) | Add an intermediate milestone or leading indicator | |
| Outside team control (requires another team to move) | Adjust to a metric the team directly influences | |

Only populate rows where an issue exists. If all KRs pass, state "All Key Results pass the health check."

## 4. Leading Indicators Dashboard
For each Objective, identify 1–2 leading indicators — early signals that will appear in weeks 2–4 of the quarter to show the team is on track before the final KR target is reachable. These are not KRs; they are internal tracking signals.

| Objective | Leading Indicator | Check-in cadence | What a green signal looks like |
|---|---|---|---|

## 5. Risks to OKR Achievement
List the top 3 risks that could prevent the team from hitting these OKRs. For each:
- The risk
- Likelihood: High / Medium / Low
- Mitigation action the PM should take in week 1 of the quarter

## 6. OKR Communication Draft
Write a short message (Slack / Teams format, under 200 words) the PM can send to their team to introduce these OKRs at the start of the quarter. Tone: clear, energizing, and grounded in why the work matters — not corporate.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[COMPANY OKRS]` | The company OKRs as written by leadership | "O1: Become the #1 choice for mid-market HR teams. KR1: Grow ARR from $8M to $12M. KR2: Achieve NPS of 45+" |
| `[TEAM NAME]` | Your team's name | "Growth & Activation Team" |
| `[PRODUCT AREA OR DOMAIN]` | What the team owns | "User onboarding, activation flow, free-to-paid conversion" |
| `[TEAM SIZE AND ROLES]` | Headcount and composition | "1 PM, 4 engineers, 1 designer, 1 analyst" |
| `[CURRENT QUARTER]` | Quarter and year | "Q3 2025" |
| `[INITIATIVES ALREADY PLANNED]` | Committed or likely work | "Redesigning setup wizard, shipping SSO, A/B testing pricing page" |
| `[KEY CONSTRAINTS]` | Blockers, dependencies, limits | "Dependent on data platform team for event tracking; one engineer on leave in August" |
| `[BASELINE METRICS]` | Current numbers for relevant metrics | "Activation rate: 38%, time-to-value: 6 days, free-to-paid: 4.2%" |

## Tips

- **Paste your company OKRs verbatim** — even if they are poorly written, the AI needs the exact language to identify the cascade connection
- **Baselines are critical** — a KR without a baseline ("increase activation rate to 50%") is untrackable; if you don't have one, say so and the AI will flag it
- **Aim for 60–70% confidence on targets** — OKRs should be stretching, not sandbagged; if you are 100% confident, the target is too low
- **Fewer is better** — 2 strong Objectives with 3 sharp KRs each outperforms 5 Objectives with vague KRs; use the Health Check output to cut ruthlessly
- **Run a team review session** — use the generated OKRs as a starting draft, not the final version; team co-creation increases ownership and catches blind spots the PM may have
- **Separate OKRs from the roadmap** — OKRs define what changes in the world; the roadmap defines how you get there; do not put feature names in your KRs
