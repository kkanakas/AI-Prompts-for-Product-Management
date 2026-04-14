# Example: Team OKR Generator — Growth & Activation Team

This is a worked example of the Team OKR Generator prompt (`prompts/strategy/02-team-okr-generator.md`).

## Filled-In Prompt

```
You are a senior OKR coach and product strategy advisor. I am a Product Management leader building team OKRs that cascade from our company-level OKRs.

Company OKRs (Q3 2025):
O1: Become the go-to contract management platform for mid-market companies
  KR1: Grow ARR from $6M to $9M
  KR2: Sign 25 new mid-market contracts (500–2,000 employees)
  KR3: Achieve Net Revenue Retention of 110%

O2: Prove the product can sell and activate itself
  KR1: Increase trial-to-paid conversion rate from 14% to 25%
  KR2: Reduce time-to-first-contract (new accounts) from 5 days to under 2 hours
  KR3: Achieve CSAT score of 4.5+ from new customers in their first 30 days

Team context:
- Team name: Growth & Activation
- What the team owns: Trial experience, in-app onboarding, activation flow, and the free-to-paid conversion funnel
- Team size: 1 PM, 3 engineers, 1 designer, 1 data analyst
- Current quarter: Q3 2025 (July 1 – September 30)
- Initiatives already planned: Redesigning the setup wizard, adding in-app checklist for new admins, A/B testing the upgrade prompt
- Key constraints: Data pipeline owned by Platform team; one engineer on parental leave from August 15
- Baseline metrics:
    - Trial-to-paid conversion: 14%
    - Time-to-first-contract: 5 days (120 hours)
    - Onboarding CSAT: 3.8 / 5.0
    - % of trial users completing setup wizard: 31%
    - Activation rate (uploaded first contract within 7 days): 38%
```

## Generated Output

### OKR Cascade Map

| Company Objective | Team's Area of Influence | Team Lever | Measurable Signal |
|---|---|---|---|
| O1 KR1: Grow ARR to $9M | Trial-to-paid conversion is the primary funnel lever for new ARR | Improve activation rate and reduce time-to-value so more trials convert | Trial-to-paid conversion rate |
| O1 KR3: NRR of 110% | Early activation predicts retention — users who upload a contract in week 1 churn at 3x lower rate | Ensure every new paid customer activates within 24 hours of account creation | Activation rate (first contract uploaded within 7 days) for new paid accounts |
| O2 KR1: Trial-to-paid conversion 25% | Directly owned by this team | Redesign setup wizard to reduce friction; A/B test upgrade prompts at the moment of value | Trial-to-paid conversion rate |
| O2 KR2: Time-to-first-contract under 2 hours | Owned by this team via onboarding flow | In-app checklist guides admins through setup; remove mandatory steps that can happen post-activation | Median time from account creation to first contract uploaded |
| O2 KR3: CSAT 4.5+ in first 30 days | Onboarding experience is the primary driver of early CSAT | Redesigned wizard + in-app checklist + proactive in-app tips reduce confusion and support tickets | 30-day onboarding CSAT score |

### Recommended Team OKRs

---

**Objective 1: Accelerate free-to-paid conversion by making the path to first value unmistakable**

*Connects to company Objective 2 (prove the product can sell and activate itself) and Objective 1 KR1 (ARR growth)*

- KR1: Increase trial-to-paid conversion rate from 14% to 22% by September 30
- KR2: Increase % of trial users completing the setup wizard from 31% to 55% by September 30
- KR3: Reduce median time-to-first-contract from 5 days to 8 hours by September 30

*Why this matters: Trial conversion is the highest-leverage input to ARR growth for a product-led company. A 1pt improvement in conversion at our current trial volume is worth approximately $180K ARR.*

---

**Objective 2: Make the first 30 days feel effortless for every new customer**

*Connects to company Objective 2 KR3 (CSAT) and Objective 1 KR3 (NRR)*

