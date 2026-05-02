# Given / When / Then Acceptance Criteria Generator

**Phase:** Discovery & Requirements
**Purpose:** Transform a requirements document or use case document into a complete set of Given/When/Then acceptance criteria — covering happy path, alternative flows, exception handling, edge cases, and non-functional requirements — ready for engineering, QA, and sprint refinement.

## Prompt Template

```
You are a senior product manager and QA strategist generating acceptance criteria from a requirements document. Your output will be used directly in sprint refinement, QA test planning, and engineering implementation.

Paste your requirements or use case document below:

[PASTE_DOCUMENT]

Additional context:
- Feature or requirement name: [FEATURE_NAME]
- Actors involved: [ACTORS — e.g., "end user, admin, system, external API"]
- System or product: [PRODUCT — brief description of what the product is]
- QA tooling (optional): [QA_TOOL — e.g., "Cucumber / Gherkin", "plain text", "TestRail", or leave blank]

---

## Step 1 — Requirement Extraction

Before writing any GWT criteria, extract and list every discrete requirement from [PASTE_DOCUMENT]. Group them into:

**Functional requirements** — what the system must do:
| ID | Requirement | Source (section or step in the document) | Actor |
|---|---|---|---|
| FR-01 | [requirement statement] | [section/step reference] | [actor] |

**Non-functional requirements** — performance, security, accessibility, reliability:
| ID | Requirement | Type | Measurable threshold |
|---|---|---|---|
| NFR-01 | [requirement statement] | [Performance / Security / Accessibility / Reliability / Compliance] | [e.g., "response < 2s at p95", "WCAG 2.1 AA", "99.9% uptime"] |

**Business rules** — constraints and logic the system must enforce:
| ID | Rule | Trigger condition | Expected enforcement |
|---|---|---|---|
| BR-01 | [rule statement] | [when this rule applies] | [how the system enforces it] |

Flag any ambiguous or missing requirements — gaps that need a decision before criteria can be written.

---

## Step 2 — Given / When / Then Criteria

**And / But usage rules:**
- `And` after `Given` — adds a second or third precondition that must also be true before the scenario starts
- `And` after `When` — chains a second action that follows immediately from the first (use sparingly — prefer one When per scenario)
- `And` after `Then` — adds a second observable outcome in the same scenario
- `But` after `Then` — asserts what must NOT be true (e.g., "But the original data must not be deleted")

Use `And` and `But` wherever a single line would be incomplete without them. Do not pad — only add `And` or `But` lines when the scenario genuinely requires them.

For each functional requirement, generate the full set of GWT criteria. Structure them as follows:

---

### [FR-ID]: [Requirement name]

**Actor:** [who triggers this requirement]
**Precondition summary:** [the state the system must be in before this requirement applies]

#### Happy Path

```gherkin
Given [the primary precondition — system state, user state, or data state]
And   [a second precondition that must also hold, if required]
When  [the specific action the actor takes]
And   [a second action that follows immediately, if required]
Then  [the primary observable outcome — what the system does or displays]
And   [a second observable outcome in the same scenario, if required]
But   [something that must NOT happen — e.g., "But the previous record must not be overwritten"]
```

```gherkin
Given [a second valid precondition variant]
And   [any additional precondition for this variant]
When  [the same or related action]
Then  [the expected outcome for this variant]
And   [any additional outcome]
```

#### Alternative Flows

```gherkin
Given [the precondition for the alternative path]
And   [any additional condition that directs the flow to this alternative]
When  [the action that triggers the alternative]
Then  [the primary expected alternative outcome]
And   [any secondary outcome — e.g., "And the user is notified of the alternative path taken"]
```

#### Exception and Error Handling

```gherkin
Given [the error or invalid state condition]
And   [any additional condition that contributes to the error — e.g., "And the session token has expired"]
When  [the action that triggers the error]
Then  [the exact system response — include error message wording and UI state]
And   [the recovery option surfaced to the user — e.g., "And a 'Try again' button is displayed"]
But   [what must not happen — e.g., "But no data must be persisted from the failed request"]
```

```gherkin
Given [a second error condition — e.g., network failure, timeout, permission denied]
And   [any additional contributing condition]
When  [the triggering action]
Then  [the expected graceful degradation or fallback behavior]
And   [the user notification or audit log entry, if required]
But   [what the system must not expose — e.g., "But internal stack traces must not be shown to the user"]
```

#### Edge Cases and Boundaries

```gherkin
Given [a boundary condition — e.g., maximum input length, zero results, first-time user, empty state]
And   [any additional boundary condition — e.g., "And no prior session data exists"]
When  [the action]
Then  [the expected behavior at this boundary]
And   [any secondary effect at the boundary — e.g., "And the character counter displays 0 remaining"]
```

```gherkin
Given [a concurrent or race condition, if applicable]
And   [the second concurrent actor or state]
When  [the simultaneous or near-simultaneous actions]
Then  [the expected system behavior — which action takes precedence]
And   [what the other actor sees or receives]
But   [what must not happen — e.g., "But data from both actors must not be merged into a corrupt state"]
```

#### Security and Permissions (generate if applicable)

```gherkin
Given [an actor without the required permission or role]
And   [they are otherwise authenticated — i.e., this is an authorization failure, not an authentication failure]
When  [they attempt the restricted action]
Then  [the system denies access with an appropriate HTTP status or UI message]
And   [the attempt is logged in the audit trail]
But   [internal permission configuration or other user data must not be exposed in the error response]
```

```gherkin
Given [a session has expired or an unauthenticated actor]
And   [the actor was attempting to reach a specific destination]
When  [they attempt the action]
Then  [the system redirects to the login page]
And   [the intended destination is preserved so the actor is returned there after successful authentication]
But   [any sensitive data from the interrupted request must not be cached or logged in plaintext]
```

---

Repeat the above structure for every FR-ID extracted in Step 1.

---

## Step 3 — Non-Functional Acceptance Criteria

For each non-functional requirement, generate testable GWT criteria:

### [NFR-ID]: [Requirement name]

```gherkin
Given [the baseline system state — e.g., "the system is under normal load"]
And   [any additional baseline condition — e.g., "And the user has a standard-tier account"]
When  [the relevant action or condition — e.g., "a user submits a search query"]
Then  [the measurable primary outcome — e.g., "the response is returned in under 2 seconds at the 95th percentile"]
And   [any secondary measurable outcome — e.g., "And the response payload does not exceed 500KB"]
```

```gherkin
Given [a stress or edge condition — e.g., "100 concurrent users are submitting queries"]
And   [any compounding condition — e.g., "And the database is at 80% capacity"]
When  [the same action]
Then  [the system maintains [NFR threshold]]
And   [it does not degrade below [floor metric]]
But   [it must not return cached stale results to compensate for load]
```

---

## Step 4 — Business Rule Verification Criteria

For each business rule, generate at least two GWT criteria — one where the rule is satisfied and one where it is violated:

### [BR-ID]: [Rule name]

**Rule satisfied:**
```gherkin
Given [the condition where the rule is met]
And   [any additional condition confirming the rule applies]
When  [the actor takes the action]
Then  [the system proceeds as expected — rule enforcement is transparent to the user]
And   [any secondary confirmation — e.g., "And the audit log records the successful action"]
```

**Rule violated:**
```gherkin
Given [the condition where the rule would be violated]
And   [any additional contributing condition]
When  [the actor attempts the action]
Then  [the system blocks the action with a clear, user-friendly explanation]
And   [the user is offered a valid path forward where applicable]
But   [the system must not silently discard the input — the user must always know why the action was blocked]
```

---

## Step 5 — Criteria Coverage Matrix

Produce a matrix that maps every requirement to its GWT criteria and flags any gaps:

| Requirement ID | Requirement name | Happy path | Alt flows | Error handling | Edge cases | Security | NFR | Status |
|---|---|---|---|---|---|---|---|---|
| FR-01 | [name] | ✓ | ✓ | ✓ | ✓ | — | — | Complete |
| FR-02 | [name] | ✓ | — | ✓ | — | — | — | Missing alt flow |
| NFR-01 | [name] | — | — | — | — | — | ✓ | Complete |
| BR-01 | [name] | ✓ | — | ✓ | — | — | — | Complete |

**Total criteria generated:** [N]
**Requirements with gaps:** [list FR/NFR/BR IDs with missing coverage and what is missing]
**Ambiguous requirements that need clarification before criteria can be completed:** [list with specific questions]

---

## Step 6 — QA Scenario Summary

Produce a flat list of all GWT scenarios suitable for import into a test management tool or for use in a sprint refinement session:

| Scenario ID | Requirement | Flow type | Given (summary) | When (summary) | Then (summary) |
|---|---|---|---|---|---|
| TC-001 | FR-01 | Happy path | [brief] | [brief] | [brief] |
| TC-002 | FR-01 | Error | [brief] | [brief] | [brief] |
| TC-003 | FR-02 | Happy path | [brief] | [brief] | [brief] |
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PASTE_DOCUMENT]` | The full requirements or use case document | Paste the complete PRD section, use case output from `02-use-case-documentation.md`, or feature spec |
| `[FEATURE_NAME]` | Name of the feature or requirement set | `"Self-serve password reset"` |
| `[ACTORS]` | All actors who interact with this feature | `"Registered user, unauthenticated visitor, system email service, admin"` |
| `[PRODUCT]` | Brief description of the product | `"B2B SaaS project management tool, web app"` |
| `[QA_TOOL]` | QA or test management tool in use | `"Cucumber / Gherkin"` — or leave blank for plain-text format |

