# Dependency Identification

**Phase:** Strategy & Planning
**Purpose:** Identify and categorize all dependencies for a feature or product initiative across team, technical, product, regulatory, third-party, and timeline dimensions — so you can surface blockers early, assign ownership, and sequence work before committing to a delivery date.

## Prompt Template

```
You are a product analyst helping identify dependencies for a feature or product initiative. Your information sources are strictly limited to the following URL(s): [SOURCE_URLS]

Given the feature or product area described below, identify and categorize all dependencies across these dimensions:

**Team/squad dependencies** — Which other teams must deliver something for this feature to ship?

**Technical dependencies** — APIs, services, platforms, data sources, or infrastructure this feature relies on

**Product/feature dependencies** — Other features or capabilities that must exist or be in a certain state first

**Regulatory or compliance dependencies** — Any policy, security, or legal gates (e.g. FedRAMP, SOC 2, GDPR, MITRE ATT&CK alignment, accessibility standards)

**Third-party or partner dependencies** — External vendors, integrations, or partner organizations involved

**Timeline dependencies** — Hard deadlines, milestone sequencing, release train constraints, or fiscal calendar gates

For each dependency identified, note:
1. What it blocks
2. Who owns it
3. Its current known status (if available in the source)

Feature / Product Area:
[FEATURE_DESCRIPTION]

Output format:

1. **Dependency map** — a structured table with columns: Dependency | Category | Blocks | Owner | Status
2. **Top 3 highest-risk dependencies** — for each, explain: why it is high risk, what the consequence is if it slips, and what the recommended mitigation is
3. **Critical path** — a sequenced list of the dependencies that, if delayed, would directly delay the ship date
4. **Open questions** — dependencies where ownership or status could not be determined from the source material
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[SOURCE_URLS]` | One or more URLs the analysis is grounded in — Jira epic, intranet/wiki page, competitor page, architecture doc | `https://jira.company.com/browse/PROJ-1234`, `https://wiki.company.com/platform-roadmap` |
| `[FEATURE_DESCRIPTION]` | A brief description of the feature or initiative being planned | `"Real-time anomaly detection alerts for enterprise security dashboards"` |

## Source Type Tips

**For Jira epics or board URLs:**
Pass in the epic or board URL and ask the model to parse linked tickets for blockers, linked issues, team assignments, and unresolved dependencies. It will surface cross-team blockers that are already logged but not yet escalated.

**For intranet or wiki pages:**
Works well for surfacing org-level policies, platform roadmaps, engineering standards, or approval workflows that gate your work — things that are rarely captured in Jira but are real blockers.

**For competitor or market URLs:**
Surfaces capability gaps or parity dependencies your roadmap needs to address. Use when a competitor feature represents a market requirement that must exist before your feature has credibility.

**For architecture or API documentation:**
Surfaces technical dependencies, versioning constraints, and deprecation timelines that engineering may not have flagged yet.

## Output Variants

**Executive summary only** — add to the prompt:
```
Summarize the dependency map as a single paragraph suitable for a steering committee update. Lead with the critical path, highlight the top risk, and state what decision or action is needed from leadership.
```

**Jira ticket drafts** — add to the prompt:
```
For each Team/squad dependency identified, draft a Jira ticket stub: title, description (what is needed and why), acceptance criteria, and a suggested assignee team. Format each as a separate block.
```

**RAID log entry** — add to the prompt:
```
Convert the dependency map into a RAID log format with four sections: Risks (dependencies that may not resolve in time), Assumptions (things we are assuming are already in place), Issues (blockers that are already active), Dependencies (external items we are waiting on). For each entry include: description, owner, status, and mitigation.
```

## Tips

- **Narrow to a single epic or milestone** — a feature-level dependency map is actionable; a program-level map without a scope constraint produces a list too long to act on
- **Run this before sprint planning** — dependency identification is most valuable 2–4 weeks before the planning ceremony, when there is still time to act on what you find
- **Use the critical path output for your milestone plan** — paste it directly into your milestone slide or PRD technical feasibility section
- **Pair with the DACI prompt** — once you have the owner column populated, run the DACI decision framework prompt to clarify who is accountable for resolving each high-risk dependency
- **Pair with the working backwards prompt** — run working backwards first to define what you are building and why, then run dependency identification to understand what has to be true for it to ship
- **Re-run at each planning horizon** — dependencies change; run this at discovery, at quarterly planning, and two weeks before each milestone to keep the map current
