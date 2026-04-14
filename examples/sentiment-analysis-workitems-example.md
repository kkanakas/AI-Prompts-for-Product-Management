# Example: Sentiment Analysis in Work Items — Onboarding Squad Jira Board

This is a worked example of the Sentiment Analysis in Work Items prompt (`prompts/customer-discovery/10-sentiment-analysis-in-workitems`).

## Filled-In Prompt

```
You are a senior product intelligence analyst. I will provide you with a set of Jira issues (including titles, descriptions, comments, and metadata such as priority, labels, assignee, and status). Perform a structured sentiment analysis across these issues with the following dimensions: [full prompt template]

Here are the Jira issues:

ONBRD-214 | Priority: Critical | Status: In Progress | Label: customer-escalation
Title: New enterprise accounts failing to complete setup wizard — Meridian Logistics blocked
Description: Meridian Logistics (250-seat enterprise deal) reports that 8 of their 14 admins cannot complete step 3 of the setup wizard. Error state is silent — no message shown. They have been stuck for 3 days. CSM has escalated twice.
Comments:
  - [CSM, Day 1]: "Meridian is asking if they made a mistake purchasing. Please prioritise."
  - [Engineer, Day 2]: "Reproducing locally. Root cause is a race condition in the role assignment API call."
  - [CSM, Day 3]: "Meridian VP of Legal has now emailed our CEO directly."

ONBRD-198 | Priority: High | Status: Done | Label: ux-debt
Title: Setup wizard progress bar resets on browser refresh
Description: Users who refresh the browser mid-wizard lose their progress and return to step 1. Reported by 12 customers in the past 30 days. Workaround: don't refresh.
Comments:
  - [PM]: "This has been in the backlog for two quarters. Customers are frustrated but it's not blocking."
  - [Engineer]: "Fixed in this PR. Progress is now persisted in localStorage."
  - [QA]: "Verified on Chrome, Firefox, Safari."

ONBRD-201 | Priority: Medium | Status: To Do | Label: feature-request
Title: In-app checklist for first-time admins
Description: Multiple CSMs have requested a step-by-step checklist visible on the dashboard after account creation. Reduces support tickets and improves time-to-first-contract.
Comments:
  - [CSM A]: "Every onboarding call I do manually walks through these steps. If the product did this automatically we'd save 2 hours per customer."
  - [CSM B]: "Three customers this month asked why there's no getting-started guide inside the app."
  - [PM]: "Scoped and ready for next sprint."

ONBRD-189 | Priority: High | Status: In Progress | Label: performance
Title: Setup wizard loads in 8–12 seconds on first open for accounts with >50 users
Description: Large accounts see a significant delay on wizard load. Engineering identified a missing database index as the cause.
Comments:
  - [Engineer]: "Index added in staging. Load time drops to under 1 second."
  - [PM]: "When can this ship? We have two enterprise prospects in trial right now."
  - [Engineer]: "Ready for review. Needs QA sign-off before we push."

ONBRD-177 | Priority: Low | Status: Done | Label: copy
Title: Improve empty state messaging on the contracts list page
Description: New users land on the contracts page and see a blank table with no guidance. Updated copy now reads "Upload your first contract to get started — it takes less than 2 minutes."
Comments:
  - [Designer]: "Copy tested well in usability study. Users reported feeling less confused."
  - [PM]: "Small change, nice improvement."
```

## Generated Output

### 1. Overall Sentiment Summary

**Aggregate sentiment: Predominantly negative with isolated positive signals**
**Confidence: High**

The board is dominated by customer-facing friction in the critical onboarding path. Two high-severity issues (ONBRD-214, ONBRD-189) involve active customer impact and escalation language. One resolved item (ONBRD-198) reflects accumulated frustration that persisted across multiple quarters before resolution. Positive sentiment is present but limited to two completed items with low strategic weight.

No timestamps were available to assess sentiment shift over time, but the presence of a two-quarter-old backlog item (ONBRD-198) alongside a current Critical escalation (ONBRD-214) suggests the onboarding path has been a persistent pain area without sufficient prioritisation.

### 2. Dimension-Level Sentiment Breakdown

**Customer / user impact language**
Negative and escalating. ONBRD-214 contains explicit signals of buyer remorse ("asked if they made a mistake purchasing") and executive escalation (VP-to-CEO email). ONBRD-198 reflects 30-day recurring frustration across 12 customers. ONBRD-201 contains positive CS signals — customers are asking for something, which is engagement, not complaint.

