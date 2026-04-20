# Big Rock Decomposition

**Phase:** Strategy & Planning
**Purpose:** Decompose a large, complex initiative ("Big Rock") into a structured, deliverable hierarchy — outcomes, epics, features, and work items — that product and platform teams can sequence, own, and execute without losing sight of the original strategic intent.

## Prompt Template

```
You are a senior product leader helping decompose a large initiative into a manageable set of deliverables. Using the context below, generate a complete Big Rock decomposition.

Initiative name: [INITIATIVE_NAME]
Strategic intent: [STRATEGIC_INTENT — why this initiative matters, what business or customer outcome it drives]
Target customer or user: [TARGET_USER — who benefits from this initiative]
Team type: [TEAM_TYPE — e.g., "product team", "platform team", "shared services team", "cross-functional squad"]
Constraints: [CONSTRAINTS — e.g., "must ship MVP in Q3", "limited to 8 engineers", "cannot break existing API contracts", "regulatory approval required"]
Dependencies or related initiatives: [DEPENDENCIES — or "none known"]
Current state: [CURRENT_STATE — e.g., "no existing capability", "legacy system in place", "partial implementation exists"]

---

## Section 1 — Big Rock Definition

### 1.1 Outcome Statement
Write a clear, measurable outcome statement for the initiative in this format:

**We will know this Big Rock is complete when:**
- Customer/user outcome: [e.g., "enterprise customers can self-serve onboarding in under 30 minutes without contacting support"]
- Business outcome: [e.g., "onboarding NPS increases from X to Y and support tickets for onboarding drop by Z%"]
- Platform/technical outcome: [e.g., "the onboarding platform supports 10x current volume without manual intervention"]

### 1.2 Scope Boundary
Define what is IN scope and what is explicitly OUT of scope to prevent scope creep.

**In scope:**
- [Capability or outcome 1]
- [Capability or outcome 2]
- [Capability or outcome 3]

**Out of scope (for this initiative):**
- [What will not be addressed — be specific]
- [What is deferred to a future initiative]

### 1.3 Success Metrics

| Metric | Baseline | Target | Measurement method |
|---|---|---|---|
| [Primary outcome metric] | [current] | [target] | [how measured] |
| [Secondary metric] | [current] | [target] | [how measured] |
| [Leading indicator] | [current] | [target] | [how measured] |

---

## Section 2 — Decomposition Hierarchy

### 2.1 Epics (Themes of Work)
Break the Big Rock into 3–6 epics. Each epic is a coherent theme of work that delivers a meaningful slice of value and can be owned by a single team or workstream.

For each epic:

**Epic [N]: [EPIC_NAME]**
- Description: [what this epic delivers and why it matters]
- Customer/user value: [what the customer or user can do once this epic is complete]
- Team owner: [which team or squad owns this epic]
- Estimated size: [S / M / L / XL — relative to other epics]
- Dependencies: [which other epics must precede or run in parallel]
- Definition of done: [measurable completion criteria]

---

### 2.2 Features (Deliverable Capabilities per Epic)
For each epic, identify the 3–5 features (discrete, deliverable capabilities) that together complete it.

**Epic [N] — Features:**

| Feature | Description | Value delivered | Owner | Size | Dependency |
|---|---|---|---|---|---|
| [Feature 1] | [what it does] | [who benefits and how] | [team/squad] | [S/M/L] | [none or Epic X] |
| [Feature 2] | | | | | |
| [Feature 3] | | | | | |

---

### 2.3 Work Items (Stories and Tasks per Feature)
For the highest-priority feature in each epic, break it into work items (user stories or tasks) at a level of detail actionable in a sprint.

**Feature: [FEATURE_NAME]**

User stories:
- As a [user type], I want to [action], so that [outcome]
- As a [user type], I want to [action], so that [outcome]
- As a [user type], I want to [action], so that [outcome]

Platform/technical tasks (if applicable):
- [Infrastructure or API work]
- [Data migration or schema changes]
- [Security or compliance gates]

Acceptance criteria for this feature:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## Section 3 — MVP Identification

### 3.1 Minimum Viable Increment
Identify the smallest coherent set of epics and features that delivers measurable value and validates the core hypothesis — without building everything.

**MVP scope:**
- Epics included: [list the epics included in MVP]
- Epics deferred: [list epics moved to post-MVP and why]
- Features included: [the specific features within MVP epics]
- Features deferred: [features cut from MVP with rationale]

**MVP outcome statement:** [What a customer or user can do after MVP ships that they cannot do today]

**MVP success gate:** [The metric or signal that tells you the MVP has achieved its purpose and you should proceed to full build]

### 3.2 Phased Delivery Plan

| Phase | Epics included | Key deliverable | Target completion | Team |
|---|---|---|---|---|
| MVP | [epics] | [what ships] | [date or sprint] | [team] |
| Phase 2 | [epics] | [what ships] | [date or sprint] | [team] |
| Phase 3 | [epics] | [what ships] | [date or sprint] | [team] |

---

## Section 4 — Dependency and Risk Map

### 4.1 Cross-Epic Dependencies

| Dependent epic | Depends on | Type of dependency | Risk if delayed |
|---|---|---|---|
| [Epic B] | [Epic A] | Sequential — A must complete before B starts | [impact] |
| [Epic C] | [Epic B] | Parallel — can run concurrently but shares API contract | [impact] |

### 4.2 External Dependencies

| Dependency | Type | Owner | Status | Risk |
|---|---|---|---|---|
| [Platform API / third-party / compliance gate] | [technical / regulatory / partner] | [team or vendor] | [confirmed / pending / unknown] | [High/Med/Low] |

### 4.3 Top 3 Risks to Delivery

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk 1] | High / Med / Low | High / Med / Low | [mitigation] | [owner] |
| [Risk 2] | | | | |
| [Risk 3] | | | | |

---

## Section 5 — Team and Capacity View

### 5.1 Work Allocation by Team

| Team / Squad | Epics owned | Estimated total size | Parallel capacity | Notes |
|---|---|---|---|---|
| [Team A] | [Epic 1, Epic 3] | [XL] | [can run Epics 1 and 3 in parallel] | [constraint] |
| [Team B] | [Epic 2] | [L] | [sequential after Epic 1] | [dependency] |

### 5.2 Critical Path
List the sequence of epics and features that, if delayed, directly delays the final delivery date:

1. [Epic/Feature A] → 2. [Epic/Feature B] → 3. [Epic/Feature C] → **Delivery**

**Critical path length:** [estimated total duration]
**Earliest possible completion date:** [based on constraints and team capacity]

---

## Section 6 — Communication and Alignment

### 6.1 Stakeholder Summary (one paragraph)
Write a plain-language summary of this Big Rock decomposition for a steering committee or executive sponsor. Cover: what the initiative is, how it is structured, what ships in MVP, what the critical path is, and what decisions or support are needed from leadership.

### 6.2 Team Briefing (one paragraph per team)
For each team that owns at least one epic, write a 3–4 sentence briefing: what they own, why it matters, what they depend on from other teams, and what their first sprint should focus on.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[INITIATIVE_NAME]` | Name of the Big Rock initiative | `"Unified Customer Data Platform"` |
| `[STRATEGIC_INTENT]` | Why this initiative matters — the business or customer outcome it drives | `"Enable real-time personalization across all customer touchpoints to reduce churn by 15%"` |
| `[TARGET_USER]` | Who benefits from this initiative | `"Marketing operations teams and end customers receiving personalized experiences"` |
| `[TEAM_TYPE]` | The type of team(s) delivering this work | `"Two product squads plus one platform team"` |
| `[CONSTRAINTS]` | Hard constraints on time, people, or technology | `"Must not disrupt existing integrations; 6-engineer platform team; Q4 board demo required"` |
| `[DEPENDENCIES]` | Known upstream or downstream dependencies | `"Identity service migration (Platform Team B), GDPR compliance review (Legal)"` |
| `[CURRENT_STATE]` | What exists today | `"Siloed data in three separate systems with no unified API"` |