## Output Variants

**Gherkin feature file format** — add to the prompt:
```
Format the output as valid Gherkin .feature files ready to use with Cucumber, Behave, or SpecFlow. For each functional requirement, output one Feature block. Use Background for preconditions shared across scenarios. Use Scenario Outline with an Examples table for criteria that vary by input value (e.g., invalid email formats, boundary values). Each scenario must have a unique, descriptive title.
```

**Single feature / story focus** — add to the prompt:
```
Focus only on the following specific requirement or user story from the document: [SPECIFIC_REQUIREMENT]. Generate the complete set of GWT criteria for that single item only — happy path, all alternative flows, all exception flows, all edge cases, and any security or permission scenarios. Do not generate criteria for other requirements in the document.
```

**Refinement session format** — add to the prompt:
```
Format the output for use in a sprint refinement session. For each requirement, produce: (1) a one-sentence "testability statement" the team reads aloud to confirm the requirement is ready to estimate, (2) the GWT criteria as a numbered checklist QA can verify during the sprint, and (3) a single "definition of ready" checklist the team must confirm before the story enters a sprint. Flag any requirement that is not yet ready to estimate.
```

**API / backend requirements** — add to the prompt:
```
These requirements describe API or backend behavior with no user-facing UI. Rewrite all GWT criteria using system-level language: replace "the user sees" with "the API returns", replace "the screen shows" with "the response body contains", and replace UI states with HTTP status codes and response schemas. For each endpoint or operation, include: authentication criteria, authorization criteria, request validation criteria, response format criteria, and error response criteria.
```

