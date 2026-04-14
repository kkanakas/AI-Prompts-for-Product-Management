# Example: Kano Analysis — Project Management Tool for Ops Teams

This is a worked example of the Kano Analysis prompt (`prompts/idea-evaluation/05-kano-analysis.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I am a Product Manager evaluating a set of features for Flowdesk, a workflow automation platform for operations teams at mid-market B2B SaaS companies.

Features to evaluate:
1. Drag-and-drop workflow builder
2. AI-suggested next steps based on past workflow patterns
3. Role-based access controls (view / edit / admin)
4. Real-time collaboration (multiple users editing a workflow simultaneously)
5. Native Slack integration for task notifications
6. White-label branding for customers who resell Flowdesk to their clients
7. Exportable audit log (CSV / PDF)
8. Offline mode

Additional context:
- Primary customers are ops managers at Series B–D SaaS companies (100–1,000 employees)
- Top NPS detractor themes: "hard to control who can change what" and "I have to check Slack to know if anything moved"
- Competitor Zapier has automation breadth but no real-time collab; Make.com is similar
- Enterprise deals are being lost because procurement requires audit logs for SOC 2 evidence
```

## Generated Output

### Kano Classification Table

| Feature | Kano Category | Rationale | Customer Reaction if Present | Customer Reaction if Absent |
|---|---|---|---|---|
| Drag-and-drop workflow builder | **Basic** | Core interaction model; every competitor has it; customers assume it exists | No positive reaction — expected | Strong dissatisfaction; product feels unusable |
| Role-based access controls | **Basic** | Top NPS complaint is lack of control over who can edit; SOC 2 prospects require it | Relieved, not delighted | Active frustration; a reason to churn or not buy |
| Exportable audit log | **Basic** | Actively blocking enterprise sales per context; compliance requirement | Expected and appreciated | Deal-breaker for procurement teams |
| Native Slack integration | **Performance** | NPS feedback explicitly names Slack visibility as missing; more coverage = more satisfaction | Noticeably more satisfied as coverage improves | Moderate frustration; users resort to manual check-ins |
| Real-time collaboration | **Delighter** | No major competitor offers this well; ops teams working simultaneously is a genuine pain today | Surprise and delight — "this is exactly what we needed" | No dissatisfaction — customers don't know to expect it |
| AI-suggested next steps | **Delighter** | Unexpected capability; high potential for "wow" moments if accuracy is high | Strong positive reaction if relevant and accurate | No dissatisfaction — not on customers' radar yet |
| White-label branding | **Indifferent** | Relevant only to a small reseller segment; mainstream ops managers don't need or notice it | No reaction from primary segment | No dissatisfaction from primary segment |
| Offline mode | **Reverse** | Ops workflows are inherently collaborative and live; offline mode adds complexity without value for this segment; some users may distrust sync reliability | Neutral to slightly negative (concerns about data sync) | No dissatisfaction |

### Investment Priority Tiers

| Priority Tier | Feature(s) | Reasoning |
|---|---|---|
| **Tier 1 — Fix first** | Role-based access controls, Exportable audit log | Both are Basic gaps actively causing churn signals and blocking enterprise deals |
| **Tier 2 — Scale next** | Native Slack integration | Performance feature with direct, linear satisfaction return; every improvement is noticed |
| **Tier 3 — Differentiate** | Real-time collaboration, AI-suggested next steps | Highest potential to create memorable moments; no competitor owns this space |
| **Tier 4 — Defer or drop** | White-label branding, Offline mode | Low or negative return for the primary customer segment |

### Satisfaction Risk Assessment

| Missing Basic Feature | Customer Impact | Address By |
|---|---|---|
| Role-based access controls | High — top NPS detractor theme | Urgent — this quarter |
| Exportable audit log | High — blocking enterprise procurement | Urgent — this quarter |

### Delight Opportunity Spotlight

**Real-time collaboration**
- Why it resonates: Ops teams frequently have two or three people maintaining the same workflow — a daily standup process, an onboarding checklist, an incident response runbook. Today they take turns editing or accidentally overwrite each other. The pain is real and frequent, but no competitor has solved it well.
- Suggested MVP scope: Start with presence indicators (show who is viewing a workflow) and last-edit attribution before building simultaneous editing. This tests whether collaboration visibility alone reduces friction before investing in conflict resolution logic.
- Success signal: If users with two or more team members active on a workflow reduce their "who changed this?" support tickets by 40% and increase daily active workflow edits, it is landing as a Delighter. If only solo users adopt it, reclassify as Indifferent.

### Executive Summary

Flowdesk's feature portfolio has two urgent Basic gaps — role-based permissions and audit logs — that are actively costing deals and driving NPS detractors. These must be addressed before any Delighter investment. Once the table-stakes floor is in place, the highest-leverage opportunity is real-time collaboration: no competitor owns this, the pain is real for ops teams working in parallel, and an MVP starting with presence indicators is low-cost enough to test the hypothesis quickly. White-label branding and offline mode should be dropped from the roadmap for the primary segment — they carry real investment cost with negligible satisfaction return.

## What to Notice

- The context included verbatim NPS themes and a known sales blocker — this sharpened the Basic vs. Indifferent classifications significantly
- Offline mode was classified as Reverse, not just Indifferent — the rationale explains why presence would actively reduce trust for this segment
- The Delight Opportunity includes a deliberately small MVP scope (presence indicators before simultaneous editing) to test the hypothesis cheaply
- The summary explicitly names what to *remove* from the roadmap, not just what to build