- KR1: Increase 30-day onboarding CSAT from 3.8 to 4.4 by September 30
- KR2: Increase activation rate (first contract uploaded within 7 days) from 38% to 60% for new paid accounts by September 30
- KR3: Reduce "how do I get started?" support tickets in first 14 days by 40% (from current 220/month to 132/month) by September 30

*Why this matters: Customers who activate in week 1 retain at 3x the rate of those who don't. Improving early activation is the most efficient lever we have for NRR.*

---

### OKR Health Check

| KR | Issue | Suggested Fix |
|---|---|---|
| O1 KR3: Reduce time-to-first-contract to 8 hours | Target is more aggressive than the company KR (2 hours). Confirm this is intentional — if it is a stepping-stone target, document that the team expects to hit 2 hours by Q4, not Q3. | Clarify whether 8 hours is a Q3 milestone or the final target, and align with company KR language |

All other Key Results pass the health check — each has a numeric baseline, a specific target, a date, and measures an outcome rather than an activity.

### Leading Indicators Dashboard

| Objective | Leading Indicator | Check-in cadence | Green signal |
|---|---|---|---|
| O1 — Free-to-paid conversion | % of trial users reaching step 3 of the redesigned setup wizard | Weekly (from week 2 post-launch) | >45% of new trials reaching step 3 by week 3 |
| O1 — Free-to-paid conversion | A/B test lift on upgrade prompt click-through rate | Weekly | Variant outperforming control by >15% at 80% confidence |
| O2 — First 30 days | In-app checklist completion rate for new paid accounts | Weekly | >50% completion rate in first 7 days of new accounts |
| O2 — First 30 days | Support ticket volume tagged "onboarding confusion" | Weekly | Ticket volume declining week-over-week from launch |

### Risks to OKR Achievement

| Risk | Likelihood | Week 1 mitigation |
|---|---|---|
| Data pipeline dependency on Platform team delays activation tracking for KR2 | High | Meet with Platform team lead in week 1 to confirm event tracking for "first contract uploaded" is scoped into their Q3 sprint — if not, escalate to Head of Engineering |
| Engineer capacity drops 33% from August 15 when parental leave begins | High | Re-sequence sprint: ship setup wizard redesign by August 1 so it is in production before capacity drops; in-app checklist becomes the August–September focus |
| A/B test on upgrade prompt may not reach statistical significance before September 30 | Medium | Launch the test no later than July 7; if significance isn't reached by September 1, document directional findings and commit to a full rollout decision in Q4 planning |

### OKR Communication Draft

Hey team 👋

Kicking off Q3 with a clear north star: **make the path from trial to first contract so obvious that users get there in under a day.**

Company is pushing hard to prove that Clearpath can sell itself — and our two objectives this quarter sit right at the centre of that bet. We're redesigning the setup wizard, shipping an in-app admin checklist, and testing how we prompt trial users to upgrade at the moment they first see value.

If we hit our targets — 22% trial conversion and 60% activation rate for new paid accounts — we unlock roughly $500K of ARR impact and prove that the product-led motion works at mid-market scale.

A heads-up on constraints: we're losing one engineer from mid-August, so I've sequenced the setup wizard as our first ship. More on sprint planning in tomorrow's kickoff.

Excited to build this one with you. Questions or pushback on these targets — bring them to Friday's retro.

---

## What to Notice

- Company OKRs were pasted verbatim, even though they used inconsistent formatting — the cascade map correctly identified what each team lever was regardless
- KR targets (22% conversion, 60% activation) are deliberately set below the company KR ceiling (25%) — acknowledging the team owns only part of the funnel
- The Health Check caught a real tension: the team set 8 hours as a target when the company KR says 2 hours — this needs a conversation before the OKRs are finalised
- Leading indicators are all checkable within 2–3 weeks of a launch, not at quarter-end — they serve as early warning signals, not lagging measures
- The team announcement avoids corporate language and explains the *why* — including what success unlocks for the business
