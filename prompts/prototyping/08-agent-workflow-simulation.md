# Agent Workflow Simulation

**Phase:** Prototyping
**Purpose:** Generate a structured simulation of a multi-step agentic AI workflow — task decomposition, agent/human handoff points, decision nodes, error paths, and validation questions — for mapping in Miro, Notion, or FigJam before any code is written.

## Prompt Template

```
You are a product manager designing an agentic AI workflow. An agentic workflow is one where an AI agent performs a sequence of tasks autonomously, makes decisions, calls tools or APIs, and hands off to humans at defined points — rather than just answering a single question. Using the context below, generate a complete workflow simulation I can map in Miro or Notion and validate with stakeholders and users before any engineering begins.

Workflow name: [WORKFLOW_NAME — e.g. "Automated invoice processing", "Customer onboarding agent", "Code review assistant"]
Goal: [WORKFLOW_GOAL — what the agent is trying to accomplish on behalf of the user]
Trigger: [TRIGGER — what starts the workflow, e.g. "user uploads a PDF", "customer submits a support ticket", "scheduled nightly job"]
Inputs available to the agent: [INPUTS — what data, documents, APIs, or tools the agent can access]
Expected output or outcome: [EXPECTED_OUTPUT — what the workflow produces when it completes successfully]
Human oversight requirement: [HUMAN_OVERSIGHT — e.g. "human must approve before any external action", "human reviews only on low-confidence decisions", "fully autonomous — no human in the loop"]
Known constraints: [CONSTRAINTS — e.g. "must complete within 60 seconds", "cannot access PII without explicit user consent", "must log every decision for audit", or "none"]

---

## Section 1 — Workflow Overview

Write a plain-language description of the workflow in 3–5 sentences. Describe what triggers it, what the agent does, where humans are involved, and what the end state looks like. This is the version you read to a stakeholder who is not technical.

---

## Section 2 — Task Decomposition

Break the workflow into discrete, sequenced steps. For each step:

**Step [N]: [Step name]**
- Actor: [Agent / Human / External system]
- Action: [what happens — be specific about what is read, processed, generated, or sent]
- Input: [what this step consumes — from prior step, from user, or from external system]
- Output: [what this step produces — data, decision, artifact, or trigger for next step]
- Tool or capability used: [e.g. "LLM call", "database query", "API call to Stripe", "email send", "human review queue"]
- Decision point: [Yes / No — does this step produce a decision that branches the workflow?]
- If yes — branch conditions: [list the conditions and where each leads]

Generate all steps from trigger to final output, including error and exception paths.

---

## Section 3 — Workflow Map (Text Format)

Produce the workflow as a text-based map suitable for importing into Miro or re-drawing in FigJam. Use indentation to show branching.

[TRIGGER]
  → Step 1: [name] (Agent)
      → Step 2: [name] (Agent)
          → [Branch: condition A] → Step 3a: [name]
          │     → Step 4: [name] (Human approval)
          │         → [Approved] → Step 5: [name]
          │         → [Rejected] → Step 3a-reject: [name]
          → [Branch: condition B] → Step 3b: [name]
              → Step 4: [name]
  → [Error: trigger condition] → Error handler: [name]
      → [Retry] → Step 1
      → [Escalate] → Human intervention: [name]

[SUCCESS STATE: final output]
[FAILURE STATE: final state if not recoverable]

---

## Section 4 — Human-in-the-Loop Design

For each human touchpoint in the workflow, specify:

**Handoff [N]: [Name]**
- Trigger condition: [what causes the workflow to pause and wait for a human]
- What the human sees: [the information surfaced to the human — summarize the context the agent has gathered]
- Decision required: [what the human must approve, reject, edit, or provide]
- Time limit: [how long the workflow waits before escalating or timing out]
- Escalation path: [what happens if the human does not respond in time]
- Audit log entry: [what is recorded about this handoff for compliance or review purposes]

Also specify:
- The minimum human oversight model for this workflow (which handoffs are mandatory vs. optional)
- The path to "lights out" operation (which handoffs could be removed if the agent reaches sufficient confidence)

---

## Section 5 — Error and Exception Handling

For each step that can fail, specify the error handling behavior:

| Step | Failure mode | Agent response | Human notification | Recovery path |
|---|---|---|---|---|
| [Step N] | [e.g. API timeout, low confidence, missing data, policy violation] | [retry / skip / flag / abort] | [Y / N — and what they are told] | [retry after X seconds / escalate to human / terminate workflow] |

Generate error handling for at least:
- External API or tool failure
- Low-confidence AI decision (below the threshold defined in [HUMAN_OVERSIGHT])
- Missing or malformed input
- Policy or safety guardrail trigger
- Timeout (workflow exceeds maximum allowed duration)

---

## Section 6 — Validation Questions

Before building, these questions must be answered by stakeholders, engineers, or users:

**Scope and trigger:**
- [ ] Is the trigger condition well-defined enough for the agent to start reliably, or are there edge cases that could cause false starts?
- [ ] What is explicitly out of scope for this agent — what should it never attempt?

**Task decomposition:**
- [ ] Is every step's input available at the time the step runs, or are there sequencing dependencies that have not been surfaced?
- [ ] Are there steps that require capabilities the agent does not currently have?

**Human oversight:**
- [ ] Are the handoff conditions specific enough to implement, or does "low confidence" need a numeric threshold?
- [ ] Is the human review queue realistic — how many handoffs per day/hour will humans need to process?

**Error handling:**
- [ ] Is there a recovery path for every failure mode, or are there dead ends?
- [ ] What is the user experience when the workflow fails — do they get a notification, a fallback, or silence?

**Compliance and audit:**
- [ ] Is every agent decision logged in a way that satisfies [CONSTRAINTS]?
- [ ] Can a human reconstruct exactly what the agent did and why for any completed workflow instance?

---

## Section 7 — Simulation Script

Write a walkthrough script for presenting this workflow simulation to stakeholders in a 15-minute review. Format as:

"[Facilitator narration for each step of the workflow map — describe what is happening in plain language, why the agent makes the decisions it does, and where the humans are involved.]"

Include:
- One "happy path" walkthrough (trigger → success state)
- One error path walkthrough (one failure mode → recovery)
- Three stakeholder questions to prompt at the end of the session
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[WORKFLOW_NAME]` | Name of the agentic workflow | `"Automated invoice exception handler"` |
| `[WORKFLOW_GOAL]` | What the agent is trying to accomplish | `"Process incoming invoices, match them to purchase orders, flag exceptions, and route approved invoices to payment"` |
| `[TRIGGER]` | What starts the workflow | `"A new invoice PDF is uploaded to the shared finance inbox"` |
| `[INPUTS]` | Data, documents, APIs, or tools available | `"Invoice PDF, purchase order database, vendor master data, approval authority matrix"` |
| `[EXPECTED_OUTPUT]` | What the workflow produces | `"Invoice matched and queued for payment, or exception logged and routed to AP team"` |
| `[HUMAN_OVERSIGHT]` | Human oversight requirement | `"Human approval required for any invoice above $10,000 or any exception flagged as anomalous"` |
| `[CONSTRAINTS]` | Hard constraints | `"Must complete within 90 seconds for straight-through processing; every decision must be logged for SOX audit"` |

