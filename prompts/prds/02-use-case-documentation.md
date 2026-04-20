# Use Case Documentation

**Phase:** Discovery & Requirements
**Purpose:** Generate comprehensive, well-structured use case documentation that captures actor goals, preconditions, main success flows, alternative paths, and exception handling — giving product, engineering, QA, and design teams a shared, unambiguous specification they can build, test, and validate against.

## Prompt Template

```
You are a senior product manager and business analyst generating formal use case documentation. Using the context below, produce a complete use case document.

Feature or system name: [FEATURE_NAME]
Feature description: [FEATURE_DESCRIPTION — what the feature does and why it exists]
Target users / actors: [ACTORS — e.g., "end user (customer)", "admin user", "system (automated process)", "third-party API"]
Business context: [BUSINESS_CONTEXT — the business goal or problem this feature addresses]
Scope boundary: [SCOPE — what is in scope for these use cases, and what is explicitly excluded]
Related systems or integrations: [INTEGRATIONS — e.g., "Salesforce CRM", "payment gateway", "notification service", "identity provider"]

---

## Use Case Overview

Generate a use case index for this feature — the complete list of use cases, organized by actor and goal.

| UC ID | Use Case Name | Primary Actor | Goal | Priority |
|---|---|---|---|---|
| UC-01 | [name] | [actor] | [what the actor is trying to achieve] | Must / Should / Could |
| UC-02 | | | | |
| UC-03 | | | | |

---

## Detailed Use Case Specifications

For each use case in the index, generate a full specification using the template below.

---

### UC-[ID]: [USE CASE NAME]

**Version:** 1.0
**Status:** Draft
**Last updated:** [DATE]

#### Summary
[2–3 sentences: what this use case does, who initiates it, and what the successful outcome is]

#### Actors

| Actor | Type | Role in this use case |
|---|---|---|
| [Primary actor] | Human / System | [what they do — initiates, approves, receives, etc.] |
| [Secondary actor 1] | Human / System | [supporting role] |
| [Secondary actor 2] | Human / System | [supporting role] |

#### Preconditions
Conditions that must be true before this use case can begin:
- [ ] [Precondition 1 — e.g., "User is authenticated and has role X"]
- [ ] [Precondition 2 — e.g., "The target record exists in the system"]
- [ ] [Precondition 3 — e.g., "The integration with [system] is active and reachable"]

#### Postconditions
Guaranteed outcomes when the use case completes successfully:
- [ ] [Postcondition 1 — e.g., "The record has been updated and the change is persisted"]
- [ ] [Postcondition 2 — e.g., "A confirmation notification has been sent to the actor"]
- [ ] [Postcondition 3 — e.g., "An audit log entry has been created"]

#### Trigger
[What initiates this use case — e.g., "User clicks 'Submit' on the checkout form", "System receives webhook from payment gateway", "Scheduled job runs at midnight UTC"]

---

#### Main Success Scenario (Basic Flow)
The step-by-step sequence for the most common, uninterrupted path to success.

| Step | Actor | Action | System response |
|---|---|---|---|
| 1 | [Actor] | [What the actor does] | [What the system does in response] |
| 2 | System | [Automated step] | [Outcome or state change] |
| 3 | [Actor] | [What the actor does] | [What the system does in response] |
| 4 | | | |
| 5 | | | |

**Outcome:** [Final state after the last step — what the actor can now do or see]

---

#### Alternative Flows
Variations on the main flow that still lead to a successful or acceptable outcome.

**AF-[ID]A — [Alternative flow name]**
Trigger: [Step X in the main flow — describe the condition that causes this branch]
Steps:
1. [Step]
2. [Step]
3. Rejoins main flow at Step [N] — or — ends with outcome: [state]

**AF-[ID]B — [Alternative flow name]**
Trigger: [condition]
Steps:
1. [Step]
2. [Step]
Outcome: [state]

---

#### Exception Flows
Conditions that interrupt the flow and produce an error, failure, or blocked state.

**EF-[ID]A — [Exception name]**
Trigger: [What goes wrong — e.g., "Payment gateway returns timeout", "User does not have required permission", "Required field is missing"]
Steps:
1. System detects [condition]
2. System [action — e.g., displays error message, rolls back transaction, sends alert]
3. [Actor] [how they can recover — or — use case terminates]
Recovery path: [How the actor resumes — or "No recovery; use case must restart from Step 1"]
Error message shown: "[exact text of error message displayed to the user]"

**EF-[ID]B — [Exception name]**
Trigger: [condition]
Steps:
1. [Step]
2. [Step]
Recovery path: [recovery or termination]

---

#### Business Rules
Rules and constraints that govern the behavior of this use case — independent of implementation.

| BR ID | Rule | Enforcement point | Source |
|---|---|---|---|
| BR-01 | [e.g., "A user may not submit more than 3 requests per 24-hour window"] | Step [N] in main flow | [e.g., "Rate limiting policy v2.1"] |
| BR-02 | [e.g., "Approval is required for transactions above $10,000"] | [step] | [source] |
| BR-03 | | | |

---

#### Non-Functional Requirements

| Dimension | Requirement | Measurement |
|---|---|---|
| Performance | [e.g., "System response to Step 3 must be < 2 seconds at p95"] | [how measured] |
| Availability | [e.g., "This flow must be available 99.9% of the time"] | [SLA or uptime monitor] |
| Security | [e.g., "All data submitted in this use case must be encrypted in transit (TLS 1.2+)"] | [security review / pen test] |
| Accessibility | [e.g., "All interactive elements must be keyboard-navigable (WCAG 2.1 AA)"] | [accessibility audit] |
| Auditability | [e.g., "All state changes must be logged with timestamp, actor ID, and before/after values"] | [audit log review] |

---

#### UI and Wireframe References
- Screen: [screen name or URL] — used at Step [N]
- Screen: [screen name or URL] — used at Step [N]
- Figma / design link: [link or "TBD"]

---

#### Related Use Cases

| Relationship | UC ID | Use Case name | Nature of relationship |
|---|---|---|---|
| Extends | UC-[X] | [name] | [This UC adds behavior to UC-X under condition Y] |
| Includes | UC-[X] | [name] | [This UC always invokes UC-X as a sub-flow] |
| Precedes | UC-[X] | [name] | [This UC must complete before UC-X can begin] |
| Follows | UC-[X] | [name] | [UC-X must complete before this UC can begin] |

---

#### Open Questions

| # | Question | Owner | Due date | Status |
|---|---|---|---|---|
| 1 | [Unresolved question that blocks finalizing this use case] | [PM/Eng/Design] | [date] | Open |
| 2 | | | | |

---

#### Acceptance Criteria
Testable criteria that confirm this use case has been implemented correctly. Format as Given / When / Then.

- **Given** [precondition], **When** [actor action at Step N], **Then** [expected system response]
- **Given** [exception condition], **When** [exception trigger], **Then** [expected error handling]
- **Given** [alternative flow condition], **When** [branch trigger], **Then** [expected alternative outcome]

---

#### Change Log

| Version | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | [DATE] | [Author] | Initial draft |
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Name of the feature or system being specified | `"Self-Serve Password Reset"` |
| `[FEATURE_DESCRIPTION]` | What the feature does and why it exists | `"Allows users to reset their password via email verification without contacting support"` |
| `[ACTORS]` | All humans and systems that participate | `"Registered user, email service, identity provider (Okta)"` |
| `[BUSINESS_CONTEXT]` | Business goal or problem | `"Reduce support ticket volume for password resets by 60%"` |
| `[SCOPE]` | What is in and out of scope | `"In scope: email-based reset. Out of scope: SMS reset, admin-initiated reset"` |
| `[INTEGRATIONS]` | Related external systems | `"Okta for identity, SendGrid for email, Salesforce for CRM audit trail"` |

## Output Variants

**Single use case only** — add to the prompt:
```
Generate a detailed specification for one specific use case only: [USE CASE NAME]. Skip the use case index and go directly to the full UC specification template. Make the alternative flows, exception flows, and acceptance criteria sections as comprehensive as possible.
```

**QA test plan format** — add to the prompt:
```
After the standard use case documentation, generate a QA test plan derived from the use cases. For each use case, produce: test case ID, test scenario, test steps, test data required, expected result, and pass/fail criteria. Include test cases for the main flow, all alternative flows, and all exception flows.
```

**Swimlane process map** — add to the prompt:
```
After the use case specifications, generate a Mermaid flowchart that visualizes the main success scenario as a swimlane diagram. Use one swimlane per actor (including the system as an actor). Show decision points at each alternative and exception flow branch. Use `flowchart LR` orientation.
```

**API contract notes** — add to the prompt:
```
For each system-to-system interaction in the use cases (steps where the system calls an external service or receives a callback), add an API contract note: the endpoint or event name, request payload fields, success response structure, error codes and their meanings, and the timeout or retry policy. Format as a separate appendix after the use case specifications.
```

## Tips

- **One use case per actor goal** — a use case describes one actor achieving one goal; if you find yourself writing a use case that has two distinct outcomes or two distinct primary actors, split it into two
- **Main flow should have no branches** — the main success scenario is the uninterrupted happy path; every branch belongs in an alternative or exception flow; if your main flow has an "if", it needs to be moved
- **Exception flows are where QA lives** — the most valuable part of a use case for an engineering team is the exception flows; ensure every EF has a defined recovery path and an exact error message
- **Business rules unlock traceability** — by capturing business rules with a BR-ID, you create a traceability link between the use case, the implementation, and the test case; use these IDs in Jira tickets and test plans
- **Acceptance criteria are the contract** — the Given/When/Then criteria at the end of each UC are the exact conditions your QA team will test and your engineers will implement against; write them before development starts, not after
- **Pair with the PRD prompt** — the PRD sets the strategic context ("what and why"); use cases specify the behavioral detail ("exactly how"); run the PRD prompt first, then use this prompt to elaborate the functional requirements section
- **Pair with the Big Rock decomposition prompt** — use the epic and feature hierarchy from the decomposition as the input scope for this prompt; each feature in the decomposition typically maps to 2–5 use cases
