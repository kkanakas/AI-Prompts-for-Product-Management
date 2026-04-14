# Example: DACI Decision Framework — Mobile Strategy for Enterprise Expansion

This is a worked example of the DACI Decision Framework prompt (`prompts/stakeholder-management/02-daci-decision-framework.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I need to document a key decision using the DACI framework.

Decision to be made:
Whether to build native iOS and Android apps or invest in a Progressive Web App (PWA) to support Clearpath's mobile strategy for enterprise customers in Q3.

Context and background:
Three enterprise prospects in the current pipeline have asked about mobile access during procurement reviews. Two deals have been verbally delayed pending a mobile answer. Engineering has produced estimates, but they diverge significantly depending on the approach. A decision is needed before Q3 sprint planning begins on June 9.

Options under consideration:
- Option A: Build native iOS and Android apps (separate codebases)
- Option B: Build a Progressive Web App (PWA) with offline capability
- Option C: Defer mobile investment to Q4 and communicate a roadmap commitment to prospects

Decision deadline:
June 6 — sprint planning begins June 9 and engineering cannot begin work without a confirmed direction.

People involved:
- Maya Osei — Chief Product Officer
- Ravi Suresh — VP of Engineering
- James Okafor — Head of Sales
- Priya Nair — Customer Success Lead
- Tanya Bloom — Head of Finance
- Leo Morales — Enterprise Account Executive
- Dana Kim — Lead Mobile Engineer

Constraints or non-negotiables:
- No budget to hire a dedicated mobile engineering team in Q3
- Must deliver something customer-visible by end of Q3 (September 30)
- Any solution must work within the existing SOC 2 compliance boundary
```

## Generated Output

### 1. Decision Statement

Decide the mobile delivery approach (native apps, PWA, or deferral) for Clearpath's enterprise customer segment by June 6, 2025, in order to unblock Q3 sprint planning and provide a credible answer to the three enterprise deals currently pending a mobile commitment.

---

### 2. DACI Role Assignment

| Name | Role / Team | DACI Role | Why this role |
|---|---|---|---|
| Maya Osei | Chief Product Officer | **Approver** | Owns the product strategy and investment trade-offs; the decision has cross-functional implications that require CPO authority |
| Ravi Suresh | VP of Engineering | **Driver** | Best positioned to coordinate input across engineering, finance, and product; owns the delivery feasibility assessment and will run the decision meeting |
| James Okafor | Head of Sales | **Contributor** | Owns the pipeline context — only he can confirm whether deals are truly blocked vs. using mobile as a negotiating lever |
| Dana Kim | Lead Mobile Engineer | **Contributor** | Owns the technical estimate; her input on build complexity and SOC 2 implications is non-substitutable |
| Tanya Bloom | Head of Finance | **Contributor** | Owns the budget constraint validation — must confirm whether Q3 budget can absorb a native build before Option A is on the table |
| Priya Nair | Customer Success Lead | **Informed** | Needs the outcome to brief existing customers and set expectations; no unique input that changes the decision |
| Leo Morales | Enterprise Account Executive | **Informed** | Needs the outcome and talking points for prospect conversations; James Okafor represents the sales perspective as Contributor |

---

### 3. Decision Criteria

| Criterion | Weight | Who assesses it | What "good" looks like |
|---|---|---|---|
| Deal impact — does this unblock the three pipeline deals? | High | James Okafor | At least two of the three deals confirm mobile was a genuine blocker, not a nice-to-have |
| Delivery feasibility within Q3 and existing team | High | Dana Kim + Ravi Suresh | A working, customer-demoable version ships by September 30 without pulling engineers off Critical backlog items |
| Budget fit within Q3 envelope | High | Tanya Bloom | Investment does not require a budget reforecast or headcount addition |
| SOC 2 compliance maintained | High | Ravi Suresh + Dana Kim | Solution operates within existing compliance boundary without requiring a new audit |
| Long-term architecture alignment | Medium | Ravi Suresh | The approach does not create mobile-specific tech debt that doubles cost in Q4 |
| Customer experience quality | Medium | Maya Osei | The delivered experience is good enough that enterprise prospects consider it a genuine capability, not a placeholder |

---

### 4. Options Analysis

| Option | Strengths | Risks / Trade-offs | Alignment with constraints |
|---|---|---|---|
| **A: Native iOS + Android** | Best customer experience; strongest enterprise perception; most feature-complete over time | Requires two codebases; Dana Kim estimates 4–5 months for a production-ready v1; almost certainly misses Q3 | Fails the Q3 delivery constraint and the no-new-headcount constraint; not viable without scope reduction |
| **B: Progressive Web App (PWA)** | Single codebase; ships faster (Dana Kim estimates 6–8 weeks for a solid MVP); works within SOC 2 boundary; installable on home screen on both iOS and Android | Lower initial perception than native; some enterprise IT policies restrict PWAs; offline capability requires additional engineering | Meets all constraints if scoped to core use cases (view contracts, approve, sign); recommended |
| **C: Defer to Q4** | No engineering cost in Q3; keeps Q3 sprint capacity intact | Directly risks losing two pipeline deals; CSM must manage customer expectations without a credible answer; creates a Q4 crunch | Meets budget and headcount constraints but fails the deal-impact criterion |

**Recommended option: B — PWA**
Scoped to three core use cases: view contract status, approve a contract, and add a signature. This is sufficient to answer the enterprise procurement question and can be demoed credibly by end of Q3.

**Key assumption:** If it turns out that the three enterprise prospects' IT policies explicitly block PWA installation (some corporate MDM policies restrict this), Option B loses its deal-unblocking value and Option C becomes the correct choice. James Okafor must validate this with procurement contacts before June 4.

---

### 5. Input Needed from Contributors

| Contributor | Question to answer | Input format | Input deadline |
|---|---|---|---|
| James Okafor | For each of the three pipeline deals: is mobile access a hard procurement requirement that will block signing, or a preference? And do their IT environments allow PWA installation? | Written async — email or Slack summary per deal | June 3 |
| Dana Kim | For a PWA scoped to contract view, approval, and signature only: what is the realistic delivery date, and are there any SOC 2 implications we need to address? | 30-minute sync with Ravi Suresh + written estimate | June 3 |
| Tanya Bloom | Does the Q3 engineering budget have headroom for a 6–8 week PWA build without a reforecast? | Written async — yes / no with any conditions | June 4 |

---

### 6. Decision Log Entry

- **Decision ID:** DEC-2025-031
- **Decision statement:** Decide the mobile delivery approach for Clearpath's enterprise segment by June 6, 2025, to unblock Q3 sprint planning and address three pending enterprise deals
- **Date decided:** [TO BE FILLED]
- **Approver:** Maya Osei, CPO
- **Decision made:** [TO BE FILLED — Option A / B / C]
- **Rationale:** [TO BE FILLED — 2–3 sentences]
- **Conditions or caveats:** [TO BE FILLED — e.g. "PWA scope limited to view, approve, sign; native apps remain on Q4 roadmap for consideration"]
- **Communication sent to Informed parties:** [TO BE FILLED — date and method]
- **Next decision triggered:** If Option B is chosen — decide PWA feature scope and Q4 native app roadmap commitment by June 16

---

### 7. Risk Flags

- **Driver and Approver are different people** ✅ No rubber-stamp risk — Ravi Suresh drives the process, Maya Osei makes the final call
- **Contributor count** ✅ Three Contributors is within the healthy range; Leo Morales correctly moved to Informed rather than added as a fourth sales voice
- **Missing key voice** ⚠️ If any of the three pipeline deals involves a customer with a known MDM or IT policy that restricts PWAs, their IT security contact should be informally consulted by James Okafor before June 4 — this is not a formal Contributor role but the information is decision-critical
- **Decision deadline has a concrete consequence** ✅ June 6 deadline is tied to June 9 sprint planning — the consequence of missing it is real and specific

No structural DACI risks identified. The only pre-decision dependency is James Okafor's PWA compatibility check with prospect IT teams — if this is not completed by June 4, the Approver should be notified and the decision timeline may need to extend by 48 hours.

---

## What to Notice

- The decision statement is specific enough to be falsifiable — "decide the mobile delivery approach by June 6 to unblock sprint planning" leaves no ambiguity about whether the decision has been made
- Option A is cleanly eliminated against the constraints (no new headcount, Q3 delivery) rather than left as a "possible future option" — this reduces revisiting
- The key assumption in the Options Analysis (PWA blocked by enterprise MDM policies) becomes a specific action item in the Contributors table — it does not stay as an abstract risk
- Leo Morales is moved to Informed despite being in Sales — his perspective is already represented by James Okafor, and adding him as a Contributor would add no unique input
- The Decision Log Entry is pre-filled with what is known and left with explicit placeholders for what is not — it is ready to complete in the meeting, not after
