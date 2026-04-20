# Value Proposition Design

**Phase:** Strategy & Discovery
**Purpose:** Develop a rigorous, evidence-backed value proposition by mapping customer jobs, pains, and gains to pain relievers and gain creators — then stress-test the result against three fit criteria (problem-solution, product-market, and business model) to confirm the proposition is grounded in real customer need and can support a profitable, scalable business.

## Prompt Template

```
You are a senior product strategist helping develop a well-crafted value proposition. Using the context below, generate a complete value proposition canvas and fit analysis.

Product or feature name: [PRODUCT_NAME]
One-line description: [PRODUCT_DESCRIPTION]
Target customer segment: [CUSTOMER_SEGMENT — e.g., "enterprise SOC analysts at Fortune 500 companies", "SMB e-commerce merchants processing <$1M GMV"]
Existing evidence available: [EVIDENCE — e.g., "12 customer interviews, NPS data, 3 win/loss reports, usage analytics" — or "none yet"]
Top competitors or alternatives: [COMPETITORS — e.g., "Splunk, Microsoft Sentinel, manual spreadsheet-based workflows"]

---

## Section 1 — Customer Profile

### 1.1 Customer Jobs
Identify the functional, social, and emotional jobs this customer segment is trying to get done.

**Functional jobs** (practical tasks or problems they need to solve):
- Job 1: [what they are trying to accomplish]
- Job 2:
- Job 3:

**Social jobs** (how they want to be perceived by others):
- Job 1: [e.g., "be seen as a strategic leader by the CISO"]
- Job 2:

**Emotional jobs** (how they want to feel):
- Job 1: [e.g., "feel confident that the environment is secure"]
- Job 2:

**Critical jobs** (rank the top 2–3 jobs that matter most — the ones customers are most motivated to accomplish and where failure is most costly):

### 1.2 Customer Pains
Identify the obstacles, frustrations, risks, and undesired outcomes customers experience before, during, or after trying to get their jobs done.

**Functional pains** (things that don't work, are too slow, or require too much effort):
- Pain 1:
- Pain 2:
- Pain 3:

**Financial pains** (costs, budget pressure, wasted spend, revenue risk):
- Pain 1:
- Pain 2:

**Social and reputational pains** (risks to status, credibility, or relationships):
- Pain 1:
- Pain 2:

**Technical pains** (integration complexity, reliability, security risk, data quality):
- Pain 1:
- Pain 2:

**Pain severity ranking** — classify each pain as: Extreme / Moderate / Mild. Flag the top 3 extreme pains.

### 1.3 Customer Gains
Identify the outcomes and benefits customers want — required, expected, desired, and unexpected.

**Required gains** (minimum outcomes without which the solution is unacceptable):
- Gain 1:
- Gain 2:

**Expected gains** (outcomes customers assume any decent solution will deliver):
- Gain 1:
- Gain 2:

**Desired gains** (outcomes customers would love but don't necessarily expect — often unarticulated):
- Gain 1:
- Gain 2:

**Unexpected gains** (delighters — outcomes that would surprise and delight, analogous to Kano Delighters):
- Gain 1:
- Gain 2:

**Gain relevance ranking** — classify each gain as: Essential / Nice-to-have / Delighter.

---

## Section 2 — Value Map

### 2.1 Pain Relievers
For each extreme pain identified above, describe specifically how the product or feature relieves it. Classify each reliever by type.

**Time savings** — how does the product reduce time-to-outcome or eliminate manual steps?
- Reliever 1: [links to Pain X]
- Reliever 2:

**Resource savings** — how does the product reduce headcount, tooling costs, or operational overhead?
- Reliever 1: [links to Pain X]
- Reliever 2:

**Financial risk mitigation** — how does the product reduce revenue risk, cost overruns, or penalty exposure?
- Reliever 1: [links to Pain X]
- Reliever 2:

**Social and reputational risk mitigation** — how does the product protect the customer's credibility or standing?
- Reliever 1: [links to Pain X]

**Technical risk mitigation** — how does the product reduce integration complexity, security exposure, reliability risk, or data quality issues?
- Reliever 1: [links to Pain X]
- Reliever 2:

### 2.2 Gain Creators
For each essential and delighter gain identified above, describe specifically how the product or feature creates that gain. Classify each creator by dimension.

**Time gains** — how does the product help customers accomplish jobs faster or free up time for higher-value work?
- Creator 1: [links to Gain X]
- Creator 2:

**Financial gains — lower TCO** — how does the product reduce total cost of ownership (licensing, integration, maintenance, training)?
- Creator 1: [links to Gain X]
- Creator 2:

**Capability gains — more services or outcomes** — how does the product expand what the customer can do or deliver to their own stakeholders?
- Creator 1: [links to Gain X]
- Creator 2:

**Usability and accessibility gains** — how does the product make the job easier, more intuitive, or accessible to a wider range of users?
- Creator 1: [links to Gain X]
- Creator 2:

**Delighters (Kano model)** — what unexpected gain creators go beyond what any competitor offers today?
- Delighter 1: [links to Gain X]
- Delighter 2:

---

## Section 3 — Value Proposition Statement

Synthesize the above into a structured value proposition statement:

**For** [customer segment]
**who** [top functional job or critical pain],
**[product name]** is a [product category]
**that** [top 2–3 pain relievers and gain creators],
**unlike** [primary alternative or competitor],
**our product** [key differentiator — the one thing no alternative delivers].

Then write a **one-sentence customer-facing value headline** (plain language, no jargon, customer outcome first):
> "[DRAFT HEADLINE]"

---

## Section 4 — Fit Analysis

### 4.1 Problem–Solution Fit
*Definition: You have evidence that customers care about specific jobs, pains, and gains, and you have designed a value proposition that directly addresses them.*

**Evidence inventory:**

| Evidence Type | Source | What it validates | Strength (Strong / Moderate / Weak) |
|---|---|---|---|
| Customer interviews | [source] | [which jobs/pains/gains] | [strength] |
| Usage data / analytics | [source] | [which behaviors] | [strength] |
| Win/loss analysis | [source] | [which pains competitors fail to address] | [strength] |
| NPS or CSAT verbatims | [source] | [which gains customers value most] | [strength] |
| Support ticket themes | [source] | [which pains are most extreme] | [strength] |

**Fit verdict:** Strong / Partial / Weak
**Gaps:** What evidence is still missing to confirm problem–solution fit?
**Recommended next steps:** [e.g., "Run 5 additional discovery interviews focused on Pain 2 and Pain 3 before committing to build"]

### 4.2 Product–Market Fit
*Definition: You have evidence that the product's pain relievers and gain creators are compelling enough to drive adoption, retention, and expansion within a reachable market.*

**Signals to assess:**

| Signal | Current status | Target benchmark | Gap |
|---|---|---|---|
| Activation rate (% of users who reach first value moment) | [current] | [target]% | [delta] |
| Retention at 30/60/90 days | [current] | [target]% | [delta] |
| NPS or customer satisfaction score | [current] | ≥ [target] | [delta] |
| Expansion revenue or upsell rate | [current] | [target]% | [delta] |
| Organic referrals or word-of-mouth | [current] | [target] | [delta] |
| Churn reason analysis | [current top reason] | Pain relievers address top churn reason | [gap] |

**Fit verdict:** Strong / Partial / Weak
**Gaps:** What signals are missing or below threshold?
**Recommended next steps:** [e.g., "Run a 90-day cohort retention study with Phase 2 preview customers"]

### 4.3 Business Model Fit
*Definition: You have evidence that the value proposition can be embedded in a profitable and scalable business model.*

**Business model dimensions:**

| Dimension | Current state | Fit assessment | Risk |
|---|---|---|---|
| Pricing model | [e.g., per-seat SaaS, consumption-based] | [does pricing capture the value delivered?] | [risk] |
| Willingness to pay | [evidence — e.g., "customers confirmed $X/month in interviews"] | [aligns with cost to deliver?] | [risk] |
| Customer acquisition cost (CAC) | [current or estimated] | [sustainable relative to LTV?] | [risk] |
| Lifetime value (LTV) | [current or estimated] | [LTV:CAC ≥ 3:1?] | [risk] |
| Scalability | [delivery model — e.g., self-serve, high-touch] | [can the model scale without linear cost growth?] | [risk] |
| Competitive moat | [e.g., data network effects, switching costs, IP] | [does the value prop build defensible advantage?] | [risk] |

**Fit verdict:** Strong / Partial / Weak
**Gaps:** What business model assumptions still need validation?
**Recommended next steps:** [e.g., "Run a pricing experiment with 10 prospects to test willingness to pay at $X vs $Y tier"]

---

## Section 5 — Value Proposition Scorecard

| Dimension | Score (1–5) | Rationale |
|---|---|---|
| Job importance — how critical are the jobs addressed? | | |
| Pain severity — how extreme are the pains relieved? | | |
| Gain relevance — how essential are the gains created? | | |
| Uniqueness — how differentiated vs. best alternative? | | |
| Evidence strength — how well validated is this VP? | | |
| Business model viability — how scalable and profitable? | | |
| **Overall VP strength** | **/30** | |

**Recommended action based on score:**
- 25–30: Proceed to build and scale — the VP is well-validated
- 18–24: Proceed with targeted validation — address the lowest-scoring dimensions before GA
- 10–17: Pause and revalidate — significant gaps in evidence or differentiation; risk of building the wrong thing
- Below 10: Pivot — the current framing does not have sufficient customer or business validation
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT_NAME]` | Name of the product or feature | `"Autonomous Threat Response"` |
| `[PRODUCT_DESCRIPTION]` | One-line description of what it does | `"AI-driven containment of security incidents without analyst intervention"` |
| `[CUSTOMER_SEGMENT]` | Specific segment — not "enterprises" but a tight profile | `"SOC managers at financial services firms with 50–200 analysts"` |
| `[EVIDENCE]` | What research or data you already have | `"8 discovery interviews, Q4 NPS verbatims, 2 win/loss reports"` |
| `[COMPETITORS]` | Primary alternatives customers use today | `"CrowdStrike Falcon, manual playbooks, MSSP outsourcing"` |

