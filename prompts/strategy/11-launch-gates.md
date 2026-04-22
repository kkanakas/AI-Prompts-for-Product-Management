# Launch Gates

**Phase:** Strategy & Go-to-Market
**Purpose:** Define, manage, and evaluate the launch gates required to release a capability to private preview, public preview, or general availability — giving product, engineering, legal, security, support, and marketing teams a shared, unambiguous checklist of what must be true at each gate before the release proceeds.

## Prompt Template

```
You are a senior product manager defining and managing launch gates for a feature or capability release. Using the context below, generate a complete launch gate framework.

Feature or capability name: [FEATURE_NAME]
One-line description: [FEATURE_DESCRIPTION]
Release type: [RELEASE_TYPE — e.g., "Private Preview", "Public Preview", "Limited GA", "General Availability"]
Target customer segment: [TARGET_SEGMENT — e.g., "enterprise security teams", "all paying customers", "internal teams only"]
Target release date: [TARGET_DATE or "TBD"]
Known risks or concerns: [RISKS — e.g., "performance at scale", "data privacy for regulated industries", "high support complexity", "incomplete documentation"]
Teams involved: [TEAMS — e.g., "Product, Engineering, QA, Security, Legal, Support, Marketing, Sales Engineering"]
Decision maker for Go/No-Go: [DECISION_MAKER — e.g., "VP of Product", "Release Committee", "GM"]

---

## Section 1 — Release Tier Definition

Clarify what this release tier means, who has access, and what the operating constraints are.

### Release Tier: [RELEASE_TYPE]

| Dimension | Definition |
|---|---|
| Who has access | [e.g., "Named accounts only — PM-approved cohort of 5–10 customers"] |
| How access is granted | [e.g., "Feature flag enabled per account by PM", "Self-signup via waitlist form"] |
| SLA commitment | [e.g., "No SLA — best effort only", "Standard SLA applies"] |
| Support model | [e.g., "CSM-led white-glove", "Self-serve docs + async Slack channel"] |
| Feedback commitment | [e.g., "Weekly check-in calls required", "In-product NPS survey bi-weekly"] |
| Data and privacy posture | [e.g., "Preview data isolated from production", "Standard data handling applies"] |
| Pricing and packaging | [e.g., "Free during preview with conversion to paid at GA", "Included in existing plan"] |
| Rollback policy | [e.g., "Feature can be disabled per account within 1 hour by on-call engineer"] |

---

## Section 2 — Launch Gate Scorecard

For each gate, every criterion must be either PASS, CONDITIONAL PASS (with named condition), or FAIL. A single FAIL blocks the release unless formally waived by the decision maker with documented rationale.

---

### Gate 1 — Engineering Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| E1 | All P0 and P1 bugs resolved | Engineering Lead | PASS / FAIL / CONDITIONAL | Bug tracker report with zero open P0/P1s |
| E2 | Automated test coverage ≥ [TARGET]% for new code paths | Engineering Lead | PASS / FAIL / CONDITIONAL | Coverage report from CI pipeline |
| E3 | Integration tests passing in staging environment | QA Lead | PASS / FAIL / CONDITIONAL | CI/CD test run result |
| E4 | Performance benchmarks met: [TARGET — e.g., p95 response < 2s at 1,000 concurrent users] | Engineering Lead | PASS / FAIL / CONDITIONAL | Load test report |
| E5 | Feature flags implemented and rollback tested | Engineering Lead | PASS / FAIL / CONDITIONAL | Rollback runbook signed off |
| E6 | Logging, monitoring, and alerting in place | Platform/SRE | PASS / FAIL / CONDITIONAL | Observability dashboard link |
| E7 | Data migration (if applicable) rehearsed and validated | Engineering Lead | PASS / FAIL / CONDITIONAL | Migration dry-run report |
| E8 | No unresolved technical debt that blocks safe operation | Engineering Lead | PASS / FAIL / CONDITIONAL | Tech debt register reviewed |

**Gate 1 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

### Gate 2 — Security and Compliance Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| S1 | Security review completed and all Critical/High findings resolved | Security Lead | PASS / FAIL / CONDITIONAL | Security review sign-off |
| S2 | Penetration test completed (if required for this release tier) | Security Lead | PASS / FAIL / CONDITIONAL | Pen test report or waiver |
| S3 | Data privacy impact assessment (DPIA) completed | Privacy/Legal | PASS / FAIL / CONDITIONAL | DPIA sign-off |
| S4 | Compliance requirements met: [e.g., SOC 2, FedRAMP, GDPR, HIPAA] | Legal/Compliance | PASS / FAIL / CONDITIONAL | Compliance attestation |
| S5 | Audit logging in place for all user actions on sensitive data | Engineering Lead | PASS / FAIL / CONDITIONAL | Audit log sample review |
| S6 | Access controls and least-privilege permissions validated | Security Lead | PASS / FAIL / CONDITIONAL | Access control review |
| S7 | Secrets management and credential rotation confirmed | Engineering Lead | PASS / FAIL / CONDITIONAL | Secrets audit |

**Gate 2 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

### Gate 3 — Product and UX Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| P1 | Core user flows tested end-to-end by PM or QA | PM / QA Lead | PASS / FAIL / CONDITIONAL | Test session notes or recording |
| P2 | Acceptance criteria from all Must-Have stories verified | PM | PASS / FAIL / CONDITIONAL | Story sign-off log |
| P3 | Accessibility requirements met: [e.g., WCAG 2.1 AA] | Design / QA | PASS / FAIL / CONDITIONAL | Accessibility audit report |
| P4 | Error states and empty states designed and implemented | Design | PASS / FAIL / CONDITIONAL | Design review sign-off |
| P5 | Mobile/responsive behavior validated (if applicable) | QA Lead | PASS / FAIL / CONDITIONAL | Device testing report |
| P6 | Onboarding flow validated with at least [N] test users | PM | PASS / FAIL / CONDITIONAL | Usability test notes |
| P7 | Analytics and instrumentation verified: key events tracked | PM / Analytics | PASS / FAIL / CONDITIONAL | Analytics event schema signed off |

**Gate 3 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

### Gate 4 — Documentation and Support Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| D1 | User-facing documentation written and reviewed | Technical Writer | PASS / FAIL / CONDITIONAL | Doc link and reviewer sign-off |
| D2 | In-product help text and tooltips reviewed | PM / Design | PASS / FAIL / CONDITIONAL | UX copy review sign-off |
| D3 | Support runbook written and approved by support team | Support Lead | PASS / FAIL / CONDITIONAL | Runbook link and sign-off |
| D4 | Support team trained on new capability | Support Lead | PASS / FAIL / CONDITIONAL | Training completion record |
| D5 | Known issues and workarounds documented | PM | PASS / FAIL / CONDITIONAL | Known issues log |
| D6 | Escalation path defined and on-call engineers briefed | Engineering Lead | PASS / FAIL / CONDITIONAL | On-call runbook updated |
| D7 | FAQ or troubleshooting guide published | Technical Writer | PASS / FAIL / CONDITIONAL | FAQ link |

**Gate 4 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

### Gate 5 — Legal and Commercial Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| L1 | Terms of service or preview agreement updated and approved | Legal | PASS / FAIL / CONDITIONAL | Legal sign-off |
| L2 | Pricing and packaging approved by Finance and Revenue | Finance / PM | PASS / FAIL / CONDITIONAL | Pricing approval memo |
| L3 | Any required third-party licenses or contracts in place | Legal | PASS / FAIL / CONDITIONAL | Contract / license confirmation |
| L4 | Export control review completed (if applicable) | Legal | PASS / FAIL / CONDITIONAL | Export review sign-off |
| L5 | Revenue recognition treatment confirmed (if applicable) | Finance | PASS / FAIL / CONDITIONAL | Finance sign-off |

**Gate 5 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

### Gate 6 — Go-to-Market Readiness

| # | Criterion | Owner | Status | Evidence required |
|---|---|---|---|---|
| G1 | Internal announcement drafted and approved | PMM / PM | PASS / FAIL / CONDITIONAL | Announcement draft reviewed |
| G2 | Sales and Solutions Engineering briefed and trained | PMM / SE Lead | PASS / FAIL / CONDITIONAL | Enablement session completed |
| G3 | External-facing messaging and positioning approved | PMM | PASS / FAIL / CONDITIONAL | Messaging framework sign-off |
| G4 | Customer-facing release notes or changelog entry drafted | PM / PMM | PASS / FAIL / CONDITIONAL | Release notes draft reviewed |
| G5 | Customer success playbook for preview/GA cohort updated | CSM Lead | PASS / FAIL / CONDITIONAL | Playbook link and sign-off |
| G6 | Reference customers or case study candidates identified | PMM / CSM | PASS / FAIL / CONDITIONAL | List of confirmed references |
| G7 | Press or analyst embargo plan in place (GA only) | PMM / Comms | PASS / FAIL / CONDITIONAL | Embargo list and timing confirmed |

**Gate 6 verdict:** PASS / FAIL / CONDITIONAL
**Blocking items:** [list any FAIL or open CONDITIONAL items]

---

## Section 3 — Overall Gate Summary

| Gate | Verdict | Open blocking items | Owner | Resolution deadline |
|---|---|---|---|---|
| Gate 1 — Engineering | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| Gate 2 — Security & Compliance | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| Gate 3 — Product & UX | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| Gate 4 — Documentation & Support | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| Gate 5 — Legal & Commercial | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| Gate 6 — Go-to-Market | PASS / FAIL / CONDITIONAL | [count] | [lead] | [date] |
| **Overall release verdict** | **GO / NO-GO / CONDITIONAL GO** | | | |

---

## Section 4 — Waiver Register

For any criterion that cannot be met before the target release date, document a formal waiver. Waivers require decision-maker sign-off.

| Criterion ID | Criterion | Reason for waiver | Risk accepted | Mitigation | Waiver approved by | Expiry date |
|---|---|---|---|---|---|---|
| [E.g., S2] | [Pen test not completed] | [External vendor unavailable before release date] | [Low — no external user data exposed in this tier] | [Pen test scheduled within 30 days post-release] | [Decision maker name] | [Date] |

---

## Section 5 — Go/No-Go Meeting Agenda

Use this agenda for the formal Go/No-Go decision meeting.

**Meeting:** [FEATURE_NAME] — [RELEASE_TYPE] Go/No-Go Review
**Date:** [DATE]
**Duration:** 30–45 minutes
**Decision owner:** [DECISION_MAKER]
**Required attendees:** [list of gate owners]

| Time | Agenda item | Owner |
|---|---|---|
| 0–5 min | Feature recap: what ships and to whom | PM |
| 5–10 min | Gate summary walkthrough: pass/fail/conditional per gate | PM |
| 10–20 min | Review of open blocking items and waivers | Gate owners |
| 20–25 min | Risk discussion: top 3 risks if we release vs. if we delay | PM |
| 25–30 min | Decision: Go / No-Go / Conditional Go + any conditions | Decision maker |
| 30–35 min | Next steps: who does what by when | All |

**Decision record template:**
- Decision: GO / NO-GO / CONDITIONAL GO
- Conditions (if conditional): [list]
- Release date confirmed: [date]
- Decision made by: [name, title]
- Date of decision: [date]
- Attendees: [list]

---

## Section 6 — Post-Release Monitoring Plan

Define what you will watch in the 24, 72, and 168 hours after release to confirm the release is healthy and catch issues before they escalate.

| Timeframe | Metric | Threshold | Owner | Action if breached |
|---|---|---|---|---|
| 0–24 hours | Error rate | < [TARGET]% | Engineering | Page on-call, consider rollback |
| 0–24 hours | Support tickets opened | < [TARGET] | Support Lead | Triage and escalate to PM |
| 0–24 hours | Successful activation rate | ≥ [TARGET]% | PM | Investigate onboarding funnel |
| 24–72 hours | p95 response time | < [TARGET] ms | Engineering | Performance investigation |
| 24–72 hours | Customer-reported P0/P1 bugs | 0 | PM / Engineering | Hotfix or rollback |
| 72–168 hours | Feature adoption rate | ≥ [TARGET]% | PM | PM outreach to non-adopters |
| 72–168 hours | NPS / CSAT pulse | ≥ [TARGET] | PM / CSM | Immediate customer check-in |

**Rollback trigger:** [Define the specific condition that automatically triggers a rollback decision — e.g., "Error rate > 5% for more than 10 minutes" or "Any P0 data integrity bug confirmed"]
**Rollback owner:** [Name and on-call rotation]
**Rollback procedure:** [Link to runbook]
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Name of the feature or capability being released | `"AI-Assisted Threat Detection"` |
| `[FEATURE_DESCRIPTION]` | One-line description | `"Real-time anomaly detection surfacing threats in the SOC dashboard"` |
| `[RELEASE_TYPE]` | The tier being gated | `"Private Preview"`, `"Public Preview"`, `"Limited GA"`, `"General Availability"` |
| `[TARGET_SEGMENT]` | Who gets access at this tier | `"Named enterprise accounts — PM-approved cohort"` |
| `[TARGET_DATE]` | Planned release date | `"2026-06-01"` or `"End of Q2 2026"` |
| `[RISKS]` | Known risks going into the gate review | `"Performance at scale unvalidated; EU data residency requirements"` |
| `[TEAMS]` | All teams that own gate criteria | `"Product, Engineering, QA, Security, Legal, Support, PMM"` |
| `[DECISION_MAKER]` | Who makes the final Go/No-Go call | `"VP of Product"` |

## Output Variants

**Lightweight gate for internal preview only** — add to the prompt:
```
This release is internal-only (dogfood). Simplify the gate scorecard: remove Gate 5 (Legal & Commercial) and Gate 6 (Go-to-Market) entirely. Reduce Gate 2 (Security) to internal-risk criteria only. Keep Gate 1 (Engineering), Gate 3 (Product & UX), and Gate 4 (Documentation & Support) but reduce each to the 3 most critical criteria. Output a condensed one-page checklist.
```

**Gate tracking spreadsheet format** — add to the prompt:
```
Format the entire gate scorecard as a flat table suitable for a Google Sheet or Excel tracker. Columns: Gate | Criterion ID | Criterion description | Owner | Due date | Status (Not started / In progress / PASS / FAIL / WAIVED) | Evidence link | Notes. Include one row per criterion across all gates.
```

**Conditional Go action plan** — add to the prompt:
```
The Go/No-Go decision is CONDITIONAL GO. For each open blocking item, generate an action card: criterion ID, what is missing, the specific action required to close it, the owner, the deadline, and the verification step that confirms it is closed. Format as a numbered action list ordered by deadline.
```

**Retrospective format** — add to the prompt:
```
This release has already shipped. Convert the gate scorecard into a launch retrospective: for each gate, summarize what passed cleanly, what was conditionally waived, what issues emerged post-release, and what the team should do differently for the next launch. Add a "Lessons Learned" section at the end with the top 3 process improvements.
```

## Tips

- **Define gates before work starts, not at the end** — gate criteria set at the beginning of a release cycle become the engineering and QA acceptance bar; criteria defined at the last minute become negotiating points
- **Every FAIL needs an owner and a date** — a gate scorecard without named owners is a wish list, not a gate; the moment a criterion is logged as FAIL, assign the owner and resolution deadline in the same breath
- **Waivers are not failures — undocumented waivers are** — every release has something that doesn't pass cleanly; the waiver register makes the risk visible, accepted, and traceable so it doesn't become a surprise post-release
- **Pair with the private preview plan prompt** — the private preview plan defines the phases and cohort structure; this prompt defines the gate criteria that must be met before each phase opens
- **Pair with the dependency identification prompt** — external dependencies (third-party audits, legal reviews, platform team deliverables) are the most common source of gate failures; run dependency identification early so gate owners have enough lead time
- **Post-release monitoring is part of the gate** — a release without a monitoring plan is not finished; Section 6 should be agreed before the Go/No-Go meeting, not after the feature ships
- **Gate criteria should be binary** — "documentation is good enough" is not a criterion; "documentation reviewed and signed off by Technical Writer by [date]" is; every criterion should have a clear yes/no test
