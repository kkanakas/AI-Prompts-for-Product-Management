# Flowchart Diagram from Git Repository

**Phase:** Architecture Diagram Generation
**Purpose:** Analyze a GitHub repository and generate a flowchart that visualizes the logic, decision points, and control flow of a process, feature, or system — giving product managers, engineers, and stakeholders a clear picture of how the system behaves at runtime without reading every function.

## Prompt Template

```
I have a GitHub repository here: [GITHUB_REPO_URL]

Please analyze the codebase and generate a flowchart that captures the control flow and decision logic of the system.

Focus on:

1. **Entry points** — where the process begins (e.g., API endpoint, user action, scheduled job, event trigger, CLI command)
2. **Process steps** — the key operations, transformations, or actions that happen in sequence (e.g., validate input, fetch data, apply business rule, send notification)
3. **Decision points** — conditional branches where the flow splits based on a condition (e.g., "Is user authenticated?", "Does record exist?", "Is payment successful?")
4. **Loops and retries** — any iterative or retry logic (e.g., polling, batch processing, exponential backoff)
5. **External system interactions** — calls to external APIs, databases, queues, or third-party services that are part of the flow
6. **Error and exception paths** — how the system handles failures, validation errors, or unexpected states (e.g., fallback, error response, dead-letter queue)
7. **Terminal states** — where the process ends, including success, failure, and no-op outcomes

Scope: [SCOPE — e.g., "the user registration and email verification flow", "the /api/checkout endpoint", "the background job in workers/invoice-processor.py", "the entire order fulfilment process"]

Output format: Generate the diagram in **Mermaid `flowchart TD` syntax** (top-down orientation). Use standard Mermaid node shapes:
- Rectangles `[text]` for process steps
- Diamonds `{text}` for decision points
- Rounded rectangles `(text)` for start and end states
- Parallelograms `[/text/]` for input/output operations
- Subroutine shapes `[[text]]` for calls to other processes or functions

After the diagram, provide:

1. **Flow summary** — 3–5 sentences describing what this process does, who or what triggers it, and what the primary success and failure outcomes are
2. **Critical decision points** — the 2–3 branching conditions that most significantly affect the outcome and where bugs or edge cases are most likely to hide
3. **Happy path** — a numbered list of the steps in the primary success flow from start to finish
4. **Error handling gaps** — any missing error paths, unhandled edge cases, or places where the flow terminates without a clear outcome
5. **Assumptions** — any inferences you made due to incomplete visibility (e.g., assumed retry logic from naming conventions, inferred error handling from surrounding code)
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[GITHUB_REPO_URL]` | Full URL to the GitHub repository | `https://github.com/owner/repo` |
| `[SCOPE]` | The specific process, feature, or file to analyse | `"the password reset flow"`, `"the /api/orders POST endpoint"`, `"the nightly batch job in jobs/sync.py"` |

## Output Variants

Depending on your goal, add one of these instructions after the main prompt:

**Happy path only** — add to the prompt:
```
Show only the primary success path — omit error handling, retries, and edge cases. The goal is a simple, readable diagram suitable for a customer-facing walkthrough or onboarding documentation.
```

**Error and exception paths only** — add to the prompt:
```
Focus exclusively on error handling, exception paths, fallbacks, and failure modes. Omit the happy path steps except as context. The goal is a map of how the system behaves when things go wrong.
```

**Cross-service flow** — add to the prompt:
```
Show the flow across service boundaries. For each step that calls an external service, API, queue, or database, label the interaction explicitly. Use subgraph blocks to group steps by service owner. The goal is to understand ownership, failure domains, and integration points.
```

**User-facing flow** — add to the prompt:
```
Frame the flow from the user's perspective. Label decision points and steps in plain language a non-technical stakeholder can follow. Omit internal implementation details — focus on what the user sees, what choices they face, and what outcomes they experience.
```

## Tips

- **Narrow scope produces better diagrams** — "the checkout flow" produces a useful flowchart; "the entire application" produces an unreadable tangle; always specify a feature, endpoint, or process
- **Use for PRD acceptance criteria** — the happy path output maps directly to acceptance criteria; the error handling gaps output identifies edge cases the PRD should explicitly cover
- **Pair with the sequence diagram prompt** — a flowchart shows decision logic within a single process; a sequence diagram shows message passing across multiple systems; use both for complex integrations
- **Decision points reveal product risk** — branches with no error handling or ambiguous conditions are exactly where production incidents originate; use the critical decision points output to prioritize testing
- **Re-run after major refactors** — flowcharts decay as code evolves; tie each diagram to a specific commit SHA so the team knows when it was last validated
- **Left-right orientation for wide flows** — if the diagram becomes too tall, change `flowchart TD` to `flowchart LR` for a left-to-right layout

## Rendering

Paste the Mermaid output into any of these tools to render it:

- [Mermaid Live Editor](https://mermaid.live) — instant browser rendering, shareable link
- GitHub Markdown — Mermaid renders natively in `.md` files
- Notion — paste as a code block with `mermaid` language tag
- VS Code — install the Markdown Preview Mermaid Support extension
- Confluence — use the Mermaid macro (available via Marketplace plugin)