## Output Variants

**Multi-agent variant** — add to the prompt:
```
This workflow involves multiple specialized agents, not a single agent. Define each agent as a named role with a specific capability boundary: [Agent A: document extraction], [Agent B: policy compliance check], [Agent C: approval routing]. Map the handoffs between agents explicitly — show what each agent passes to the next and what it is not allowed to pass (e.g. "Agent A does not pass PII to Agent B — it passes only extracted fields").
```

**User-facing transparency variant** — add to the prompt:
```
Users can see the agent's progress in real time via a "workflow status" panel. For each step in the task decomposition, write the user-facing status message that appears in the panel — plain language, present tense, no technical jargon. Also write the notification the user receives when the workflow completes, when it requires their input, and when it fails.
```

## Tips

- Agentic workflow failures are almost always sequencing problems — a step that needs data which has not been produced yet; the task decomposition in Section 2 forces these dependencies to the surface before code is written
- "Human in the loop" is a spectrum, not a binary — Section 4 forces the team to specify exactly when humans are needed rather than defaulting to "AI does everything" or "humans review everything"
- The simulation script in Section 7 is the most underused output — walking stakeholders through a workflow map with narration surfaces objections and missing steps in 15 minutes that would otherwise take weeks to find in code review
- Pair with `05-dependency-identification.md` for the broader initiative and `07-ai-feature-stub.md` for generating the hardcoded outputs used in each workflow step during testing
