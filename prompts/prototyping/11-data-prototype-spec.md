# Data Prototype Specification

**Phase:** Prototyping
**Purpose:** Generate a complete data dashboard prototype specification — insight hypotheses, chart and component inventory, sample data structure, and a user validation plan — for building in Looker, Tableau, Power BI, or a coded prototype to test whether a metric or insight is actually useful to users before investing in production data infrastructure.

## Prompt Template

```
You are a product manager designing a data prototype — a dashboard or analytics view built with sample data to test whether a specific metric, insight, or data visualization is actually useful to users. Using the context below, generate the complete specification.

Dashboard or report name: [DASHBOARD_NAME]
Who will use it: [USER — role, context, and the decision they are trying to make]
Decision this dashboard supports: [DECISION — the specific business decision or action the user should be able to take after seeing this dashboard, e.g. "decide which customer accounts need intervention this week", "determine whether to increase ad spend in a channel", "identify which team members are at capacity"]
Data sources available (or that would need to exist): [DATA_SOURCES — e.g. "CRM (Salesforce)", "product usage events (Mixpanel)", "support tickets (Zendesk)", "manual CSV export from finance system"]
Primary metric the user cares most about: [PRIMARY_METRIC]
Secondary metrics: [SECONDARY_METRICS — 2–4 other metrics that provide context for the primary metric]
Time horizon: [TIME_HORIZON — e.g. "real-time", "daily", "weekly", "trailing 90 days", "fiscal year to date"]
Tool for building the prototype: [PROTOTYPE_TOOL — e.g. "Looker", "Tableau", "Power BI", "Observable", "Retool", "hand-coded React with Recharts", "Google Sheets with charts"]
What "useful" looks like: [USEFULNESS_CRITERIA — e.g. "user can identify the top 3 accounts at risk in under 2 minutes", "user changes their planned action based on what they see", "user says 'I would check this every Monday morning'"]

---

## Section 1 — Insight Hypotheses

Before specifying any charts, define the insights this dashboard should deliver. For each hypothesis:

**Hypothesis [N]: [Short label]**
- Insight statement: [The specific pattern, trend, or signal the user needs to see — e.g. "Accounts that have not logged in for 14+ days are 3x more likely to churn in the next 30 days"]
- Why it matters for [DECISION]: [How this insight connects to the action the user will take]
- Data required: [which fields, metrics, or events from [DATA_SOURCES] are needed]
- Visualization type: [the chart or table type that best communicates this pattern — and why]
- Null hypothesis: [what it means if this insight is NOT visible in the data — is it good news or bad news or missing data?]

Generate 4–6 hypotheses. These are the tests the prototype is designed to run on the data.

---

## Section 2 — Dashboard Layout

Describe the dashboard layout as a structured inventory — no design tool needed.

**Page / tab structure:**
| Tab name | Primary audience | Purpose |
|---|---|---|
| [Tab 1] | [user role] | [what decisions this tab supports] |

**For each tab, specify the component grid:**

**[Tab name]**

| Row | Component | Type | Size | Purpose |
|---|---|---|---|---|
| 1 | [e.g. "At-Risk Accounts KPI"] | Scorecard / KPI tile | [1/4 width] | [surface the single most important number] |
| 1 | [e.g. "Churn Risk Trend"] | Line chart | [3/4 width] | [show the trend over [TIME_HORIZON]] |
| 2 | [e.g. "Account Health Table"] | Data table with filters | [Full width] | [let user drill into individual accounts] |
| 3 | [e.g. "Risk by Segment"] | Bar chart | [1/2 width] | [compare risk across customer segments] |

---

## Section 3 — Component Specifications

For each component in the layout, provide the full specification:

**[Component name]**
- Chart / component type: [exact type — e.g. "grouped bar chart", "sparkline in a table cell", "donut chart", "heatmap", "ranked list with delta indicators"]
- Metric(s) displayed: [primary metric + any secondary metrics shown on the same component]
- Dimensions / breakdowns: [what the X axis, color, or grouping represents — e.g. "X axis: week", "color: customer segment", "rows: individual accounts"]
- Time range: [what time window this component covers — may differ from the global [TIME_HORIZON]]
- Filters available: [what the user can filter by on this component]
- Drill-down: [can the user click through to a detail view? what do they see?]
- Thresholds and alerts: [are any values color-coded or flagged? at what threshold?]
- Tooltip: [what appears when the user hovers over a data point]
- Empty state: [what is shown if there is no data matching the current filters]

---

## Section 4 — Sample Data Specification

Define the sample data needed to make this prototype feel realistic. This data will be hardcoded or generated for the prototype — it is not connected to a real data source.

**For each data entity:**

**[Entity name — e.g. "Customer Accounts"]**

Schema:
| Field | Type | Sample values | Notes |
|---|---|---|---|
| [field name] | [string / number / date / boolean / enum] | [3–5 realistic example values] | [range, format, or distribution notes] |

Row count for prototype: [N rows — enough to make the visualization meaningful without overwhelming]
Distribution guidance: [e.g. "20% high risk, 50% medium risk, 30% low risk — so the risk distribution chart has a meaningful spread", "values should follow a roughly normal distribution around [mean]"]

Generate sample data specs for all entities needed to populate the components in Section 3.

---

## Section 5 — User Validation Plan

Define how to test whether this dashboard is actually useful before building the real data infrastructure.

**Session format:** [moderated / unmoderated / async review]
**Participants:** [N users matching [USER] profile]
**Session length:** [minutes]

**Task prompts (give participants a realistic decision to make using the prototype):**
| Task | Prompt | Success criteria | Time limit |
|---|---|---|---|
| 1 | [e.g. "You have 10 minutes before your Monday morning standup. Which three accounts would you prioritize this week?"] | [User identifies 3 accounts using the dashboard, not from memory] | [2 min] |
| 2 | [e.g. "Your VP wants to know if churn risk has improved or worsened since last month. What do you tell her?"] | [User finds the trend and gives a specific answer] | [3 min] |

**Post-task probes:**
- "How confident are you in the number you just cited? What would make you more confident?"
- "Is there anything you expected to see that wasn't there?"
- "If this were available to you every week, how would it change how you prepare for [DECISION]?"
- "What would you need to add, remove, or change before you'd rely on this dashboard?"

**Usefulness gate:**
The dashboard concept is validated when: [USEFULNESS_CRITERIA] is achieved by [N out of M] participants, AND no participant asks for a metric that is fundamentally different from what was specced.

---

## Section 6 — Data Infrastructure Implications

After validation, this prototype implies the following data requirements. Use this as a brief for the data engineering team:

| Metric or dimension | Source system | Availability (exists / needs instrumentation / needs modeling) | Refresh frequency needed | Owner |
|---|---|---|---|---|
| [PRIMARY_METRIC] | [DATA_SOURCES] | [exists / needs instrumentation / needs modeling] | [real-time / daily / weekly] | [team] |
| [Secondary metric] | | | | |

Flag any metric that requires new instrumentation or modeling — these are dependencies that affect the build timeline and should be surfaced before committing to a launch date.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[DASHBOARD_NAME]` | Name of the dashboard or report | `"Customer Health Monitor — CSM Weekly View"` |
| `[USER]` | Who uses it and what decision they make | `"Customer Success Managers running weekly account reviews — deciding which accounts to proactively reach out to before renewal"` |
| `[DECISION]` | Specific action enabled by the dashboard | `"Identify the 3–5 accounts most at risk of churn or expansion block before Monday morning team standup"` |
| `[DATA_SOURCES]` | Available data | `"Salesforce (account metadata, renewal dates), Mixpanel (product usage events), Zendesk (support ticket volume and CSAT)"` |
| `[PRIMARY_METRIC]` | The metric the user cares most about | `"Health score (composite of usage, support sentiment, and renewal proximity)"` |
| `[SECONDARY_METRICS]` | Supporting metrics | `"Days since last login, open support tickets, NPS score, days to renewal"` |
| `[TIME_HORIZON]` | Time window | `"Trailing 90 days with weekly granularity"` |
| `[PROTOTYPE_TOOL]` | Tool for building | `"Retool with hardcoded JSON data source"` |
| `[USEFULNESS_CRITERIA]` | What "useful" looks like | `"CSM can identify their top 3 at-risk accounts in under 2 minutes without any verbal guidance"` |