## Output Variants

**Platform team focus** — add to the prompt:
```
This is a platform team initiative — the "customers" are internal product teams, not end users. Frame all user stories, value statements, and outcome metrics from the perspective of internal product team velocity and developer experience. Replace customer-facing outcome metrics with platform metrics: API adoption rate, integration time, uptime SLA, and onboarding time for new product teams consuming the platform.
```

**Agile backlog format** — add to the prompt:
```
Output the full decomposition as a ready-to-import backlog structure: Epic → Feature → User Story → Acceptance Criteria. Format each level as a numbered hierarchy. For each story, include: story title, description, acceptance criteria (as a checklist), estimated story points (1/2/3/5/8), and suggested sprint number based on the phased delivery plan.
```

**Executive one-pager** — add to the prompt:
```
Condense the decomposition into a single executive briefing: initiative name, strategic intent, MVP scope and completion date, full scope and completion date, critical path, top 3 risks, and the one decision needed from leadership this week. Format for a slide or steering committee pre-read. No section should exceed 3 bullet points.
```

**Platform + product split view** — add to the prompt:
```
Separate the decomposition into two parallel tracks: (1) Platform track — infrastructure, APIs, data pipelines, and shared services that product teams depend on; (2) Product track — customer-facing features that depend on the platform track. Show the handoff points between tracks and flag any features in the product track that are blocked until specific platform capabilities ship.
```

## Tips

- **Start with outcomes, not features** — the most common Big Rock decomposition failure is jumping straight to features; spend 20% of the time on Section 1 (outcome statement, scope boundary, success metrics) or you will build the wrong things correctly
- **Three levels is enough** — Epic → Feature → Story is the right granularity; going deeper than stories in a decomposition session produces false precision and wastes time
- **MVP is a negotiation, not a cut** — use the MVP identification section explicitly with stakeholders; what gets cut from MVP is a decision, not a default; the prompt forces that conversation to happen deliberately
- **Critical path is your planning anchor** — any work not on the critical path can flex; focus risk mitigation and weekly check-ins on the critical path only
- **Pair with the dependency identification prompt** — run dependency identification first on the full Big Rock to surface external blockers, then use this prompt to decompose the work you actually control
- **Pair with the DACI prompt** — one of the most common Big Rock failures is unclear ownership at the epic level; run the DACI decision framework for the 1–2 highest-risk epics to lock in accountability before work starts
- **Re-run Section 3 at each phase gate** — the MVP and phasing plan should be revisited after each phase completes; what you learn in Phase 1 almost always changes what goes into Phase 2
