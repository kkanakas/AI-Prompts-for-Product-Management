# TAM / SAM / SOM and Full Competitive Analysis

**Phase:** Market Research
**Purpose:** Produce a rigorous, citation-grounded market sizing (TAM/SAM/SOM), a complete competitive analysis with value chain mapping, inefficiency identification, and an anchored SWOT — sourced exclusively from Gartner, Forrester, IDC, SEC filings (EDGAR), public vendor websites, and well-cited funding databases for private companies.

## Prompt Template

```
You are a senior market researcher with 15 years of experience advising product and strategy teams at enterprise software companies. Your research methodology draws exclusively from:

1. Analyst reports — Gartner, Forrester, IDC (cite report name, year, and analyst where known)
2. SEC 10-K and 10-Q filings via EDGAR (edgar.sec.gov) for publicly traded competitors
3. Official vendor websites and investor relations pages for public companies
4. Funding databases (Crunchbase, PitchBook, CB Insights) for private companies — state which source you are drawing from and the round count / total raised
5. Peer-reviewed or widely cited industry publications (e.g., Harvard Business Review, McKinsey Global Institute) when analyst coverage is absent

Hard constraints:
- Cite the source category and specific document for every quantitative claim.
- Where exact figures are unavailable, state the estimation methodology (top-down analyst extrapolation, bottom-up unit economics, comparable market proxy) and attach a confidence level: High / Medium / Low.
- Do NOT use Wikipedia, blog posts, or unverified news articles as primary sources.
- Before delivering any section, silently triple-check every number for internal consistency (e.g., SAM cannot exceed TAM; SOM cannot exceed SAM).
- After completing the full draft, second-guess your own analysis: identify the single assumption most likely to be wrong and explain how it would change the conclusion. Surface this in the Reflection section.

---

## Inputs

**Solution under analysis:**
[SOLUTION NAME AND DESCRIPTION — include what it does, which customer problem it solves, and the key differentiating mechanism (e.g., "AcmeScan — an AI-powered invoice reconciliation platform that eliminates manual matching for mid-market finance teams by learning from historical ERP data")]

**Primary competitors (public and private):**
[LIST COMPETITORS — name, website or ticker, and whether public or private. Leave blank to let the AI select the top 5 based on the segment.]

**Market segment / use-case focus:**
[SEGMENT — e.g., "AI-powered accounts payable automation for mid-market B2B companies"]

**Geography:**
[GEOGRAPHY — e.g., North America; leave blank for global]

**Target customer profile:**
[ICP — company size, industry verticals, buyer persona; e.g., "CFO and VP Finance at B2B SaaS companies with 200–2,000 employees"]

---

## Output Format

### 1. Executive Summary (write last)
A 200-word C-suite-ready synthesis covering: where this solution sits in the market today, the single most important competitive threat, and the highest-leverage opportunity to capture value. Flag the #1 assumption the entire analysis rests on.

---

### 2. Market Sizing — TAM / SAM / SOM

For each tier, apply both a top-down (analyst-derived) and a bottom-up (unit-economics-derived) methodology, then reconcile the two estimates.

#### 2a. Total Addressable Market (TAM)
- Define the broadest relevant market boundary.
- Top-down estimate: cite the analyst report (Gartner / Forrester / IDC), report title, year, and stated CAGR.
- Bottom-up estimate: [total addressable accounts] × [average contract value] = TAM. Show your unit-economics assumptions.
- Reconciled TAM: present as a range (low / mid / high) with confidence level.

#### 2b. Serviceable Addressable Market (SAM)
- Filter TAM by: geography, segment fit, deployment model, and ICP constraints.
- State each filter and the percentage of TAM it removes.
- Cite any analyst sub-segment data that supports the filter.
- Present SAM as a range with confidence level.

#### 2c. Serviceable Obtainable Market (SOM)
- Apply realistic market-share capture assumptions for years 1, 3, and 5.
- Justify share assumptions against: competitor win rates (from 10-K disclosures or analyst data), sales capacity, and typical enterprise sales cycles.
- Present SOM as a range with confidence level.

| Tier | Low | Mid | High | Confidence | Primary Source | Methodology |
|------|-----|-----|------|------------|----------------|-------------|
| TAM  |     |     |      |            |                |             |
| SAM  |     |     |      |            |                |             |
| SOM (Yr 1) |  |   |    |            |                |             |
| SOM (Yr 3) |  |   |    |            |                |             |
| SOM (Yr 5) |  |   |    |            |                |             |

---

### 3. Competitive Landscape

#### 3a. Competitor Profiles
For each competitor, produce a structured profile. For **public companies**, pull revenue, gross margin, R&D spend, and strategic commentary from the most recent 10-K or 10-Q on EDGAR. For **private companies**, report the number of funding rounds, total capital raised, last known valuation (if disclosed), and the source (Crunchbase / PitchBook / CB Insights).

| Competitor | Public / Private | Funding / Revenue | Key Offering | Primary Segment | Pricing Model | Strategic Moat | Source |
|------------|-----------------|-------------------|--------------|-----------------|---------------|----------------|--------|

#### 3b. Feature and Capability Comparison
Compare each competitor against your solution across the capabilities that matter most to the ICP.

| Capability | [SOLUTION NAME] | Competitor 1 | Competitor 2 | Competitor 3 | Customer Importance |
|------------|----------------|-------------|-------------|-------------|---------------------|

Use: ✓ Full / ~ Partial / ✗ Absent. Rate Customer Importance as Critical / High / Medium / Low.

#### 3c. Positioning Map
Describe (in prose or ASCII) the two dimensions that most differentiate players in this segment. Plot each competitor and your solution. Identify any white space.

---

### 4. Value Chain Analysis

Map the full value chain for this market segment — from raw inputs through to end-customer value delivery. For each stage:

| Value Chain Stage | Activities | Current Primary Players | Cost Share (est.) | Customer Pain Level |
|-------------------|-----------|------------------------|-------------------|---------------------|

Rate Customer Pain Level as High / Medium / Low.

#### 4a. Inefficiency Identification
For each stage where Customer Pain is High or Medium, identify the specific inefficiency (e.g., manual reconciliation, data silos, compliance overhead) and quantify its cost to the customer where evidence exists.

| Stage | Inefficiency | Evidence / Source | Estimated Cost to Customer | Value Capture Opportunity for [SOLUTION NAME] |
|-------|-------------|-------------------|---------------------------|----------------------------------------------|

#### 4b. Where the Solution Can Capture Value
Based on the inefficiency map, identify the top 3 stages where [SOLUTION NAME] has the strongest opportunity to capture durable value. For each:
- Why this stage is structurally underserved
- What the competitive window looks like (open / narrowing / already contested)
- What capability investment is required to win it

---

### 5. SWOT Analysis

Anchor every point to a specific competitor move, analyst finding, 10-K disclosure, or market data point. Avoid generic statements.

| Dimension | Finding | Evidence / Source | Competitor or Market Reference |
|-----------|---------|-------------------|-------------------------------|

Group rows by: **Strengths**, **Weaknesses**, **Opportunities**, **Threats**.

---

### 6. Strategic Implications

Synthesize the analysis into 3–5 prioritized strategic recommendations. For each recommendation:
- State the action
- State the market evidence that makes it urgent
- State the risk of inaction (with a time horizon)

---

### 7. Reflection and Second-Guess

Before finalizing, explicitly:
1. **Identify the single most fragile assumption** in the TAM/SAM/SOM model and quantify how a 50% error in that assumption changes the SOM.
2. **Name the competitor most likely underestimated** in this analysis and explain what information would change the competitive picture.
3. **Flag any data gaps** that, if filled, would materially alter a strategic recommendation.

| # | What to Second-Guess | How It Changes the Analysis | What Would Resolve It |
|---|---------------------|-----------------------------|-----------------------|

---

### 8. Source Inventory

List every source category referenced. For each: what it contributed, its known limitations (recency, geographic bias, vendor self-reporting), and a reliability rating (High / Medium / Low).

| Source | Category | What It Contributed | Limitation | Reliability |
|--------|----------|---------------------|------------|-------------|
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[SOLUTION NAME AND DESCRIPTION]` | What you are analyzing — name, problem solved, differentiating mechanism | "AcmeScan — AI invoice reconciliation for mid-market finance teams" |
| `[LIST COMPETITORS]` | Named competitors with ticker or website and public/private status | "Bill.com (BILL, public), Tipalti (private), Coupa Software (COUP, public)" |
| `[SEGMENT]` | The specific segment or use case to size | "AI-powered accounts payable automation for mid-market B2B" |
| `[GEOGRAPHY]` | Geographic scope for market sizing and PESTLE | "North America" |
| `[ICP]` | Ideal customer profile — size, vertical, buyer | "CFO and VP Finance at B2B SaaS, 200–2,000 employees" |

## Tips

- **Run the Reflection section first mentally.** If you can already name the fragile assumption before the AI does, add it as a constraint — sharper inputs produce sharper sizing.
- **Pair with `03-comprehensive-market-landscape.md`** for PESTLE and macro-trend context to complement the competitive and sizing depth here.
- **Attach 10-K excerpts when possible.** The prompt is designed to work with zero attachments via public sources, but pasting the relevant MD&A or revenue breakdown section from EDGAR dramatically improves accuracy.
- **Use the Value Chain Inefficiency table as your product roadmap input.** The highest-pain, lowest-competition stages are your best bets for the next two quarters of investment.
- **Treat SOM Yr 1 as a board-ready sanity check.** If SOM Yr 1 is larger than your current sales capacity can support, size down before presenting — credibility is lost once a plan is obviously over-indexed.
- **Re-run with updated 10-K data each quarter.** Public-company financials shift fast; stale competitor revenue figures undermine the entire competitive narrative.
