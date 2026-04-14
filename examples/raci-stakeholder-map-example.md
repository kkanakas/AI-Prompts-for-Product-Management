# Example: RACI Stakeholder Map — Platform Re-architecture Initiative

This is a worked example of the RACI Stakeholder Map prompt (`prompts/stakeholder-management/01-raci-stakeholder-map.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I am a Product Manager leading a platform re-architecture initiative at a 300-person B2B SaaS company.

Initiative: Migrate our monolithic application to a modular service architecture to support enterprise scalability and reduce deployment risk.

Stakeholders:
- Sarah Chen — VP of Engineering
- Marcus Webb — Head of Product (my manager)
- Priya Nair — Customer Success Lead
- James Okafor — Head of Sales
- Donna Park — CTO
- Ravi Suresh — Lead Architect (engineering)
- Tanya Bloom — Head of Finance
- Leo Morales — Enterprise Account Executive (Sales)
```

## Generated Output

### RACI Matrix

| Activity | Sarah Chen (VP Eng) | Marcus Webb (Head of Product) | Priya Nair (CS Lead) | James Okafor (Head of Sales) | Donna Park (CTO) | Ravi Suresh (Lead Architect) | Tanya Bloom (Finance) | Leo Morales (AE) |
|---|---|---|---|---|---|---|---|---|
| Define technical requirements | C | C | — | — | A | R | — | — |
| Approve scope and investment | C | C | — | — | A | C | R | — |
| Build and deliver | R | I | — | — | I | R | — | — |
| Customer communication plan | C | A | R | C | I | — | — | C |
| Go-to-market / launch readiness | I | A | R | R | I | — | — | R |
| Post-launch review | C | A | R | C | I | C | C | — |

### Influence & Support Matrix

| Stakeholder | Influence Level | Support Stance | Primary Concern or Motivation |
|---|---|---|---|
| Donna Park (CTO) | High | Champion | Long-term technical scalability; board-level credibility of the platform |
| Sarah Chen (VP Eng) | High | Supporter | Engineering team capacity; deployment stability during migration |
| Marcus Webb (Head of Product) | High | Supporter | Roadmap continuity; ensuring the migration does not consume all product investment |
| Ravi Suresh (Lead Architect) | Medium | Champion | Technical correctness; avoiding shortcuts that create new debt |
| Priya Nair (CS Lead) | Medium | Neutral | Customer impact during cutover; SLA commitments to enterprise accounts |
| James Okafor (Head of Sales) | High | Skeptic | Whether this delays features the sales team has promised; deal risk during transition |
| Tanya Bloom (Finance) | Medium | Neutral | Budget predictability; understanding the investment case |
| Leo Morales (AE) | Low | Skeptic | Impact on enterprise deals currently in the pipeline; customer questions about stability |

### Engagement Strategy

| Stakeholder | Cadence | Key Message | Action to Move Skeptic / Detractor |
|---|---|---|---|
| Donna Park | Monthly steering review + async updates on major milestones | "This migration is the foundation for the enterprise scalability story we need for the next funding round." | Already a Champion — ensure she stays visible as a sponsor in cross-functional forums |
| Sarah Chen | Weekly sync | "We are sequencing this to protect sprint capacity; engineering sets the pace, not the business." | Already a Supporter — give her veto rights on sprint scope to maintain trust |
| Marcus Webb | Weekly sync | "The migration is ring-fenced; it will not crowd out roadmap commitments." | Already a Supporter — share a monthly capacity split report to keep this visible |
| Ravi Suresh | Embedded in sprint ceremonies | "Your technical judgment is the backstop — no architecture decisions get made without your input." | Already a Champion — no action needed |
| Priya Nair | Bi-weekly update + 2-week heads-up before any customer-facing cutover | "Enterprise customers will have 30 days notice before any cutover and a dedicated rollback plan." | Schedule a 1:1 to walk through the customer communication plan before it is finalised |
| James Okafor | Monthly business update | "The migration reduces deployment risk and makes us more credible in enterprise deals, not less." | Share one concrete example of a past deal where technical debt caused a sales problem; reframe migration as sales enablement |
| Tanya Bloom | Quarterly business review | "The investment is time-boxed with a clear ROI: reduced incident cost and faster feature delivery." | Send a one-page investment case before the next QBR so Finance has context before the numbers are presented |
| Leo Morales | Ad-hoc, as deals arise | "We can give enterprise prospects a technical briefing on our architecture roadmap as a trust signal." | Convert his concern into an asset — offer to join his next enterprise call to answer technical credibility questions |

### Risk Flags

- **Accountability gap:** Customer communication plan has no single Accountable owner in engineering — Priya Nair is Responsible for execution but Marcus Webb should formally own the outcome. Confirm this before the initiative kicks off.
- **High-influence detractors:** James Okafor has high influence over pipeline and is a Skeptic. If his concern about delayed features is not addressed in the first two weeks, he has the standing to escalate to the CTO and create resourcing pressure. Prioritise the 1:1 with him in week 1.
- **Missing stakeholder:** Consider adding the Head of Security or Compliance if the re-architecture touches data handling or authentication boundaries — enterprise prospects will ask.

### Executive Summary

The platform re-architecture has strong executive sponsorship in Donna Park (CTO) and solid engineering alignment with Ravi Suresh. The primary risk is James Okafor (Head of Sales), who has high influence and is currently a Skeptic — his concern is deal risk during the transition, and if left unaddressed he can surface this at leadership level. The most important relationship to invest in first is James: reframe the migration as a sales credibility asset rather than a distraction, and give him a concrete customer-facing story he can use in enterprise conversations. Secondary priority is Priya Nair — her team will manage customer impact during cutover and she needs a communication plan in her hands before she can fully move to Supporter.

## What to Notice

- Stakeholders were listed with role and team only — the prompt inferred their likely concerns and stances from context
- James Okafor's high-influence / Skeptic combination is correctly flagged as the top risk, not just noted in a table
- The engagement action for Leo Morales reframes his concern as an opportunity (join enterprise calls) rather than just trying to neutralise his resistance
- The missing stakeholder flag (Head of Security) demonstrates that the prompt is designed to find gaps, not just map what was given
