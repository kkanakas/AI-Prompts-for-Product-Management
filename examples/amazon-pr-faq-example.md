# Example: Amazon PR/FAQ — Clearpath Renewal Alerts

This is a worked example of the Amazon PR/FAQ prompt (`prompts/strategy/04-amazon-pr-faq.md`).

## Filled-In Prompt

```
Feature: Clearpath Renewal Alerts

What I am building:
A feature that automatically notifies in-house legal teams 90, 60, and 30 days before a contract expires, with the renewal terms, counterparty contacts, and prior negotiation notes surfaced in each alert.

Target customer:
General Counsel or Senior Legal Counsel at a mid-market SaaS company (500–2,000 employees) managing 50–150 active vendor contracts with no dedicated contract operations team.

The problem:
Contract renewal dates live in a spreadsheet that gets updated inconsistently. Legal teams find out a renewal is approaching when Finance forwards an auto-renewal invoice they did not want, or when a vendor relationship lapses because nobody initiated the conversation in time. By then, the negotiation window is closed and the team is locked into another term from a weak position.

The solution:
Legal teams receive a renewal alert 90, 60, and 30 days before each contract expiry. Each alert includes the renewal clause from the contract, the counterparty's primary contact, and any notes saved against that contract in Clearpath. No setup required — it runs automatically on contracts already in the system.

Key differentiators:
Unlike a calendar reminder, each alert includes the contract context needed to act. Unlike enterprise CLMs, there is no implementation project — it works from the data already in Clearpath. Unlike a spreadsheet, it does not require anyone to remember to check it.

Constraints:
Email and in-app notifications only in v1; no Slack or Teams integration. Available on Professional and Enterprise plans. Must ship within 6 weeks. No changes to the core data model.
```

## Generated Output

---

## PRESS RELEASE

**San Francisco, CA — May 12, 2025 —**

### Headline
Legal teams can now see every contract renewal coming 90 days out — with the renewal terms and counterparty contacts already in front of them.

### Subheadline
Clearpath Renewal Alerts eliminates the spreadsheet-and-panic cycle that causes in-house legal teams to miss renewal windows and negotiate from a position of no preparation.

### Opening Paragraph — The World Before
For General Counsel at growing companies, contract renewals are a managed anxiety. Fifty, eighty, a hundred vendor contracts sit in a shared drive, each with a renewal date that someone was supposed to add to a spreadsheet. Some were. Most were not updated when they changed. The legal team finds out a renewal is in three weeks when Finance forwards an invoice they did not want, or when a vendor opens a renewal conversation with a proposed 30% price increase and a two-week deadline to respond.

### Problem Paragraph — The Real Cost
The cost is not just the missed window. It is the negotiating disadvantage that comes from discovering a renewal under time pressure. Legal teams that find out 90 days out get competitive quotes, push back on terms, and exit relationships that are no longer working. Legal teams that find out three weeks out auto-renew or accept whatever the vendor proposes. Across a portfolio of 80 contracts, the difference between proactive and reactive renewal management is measured in hundreds of thousands of dollars and months of locked-in obligations that should have been renegotiated or exited.

### Solution Paragraph — The New Reality
Clearpath now monitors every contract in the system and sends renewal alerts at 90, 60, and 30 days before each expiry. Each alert arrives with the renewal clause from the contract, the counterparty's primary contact, and the notes from the last negotiation — everything needed to act, already there. Legal teams open the alert, see what is coming, and decide what to do about it with time to do it well. For the first time, renewal conversations start on the legal team's schedule, not the vendor's.

### Getting Started
Legal teams on Professional and Enterprise plans are already enrolled — if your contracts have expiry dates in Clearpath, your renewal calendar is already running.

### Customer Quote
> "We had an auto-renewal fire at least once a quarter — someone would find an invoice for a tool we hadn't used in a year and I'd have to explain why we were locked in again. I got my first 90-day alert two weeks ago for a contract I had completely forgotten about. I've already started a conversation with three other vendors and I know exactly what I want to renegotiate. This is what it should have looked like all along."
>
> — **General Counsel, Series C SaaS company, 900 employees**

### Company Quote
> "Contract renewals are one of the highest-leverage moments a legal team has — and most teams have been flying blind on timing for years. Renewal Alerts is the feature we hear about most from customers who join Clearpath from spreadsheets. Getting them that lead time, with the context they need to act, is the whole point."
>
> — **Head of Product, Clearpath**