## Output Variants

**Discovery-first (no evidence yet)** — add to the prompt:
```
We are in early discovery with no customer evidence yet. For each section, generate a hypothesis-first version: what we believe to be true, what evidence would confirm or refute it, and what the highest-priority research question is. Frame the output as a discovery research plan rather than a validated VP canvas.
```

**Executive one-pager** — add to the prompt:
```
Condense the full value proposition canvas into a single-page executive summary: customer segment, top 3 jobs/pains/gains, top 3 pain relievers and gain creators, the value proposition statement, fit verdict for each of the three fit types, and the overall scorecard. Format for a leadership pre-read. No section should exceed 4 bullet points.
```

**Competitive differentiation focus** — add to the prompt:
```
For each pain reliever and gain creator, add a column comparing how the top 2 competitors address the same dimension today. Highlight where our value proposition is clearly superior, at parity, or weaker. Use this to identify the 1–2 differentiators that should anchor all go-to-market messaging.
```

## Tips

- **Specificity beats breadth** — a VP canvas that claims to address 12 pains is addressing none of them well; focus on the 3 most extreme pains and the 2–3 most essential gains
- **Jobs drive everything** — if you are unsure what goes in the pain or gain sections, go back to the job; pains are obstacles to getting the job done, gains are the ideal outcome of getting it done well
- **Pair with the working backwards prompt** — use working backwards to sharpen the customer narrative before running this canvas; the internal press release headline often becomes the VP statement
- **Pair with the Kano analysis prompt** — Kano tells you which gain creators are must-haves vs. delighters; use that output to populate the gain relevance ranking in Section 1.3
- **Business model fit is the most neglected** — most product teams validate problem–solution fit and assume the rest will follow; run the business model fit section explicitly before committing to a pricing or GTM model
- **Revisit at each fit milestone** — the VP canvas is not a one-time artifact; update it when you complete discovery, when you enter private preview, and before GA; the fit verdicts should improve at each stage
