# Private Preview Plan

**Phase:** Strategy & Planning
**Purpose:** Generate a structured, multi-phased private preview plan for a feature — covering cohort selection, entry and exit criteria, feedback loops, risk controls, and graduation gates — so you can validate with real customers before general availability while limiting blast radius and maintaining control.

## Prompt Template

```
You are a senior product manager planning a multi-phased private preview for a new feature. Using the context below, generate a complete private preview plan.

Feature name: [FEATURE_NAME]
Feature description: [FEATURE_DESCRIPTION]
Target customer segment: [TARGET_SEGMENT — e.g., "enterprise security teams", "SMB e-commerce merchants", "internal power users"]
Key hypothesis to validate: [HYPOTHESIS — e.g., "customers can complete onboarding in under 10 minutes without support", "the alert accuracy is high enough to reduce false positives by 30%"]
Known risks or concerns: [RISKS — e.g., "data privacy for regulated industries", "performance at scale", "UX complexity for non-technical users"]
Target GA date (if known): [GA_DATE or "TBD"]

Generate a multi-phased private preview plan with the following structure:

---

## Phase 0 — Internal Dogfood
**Goal:** Validate core functionality and catch critical bugs before any external exposure.
**Participants:** [Internal teams — e.g., Customer Success, Sales Engineering, PM team, internal power users]
**Duration:** [Recommended: 2–4 weeks]
**What to test:** Core happy path, basic error handling, admin controls, data integrity
**Entry criteria:** Feature is code-complete with no P0/P1 bugs; automated test coverage >80%; security review passed
**Exit criteria:** No P0/P1 bugs open; internal participants can complete the core workflow unassisted; performance benchmarks met
**Feedback mechanism:** Weekly internal sync, shared Slack channel for bugs, structured survey at week 2
**Risks to watch:** [Specific risks from input]

---

## Phase 1 — Trusted Pilot (Closed Alpha)
**Goal:** Validate with a small, forgiving cohort of high-trust customers who will give candid feedback and tolerate rough edges.
**Cohort size:** [Recommended: 3–5 customers]
**Cohort selection criteria:**
  - Strategic fit: [e.g., represents target segment, active champion relationship]
  - Risk tolerance: [e.g., willing to use pre-GA software, has signed preview agreement]
  - Feedback quality: [e.g., has dedicated technical contact, will attend weekly check-ins]
  - Exclusions: [e.g., regulated industries, large accounts where an incident is high-stakes]
**Duration:** [Recommended: 4–6 weeks]
**What to validate:** Core value proposition, onboarding experience, integration complexity, support load
**Entry criteria:** Phase 0 exit criteria met; preview agreement signed; dedicated CSM assigned per account
**Exit criteria:** All pilot accounts have successfully completed the core workflow; NPS ≥ [TARGET]; no P0/P1 bugs open; support ticket rate < [THRESHOLD] per account per week
**Feedback mechanism:** Weekly 30-min check-in call per account; in-product feedback widget; structured mid-point and end-of-phase survey; dedicated Slack connect channel
**Metrics to track:** [e.g., time-to-first-value, activation rate, support tickets opened, feature adoption depth]
**Risks to watch:** [Specific risks from input]

---

## Phase 2 — Expanded Private Preview
**Goal:** Increase cohort diversity and volume to stress-test at scale, validate with varied use cases, and build the evidence base for GA readiness.
**Cohort size:** [Recommended: 15–30 customers]
**Cohort selection criteria:**
  - Diversity requirements: [e.g., mix of company sizes, geographies, use cases, technical maturity levels]
  - Waitlist management: [how customers apply or are nominated]
  - Exclusions: [updated based on Phase 1 learnings]
**Duration:** [Recommended: 6–8 weeks]
**What to validate:** Scalability, edge cases, self-serve onboarding without white-glove support, documentation quality, pricing and packaging assumptions
**Entry criteria:** Phase 1 exit criteria met; onboarding docs published; support runbook in place; pricing model finalized for preview participants
**Exit criteria:** Activation rate ≥ [TARGET]%; weekly active usage rate ≥ [TARGET]%; support ticket volume within support team capacity; no unresolved security or compliance findings; reference customers identified for GA launch
**Feedback mechanism:** In-product NPS pulse (bi-weekly); async feedback form after key workflows; optional monthly group call; usage telemetry dashboards reviewed weekly by PM
**Metrics to track:** [Activation rate, weekly active users, time-to-value, support ticket rate, NPS, retention at 30 days]
**Risks to watch:** [Updated risks from Phase 1 learnings]

---

## Phase 3 — GA Readiness Gate
**Goal:** Confirm all GA entry criteria are met before opening to the full customer base.

**GA readiness checklist:**
- [ ] All Phase 2 exit criteria met
- [ ] Documentation complete and reviewed by technical writer
- [ ] Support team trained and runbook approved
- [ ] SLA and pricing finalized and approved by Finance and Legal
- [ ] Security and compliance sign-off obtained
- [ ] Performance and scalability benchmarks validated at [TARGET] concurrent users
- [ ] Rollback and incident response plan documented
- [ ] Marketing and go-to-market plan approved
- [ ] Reference customers confirmed for case studies or launch quotes
- [ ] Executive sponsor sign-off received

**Go / No-Go decision owner:** [DECISION_OWNER — e.g., VP Product]
**Decision date:** [TARGET_DATE]

---

## Cohort Management

| Phase | Cohort Size | Selection Method | Contacts Per Account | Preview Agreement Required |
|---|---|---|---|---|
| Phase 0 — Dogfood | Internal only | PM nomination | Slack channel | No |
| Phase 1 — Pilot | 3–5 customers | PM/CSM nomination | Weekly call + Slack | Yes |
| Phase 2 — Expanded | 15–30 customers | Application or CSM waitlist | Async + monthly group call | Yes |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk 1 from input] | High / Med / Low | High / Med / Low | [Mitigation] | [Owner] |
| Performance degradation at scale | Medium | High | Load test before Phase 2; set hard usage limits per account | Engineering |
| Support overload | Medium | Medium | Limit Phase 2 cohort size; publish self-serve docs before Phase 2 entry | Support Lead |
| Customer churns during preview | Low | High | Assign dedicated CSM; weekly check-ins; clear value milestones | CSM |

---

## Communication Plan

| Audience | Message | Channel | Cadence |
|---|---|---|---|
| Preview customers | Status updates, known issues, new capabilities | Email + Slack connect | Bi-weekly |
| Internal stakeholders | Phase progress, metrics, blockers | Steering committee update | Weekly |
| Executive sponsor | Go/No-Go recommendation | Written briefing | At each phase gate |
| Broader customer base | Waitlist availability | In-product banner + email | On Phase 2 open |

---

## Success Metrics Summary

| Metric | Phase 1 Target | Phase 2 Target | GA Gate |
|---|---|---|---|
| Activation rate | [TARGET]% | [TARGET]% | ≥ [TARGET]% |
| Time-to-first-value | < [TARGET] mins | < [TARGET] mins | < [TARGET] mins |
| NPS | ≥ [TARGET] | ≥ [TARGET] | ≥ [TARGET] |
| Support tickets / account / week | < [TARGET] | < [TARGET] | Within SLA |
| Weekly active usage rate | [TARGET]% | [TARGET]% | ≥ [TARGET]% |
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Name of the feature going into preview | `"AI-Assisted Threat Detection"` |
| `[FEATURE_DESCRIPTION]` | 1–3 sentence description of what the feature does | `"Real-time anomaly detection that surfaces threats in the SOC dashboard"` |
| `[TARGET_SEGMENT]` | The primary customer type for the preview | `"Enterprise security operations teams (500+ employees)"` |
| `[HYPOTHESIS]` | The core assumption the preview must validate | `"SOC analysts can triage alerts 40% faster without additional training"` |
| `[RISKS]` | Known risks or concerns going in | `"False positive rate may erode analyst trust; data residency requirements for EU customers"` |
| `[GA_DATE]` | Target general availability date | `"Q3 2026"` or `"TBD"` |
| `[DECISION_OWNER]` | Who makes the final Go/No-Go call | `"VP of Product"` |

## Output Variants

**Condensed one-pager for leadership** — add to the prompt:
```
Condense the plan into a single-page executive summary: phase names, dates, cohort sizes, key exit criteria, and the top 3 risks. No section should exceed 3 bullet points. Format for a slide or steering committee pre-read.
```

**Jira epic structure** — add to the prompt:
```
Convert each phase into a Jira epic stub with: epic name, description, acceptance criteria, and a list of suggested story titles. Format each epic as a separate block ready to paste into Jira.
```

**Customer-facing preview invitation** — add to the prompt:
```
Write a customer-facing email inviting a named customer to join the Phase 1 pilot. Include: what the feature does, what we need from them, what they get in return, the time commitment, and a clear call to action. Keep it under 250 words.
```

## Tips

- **Phase 0 dogfood is non-negotiable** — shipping rough features to external customers first destroys trust and creates avoidable support load; always validate internally first
- **Cohort diversity beats cohort size** — 5 customers across different segments teach you more than 20 similar accounts; optimize Phase 1 for feedback quality, not volume
- **Exit criteria must be measurable** — "customers are happy" is not an exit criterion; "NPS ≥ 30 and support ticket rate < 2 per account per week" is
- **Pair with the dependency identification prompt** — run dependency identification first to surface any blockers that could delay phase entry criteria
- **Pair with the DACI prompt** — use DACI to clarify who makes the Go/No-Go decision at each phase gate before the gate arrives, not during it
- **Keep the risk register alive** — update it weekly during Phase 1 and Phase 2; risks that were Low at the start often become High once real customers are using the feature