### Boilerplate
Clearpath is a contract management platform built for in-house legal teams at mid-market companies, replacing email threads and shared drives with a single system of record that deploys in a day.

### Contact
press@clearpath.io

---

## FAQ

### External FAQ — Questions customers will ask

**What contracts does this work for?**
Any contract in Clearpath with an expiry date populated. Renewal Alerts reads from your existing contract data — there is nothing to configure. If you have contracts without expiry dates, the Contracts Health dashboard shows you which ones are missing key fields so you can fill them in.

**What does each alert actually contain?**
The alert includes: the contract name and expiry date, the renewal or auto-renewal clause extracted from the contract, the counterparty's primary contact as saved in Clearpath, and any notes you or your team have added to the contract. In v1 it is delivered by email and in-app notification.

**Can I customise when alerts are sent?**
Not in v1. Alerts fire at 90, 60, and 30 days before expiry for all contracts. Custom timing and per-contract configuration are on the roadmap based on demand from the beta.

**What if a contract does not have an expiry date?**
No alert fires. The Contracts Health dashboard flags contracts with missing expiry dates so you can address them. We estimate that contracts without expiry dates account for about 12% of contracts in the average Clearpath account.

**Will this work for contracts that auto-renew unless cancelled?**
Yes. If the auto-renewal clause is in the contract text, it is surfaced in the alert. The 90-day alert is specifically designed to give legal teams enough lead time to exercise cancellation rights under most standard auto-renewal notice periods.

**Is this available on my plan?**
Renewal Alerts is available on Professional and Enterprise plans. Starter plan customers can see the feature but alerts will not fire. You can upgrade from the Settings page.

**What about data privacy — who can see my contract renewal alerts?**
Alerts are sent only to users who have view access to the relevant contract in Clearpath. Your existing permission settings control who receives which alerts. No contract data leaves Clearpath in the alert — the email contains a summary and a link back to the contract in the platform.

**What if I get an alert for a contract I have already renewed or terminated?**
Mark the contract as renewed or terminated in Clearpath and the alerts stop immediately. We are adding a one-click snooze and status update directly from the alert email in the next release.

**Can I delegate alerts to a paralegal or contract manager?**
Not in v1. Alerts go to the contract owner as set in Clearpath. Delegation and team-wide alert routing are planned for a future release.

**Does this replace our renewal spreadsheet?**
It replaces the need to check it. Your spreadsheet will still exist — but if your contracts are in Clearpath with expiry dates, Clearpath is now the thing that watches those dates so you do not have to.

---

### Internal FAQ — Questions leadership, engineering, finance, and legal will ask

**Why now? Why wasn't this built sooner?**
It has been the third most-requested feature for 18 months, consistently deprioritised behind core contract workflow features. Two blockers held it back: contract data quality (expiry dates were not reliably populated in earlier cohorts) and alert infrastructure (we did not have a reliable scheduled notification system). Both are resolved. With 340 Professional and Enterprise accounts and a median of 8 contracts per account with populated expiry dates, the feature is now viable and valuable for the majority of our paid base.

**Who specifically is this for and how many customers does it affect?**
All Professional and Enterprise accounts — approximately 340 accounts today. Within those accounts, any contract with a populated expiry date triggers alerts automatically. Based on current data, that covers roughly 2,800 contracts across the active paid base. Every account will see at least one alert in the first 90 days.

**How does this fit our company strategy?**
Our core value proposition is that Clearpath replaces the email-and-shared-drive patchwork for in-house legal teams. Renewal Alerts is the first feature that proactively surfaces value rather than waiting for the user to act. It moves Clearpath from a storage and workflow tool to an active system that protects customers from process failures. That is the direction we need to go to justify Enterprise pricing and expand NRR.

**What does success look like and how will we measure it?**
Primary metric: % of contracts in Clearpath with a renewal action taken (note added, contact initiated, or status updated) before expiry — target 60% within 90 days of launch, up from an estimated 18% today. Secondary metric: "missed renewal" support tickets, currently averaging 14 per month — target under 5 within 90 days. Leading indicator: alert open rate above 55% in the first two weeks.

