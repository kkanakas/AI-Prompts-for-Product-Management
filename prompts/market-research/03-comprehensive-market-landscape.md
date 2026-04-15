# Comprehensive Market Landscape Analysis

**Phase:** Market Research
**Purpose:** Produce a C-suite-ready market landscape covering trends, SWOT, PESTLE, and information gaps — grounded in public analyst and vendor sources.

## Prompt Template

```
You are a senior market research analyst specializing in [INDUSTRY SECTOR]. Your research methodology draws exclusively from public-domain sources including:
- Analyst reports (e.g., Gartner, Forrester, IDC)
- Primary vendor documentation and press releases from [KEY VENDORS]
- Data aggregators such as Statista, Crunchbase, and PitchBook
- Regulatory and government publications relevant to the sector

Constraints:
- Cite the source category (analyst report, vendor documentation, regulatory filing, etc.) for every claim.
- Where exact data is unavailable, state your assumption and confidence level explicitly.
- Prioritize analytical depth over breadth — do not pad with filler.

---

**Company / feature under analysis:**
[COMPANY OR FEATURE DESCRIPTION — include what it does, who it targets, and what problem it solves]

**Primary competitors:**
[LIST COMPETITORS — or leave blank to default to the top 3–5 publicly traded or analyst-tracked vendors in this segment]

**Market segment / use-case focus:**
[MARKET SEGMENT — e.g., endpoint security, workflow automation, observability, identity management, etc.]

**Geography (if relevant):**
[GEOGRAPHY — e.g., North America, EMEA, global; leave blank for global default]

---

Using only the sources and constraints above, produce the following sections:

## 1. Executive Summary
A 200-word C-suite-ready synthesis of where this company/feature sits in the market today and the single most important strategic implication. Write this last so it reflects the full analysis.

## 2. Market Trends
Identify 5–7 macro and micro trends shaping this segment over the next 18–36 months. Present as a table:

| # | Trend | Source / Signal | Materiality to Our Company | Rationale |
|---|-------|-----------------|---------------------------|-----------|

Rate Materiality as High / Medium / Low.

## 3. SWOT Analysis
Assess the company/feature against the named competitors. Anchor every point to a specific competitor move, analyst finding, or market data point — avoid generic statements.

| Dimension | Finding | Evidence / Source | Competitor Reference |
|-----------|---------|-------------------|---------------------|

Group rows by Strengths, Weaknesses, Opportunities, and Threats.

## 4. PESTLE Analysis
Evaluate the business environment across Political, Economic, Social, Technological, Legal, and Environmental dimensions as they apply to this market segment and geography. For each dimension, identify the top risk and top opportunity.

| Dimension | Top Risk | Top Opportunity | Impact Horizon |
|-----------|----------|-----------------|----------------|

Use Short-term (< 12 months), Medium-term (1–3 years), or Long-term (3+ years) for Impact Horizon.

## 5. Information Gap Analysis
Identify 3–5 gaps in the information provided (ambiguities, missing context, unstated assumptions) that would materially affect the quality of this analysis. For each gap:

| # | What Is Missing | Why It Matters | Best-Reasoned Assumption |
|---|----------------|----------------|--------------------------|

Provide a reasoned assumption for each gap so the analysis remains actionable without further clarification.

## 6. Appendix — Source Inventory
List every source category referenced, what it contributed to the analysis, and any known limitations (e.g., recency, geographic bias, vendor self-reporting).
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[INDUSTRY SECTOR]` | The broad industry your company operates in | "Software and Information Technology — cybersecurity" |
| `[KEY VENDORS]` | Major vendors whose public documentation should be mined | "Microsoft, AWS, GCP,Others" |
| `[COMPANY OR FEATURE DESCRIPTION]` | What you are analyzing — include what it does, who it serves, and the problem it solves | "Acme Endpoint Shield — an endpoint detection and response platform for mid-market enterprises that reduces mean time to remediate from days to minutes" |
| `[LIST COMPETITORS]` | Named competitors to benchmark against; leave blank to let the AI select the top 3–5 | "CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne Singularity" |
| `[MARKET SEGMENT]` | The specific segment or use case to focus the analysis on | "endpoint detection and response (EDR)" |
| `[GEOGRAPHY]` | Geographic scope for PESTLE and regulatory analysis | "North America" |

## Tips

- **Start with the Gap Analysis output.** Fill the gaps it identifies and re-run for a sharper second pass — this is the highest-leverage refinement step.
- **Pair with the Evidence and Contradictions prompt** (`02-evidence-and-contradictions.md`) to stress-test any surprising finding before presenting to leadership.
- **Attach real documents when possible.** The prompt is designed for zero-attachment use via public sources, but attaching actual analyst reports or competitor teardowns dramatically improves specificity.
- **Narrow the geography** if your go-to-market is regional — a global PESTLE dilutes actionability for teams operating in a single regulatory environment.
- **Re-run quarterly.** Market landscapes shift faster than annual planning cycles; treat this as a living artifact, not a one-time deliverable.
