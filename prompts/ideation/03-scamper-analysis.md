# SCAMPER Analysis

**Phase:** Ideation
**Purpose:** Apply the SCAMPER framework to systematically generate creative product or feature ideas by challenging existing assumptions from seven distinct angles.

## Prompt Template

```
I am a product manager working on the following:

Product / Feature: [PRODUCT_OR_FEATURE]
Target users: [TARGET_USERS]
Current problem or opportunity: [PROBLEM_OR_OPPORTUNITY]
Key constraints: [CONSTRAINTS]

Run a SCAMPER analysis to generate creative ideas for improving or reimagining this product/feature. For each letter of SCAMPER, provide 2–3 concrete ideas with the following structure:

1. Idea — what the change or experiment is
2. How it applies — how it specifically addresses the product or feature
3. Potential value — what benefit this could deliver to users or the business
4. Risks or challenges — what could make this difficult or backfire

SCAMPER letters to cover:
- S — Substitute: What components, materials, processes, or rules could be swapped?
- C — Combine: What could be merged with another feature, product, or workflow?
- A — Adapt: What ideas from other industries or products could be borrowed and adapted?
- M — Modify / Magnify / Minify: What could be changed, scaled up, or scaled down?
- P — Put to other uses: How could the product or feature be repurposed for different users or contexts?
- E — Eliminate: What could be removed to simplify or streamline the experience?
- R — Reverse / Rearrange: What could be reordered, flipped, or approached from the opposite direction?

After completing all seven lenses, highlight the top 3 ideas across the full analysis that you think have the highest potential, and explain why.
```

## Placeholders

| Variable | Description |
|---|---|
| `[PRODUCT_OR_FEATURE]` | The specific product, feature, or workflow you want to ideate around |
| `[TARGET_USERS]` | Who the product or feature serves (e.g., new users, enterprise admins, frontline workers) |
| `[PROBLEM_OR_OPPORTUNITY]` | The user problem, friction point, or strategic opportunity being addressed |
| `[CONSTRAINTS]` | Real boundaries on scope (e.g., no backend changes, must ship in Q2, limited engineering capacity) |

## Tips

- SCAMPER works best when you have a well-defined baseline — describe the current state in enough detail so the model can apply each lens meaningfully.
- Use the "Adapt" lens explicitly to pull in analogies from adjacent industries (e.g., fintech, gaming, healthcare) to break out of product-category tunnel vision.
- If a particular lens feels forced, that's a signal worth noting — it may reveal a constraint you haven't articulated yet.
- Run this prompt after an initial brainstorm to stress-test ideas you already have, not just to generate new ones from scratch.