**What are we explicitly not building in v1, and why?**
Slack and Teams notifications, custom alert timing, delegation to colleagues, bulk snooze, and calendar integrations are all out of scope. Each adds meaningful complexity and none is required to validate the core hypothesis: that customers will act on renewal alerts when given enough lead time. We will add the most-requested delivery preferences in v2 once we confirm the behaviour change.

**What is the cost to build and maintain?**
Three engineers for 6 weeks. Ongoing infrastructure cost is estimated at under $200/month at current contract volumes. The scheduled notification system built for this feature will be reused for obligation reminders and milestone alerts, making the per-feature cost of future notification features significantly lower.

**What are the top three risks?**
1. Alert accuracy — if alerts fire for the wrong contracts or with incorrect dates, we erode trust in Clearpath as a system of record. Mitigation: QA gate on date parsing across a sample of 500 contracts before launch; rollback mechanism ready if error rate exceeds 2%.
2. Low-quality contract data — alerts are only as good as the data in the system. Mitigation: Contracts Health dashboard prominently surfaces missing expiry dates before launch.
3. Alert fatigue — if customers have many contracts, alert volume may feel overwhelming. Mitigation: Starting with 90/60/30 day cadence; monitoring unsubscribe rates in the first month.

**What happens if we are wrong about the core assumption?**
The core assumption is that customers fail to act on renewals because they lack visibility — not because they lack capacity or ownership. If customers receive alerts and still do not act (alert open rate high but action rate low), the problem is different: workload, unclear ownership within the legal team, or tooling gaps downstream. In that case, alerts are necessary but not sufficient, and the follow-on investment would be in delegation and workflow features, not notification improvements. We will know within 30 days of launch.

**What would make us kill this mid-build?**
If the Contracts Health dashboard reveals that fewer than 30% of active contracts have populated expiry dates, the feature will generate too few alerts to create habit change and the value proposition collapses. We are running the data audit in week 1 of the build. If we hit that threshold, we pause and invest in data quality tooling first.

**What does the competitive landscape look like and how long do we have?**
Ironclad and ContractPodAi both have renewal notification features in their enterprise products. Juro does not at mid-market price points. Our window is 12–18 months before Juro ships something comparable at our price tier. The feature itself is not a long-term differentiator — it is table stakes we need to close before it becomes a reason customers choose Juro over us.

---

## PR/FAQ Readiness Score

| Dimension | Score | Notes |
|---|---|---|
| Customer specificity | 5 | Opening paragraph names the role, company stage, contract volume, and the exact moment they discover a problem ("Finance forwards an invoice") — a GC will read this and think "that's me" |
| Problem clarity | 5 | Problem paragraph quantifies the cost in negotiating position and financial terms ("hundreds of thousands of dollars") rather than describing it abstractly |
| Solution honesty | 4 | Solution paragraph describes the customer experience clearly; docked one point because "already there" in the final sentence risks sounding like marketing copy — consider "ready to act on" |
| FAQ completeness | 5 | Both External and Internal FAQs include the hard questions (data quality threshold that would kill the build, core assumption failure mode) answered directly |
| Press release discipline | 4 | Fits on one page; no superlatives or jargon; docked one point because the Company Quote edges toward mission-statement language — "the whole point" is colloquial but borderline |

**Overall readiness: 4.6 / 5 — ready for review meeting with two minor revisions noted above.**

---

## What to Notice

- The headline names the customer benefit ("see every contract renewal coming 90 days out") not the feature name ("Clearpath Renewal Alerts") — the test is whether a customer who has never heard of the product understands the value from the headline alone
- The customer quote names a specific, concrete outcome ("auto-renewal fire at least once a quarter") and a specific new behaviour ("I've already started a conversation with three other vendors") — generic quotes signal that the PM does not yet know the customer well enough
- The Internal FAQ includes the kill condition explicitly ("if fewer than 30% of active contracts have populated expiry dates, we pause") — this turns a hidden assumption into a tracked decision gate
- The competitive landscape answer is honest about the window ("12–18 months before Juro ships something comparable") and frames the feature as table stakes to close, not a lasting moat — this kind of honesty in a PR/FAQ builds more trust than confident-sounding overstatement
- The Readiness Score catches two specific sentences that drag down otherwise strong sections — it does not just give a number, it identifies exactly what to fix
