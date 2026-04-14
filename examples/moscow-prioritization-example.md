# Example: MoSCoW Prioritization — Enterprise Readiness Sprint

This is a worked example of the MoSCoW Prioritization prompt (`prompts/idea-evaluation/06-moscow-prioritization.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor facilitating a prioritization session. I am a Product Manager for Flowdesk, a workflow automation platform for operations teams.

Initiative: Enterprise Readiness Sprint — preparing Flowdesk for a $240K ARR enterprise deal that requires specific security and admin capabilities before procurement sign-off.

Capabilities to prioritize:
1. Role-based access controls (view / edit / admin)
2. SSO via SAML 2.0
3. Exportable audit log (CSV and PDF)
4. Custom contract terms and DPA agreement
5. Dedicated customer success manager assignment
6. Advanced workflow analytics dashboard
7. Bulk user import via CSV
8. In-app onboarding checklist for new admins
9. API rate limiting controls for enterprise tier
10. White-label email notifications

Context:
- Goal: Close the $240K ARR deal with Meridian Logistics by June 30
- Constraints: 8-week window, team of 3 engineers and 1 designer
- Customer signals: Meridian's security review requires RBAC, SSO, and audit log as hard requirements; bulk user import was flagged as "would be nice"
- Business constraints: Legal must countersign custom contract terms before any enterprise deal — this is a procurement dependency, not a product build
```

## Generated Output

### MoSCoW Classification

| Capability | MoSCoW Category | Rationale | Risk if Excluded |
|---|---|---|---|
| Role-based access controls | **Must Have** | Meridian's security review listed this as a hard requirement — deal cannot close without it | Deal lost |
| SSO via SAML 2.0 | **Must Have** | Hard requirement from Meridian's IT security policy | Deal lost |
| Exportable audit log | **Must Have** | Hard requirement for compliance evidence; also required for SOC 2 alignment | Deal lost |
| Custom contract terms and DPA | **Must Have** | Legal dependency — procurement cannot countersign without it; no product build required, escalate to legal team this week | Deal blocked at procurement stage |
| Bulk user import via CSV | **Should Have** | Flagged by Meridian as "would be nice"; reduces onboarding friction for their 300-person org | Onboarding friction but deal not blocked |
| In-app admin onboarding checklist | **Should Have** | Reduces time-to-value for enterprise admins; prevents support tickets during rollout | Higher support burden post-launch |
| API rate limiting controls | **Could Have** | Enterprise-grade feature but not in Meridian's stated requirements; low immediate impact | No impact on this deal |
| Advanced workflow analytics | **Could Have** | Useful long-term but not a procurement requirement; can be delivered post-launch | No impact on this deal |
| White-label email notifications | **Could Have** | Low customer demand; only relevant if Meridian resells Flowdesk internally | No impact |
| Dedicated CSM assignment | **Won't Have (this sprint)** | Operational, not product; handled by Customer Success team outside sprint scope | Address via CS team in parallel |

### Scope Health Check

**Must Have load: 4 of 10 items (40%) — within healthy range.**

One flag: Custom contract terms is a legal process dependency, not an engineering task. It should be escalated to the legal team in week 1, tracked separately, and removed from the engineering sprint board to avoid confusing sprint capacity.

**Should Have candidate for promotion:** Bulk user import may need to move to Must Have if Meridian confirms that onboarding 300 users manually would delay their internal rollout past June 30 — confirm with their IT lead before sprint planning.

**Won't Have items worth tracking for future releases:** Advanced analytics and API rate limiting are high-value for the broader enterprise segment — add to the enterprise roadmap backlog with a Q4 target.

### Recommended Delivery Phasing

| Phase | Scope | Target |
|---|---|---|
| **Phase 1 — Launch-ready** | RBAC, SSO, Audit log | Week 6 (hard deadline for Meridian security review) |
| **Phase 2 — Fast follow** | Bulk user import, Admin onboarding checklist | Week 8 (before go-live with Meridian) |
| **Phase 3 — Future backlog** | API rate limiting, Advanced analytics, White-label notifications | Q4 enterprise roadmap |

### Team Alignment Talking Points

- **Role-based access controls:** Meridian's IT security team will not approve the platform without this — it is the single hardest blocker between us and closing the deal.
- **SSO via SAML 2.0:** Enterprise procurement requires SSO as a baseline; without it, Meridian cannot onboard their 300 users under their IT policy.
- **Exportable audit log:** Meridian's legal team needs this for SOC 2 compliance evidence — it is a contractual requirement, not a preference.
- **Custom contract terms and DPA:** This does not require engineering — it needs our legal team to countersign. If this is not in motion by week 1, it will block the deal regardless of what we ship.

### Executive Summary

This sprint has a clear and tight Must Have scope: RBAC, SSO, and audit log are hard requirements from Meridian's security review, and without all three the $240K ARR deal cannot close. Custom contract terms need to be escalated to legal immediately — this is a procurement dependency, not a product task, and if it slips it will block the deal regardless of engineering progress. The biggest prioritization risk is bulk user import: currently a Should Have, it could become a Must Have if Meridian confirms manual onboarding would delay their internal go-live past June 30. Confirm with their IT lead before sprint planning.

## What to Notice

- The goal was a specific deal with a hard deadline — this produced very different MoSCoW outputs than a general roadmap prioritization would
- Custom contract terms was classified as Must Have but identified as a non-engineering task — the prompt correctly separates what needs to be *done* from what needs to be *built*
- The Should Have promotion flag on bulk user import demonstrates the Scope Health Check catching a dependency that the raw classification missed
- Team alignment talking points are written in plain language with the "why" grounded in the specific deal, not generic product principles
