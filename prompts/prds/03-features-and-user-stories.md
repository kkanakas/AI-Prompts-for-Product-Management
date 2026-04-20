# Features and User Stories from Use Cases

**Phase:** Discovery & Requirements
**Purpose:** Transform use case documentation into a structured, sprint-ready backlog — decomposing each use case into discrete features and well-formed user stories with Given/When/Then acceptance criteria, story points guidance, and definition of done — so engineering, QA, and design teams can pick up and execute without ambiguity.

## Prompt Template

```
You are a senior product manager and business analyst converting use case documentation into a sprint-ready feature and user story backlog.

Use the following use case documentation as your source:

[PASTE_USE_CASE_DOCUMENTATION]

Additional context:
- Product or feature name: [PRODUCT_NAME]
- Target users: [TARGET_USERS]
- Team structure: [TEAM_STRUCTURE — e.g., "one full-stack squad of 6", "separate frontend and backend squads", "platform team + product team"]
- Sprint length: [SPRINT_LENGTH — e.g., "2 weeks"]
- Story point scale: [STORY_POINT_SCALE — e.g., "Fibonacci: 1, 2, 3, 5, 8, 13" or "T-shirt: S/M/L/XL"]
- Definition of done: [DEFINITION_OF_DONE — e.g., "code reviewed, unit tested, integration tested, deployed to staging, PM sign-off" — or leave blank to generate a suggested DoD]

---

## Section 1 — Feature List

Derive the complete list of features from the use cases. A feature is a discrete, deliverable capability that delivers value to a user and can be shipped independently or as part of an epic.

| Feature ID | Feature name | Derived from use case(s) | User value | Epic / theme | Priority | Estimated size |
|---|---|---|---|---|---|---|
| F-01 | [name] | [UC-ID(s)] | [what the user can do once this feature exists] | [epic] | Must / Should / Could | [S/M/L/XL] |
| F-02 | | | | | | |
| F-03 | | | | | | |

---

## Section 2 — User Stories per Feature

For each feature, generate all user stories needed to fully implement it. Follow these rules:
- Each story represents one actor achieving one outcome
- Stories must be independently testable
- Stories must be small enough to complete within one sprint
- Split any story estimated at > 8 story points into smaller stories

For each story, use this full template:

---

### [F-ID]-[Story number]: [STORY TITLE]

**Feature:** [Feature name — F-ID]
**Use case source:** [UC-ID and step(s) this story implements]
**Actor:** [Who this story is for]
**Story type:** Functional / Non-functional / Technical / Spike

**User Story:**
> As a **[specific actor]**,
> I want to **[specific action or capability]**,
> So that **[specific outcome or value received]**.

**Story context:**
[1–2 sentences explaining what this story enables and why it matters at this point in the flow. Reference the use case step it implements.]

---

**Acceptance Criteria**

*Happy path:*

```
Given [the precondition or starting state],
When [the actor takes the specific action],
Then [the expected system response or state change].
```

```
Given [a second precondition variant],
When [the same or related action],
Then [the expected outcome for this variant].
```

*Alternative flow:*

```
Given [the alternative condition from AF-X],
When [the actor takes the action],
Then [the expected alternative outcome].
```

*Exception / error handling:*

```
Given [the error condition from EF-X],
When [the triggering action],
Then [the expected error response — including exact error message if applicable].
```

```
Given [a second error condition],
When [the triggering action],
Then [the expected system behavior and recovery path].
```

*Edge cases:*

```
Given [a boundary or edge condition],
When [the action],
Then [the expected behavior at the boundary].
```

---

**Out of scope for this story:**
- [What this story explicitly does NOT cover — prevents scope creep]
- [Related behavior handled in a different story — reference the story ID]

**Dependencies:**
- Blocked by: [story or feature ID, or "none"]
- Enables: [story or feature ID, or "none"]

**Technical notes:**
- [Any API endpoints, data fields, or system interactions the engineer needs to know]
- [Any non-functional constraint — e.g., "response must be < 2s at p95", "must be accessible at WCAG 2.1 AA"]
- [Any security or compliance requirement — e.g., "input must be sanitized", "action must be logged to audit trail"]

**Definition of done:**
- [ ] Code reviewed and approved
- [ ] Unit tests written and passing (coverage ≥ [TARGET]%)
- [ ] Integration test covers main flow and top exception flow
- [ ] Deployed to staging environment
- [ ] Acceptance criteria verified by PM or QA
- [ ] No open P0/P1 bugs
- [ ] [Any additional DoD items from context]

**Story points:** [estimate] | **Confidence:** High / Medium / Low

---

## Section 3 — Story Map

Organize all stories into a user story map that shows the sequence of user activities across the top and the layers of stories beneath each activity.

| User activity → | [Activity 1] | [Activity 2] | [Activity 3] | [Activity 4] |
|---|---|---|---|---|
| **MVP (must ship)** | [F-01-01] | [F-02-01] | [F-03-01] | [F-04-01] |
| **Phase 2 (should ship)** | [F-01-02] | [F-02-02] | [F-03-02] | — |
| **Phase 3 (could ship)** | — | [F-02-03] | — | [F-04-02] |

**MVP walking skeleton:** [List the minimum set of stories — one per activity — that creates an end-to-end flow a user can actually complete, even if rough]

---

## Section 4 — Sprint Plan (First Two Sprints)

Based on estimated story sizes and dependencies, suggest which stories should go into the first two sprints.

### Sprint 1 — Goal: [SPRINT_1_GOAL]

| Story ID | Story title | Points | Owner suggestion | Dependency |
|---|---|---|---|---|
| [F-ID-01] | [title] | [points] | [Frontend / Backend / Full-stack] | None |
| [F-ID-02] | [title] | [points] | [Frontend / Backend / Full-stack] | None |
| [F-ID-03] | [title] | [points] | [Frontend / Backend / Full-stack] | [story] |

**Sprint 1 total points:** [sum]
**Sprint 1 deliverable:** [What a tester or PM can verify at the end of Sprint 1]

### Sprint 2 — Goal: [SPRINT_2_GOAL]

| Story ID | Story title | Points | Owner suggestion | Dependency |
|---|---|---|---|---|
| [F-ID-04] | [title] | [points] | [Frontend / Backend / Full-stack] | Sprint 1 complete |
| [F-ID-05] | [title] | [points] | [Frontend / Backend / Full-stack] | [story] |

**Sprint 2 total points:** [sum]
**Sprint 2 deliverable:** [What a tester or PM can verify at the end of Sprint 2]

---

## Section 5 — Backlog Health Check

Review the full set of stories against the INVEST criteria and flag any issues.

| Story ID | Independent | Negotiable | Valuable | Estimable | Small | Testable | Issues |
|---|---|---|---|---|---|---|---|
| [F-ID-01] | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | [issue if any] |
| [F-ID-02] | | | | | | | |

**Stories flagged for splitting:** [list any story > 8 points with a suggested split]
**Stories flagged for merging:** [list any stories too thin to deliver independently]
**Missing stories:** [any gaps in coverage — use case steps not yet covered by a story]
**Coverage summary:** [X use case steps covered by Y stories across Z features]
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PASTE_USE_CASE_DOCUMENTATION]` | The full use case doc from prompt `02-use-case-documentation` | Paste the full markdown output |
| `[PRODUCT_NAME]` | Feature or product name | `"Self-Serve Password Reset"` |
| `[TARGET_USERS]` | Who the stories are written for | `"Registered end users and system admins"` |
| `[TEAM_STRUCTURE]` | How the team is organized | `"One full-stack squad of 5 engineers + 1 QA"` |
| `[SPRINT_LENGTH]` | How long a sprint is | `"2 weeks"` |
| `[STORY_POINT_SCALE]` | Estimation scale the team uses | `"Fibonacci: 1, 2, 3, 5, 8, 13"` |
| `[DEFINITION_OF_DONE]` | Team's DoD — leave blank to generate | `"Code reviewed, unit tested, deployed to staging, PM sign-off"` |