## Output Variants

**Executive summary dashboard variant** — add to the prompt:
```
This dashboard is for an executive audience, not a practitioner. Redesign the layout for a 5-minute weekly read: a single page with no more than 6 components. Prioritize directional signals over granular data — each component should answer a yes/no or better/worse question. Add a "key signals this week" text summary component at the top that the AI or a data analyst populates with 3 bullet points before the executive opens the dashboard.
```

**Real-time operational dashboard variant** — add to the prompt:
```
This dashboard is operational — it must reflect data no more than 5 minutes old and will be used in active incident response or live operations. Add latency requirements to each metric (acceptable data age), specify which components should auto-refresh and at what interval, and design an alerting affordance: a component that turns amber/red when a threshold is crossed and sends a notification.
```

## Tips

- The insight hypotheses in Section 1 are the most valuable output of this prompt — a dashboard without hypotheses is a data dump; hypotheses force the team to specify what signal they are looking for before building
- The sample data distribution matters as much as the schema — a dashboard full of all-green metrics teaches users nothing; design the sample data to have meaningful variance across the key dimensions
- The usefulness gate in Section 5 is the most commonly skipped step — teams build dashboards based on what data is available, not what decisions it enables; the validation task reveals whether the two are the same
- Data infrastructure implications in Section 6 are the most important output for engineering — surfacing new instrumentation requirements before committing to a launch date is far cheaper than discovering them mid-sprint
- Pair with `02-ai-product-metrics.md` when the dashboard is tracking AI product performance, and with `01-feature-success-metrics.md` for the broader feature metrics context
