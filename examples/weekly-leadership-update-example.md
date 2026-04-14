# Example: Weekly Leadership Update — Mobile Checkout Redesign

This is a worked example of the Weekly Leadership Update prompt (`prompts/communications/01-weekly-leadership-update.md`).

## Filled-In Prompt

```
You are a senior communications advisor helping a Product Manager write a weekly leadership update.

My audience is VP of Product and the CTO. They care about outcomes, risks, and decisions — not task lists or technical detail.

Here is my raw input for this week:

Product / Initiative: Mobile Checkout Redesign
Week ending: April 18, 2025

What we shipped or completed this week:
- Launched A/B test of new single-page checkout to 20% of mobile users
- Resolved the payment tokenisation bug that was causing 4% of iOS checkouts to fail
- Alignment meeting with legal completed — no blockers on the new address capture flow
- Design handed off final screens for the guest checkout flow

What we are working on next week:
- Reviewing A/B test data mid-week; full rollout if checkout completion rate holds above threshold
- Engineering begins guest checkout build
- Kick off accessibility audit with third-party vendor

Risks or blockers:
- A/B test is running slower than expected due to lower-than-normal mobile traffic this week (school holidays). May need to extend test by 3–4 days before we have statistical significance.
- Guest checkout depends on auth service changes owned by Platform team — their sprint is full and we have not secured capacity yet

Metrics or signals worth highlighting:
- Early A/B data (Day 3): checkout completion rate up 6pts in test cohort vs control (41% → 47%). Still early but directionally strong.

Decisions or support needed from leadership:
- If A/B test needs to extend to April 25, do we hold the full rollout to coincide with the May campaign launch or ship as soon as data is ready?
```

## Generated Output

---

📅 **Weekly Product Update — Mobile Checkout Redesign | Week of April 18, 2025**

**✅ This Week**
- **Checkout completion rate up 6pts in A/B test cohort** (41% → 47%) — early signal is directionally strong
- Launched single-page checkout A/B test to 20% of mobile users
- Fixed iOS payment tokenisation bug that was causing 4% of checkouts to fail
- Legal sign-off received on new address capture flow — no blockers
- Guest checkout designs handed off to engineering

**🔜 Next Week**
- Mid-week data review; full rollout if completion rate holds above threshold
- Engineering begins guest checkout build
- Accessibility audit kicks off with third-party vendor

**⚠️ Risks & Blockers**
- A/B test running 3–4 days behind pace due to low mobile traffic (school holidays) — may not reach statistical significance until April 25
- Guest checkout depends on Platform team auth changes; their sprint is full and capacity is not yet confirmed

**📊 Signal of the Week**
Early A/B test data shows checkout completion rate up 6 percentage points in the test cohort vs. control — if this holds, it would represent the largest single-session conversion improvement in 18 months.

**🙋 Decisions Needed**
- If the A/B test extends to April 25, should we hold the full rollout to align with the May campaign launch, or ship as soon as statistical significance is reached?

---

## What to Notice

- Raw notes were bullet points and fragments — the output is polished and executive-ready without losing any substance
- The most important metric (6pt lift) is bolded and leads the "This Week" section
- The A/B test timing risk is named plainly with a cause (school holidays) and a concrete impact (3–4 day delay) — not softened
- The decision ask is framed as a specific choice with two options, not a vague "need input on timeline"
- Total message is under 250 words