## Output Variants

**Jira-ready import format** — add to the prompt:
```
Format the output as a Jira-compatible structure. For each story output: Epic Link (feature name), Summary (story title), Description (user story + context), Acceptance Criteria (as a numbered list), Story Points, Labels (actor name and use case ID), and linked stories (blocked by / enables). Separate each story with a horizontal rule so it can be copy-pasted into Jira individually.
```

**BDD / Gherkin format** — add to the prompt:
```
Format all acceptance criteria in strict Gherkin syntax for use with Cucumber, Behave, or SpecFlow. For each story, output a complete .feature file with: Feature name, Background (shared preconditions), and one Scenario block per acceptance criterion. Use Scenario Outline with Examples tables for criteria that vary by input value.
```

**Technical stories only** — add to the prompt:
```
Generate only the technical and non-functional stories: API contracts, data migration tasks, infrastructure setup, security hardening, logging and audit trail implementation, and performance optimization. For each, include: the technical goal, the definition of done, the acceptance test (e.g., load test threshold, security scan pass), and the estimated complexity.
```

**Accessibility stories** — add to the prompt:
```
For every user-facing story in the backlog, generate a paired accessibility story that covers: keyboard navigation, screen reader support (ARIA labels and roles), color contrast compliance (WCAG 2.1 AA), focus management, and error message accessibility. Link each accessibility story to its parent functional story.
```

## Tips

- **Use cases are inputs, not stories** — a use case step is not a user story; this prompt's job is to translate what the system must do (use case) into what the team will build (story); each UC step typically becomes 1–3 stories
- **Given/When/Then is a contract, not a format** — write the Given to capture the exact system state; the When to capture the precise user action; the Then to capture the observable, testable outcome; vague Thens ("then it works") are untestable
- **One story per acceptance criterion is a smell** — if every story has only one Given/When/Then, you are probably over-splitting; each story should cover one coherent piece of behavior with multiple criteria covering happy path, alternatives, and exceptions
- **Exception flows become the most valuable stories** — the exception handling stories (EF-X) are where production incidents originate; write them first and make sure they have complete Given/When/Then before the happy path stories are estimated
- **Run this prompt after the use case prompt** — the output of `02-use-case-documentation` is the direct input to this prompt; the UC-IDs, actor names, preconditions, and exception flows feed directly into the story template
- **Pair with the Big Rock decomposition prompt** — use the feature list from the decomposition as the epic structure; this prompt fills in the stories beneath each feature in that structure