## Tips

- **The Given is a contract, not a description** — write the Given as a precise, testable precondition the QA engineer can set up programmatically, not a narrative ("Given the user is on the dashboard" is vague; "Given a registered user with at least one active project is authenticated and viewing the project dashboard" is testable)
- **And after Given compounds the precondition** — use it when the scenario only makes sense if two independent conditions are both true (e.g., "Given a user has editor role And the document is in draft state"); if either condition alone is enough, write two separate scenarios
- **One When per scenario is the default** — if you add `And` after `When`, each action must be a separate step in a chain, not two ways of describing the same action; if removing the `And` line changes the outcome, keep it; if not, drop it
- **And after Then adds a second observable outcome** — use it when a single action genuinely produces two independently verifiable results (e.g., "Then the record is saved And the user receives a confirmation email"); if only one outcome matters for this test, keep it to one Then
- **But is for negative assertions** — use `But` to explicitly assert what must NOT happen (e.g., "But the original record must not be deleted", "But no PII must appear in the error message"); negative assertions are as important as positive ones and are most critical in error-handling and security scenarios
- **The Then must be observable** — "then it works" and "then the system updates" are not testable; every Then must describe a specific, observable state change a human or automated test can verify
- **Exception flows generate the most production incidents** — write error GWT before happy path GWT; the team's instinct is to skip them and QA always finds them in production
- **Business rules need both positive and negative criteria** — a business rule with only a happy-path criterion is half-tested; always generate the violation scenario
- **Use this prompt after `02-use-case-documentation.md`** — the use case output provides actors, preconditions, main flow steps, alternative flows, and exception flows that map directly to GWT structure
- **Pair with `03-features-and-user-stories.md`** for the full backlog when you also need story decomposition, story points, and sprint planning — use this prompt when you already have stories and need criteria only
