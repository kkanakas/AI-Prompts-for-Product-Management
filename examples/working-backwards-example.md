# Example: Working Backwards Plan — Automated Contract Renewal Alerts

This is a worked example of the Working Backwards Plan prompt (`prompts/strategy/03-working-backwards.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I am a Product Manager building a working backwards plan for Automated Contract Renewal Alerts in Clearpath.

What I am building:
A feature that notifies in-house legal teams 90 days, 60 days, and 30 days before a contract expires and surfaces the key renewal terms, counterparty contacts, and historical negotiation notes at each alert.

Target customer:
General Counsel or Senior Legal Counsel at mid-market companies (500–2,000 employees) managing 50–200 active contracts at any time.

The problem today:
Contract renewal dates live in spreadsheets that no one consistently updates. Legal teams discover renewals are approaching when a finance or sales colleague panics about an auto-renewal they did not want, or when a vendor relationship lapses because no one initiated the conversation in time. The result is rushed renewals negotiated from a weak position, missed opportunities to exit poor vendor relationships, and occasional legal liability from auto-renewing contracts that should have been renegotiated.

The outcome I want customers to have:
Legal teams arrive at every renewal conversation prepared — with enough lead time to negotiate, exit, or escalate — and never miss a renewal window because of a process failure.

Key constraints:
Must ship in 6 weeks; no changes to the core data model; available on Professional and Enterprise plans only; email and in-app notifications only in v1 (no Slack or Teams integration).
```

## Generated Output

---

### 1. Internal Press Release

**Clearpath Gives Legal Teams Their Renewal Calendar Back**

**In-house legal teams at mid-market companies can now see every contract renewal coming 90 days out — with everything they need to act already in front of them.**

For most in-house legal teams, contract renewals sneak up on them. A vendor's auto-renewal clause fires quietly while the General Counsel is buried in other work. A supplier relationship that should have been renegotiated gets locked in for another year because no one flagged the window in time. It is not a capability problem — it is a visibility problem. Contracts and their renewal dates live in spreadsheets, email threads, and shared drives that no one is responsible for watching.

Today, General Counsel and their teams spend hours each quarter manually checking contract dates, chasing down counterparty contacts, and reconstructing negotiation history from scattered emails. The cost is not just time — it is the compounding disadvantage of arriving at every renewal without preparation, or worse, missing the window entirely. One missed auto-renewal on a five-year SaaS contract can cost six figures and six months of frustration.

Clearpath now sends legal teams a renewal alert 90, 60, and 30 days before every contract expiry — and each alert includes the renewal terms, counterparty contacts, and the notes from the last negotiation, already surfaced and ready to act on. Legal teams can see what is coming, decide what to do about it, and start the conversation with the leverage that lead time provides. Renewals no longer happen to them — they happen on their terms.

> "I used to find out about renewals when someone in Finance forwarded me an auto-renewal invoice and asked why we were locked in again. Now I get an alert 90 days out with everything I need already there. Last month I renegotiated a vendor contract down 20% because I had time to get competitive quotes. That's the difference." — General Counsel, Series C SaaS company, 800 employees

Log in to Clearpath and confirm your contract dates are current — your renewal calendar is already running.

---

### 2. Frequently Asked Questions

**Customer FAQs**

*What does this actually do for me?*
Clearpath monitors every contract in your account and sends you an alert at 90, 60, and 30 days before each expiry. Each alert includes the renewal or auto-renewal terms from the contract, the counterparty's primary contact, and any notes you have saved against that contract. You do not need to configure anything — it reads from the contract data already in Clearpath.

*How is this different from what I do today?*
Most teams today maintain a separate spreadsheet or calendar reminders that require manual upkeep. Clearpath's alerts are automatic — they update when contract dates change, they include the relevant context alongside the reminder, and they fire reliably even when no one is actively checking the spreadsheet.

*What do I need to do to get started?*
Nothing, if your contracts are already in Clearpath with their expiry dates populated. If you have contracts without dates, the new Contracts Health dashboard shows you which ones are missing key fields — you can bulk-update them in under 10 minutes.

*What happens to my existing contracts and data?*
Nothing changes. The feature reads your existing contract data — it does not move or modify anything. Alerts are additive; your current workflow is unaffected.

*Is this available on my plan?*
Renewal alerts are available on Professional and Enterprise plans. Starter plan customers will see the feature but alerts will not fire — upgrade from the Settings page.

---

**Internal / Stakeholder FAQs**

*Why are we building this now?*
It is the third most-requested feature in our support queue, it appeared in 7 of the last 12 customer discovery interviews, and two enterprise deals cited "no renewal visibility" as a reason for delayed signing. It also directly reduces the most common churn trigger — customers who leave because they missed a renewal and blame Clearpath for not flagging it.

*Who is this for and how many customers does this affect?*
All Professional and Enterprise accounts — approximately 340 accounts covering around 2,800 active contracts in the system today. Every account with at least one contract with a populated expiry date will receive alerts automatically.

*How will we measure success?*
Primary metric: % of contracts in Clearpath with a renewal action taken (view, note added, or contact initiated) before expiry — target 60% within 90 days of launch, up from an estimated 18% today. Secondary metric: reduction in "missed renewal" support tickets, which currently average 14 per month.

*What are we NOT building in this version, and why?*
Slack and Teams notifications, custom alert timing, delegation to colleagues, and bulk snooze are all out of scope for v1. These are valuable but add significant complexity; v1 validates the core behaviour (do customers act on alerts?) before we invest in delivery preferences.

*What is the risk if we get this wrong?*
If alerts fire incorrectly — wrong dates, wrong contracts, or excessive volume — we erode trust in Clearpath as a system of record, which is the core value proposition. Alert accuracy is non-negotiable; we will add a QA gate on date parsing before launch.

---

**Sceptic FAQs**

*Why hasn't this been built before?*
It has been on the backlog for 18 months, consistently deprioritised in favour of core contract workflow features. The data to support it (contract dates, counterparty contacts) was not reliably populated in earlier cohorts. With the data quality improvements from Q1, it is now viable for the majority of active accounts.

*What will customers do if this doesn't work as promised?*
If alerts are late, missing, or fire for the wrong contracts, customers will revert to their existing spreadsheet process and lose confidence in Clearpath as a reliable system. We will monitor alert delivery rates in the first two weeks and have a rollback mechanism ready if error rates exceed 2%.

*How confident are we that customers actually want this?*
High confidence on the problem; moderate confidence on this specific solution. Seven discovery interviews confirmed the renewal visibility problem is real and frequent. We have not yet tested the alert format or timing with customers — that is the first thing we will validate with a beta group of 10 accounts before general release.

*What assumption is this entire plan built on, and how do we know it is true?*
The plan assumes that customers will act on alerts when they receive them — that the barrier is visibility, not capacity or willingness. If customers receive alerts and still fail to act, the problem is different (workload, ownership, or tooling) and alerts alone will not solve it. We will know within 30 days of launch whether alert open rates and downstream actions support this assumption.

---

### 3. Customer Value Statement

**"We help General Counsel at mid-market companies who are managing 50+ contracts with no reliable renewal calendar to arrive at every renewal conversation prepared and on time — by automatically surfacing renewal dates, terms, and context 90 days in advance — unlike spreadsheets and calendar reminders which require manual upkeep and carry no contract context."**

| Dimension | Score | Notes |
|---|---|---|
| Specificity | 5 | Names the role, company size, and exact situation (50+ contracts, no calendar) |
| Differentiation | 4 | Clearly contrasts with spreadsheets; could be sharper on the "context" advantage |
| Outcome clarity | 4 | "Prepared and on time" is tangible; could add a time or financial dimension |

All dimensions score 4 or above — statement is production-ready.

---

### 4. Working Backwards Checklist

| Question | Answer | Confidence |
|---|---|---|
| Can we describe the customer problem in one sentence without mentioning our product? | "Legal teams miss contract renewal windows because expiry dates live in spreadsheets no one reliably checks" | High |
| Have we talked to at least 5 customers who have this problem? | Yes — 7 discovery interviews confirmed this pattern | High |
| Do we know what customers do today to solve this? | Yes — spreadsheets, calendar reminders, and relying on vendor notices | High |
| Do we know what "good" looks like to the customer — not to us? | Yes — "enough lead time to negotiate, exit, or escalate from a position of preparation" | High |
| Have we written down what we are NOT building in v1? | Yes — no Slack/Teams, no custom timing, no delegation, no bulk snooze | High |
| Do we know the single metric that will tell us this worked? | Yes — % of contracts with a renewal action taken before expiry | High |
| Is there a named customer who would be disappointed if we cancelled this? | Yes — Meridian Logistics and two other enterprise accounts have specifically requested this | High |

No low-confidence flags. Ready to proceed to build.

---

### 5. Success Metric

| Metric type | Metric | Baseline | Target | Timeframe |
|---|---|---|---|---|
| Customer outcome metric | % of contracts with a renewal action taken before expiry | ~18% (estimated from support data) | 60% | 90 days post-launch |
| Business consequence metric | Monthly "missed renewal" support tickets | 14/month average | Under 5/month | 90 days post-launch |
| Leading indicator (weeks 1–2) | Alert open rate (email + in-app combined) | N/A (new feature) | >55% open rate | 14 days post-launch |

---

## What to Notice

- The press release is written in the past tense as if the feature already exists — this forces specificity about what the customer actually experiences, not what will be built
- The customer quote names a role, company type, and a specific outcome (20% cost reduction from competitive quotes) — generic quotes like "this saves me time" are a signal that customer value is not yet well understood
- The sceptic FAQ surfaces the core assumption explicitly ("customers will act on alerts when they receive them") and names a 30-day test to validate it — this turns a hidden bet into a tracked hypothesis
- The Working Backwards Checklist has all High confidence ratings here, but in practice several of these would be Medium or Low in an early-stage feature — those gaps should be resolved before development begins, not after
- The customer outcome metric ("% of contracts with a renewal action taken") measures a change in customer behaviour, not product engagement — page views or alert sends would be the wrong metric here
