# Working Backwards Plan Generator

**Phase:** Strategy
**Purpose:** Build a working backwards plan for a feature or product by starting with the customer outcome and writing backward to the work required — ensuring every decision is anchored in customer value before a line of code is written.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager who wants to build a working backwards plan for [FEATURE OR PRODUCT NAME].

Working backwards is a discipline of starting with the customer experience we want to create — not the technology or the roadmap — and reasoning backward to what must be built, decided, and validated. The output is a press release and FAQ document written as if the feature already exists and customers are already benefiting from it.

Here is my context:

**What I am building:**
[ONE SENTENCE DESCRIPTION — what the feature or product does]

**Target customer:**
[WHO THIS IS FOR — role, company type, situation, or pain they are in today]

**The problem today:**
[WHAT IS BROKEN, SLOW, MISSING, OR PAINFUL — be specific about the current experience]

**The outcome I want customers to have:**
[WHAT SUCCESS LOOKS LIKE FOR THE CUSTOMER — not what we ship, but what they feel or achieve]

**Key constraints:**
[TIME, TEAM, BUDGET, TECHNICAL, OR REGULATORY LIMITS — anything that bounds the solution]

---

Using this input, produce a complete Working Backwards document with the following sections:

## 1. Internal Press Release

Write a press release as if the feature has just launched and is already in customers' hands. This is an internal document — it is honest, specific, and customer-focused, not marketing copy.

Structure the press release as follows:

**Headline:** One sentence. Customer benefit, not feature name. Should pass the "so what?" test.

**Subheadline:** One sentence expanding on who benefits and how.

**Opening paragraph:** Set the scene. Who is the customer, what was their world like before, and what has changed now that this exists? (3–4 sentences)

**Problem paragraph:** Describe the pain in the customer's own voice. What were they doing before? What was frustrating, slow, or broken? What did it cost them — in time, money, confidence, or opportunity? (3–4 sentences)

**Solution paragraph:** Describe what the feature does and how it solves the problem — from the customer's perspective, not the engineering perspective. Avoid technical language. Focus on what the customer now experiences, feels, or achieves. (3–4 sentences)

**Customer quote:** A realistic quote from a customer describing the impact in their own words. Make it specific and believable — not a generic endorsement. Include the customer's role and company type.

**Call to action:** One sentence on what customers should do next.

---

## 2. Frequently Asked Questions

Write the FAQs a real customer, internal stakeholder, or sceptic would ask. Answer each one honestly — including the hard questions.

Organise into three groups:

**Customer FAQs** (what users will ask)
- What does this actually do for me?
- How is this different from what I do today?
- What do I need to do to get started?
- What happens to my existing data / workflow / setup?
- Is this available on [mobile / my plan / my region]?

**Internal / Stakeholder FAQs** (what leadership, sales, and CS will ask)
- Why are we building this now?
- Who is this for and how many customers does this affect?
- How will we measure success?
- What are we not building in this version, and why?
- What is the risk if we get this wrong?

**Sceptic FAQs** (the hard questions that test the idea)
- Why hasn't this been built before?
- What will customers do if this doesn't work as promised?
- How confident are we that customers actually want this?
- What assumption is this entire plan built on, and how do we know it is true?

---

## 3. Customer Value Statement

Distill the entire plan into a single, precise customer value statement using this format:

**"We help [CUSTOMER] who [SITUATION OR STRUGGLE] to [OUTCOME] by [MECHANISM] — unlike [ALTERNATIVE] which [LIMITATION]."**

Then rate the strength of the value statement on three dimensions:
- **Specificity** (1–5): How precisely does it describe the customer and their situation?
- **Differentiation** (1–5): How clearly does it separate us from the alternative?
- **Outcome clarity** (1–5): How measurable or tangible is the customer outcome?

If any dimension scores below 4, rewrite the statement to improve it and explain what changed.

---

## 4. Working Backwards Checklist

Before any build work begins, confirm:

| Question | Answer | Confidence |
|---|---|---|
| Can we describe the customer problem in one sentence without mentioning our product? | | High / Medium / Low |
| Have we talked to at least 5 customers who have this problem? | | High / Medium / Low |
| Do we know what customers do today to solve this? | | High / Medium / Low |
| Do we know what "good" looks like to the customer — not to us? | | High / Medium / Low |
| Have we written down what we are NOT building in v1? | | High / Medium / Low |
| Do we know the single metric that will tell us this worked? | | High / Medium / Low |
| Is there a named customer who would be disappointed if we cancelled this? | | High / Medium / Low |

Flag any row with Low confidence as a risk that must be resolved before development begins.

---

## 5. Success Metric

Define the one metric that will prove this worked for customers — not for the business. It should be:
- Measurable within 90 days of launch
- Describing a change in customer behaviour, not product usage
- Something that would go up only if customers are genuinely better off

Then name the business metric it should move as a downstream consequence, and the leading indicator you will track in the first two weeks after launch to know if you are on track.

| Metric type | Metric | Baseline | Target | Timeframe |
|---|---|---|---|---|
| Customer outcome metric | | | | |
| Business consequence metric | | | | |
| Leading indicator (weeks 1–2) | | | | |
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE OR PRODUCT NAME]` | What you are building | "Automated contract renewal alerts" |
| `[ONE SENTENCE DESCRIPTION]` | What it does | "Notifies legal teams 90 days before a contract expires and surfaces the key renewal terms" |
| `[TARGET CUSTOMER]` | Who it is for | "In-house General Counsel at mid-market SaaS companies managing 50+ active contracts" |
| `[THE PROBLEM TODAY]` | Current pain | "Legal teams miss renewal windows because contract dates live in spreadsheets no one checks" |
| `[OUTCOME I WANT CUSTOMERS TO HAVE]` | Desired customer state | "Never miss a renewal date; arrive at every renewal conversation prepared" |
| `[KEY CONSTRAINTS]` | Limits to work within | "Must ship in 6 weeks; no changes to the data model; available on existing paid plans only" |

## Tips

- **Write the press release before the PRD** — if you cannot write a compelling press release, the customer value is not clear enough to build yet
- **The customer quote is the hardest part** — if you cannot write a believable quote, you probably do not know your customer well enough yet; go do one more discovery interview first
- **The sceptic FAQs are the most valuable** — the questions you find hardest to answer honestly are the assumptions your plan is betting on; surface them now, not after launch
- **Working backwards is not a one-time exercise** — rerun this at every major scope change; if the press release changes, the build scope should too
- **"What are we NOT building" is as important as what we are** — a working backwards plan without explicit scope exclusions almost always expands in the wrong direction
