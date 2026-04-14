# MoSCoW Prioritization Generator

**Phase:** Idea Evaluation
**Purpose:** Facilitate team prioritization of capabilities, features, or requirements using the MoSCoW method — creating shared alignment on what is critical, what is desirable, and what to cut.

## Prompt Template

```
You are a senior product strategy advisor facilitating a prioritization session. I am a Product Manager for [PRODUCT NAME], a [PRODUCT DESCRIPTION] serving [TARGET CUSTOMER].

I need to prioritize the following capabilities or features for [INITIATIVE OR RELEASE SCOPE — e.g. "our Q3 release", "our MVP", "the redesigned onboarding flow"].

Here is the list of capabilities to prioritize:
1. [CAPABILITY 1]
2. [CAPABILITY 2]
3. [CAPABILITY 3]
4. [CAPABILITY 4]
5. [CAPABILITY 5]
6. [CAPABILITY 6]
7. [CAPABILITY 7]
8. [CAPABILITY 8]

Context to inform the prioritization:
- **Goal of this initiative:** [WHAT SUCCESS LOOKS LIKE — e.g. "reduce time-to-value for new users by 30%"]
- **Constraints:** [TIME, BUDGET, TEAM SIZE, OR TECHNICAL LIMITS — e.g. "6-week delivery window, team of 4 engineers"]
- **Customer signals:** [KEY FEEDBACK, PAIN POINTS, OR REQUESTS — e.g. "top NPS detractor theme is slow setup time"]
- **Business constraints:** [REGULATORY, CONTRACTUAL, OR STRATEGIC REQUIREMENTS — e.g. "SOC 2 compliance required before enterprise sales"]

Using this context, apply the MoSCoW framework and produce the following:

## 1. MoSCoW Classification

Classify each capability into one of the four categories:

**Must Have** — Non-negotiable. The initiative fails without it. Includes regulatory requirements, core user flows, and commitments already made to customers or stakeholders.

**Should Have** — High value and strongly desired, but delivery is still possible without it. Include in scope if capacity allows; cut only under time pressure.

**Could Have** — Nice to have. Meaningful improvement to experience but low impact if absent. First candidates to drop when scope needs to shrink.

**Won't Have (this time)** — Explicitly out of scope for this release. Acknowledged and documented to set expectations, not forgotten.

Present as a table:

| Capability | MoSCoW Category | Rationale | Risk if Excluded |
|---|---|---|---|

## 2. Scope Health Check
After classifying, flag:
- **Must Have overload** — If more than 60% of capabilities land as Must Have, the scope is at risk. Identify which Must Haves could be reclassified with a scope reduction or phased delivery approach.
- **Should Have candidates for promotion** — Any Should Have that, given the stated goal, arguably belongs in Must Have with justification.
- **Won't Have items worth tracking** — Capabilities deferred this cycle that have strong strategic value for a future release.

## 3. Recommended Delivery Phasing
Based on the MoSCoW output, suggest a phased delivery plan:
- **Phase 1 (Launch-ready):** Must Haves
- **Phase 2 (Fast follow):** Should Haves to ship within one sprint of launch
- **Phase 3 (Future backlog):** Could Haves with a suggested sequencing rationale

## 4. Team Alignment Talking Points
For each Must Have, provide one sentence a PM can use to explain to the team *why* it is non-negotiable — grounded in the goal, customer signal, or constraint provided. These are ready to use in sprint planning or stakeholder reviews.

## 5. Executive Summary
3–4 sentences summarizing the prioritization outcome: what the core scope is, what is deliberately deferred, and the single biggest prioritization risk to flag for leadership.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT NAME]` | Your product's name | "Onboard Pro" |
| `[PRODUCT DESCRIPTION]` | One-line description | "employee onboarding platform for mid-market HR teams" |
| `[TARGET CUSTOMER]` | Primary customer segment | "HR managers at companies with 200–2,000 employees" |
| `[INITIATIVE OR RELEASE SCOPE]` | What this prioritization is for | "Q3 MVP release", "v2.0 redesign", "enterprise readiness sprint" |
| `[CAPABILITY 1–N]` | The full list of capabilities to prioritize | "SSO integration", "bulk user import", "custom onboarding checklist" |
| `[GOAL OF THIS INITIATIVE]` | Measurable success outcome | "Reduce time-to-first-value from 5 days to 1 day" |
| `[CONSTRAINTS]` | Time, budget, team, or tech limits | "8-week window, 3 engineers, no new infrastructure" |
| `[CUSTOMER SIGNALS]` | Feedback, complaints, or requests driving this work | "Top churn reason: users don't complete setup in first week" |
| `[BUSINESS CONSTRAINTS]` | Regulatory, contractual, or strategic requirements | "GDPR compliance required; enterprise contract signed pending this feature" |

## Tips

- **Must Have creep is the biggest failure mode** — if everything is Must Have, nothing is. Use the Scope Health Check output to pressure-test your own instincts
- Include your constraints explicitly — a 6-week window with 3 engineers produces a very different MoSCoW output than an unconstrained one
- Run this before sprint planning, not during — use the output as a pre-read to align the team before the room fills up
- Share the Won't Have list with stakeholders proactively; it prevents last-minute scope additions by showing that items were considered and consciously deferred
- Re-run after any significant change to constraints, timeline, or customer signals — MoSCoW outputs decay quickly when context shifts