**Engineering / team health signals**
Neutral to cautious. Engineers are identifying root causes and shipping fixes, but ONBRD-189's "when can this ship?" exchange between PM and engineer suggests timeline pressure and a slight bottleneck in QA throughput. ONBRD-198's comment ("two quarters in the backlog") signals that technical debt is acknowledged but not systematically addressed.

**Stakeholder pressure signals**
High on ONBRD-214. VP-level customer escalation reaching the CEO is the strongest pressure signal on this board. CSM language ("please prioritise," "escalated twice") indicates internal pressure is already at peak before the issue is resolved.

**Product quality signals**
Mixed. ONBRD-189 (performance) and ONBRD-214 (race condition) indicate foundational reliability gaps in the onboarding flow. ONBRD-177 and ONBRD-198 (resolved) show the team can ship quality improvements, but the pattern suggests reactive rather than proactive quality investment.

### 3. High-Signal Issues

| Issue | Dominant Sentiment | Why Flagged | Suggested Action |
|---|---|---|---|
| ONBRD-214 | Critical / Escalating | Executive-level customer escalation; buyer remorse language; 3-day block on a named enterprise account | Ship the race condition fix today and have CSM send a personal response to Meridian's VP of Legal with a resolution timeline by end of day |
| ONBRD-189 | Urgent / Pressured | Active enterprise prospects in trial are affected; fix is ready but QA sign-off is a bottleneck | Expedite QA review — this is blocking sales pipeline, not just existing customers |
| ONBRD-198 | Chronic / Relieved | Two-quarter delay on a customer-visible bug signals a prioritisation culture issue despite the fix being complete | Use this as a case study in the next sprint retro: what kept this in the backlog for six months? |

### 4. Emerging Themes

**Theme 1 — The setup wizard is a reliability liability.** Three of five issues touch the setup wizard (ONBRD-214 race condition, ONBRD-198 progress reset, ONBRD-189 load time). This is not a coincidence — it suggests the wizard was built without sufficient resilience for edge cases (large accounts, browser refresh, concurrent API calls).

**Theme 2 — CSMs are filling product gaps manually.** ONBRD-201 reveals that CSMs are running manual onboarding walkthroughs for every new customer because the product does not guide users. This is a hidden operational cost and a retention risk — CSM capacity is finite and customer satisfaction should not depend on it.

**Theme 3 — Enterprise scale exposes foundational issues.** Both ONBRD-214 (race condition with multi-admin setup) and ONBRD-189 (performance degradation for accounts >50 users) surfaced when enterprise-scale accounts tried to onboard. As the company moves upmarket, these patterns will recur unless the onboarding infrastructure is stress-tested for scale.

### 5. Positive Signal (Momentum Indicators)

- **ONBRD-198 resolution** demonstrates the team can find and fix long-standing UX debt when it is prioritised. The fix was clean (localStorage persistence) and verified across all major browsers.
- **ONBRD-177** (empty state copy) is a small but well-executed improvement — usability testing was used to validate the change before shipping, which is good process hygiene.
- **ONBRD-201 readiness** — the in-app checklist is scoped, CSM-validated, and ready for the next sprint. This is a proactive improvement, not a reactive fix.

### 6. Executive Summary

The onboarding squad's current board reflects a team under significant pressure from a named enterprise escalation (ONBRD-214) that has reached CEO visibility and carries real churn risk. Two of the five issues indicate that the setup wizard has foundational reliability gaps — a race condition and a performance issue — that are surfacing specifically as the company pursues larger accounts. The most urgent action is resolving ONBRD-214 today and personally communicating with Meridian's VP of Legal. Beyond the immediate escalation, the broader signal is that onboarding quality has been under-invested in relative to its strategic importance: CSMs are manually compensating for product gaps, a customer-visible bug sat in the backlog for two quarters, and enterprise-scale edge cases are not being caught before they reach customers.

## What to Notice

- The Jira export was plain text — the prompt works with whatever format is available, not just structured JSON
- ONBRD-214 is correctly identified as the dominant risk even though it is only one of five issues — the escalation language ("made a mistake purchasing," "VP emailed our CEO") carries disproportionate weight
- Theme 2 (CSMs filling product gaps) is an emerging pattern that is not visible in any individual ticket — it only surfaces by reading across issues
- The suggested action for ONBRD-214 is specific and time-bound ("by end of day"), not generic
- The positive signals section is not just "here's what went well" — it identifies what the team should keep doing (usability testing, proactive scoping)
