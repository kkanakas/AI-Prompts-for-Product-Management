# Capability Gap Analysis

**Phase:** Competitive Analysis
**Purpose:** Identify the gaps between your current product capabilities, what customers need, and what competitors already deliver — then prioritize which gaps to close first.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager for [PRODUCT NAME], a [PRODUCT DESCRIPTION] serving [TARGET CUSTOMER].

I need to perform a structured capability gap analysis across three dimensions:
1. What we currently have
2. What our customers need (based on feedback, research, or stated requirements)
3. What our top competitors already deliver

Here is the context:

**Our current capabilities:**
[LIST YOUR CURRENT CAPABILITIES — features, integrations, workflows, or service qualities]

**Customer needs and expectations:**
[LIST WHAT CUSTOMERS ARE ASKING FOR — from interviews, support tickets, NPS feedback, or sales blockers]

**Competitors to benchmark against:**
- Competitor 1: [NAME] — [BRIEF DESCRIPTION OR WEBSITE]
- Competitor 2: [NAME] — [BRIEF DESCRIPTION OR WEBSITE]
- Competitor 3: [NAME] — [BRIEF DESCRIPTION OR WEBSITE]

Using this input, produce the following:

## 1. Capability Inventory Table
Create a table with these columns:
| Capability Area | We Have It | Customers Need It | Competitor 1 | Competitor 2 | Competitor 3 | Gap Type |

For **Gap Type**, use one of:
- **Critical** – customers need it and competitors have it; we are behind
- **Opportunity** – customers need it but no competitor has solved it well; whitespace
- **Parity** – we have it, competitors have it, customers expect it as table stakes
- **Differentiator** – we have it and competitors do not; protect and amplify
- **Irrelevant** – exists but neither customers nor competitors treat it as important

## 2. Gap Prioritization Matrix
Rank the Critical and Opportunity gaps by:
- **Customer Impact** – High / Medium / Low (based on how often it's requested or how much it blocks deals/retention)
- **Competitive Urgency** – High / Medium / Low (how quickly competitors are advancing in this area)
- **Estimated Effort** – High / Medium / Low (rough complexity to close the gap)

Present as a prioritized list with a recommended sequence.

## 3. Differentiator Risk Assessment
For each Differentiator gap type identified, assess:
- How defensible is this advantage? (Unique / Replicable within 6 months / Already being copied)
- Recommended action: Invest to extend / Maintain / Deprioritize

## 4. Strategic Recommendations
Based on the analysis, provide:
- The top 3 gaps to close in the next two quarters and why
- One capability area where we should aim to leapfrog competitors rather than catch up
- Any capability we should consider deprioritizing because it is neither valued by customers nor a competitive requirement

## 5. Executive Summary
A 4–5 sentence summary framing our competitive position, the most urgent gaps, and the single highest-leverage investment a product leader should make now.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT NAME]` | Your product's name | "Flowdesk" |
| `[PRODUCT DESCRIPTION]` | One-line description of what it does | "workflow automation platform for ops teams" |
| `[TARGET CUSTOMER]` | Who you primarily serve | "mid-market operations teams at B2B SaaS companies" |
| `[LIST YOUR CURRENT CAPABILITIES]` | Features, integrations, workflows you have today | "Drag-and-drop workflow builder, Slack integration, basic reporting" |
| `[LIST WHAT CUSTOMERS ARE ASKING FOR]` | Verbatim or paraphrased customer requests | "Role-based permissions, API access, audit logs, mobile app" |
| `[Competitor NAME / WEBSITE]` | Each competitor to benchmark | "Zapier — zapier.com" |

## Tips

- Pull customer needs directly from support tickets, sales call notes, or NPS verbatims for maximum accuracy — the more specific, the sharper the analysis
- Include at least one emerging or indirect competitor alongside your primary ones to surface non-obvious threats
- Re-run this analysis every quarter; gap maps shift faster than annual planning cycles reflect
- If you don't know a competitor's capability, state that explicitly so the AI flags it as an unknown rather than assuming
