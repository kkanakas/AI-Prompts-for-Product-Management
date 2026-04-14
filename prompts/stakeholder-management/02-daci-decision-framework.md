# DACI Decision Framework Generator

**Phase:** Stakeholder Management
**Purpose:** Document a product decision using the DACI framework — clarifying who Drives the decision, who Approves it, who Contributes input, and who is Informed of the outcome — so that decisions move forward without ambiguity, revisiting, or silent disagreement.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager who needs to document a key decision using the DACI framework to create clarity on ownership, prevent decision paralysis, and ensure the right people are consulted before a choice is locked.

**Decision to be made:**
[STATE THE DECISION CLEARLY — one sentence describing what is being decided, not the background or context]

**Context and background:**
[WHY THIS DECISION NEEDS TO BE MADE NOW — the trigger, the problem it solves, or the opportunity it captures]

**Options under consideration:**
- Option A: [DESCRIPTION]
- Option B: [DESCRIPTION]
- Option C: [DESCRIPTION — add or remove options as needed]

**Decision deadline:**
[DATE BY WHICH THE DECISION MUST BE MADE AND WHY]

**People involved:**
[LIST NAMES, ROLES, AND TEAMS]

**Constraints or non-negotiables:**
[ANY FACTORS THAT ARE FIXED AND CANNOT BE CHANGED — budget caps, regulatory requirements, prior commitments, technical limits]

---

Using this input, produce a complete DACI document with the following sections:

## 1. Decision Statement
A single, unambiguous sentence that captures exactly what is being decided. It should be specific enough that two people reading it independently would agree on whether the decision has been made.

Format: "Decide [WHAT] for [SCOPE OR PRODUCT AREA] by [DATE] in order to [OUTCOME OR UNBLOCK]."

## 2. DACI Role Assignment

Assign each person to exactly one DACI role:

**Driver (1 person only)**
The single person accountable for moving this decision forward. Owns the process: gathers input, runs the decision meeting, documents the outcome, and ensures the decision is communicated. The Driver does not necessarily make the decision — they ensure it gets made.

**Approver (1 person only)**
The single person with final decision authority. If there is disagreement among Contributors, the Approver decides. There can only be one Approver — if more than one person is proposed, flag this as a decision risk.

**Contributors (as many as needed, as few as possible)**
People whose input must be sought before the decision is made. They have a voice, not a vote. Contributors should be limited to people with unique expertise or perspective that would change the decision if withheld. List why each Contributor's input is essential.

**Informed (as many as needed)**
People who need to know the outcome but do not provide input. Informed parties receive a communication after the decision is made, not an invitation to weigh in.

Present as a table:

| Name | Role / Team | DACI Role | Why this role |
|---|---|---|---|

## 3. Decision Criteria
List the 4–6 criteria that will be used to evaluate the options. For each criterion, note its weight (High / Medium / Low) and who owns the assessment of that criterion.

| Criterion | Weight | Who assesses it | What "good" looks like |
|---|---|---|---|

## 4. Options Analysis
For each option under consideration, assess it against the decision criteria and note the key trade-off.

| Option | Strengths | Risks / Trade-offs | Alignment with constraints |
|---|---|---|---|

Identify which option you would recommend based on the criteria, and state the one key assumption that would change the recommendation if it turned out to be wrong.

## 5. Input Needed from Contributors
For each Contributor, specify:
- The specific question they need to answer (not "share your thoughts" — a precise question)
- The format of their input (written async, 30-min sync, data pull, etc.)
- The deadline for their input (must be before the decision deadline)

| Contributor | Question to answer | Input format | Input deadline |
|---|---|---|---|

## 6. Decision Log Entry
Once the decision is made, this section documents it for the record. Pre-fill what is known now; leave outcome fields as placeholders.

- **Decision ID:** [GENERATE A SHORT ID — e.g. DEC-2025-047]
- **Decision statement:** [FROM SECTION 1]
- **Date decided:** [TO BE FILLED]
- **Approver:** [NAME]
- **Decision made:** [TO BE FILLED — which option was chosen]
- **Rationale:** [TO BE FILLED — 2–3 sentences on why this option was selected]
- **Conditions or caveats:** [TO BE FILLED — any constraints on the decision, e.g. "valid for 6 months", "revisit if X happens"]
- **Communication sent to Informed parties:** [TO BE FILLED — date and method]
- **Next decision triggered:** [TO BE FILLED — any downstream decisions this unlocks or requires]

## 7. Risk Flags
Identify any structural problems with this DACI that could cause the decision to stall or be revisited:

- **Multiple Approvers proposed** — name the conflict and recommend who should hold the role
- **Driver and Approver are the same person** — flag if this creates a rubber-stamp risk
- **Too many Contributors** — if more than 5, recommend which to move to Informed
- **Missing key voice** — any person or team whose absence could invalidate the decision post-facto
- **Decision deadline is not tied to a consequence** — deadlines without stakes are ignored; recommend adding one

If no flags apply, state "No structural risks identified."
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[DECISION TO BE MADE]` | One-sentence statement of what is being decided | "Whether to build native mobile apps or invest in a responsive web experience for Q3" |
| `[CONTEXT AND BACKGROUND]` | Why this decision is needed now | "Enterprise prospects are asking about mobile; engineering estimates diverge by 3x between options" |
| `[OPTION A / B / C]` | The choices under consideration | "Option A: Native iOS + Android. Option B: Progressive Web App. Option C: Defer 6 months." |
| `[DECISION DEADLINE]` | When the decision must be made and why | "June 6 — engineering must begin Q3 sprint planning the following week" |
| `[LIST NAMES, ROLES, TEAMS]` | Everyone involved in the decision | "Maya — CPO; Ravi — Lead Engineer; James — Head of Sales" |
| `[CONSTRAINTS OR NON-NEGOTIABLES]` | Fixed factors that bound the options | "No budget for a separate mobile engineering team; must ship something in Q3" |

## Tips

- **One Approver, always** — the most common DACI failure is two people who both believe they are the Approver; surface and resolve this before the decision meeting, not during it
- **Keep Contributors to five or fewer** — beyond five, the document becomes a consultation exercise rather than a decision; move additional people to Informed
- **The Driver is not the Approver** — separating these roles prevents the person running the process from also being the person whose preference wins; when they are the same person, flag it and confirm it is intentional
- **Use the Decision Log Entry in every post-mortem** — teams that record decisions with rationale rarely relitigate them; teams that don't, do
- **A DACI is not a meeting agenda** — create it before the decision meeting so participants arrive knowing their role, not discovering it in the room
