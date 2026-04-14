# Example: Capability Gap Analysis — B2B Contract Management Platform

This is a worked example of the Capability Gap Analysis prompt (`prompts/competitive-analysis/04-capability-gap-analysis.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I am a Product Manager for Clearpath, a contract management platform for in-house legal teams serving mid-market companies (500–5,000 employees).

Our current capabilities:
- Drag-and-drop contract builder with clause library
- E-signature via DocuSign integration
- Contract status dashboard
- Basic search across stored contracts
- Slack notifications for contract milestones
- PDF export

Customer needs and expectations:
- Role-based permissions (Sales can view but not edit; Legal can approve)
- Automated reminders for renewal dates and obligations
- Redlining and tracked changes inside the platform (currently done in Word)
- API access for CRM integration (Salesforce, HubSpot)
- Audit log for compliance evidence
- AI-assisted risk flagging in contract language
- Mobile app for approvals on the go

Competitors to benchmark against:
- Competitor 1: Ironclad — ironclad.com
- Competitor 2: Juro — juro.com
- Competitor 3: ContractPodAi — contractpodai.com
```

## Generated Output

### Capability Inventory Table

| Capability Area | We Have It | Customers Need It | Ironclad | Juro | ContractPodAi | Gap Type |
|---|---|---|---|---|---|---|
| Contract builder | ✅ | ✅ | ✅ | ✅ | ✅ | Parity |
| E-signature | ✅ | ✅ | ✅ | ✅ | ✅ | Parity |
| Role-based permissions | ❌ | ✅ | ✅ | ✅ | ✅ | **Critical** |
| Renewal & obligation reminders | ❌ | ✅ | ✅ | ✅ | ✅ | **Critical** |
| In-platform redlining | ❌ | ✅ | ✅ | ✅ | ✅ | **Critical** |
| CRM API integration | ❌ | ✅ | ✅ | Partial | ✅ | **Critical** |
| Audit log | ❌ | ✅ | ✅ | ✅ | ✅ | **Critical** |
| AI risk flagging | ❌ | ✅ | ✅ | ❌ | ✅ | **Opportunity** |
| Mobile approvals | ❌ | ✅ | ❌ | ❌ | ❌ | **Opportunity** |
| Contract status dashboard | ✅ | ✅ | ✅ | ✅ | ✅ | Parity |
| Slack notifications | ✅ | ✅ | ✅ | ✅ | Partial | **Differentiator** |
| Advanced analytics | ❌ | Partial | ✅ | ❌ | ✅ | Indifferent |

### Gap Prioritization Matrix

| Gap | Customer Impact | Competitive Urgency | Estimated Effort | Priority |
|---|---|---|---|---|
| Role-based permissions | High | High | Medium | **1 — Ship this quarter** |
| Audit log | High | High | Low | **2 — Ship this quarter** |
| Renewal & obligation reminders | High | High | Medium | **3 — Ship this quarter** |
| In-platform redlining | High | High | High | **4 — Next quarter** |
| CRM API integration | High | Medium | High | **5 — Next quarter** |
| AI risk flagging | Medium | Medium | High | **6 — H2 strategic bet** |
| Mobile approvals | Medium | Low | Medium | **7 — Backlog** |

### Differentiator Risk Assessment

| Differentiator | Defensibility | Recommended Action |
|---|---|---|
| Slack-native notifications | Replicable within 6 months | Extend — build deeper Slack workflow actions (approve in-thread, comment inline) before competitors copy the basic integration |

### Strategic Recommendations

1. **Close the compliance and permissions gap first.** Role-based permissions and audit log are blocking enterprise sales conversations — these are table-stakes for legal teams at 500+ employee companies and both competitors already have them.
2. **Leapfrog on mobile approvals.** No major competitor has a polished mobile approval experience. Building this now — before it becomes table-stakes — creates a Delighter that is hard to replicate quickly.
3. **Deprioritize advanced analytics.** Customers are not requesting it and only one competitor emphasises it. The investment is better directed at closing Critical gaps.

### Executive Summary

Clearpath has strong foundational capabilities but is missing five features that enterprise legal teams treat as non-negotiable: permissions, audit logs, reminders, redlining, and CRM integration. All five are already available in our top three competitors, making these Critical gaps that are actively costing deals. The highest-leverage investments this quarter are role-based permissions and audit log — both are relatively low effort and unblock compliance-sensitive buyers. Mobile approvals represent an untapped Opportunity: no competitor owns this space well, and a clean mobile experience would be a genuine differentiator for contract approvals in the field.

## What to Notice

- Current capabilities were listed honestly — including things that are just "good enough" (Parity)
- Customer needs came from real signals (sales blockers, feature requests) rather than guesses
- The Gap Type taxonomy separates "behind competitors" (Critical) from "whitespace" (Opportunity) — two very different strategic situations
- The differentiator analysis flags that even existing advantages need active investment to stay defensible
- Strategic recommendations include what to *stop* building, not just what to build next
