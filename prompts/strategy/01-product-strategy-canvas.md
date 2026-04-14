# Product Strategy Canvas Generator

**Phase:** Strategy
**Purpose:** Build a complete product strategy canvas covering vision, target customer, value proposition, competitive positioning, strategic bets, and success metrics — creating a single artifact that aligns your team and communicates direction to leadership.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager building a strategy canvas for [PRODUCT NAME], a [PRODUCT DESCRIPTION].

Use the inputs I provide below to construct a complete Product Strategy Canvas. Where I have left a section sparse, use the surrounding context to make reasonable inferences — but flag any assumption you make so I can validate it.

---

**Company / Business Context:**
[COMPANY STAGE, REVENUE MODEL, AND STRATEGIC PRIORITIES — e.g. "Series B SaaS, $8M ARR, expanding from SMB into mid-market, 18-month path to profitability"]

**Target Customer:**
[PRIMARY PERSONA — role, company type, size, key characteristics]
[SECONDARY PERSONA — if applicable]

**Problem We Are Solving:**
[THE CORE PAIN POINT OR JOB TO BE DONE — be specific about what is broken, slow, or missing today]

**Current Solution Landscape:**
[HOW CUSTOMERS SOLVE THIS TODAY — incumbent tools, workarounds, or competing products]

**Our Differentiators:**
[WHAT WE DO BETTER, DIFFERENTLY, OR UNIQUELY — capabilities, data, distribution, business model, or team advantages]

**Strategic Constraints:**
[BUDGET, TIMELINE, TEAM SIZE, TECHNOLOGY LIMITS, OR REGULATORY REQUIREMENTS]

**12-Month Goal:**
[ONE MEASURABLE OUTCOME — e.g. "reach $2M ARR from mid-market segment" or "achieve 40% DAU/MAU ratio"]

---

Using this input, generate a complete Product Strategy Canvas with the following sections:

## 1. Product Vision
A single, memorable sentence (the "north star") that describes the future state your product creates for customers. It should be aspirational but grounded — not a mission statement, not a tagline.

Format: "We believe [CUSTOMER] deserves [OUTCOME] without [CURRENT PAIN]."

## 2. Target Customer Profile
| Dimension | Primary Persona | Secondary Persona (if applicable) |
|---|---|---|
| Role & title | | |
| Company type & size | | |
| Primary job to be done | | |
| Biggest frustration today | | |
| How they measure success | | |
| Where we find them | | |

## 3. Value Proposition
Structure the value proposition using three layers:

**Functional value** — What the product does that saves time, removes friction, or enables something new
**Emotional value** — How the customer feels when using the product (confident, in control, respected)
**Business value** — The measurable outcome the customer or their organization achieves

Then write a single Value Proposition Statement:
"For [TARGET CUSTOMER] who [JOB TO BE DONE], [PRODUCT NAME] is the [CATEGORY] that [KEY BENEFIT] unlike [ALTERNATIVE] which [LIMITATION]."

## 4. Competitive Positioning Map
Identify the two most important axes of differentiation in this market (e.g. ease-of-use vs. depth of features, speed vs. accuracy, self-serve vs. enterprise). Place our product and the top 3–4 competitors on a 2x2 matrix with a text description of where each sits and why.

Then summarize:
- Our defensible position (the space we own or are building toward)
- The nearest competitive threat and what would close our moat
- One whitespace area no competitor currently owns well

## 5. Strategic Bets
List 3–5 strategic bets — deliberate choices about where to invest and what to say no to. For each:

| Bet | What we are doing | What we are NOT doing | Why this is the right trade-off |
|---|---|---|---|

## 6. Key Capabilities Required
List the top 5 capabilities (product, data, technology, or go-to-market) that must exist or be built to deliver on this strategy. For each, note:
- Current state: Have it / Partially have it / Gap
- Build, Buy, or Partner to close any gap

## 7. Success Metrics
Define metrics at three horizons:

| Horizon | Metric | Target | Why it matters |
|---|---|---|---|
| **Leading (3 months)** | Early signals the strategy is working | | |
| **Growth (6–12 months)** | Proof of product-market traction | | |
| **Strategic (12–24 months)** | Validation of the long-term position | | |

## 8. Risks & Strategic Assumptions
List the top 3–5 assumptions this strategy depends on. For each:
- The assumption
- What would invalidate it
- How we would know within 90 days if it is wrong

## 9. One-Page Summary
Compress the full canvas into a concise leadership-ready summary:
- Vision (1 sentence)
- Who we serve and what we solve (2 sentences)
- Our differentiated position (1 sentence)
- The 3 strategic bets we are making (3 bullets)
- How we will measure success in 12 months (2 metrics)
- The biggest assumption we are betting on (1 sentence)
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT NAME]` | Your product's name | "Clearpath" |
| `[PRODUCT DESCRIPTION]` | One-line description | "contract management platform for in-house legal teams" |
| `[COMPANY STAGE / REVENUE MODEL]` | Business context | "Series A, $3M ARR, SaaS subscription, expanding to enterprise" |
| `[TARGET CUSTOMER]` | Primary persona | "In-house legal counsel at mid-market companies (500–5,000 employees)" |
| `[PROBLEM WE ARE SOLVING]` | Core pain point | "Legal teams spend 60% of time on contract status follow-ups, not legal work" |
| `[CURRENT SOLUTION LANDSCAPE]` | How customers solve it today | "Email threads, shared drives, and legacy CLM tools built for large law firms" |
| `[OUR DIFFERENTIATORS]` | What makes us different | "AI-native contract review, built for in-house teams, deploys in one day" |
| `[STRATEGIC CONSTRAINTS]` | Limits to work within | "12-month runway, team of 12, no enterprise sales motion yet" |
| `[12-MONTH GOAL]` | Measurable north star | "Sign 50 mid-market contracts, reach $1.5M ARR" |

## Tips

- The more specific your inputs, the sharper the canvas — vague inputs produce generic strategy
- Treat Section 8 (Risks & Assumptions) as the most important section: strategy fails at the assumption level, not the execution level
- Share the One-Page Summary (Section 9) with leadership and the full canvas with your immediate team — they serve different audiences
- Revisit the canvas at each major milestone or when a key assumption is invalidated; a strategy canvas should be a living document, not a one-time slide
- If you are early-stage with limited data, run the Customer Discovery prompts first — the canvas is only as good as your understanding of the customer problem
