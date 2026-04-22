# TCO, Cost-Benefit Analysis & NPV Model Builder

**Phase:** Strategy / Business Case
**Purpose:** Build a rigorous financial model for a product investment — starting with Total Cost of Ownership, expanding into a full Cost-Benefit Analysis that captures time saved, money saved, effort reduction, and speed-to-value, then producing a Net Present Value model to support investment decisions and executive conversations.

## Prompt Template

```
You are a senior financial advisor and product strategist. I am a Senior Product Manager building a business case for [INITIATIVE NAME], which is [INITIATIVE DESCRIPTION].

Use the inputs I provide below to build a three-part financial model: a Total Cost of Ownership (TCO), a Cost-Benefit Analysis (CBA), and a Net Present Value (NPV) model. Where I have left a field sparse, use the surrounding context to make reasonable estimates — but flag every assumption you make so I can validate or override it.

---

**Initiative Context:**
[WHAT IS BEING BUILT, BOUGHT, OR CHANGED — e.g. "replacing our manual onboarding workflow with an automated platform"]

**Primary Stakeholders / Decision Makers:**
[WHO NEEDS TO APPROVE THIS — e.g. "VP of Engineering, CFO, and the CPO"]

**Time Horizon:**
[HOW MANY YEARS TO MODEL — e.g. "3 years" or "5 years"]

**Discount Rate (for NPV):**
[YOUR COMPANY'S HURDLE RATE OR WACC — e.g. "10%" — if unknown, leave blank and I will use 10% as a default]

**Investment Costs:**
[ALL UPFRONT AND ONGOING COSTS — include as many as you know:]
- Software / licensing: [AMOUNT or UNKNOWN]
- Infrastructure / hosting: [AMOUNT or UNKNOWN]
- Implementation / professional services: [AMOUNT or UNKNOWN]
- Internal engineering effort: [PERSON-WEEKS or HOURS, and average fully-loaded cost per week]
- Training and change management: [AMOUNT or UNKNOWN]
- Ongoing maintenance / support per year: [AMOUNT or UNKNOWN]
- Other: [ANY ADDITIONAL COST ITEMS]

**Time Saved:**
[DESCRIBE TASKS THAT WILL TAKE LESS TIME AFTER THIS INVESTMENT:]
- Task or process: [DESCRIPTION]
- Who performs it: [ROLE — e.g. "support agent", "engineer", "customer"]
- Current time per instance: [HOURS or MINUTES]
- Expected time after: [HOURS or MINUTES, or "eliminated"]
- Frequency: [TIMES PER DAY / WEEK / MONTH]
- Number of people affected: [HEADCOUNT]
- Fully-loaded hourly cost of that role: [AMOUNT or UNKNOWN]

**Money Saved:**
[DIRECT COST REDUCTIONS FROM THIS INVESTMENT:]
- Item: [DESCRIPTION — e.g. "cancel legacy tool", "reduce cloud spend", "avoid a hire"]
- Annual savings: [AMOUNT or ESTIMATE]

**Effort Saved / Capacity Unlocked:**
[WORK THAT GETS ELIMINATED OR REDIRECTED — focus on what teams can stop doing or do less of:]
- Activity: [DESCRIPTION]
- Who is affected: [TEAM or ROLE]
- Estimated hours freed per month: [HOURS]
- What that capacity will be redirected toward: [DESCRIPTION — e.g. "higher-value customer work" or "product development"]

**Speed-to-Value / Faster Delivery:**
[DESCRIBE WHERE THIS INVESTMENT ACCELERATES OUTCOMES:]
- What gets faster: [DESCRIPTION — e.g. "customer onboarding", "feature releases", "incident resolution"]
- Current cycle time: [DAYS / HOURS]
- Expected cycle time after: [DAYS / HOURS]
- Business impact of the acceleration: [REVENUE UNLOCKED, CHURN PREVENTED, DEALS UNBLOCKED, etc.]
- Estimated annual value of that impact: [AMOUNT or UNKNOWN]

**Revenue or Growth Impact (if applicable):**
[ANY DIRECT REVENUE CONTRIBUTION FROM THIS INVESTMENT:]
- Source: [NEW CUSTOMERS, UPSELL, RETENTION, FASTER TIME-TO-MARKET, etc.]
- Estimated annual value: [AMOUNT or BASIS FOR ESTIMATE]

**Risk & Uncertainty:**
[NOTE ANY COSTS OR BENEFITS YOU ARE LEAST CONFIDENT ABOUT — these will be surfaced in the sensitivity analysis]

---

Using this input, generate the following three-part financial model:

---

## PART 1 — Total Cost of Ownership (TCO)

### 1.1 Cost Inventory
Categorize every cost item into:
- **One-time costs** (upfront investment)
- **Recurring annual costs** (ongoing run cost)

| Cost Category | Year 0 (One-Time) | Year 1 | Year 2 | Year 3 (+ beyond) | Notes / Assumptions |
|---|---|---|---|---|---|
| Software & licensing | | | | | |
| Infrastructure | | | | | |
| Implementation & services | | | | | |
| Internal engineering effort | | | | | |
| Training & change management | | | | | |
| Ongoing maintenance & support | | | | | |
| Other | | | | | |
| **TOTAL** | | | | | |

### 1.2 TCO Summary
- Total investment over [TIME HORIZON]: $X
- Average annual cost: $X
- Peak spend year: Year X — explain why

### 1.3 TCO Assumptions Log
List every assumption made about costs with a confidence level (High / Medium / Low).

---

## PART 2 — Cost-Benefit Analysis (CBA)

### 2.1 Benefits Inventory

#### Time Saved
For each time-saving item, calculate:
- Hours saved per year = (time reduction per instance) × (frequency per year) × (headcount)
- Dollar value = hours saved × fully-loaded hourly rate

| Role | Process / Task | Hours Saved / Year | Hourly Rate | Annual $ Value | Assumptions |
|---|---|---|---|---|---|

**Subtotal — Time Saved:** $X/year

#### Money Saved (Direct Cost Reduction)
| Item | Annual Savings | Notes |
|---|---|---|

**Subtotal — Money Saved:** $X/year

#### Effort Saved / Capacity Unlocked
Quantify the capacity freed and its value. Where capacity is redirected to revenue-generating or strategic work, estimate the marginal value created.

| Team / Role | Hours Freed / Month | Redirected To | Estimated Annual Value | Confidence |
|---|---|---|---|---|

**Subtotal — Effort / Capacity Value:** $X/year

#### Speed-to-Value / Faster Delivery
For each acceleration item, calculate the annual value using one of these methods:
- **Revenue unlocked**: deals or contracts unblocked by faster delivery × average deal value
- **Churn prevented**: customers retained due to faster resolution × average revenue per customer
- **Time-to-market gain**: revenue pulled forward by N weeks × monthly revenue run rate

| What Gets Faster | Cycle Time Reduction | Method Used | Annual $ Value | Confidence |
|---|---|---|---|---|

**Subtotal — Speed-to-Value:** $X/year

#### Revenue / Growth Impact (if applicable)
| Source | Annual $ Value | Basis for Estimate | Confidence |
|---|---|---|---|

**Subtotal — Revenue Impact:** $X/year

### 2.2 Total Annual Benefits Summary
| Benefit Category | Year 1 | Year 2 | Year 3 | Notes |
|---|---|---|---|---|
| Time saved | | | | |
| Money saved | | | | |
| Effort / capacity | | | | |
| Speed-to-value | | | | |
| Revenue impact | | | | |
| **TOTAL BENEFITS** | | | | |

### 2.3 Net Benefit (Benefits minus Costs)
| | Year 0 | Year 1 | Year 2 | Year 3 | Cumulative |
|---|---|---|---|---|---|
| Total benefits | — | | | | |
| Total costs | | | | | |
| **Net benefit / (cost)** | | | | | |
| Cumulative net | | | | | |

### 2.4 Breakeven Analysis
- **Payback period**: Month X of Year Y — explain the calculation
- **Breakeven statement**: "The investment pays back in X months. Every year after breakeven, the net benefit is approximately $X."

### 2.5 CBA Assumptions Log
List every benefit assumption with confidence level (High / Medium / Low) and what would need to be true for it to hold.

---

## PART 3 — Net Present Value (NPV) Model

### 3.1 Discounted Cash Flow Table
Apply the discount rate of [DISCOUNT RATE]% to convert all future benefits and costs to present value.

| Period | Net Cash Flow (Undiscounted) | Discount Factor | Present Value |
|---|---|---|---|
| Year 0 | | 1.000 | |
| Year 1 | | | |
| Year 2 | | | |
| Year 3 | | | |
| **NPV** | | | **$X** |

Show the discount factor formula used: 1 / (1 + r)^n

### 3.2 NPV Interpretation
- **NPV**: $X
- **IRR** (Internal Rate of Return): X% — the discount rate at which NPV = 0
- **Decision signal**:
  - If NPV > 0: investment creates value at the assumed discount rate
  - If NPV < 0: flag which assumptions would need to change to make it viable

### 3.3 Sensitivity Analysis
Test three scenarios — Conservative, Base, and Optimistic — by varying the two or three highest-uncertainty inputs identified in the assumptions logs.

| Scenario | Key Assumption Changes | NPV | Payback Period | Recommendation |
|---|---|---|---|---|
| Conservative | | | | |
| Base (most likely) | | | | |
| Optimistic | | | | |

Explain which scenario you consider most credible and why.

### 3.4 Decision Summary for Leadership
Write a concise (half-page) executive summary suitable for a CFO or CPO that includes:
- The investment being made and why now
- Total cost over [TIME HORIZON]: $X
- Total benefits over [TIME HORIZON]: $X
- Net benefit: $X
- NPV: $X at [DISCOUNT RATE]% discount rate
- Payback period: X months
- Biggest risk to these numbers: [TOP 1–2 UNCERTAINTIES]
- Recommended decision: Proceed / Proceed with staged investment / Do not proceed — with a one-sentence rationale
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[INITIATIVE NAME]` | Short name for what you are evaluating | "AI-Assisted Onboarding Platform" |
| `[INITIATIVE DESCRIPTION]` | One sentence on what it is | "An automated customer onboarding tool replacing a manual 12-step process handled by the CS team" |
| `[TIME HORIZON]` | Years to model | "3 years" |
| `[DISCOUNT RATE]` | Hurdle rate or WACC | "10%" |
| `[INVESTMENT COSTS]` | All cost line items | See section above |
| `[TIME SAVED]` | Tasks that take less time after | "Support ticket triage: 45 min → 5 min, 200 tickets/week, 8 agents" |
| `[MONEY SAVED]` | Direct cost reductions | "Cancel legacy CRM: $120K/year" |
| `[EFFORT SAVED]` | Work eliminated or redirected | "Manual reporting: 20 hrs/month freed per analyst, 4 analysts" |
| `[SPEED-TO-VALUE]` | What gets faster and the business impact | "Customer onboarding: 14 days → 3 days; 40 deals/year × $25K ACV at risk" |
| `[REVENUE IMPACT]` | Direct revenue contribution | "Faster onboarding reduces 90-day churn by 15%; 500 customers × $2K MRR" |

## Tips

- Start with costs — they are almost always more knowable than benefits. Anchor your credibility there before projecting benefits.
- Use fully-loaded labor costs (salary + benefits + overhead), not just base salary — typically 1.25–1.5× base for knowledge workers.
- When a benefit is hard to quantify (e.g. "team morale"), acknowledge it qualitatively rather than forcing a number — overclaiming destroys credibility.
- The sensitivity analysis is your most important slide with the CFO — show you understand where your model is fragile.
- A positive NPV does not automatically mean "do it" — also ask whether this is the highest-value use of the same capital.
- If the payback period exceeds your planning horizon or the company's runway, reframe the investment as a staged or phased commitment.
- Revisit the model after 6 months with actuals — teams that track forecast vs. actual build the most credibility for future business cases.
