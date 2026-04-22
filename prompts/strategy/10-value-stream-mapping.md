# Value Stream Map Generator

**Phase:** Strategy / Discovery / Process Improvement
**Purpose:** Build a complete Value Stream Map (VSM) for a product or feature — identifying every step from customer request to delivered value, surfacing waste, bottlenecks, and wait time, then producing a future-state map with a prioritized improvement roadmap.

## Prompt Template

```
You are a senior lean product consultant. I am a Product Manager mapping the value stream for [PRODUCT OR FEATURE NAME], which is [DESCRIPTION].

Use the inputs I provide below to build a complete Value Stream Map. Start with the current state, identify waste and bottlenecks, then design an improved future state. Where I have left a field sparse, make reasonable inferences from the surrounding context — but flag every assumption so I can validate it.

---

**What We Are Mapping:**
[THE PRODUCT, FEATURE, OR END-TO-END PROCESS — e.g. "the journey from a customer submitting a support ticket to the issue being resolved" or "the flow from a feature idea to it being live in production"]

**Customer / End User:**
[WHO RECEIVES THE VALUE AT THE END OF THIS STREAM — e.g. "enterprise customer's IT admin", "internal data analyst", "end consumer"]

**Trigger (Start of Stream):**
[WHAT KICKS OFF THE PROCESS — e.g. "customer submits a request", "PM adds a feature to the backlog", "bug is reported in production"]

**Outcome (End of Stream):**
[WHAT DOES "DONE" LOOK LIKE FROM THE CUSTOMER'S PERSPECTIVE — e.g. "customer's issue is resolved and confirmed", "feature is live and the customer can use it"]

**Process Steps (Current State):**
List every step in the current flow in order. For each step provide as much as you know:

Step 1: [STEP NAME]
- Team or role responsible: [WHO]
- Typical process time (active work): [MINUTES / HOURS / DAYS]
- Typical wait time before this step begins: [MINUTES / HOURS / DAYS]
- Work in progress (WIP) limit or queue depth: [NUMBER or UNKNOWN]
- Tools or systems used: [LIST]
- Handoff method: [HOW WORK IS PASSED TO THE NEXT STEP — e.g. email, Jira ticket, Slack, automated trigger]
- Known issues or pain points: [DESCRIPTION or NONE]

(Repeat for each step)

**Rework Loops:**
[DESCRIBE ANY STEPS WHERE WORK COMMONLY GETS SENT BACK — e.g. "designs sent back to discovery after engineering review", "PRs failing QA and returning to dev"]

**Key Metrics (if known):**
- Total lead time (trigger to outcome): [DAYS / WEEKS]
- Total process time (active work only): [HOURS / DAYS]
- On-time delivery rate: [% or UNKNOWN]
- Defect or rework rate: [% or UNKNOWN]
- Customer satisfaction at end of stream: [CSAT / NPS or UNKNOWN]

**Strategic Goal for This Stream:**
[WHAT OUTCOME ARE YOU TRYING TO IMPROVE — e.g. "cut lead time by 50%", "eliminate customer escalations", "reduce engineering toil so the team can ship faster"]

---

Using this input, generate the following value stream analysis:

---

## PART 1 — Current State Map

### 1.1 Stream Overview
Summarize the full flow in one paragraph: what triggers it, who touches it, how many steps, and the total observed lead time vs. process time. Calculate and state:
- **Process Cycle Efficiency (PCE)** = Total Process Time / Total Lead Time × 100
- A PCE below 25% typically signals significant waste in the stream.

### 1.2 Step-by-Step Current State Table

| # | Step Name | Owner | Process Time | Wait Time | Cumulative Lead Time | WIP / Queue | Handoff Method | Known Issues |
|---|---|---|---|---|---|---|---|---|

### 1.3 Current State Flow Diagram (Text)
Render the stream as a left-to-right text diagram showing:
- Each step as a box: [STEP NAME | PT: X | WT: X]
- Arrows between steps labeled with the handoff method
- Rework loops shown as back-arrows with a label
- Customer at the far right receiving value

Example format:
```
[Trigger] → [Step 1 | PT:2h | WT:1d] --Jira--> [Step 2 | PT:4h | WT:2d] → ... → [Customer ✓]
                                          ↑___rework (30%)___|
```

### 1.4 Waste Identification
Analyze the stream using the 8 lean waste categories. For each waste type found, describe the specific instance, its estimated impact, and the root cause:

| Waste Type | Definition | Instance Found in This Stream | Estimated Impact | Root Cause |
|---|---|---|---|---|
| **Defects** | Rework, errors, failures requiring correction | | | |
| **Overproduction** | Doing more than the customer needs, too early | | | |
| **Waiting** | Idle time between steps | | | |
| **Non-utilized talent** | Skills, knowledge, or creativity not leveraged | | | |
| **Transportation** | Unnecessary handoffs or tool-switching | | | |
| **Inventory** | Work piling up in queues, unfinished features | | | |
| **Motion** | Unnecessary steps, approvals, or meetings | | | |
| **Extra processing** | Work that adds no customer value | | | |

### 1.5 Bottleneck Analysis
Identify the top 1–3 bottlenecks (the steps constraining overall throughput). For each:
- **Step name**
- **Why it is the bottleneck**: longest wait time, highest WIP, most rework, single point of failure, etc.
- **Downstream effect**: what backs up or slows because of this constraint
- **Current workarounds teams use** (if any)

---

## PART 2 — Future State Map

### 2.1 Design Principles Applied
Before redesigning, state the guiding principles for the future state (e.g. pull over push, eliminate handoffs, automate repetitive steps, reduce batch size, apply WIP limits). Explain why each applies to this stream.

### 2.2 Proposed Improvements
For each improvement, be specific about what changes and why:

| # | Improvement | Steps Affected | Type of Change | Expected Impact | Effort to Implement | Priority |
|---|---|---|---|---|---|---|
| | | | Eliminate / Automate / Merge / Reorder / Timebox / Add WIP limit | Reduce wait / reduce rework / increase flow | Low / Medium / High | Must / Should / Could |

### 2.3 Future State Step Table

| # | Step Name | Owner | New Process Time | New Wait Time | New Cumulative Lead Time | Changes Made |
|---|---|---|---|---|---|---|

### 2.4 Future State Flow Diagram (Text)
Render the improved stream in the same format as 1.3. Highlight removed steps with a strikethrough note, merged steps, and new automation triggers.

### 2.5 Future State Metrics Projection

| Metric | Current State | Future State | Improvement |
|---|---|---|---|
| Total lead time | | | |
| Total process time | | | |
| Process Cycle Efficiency | | | |
| Number of handoffs | | | |
| Rework rate | | | |
| Steps in stream | | | |

---

## PART 3 — Improvement Roadmap

### 3.1 Phased Roadmap
Sequence the improvements into three phases based on effort, dependency, and impact:

**Phase 1 — Quick Wins (0–4 weeks)**
Changes that require no tooling investment, can be decided by the team, and will show results fast.

| Action | Owner | Success Signal |
|---|---|---|

**Phase 2 — Structural Improvements (1–3 months)**
Changes that require process redesign, new agreements between teams, or lightweight tooling.

| Action | Owner | Dependencies | Success Signal |
|---|---|---|---|

**Phase 3 — Systemic Changes (3–6 months)**
Changes that require significant tooling, org alignment, or platform investment.

| Action | Owner | Dependencies | Investment Required | Success Signal |
|---|---|---|---|---|

### 3.2 Measurement Plan
Define how you will track improvement. For each key metric, specify:
- Baseline (current state value)
- Target (future state value)
- How it will be measured (tool, report, or manual count)
- Review cadence

| Metric | Baseline | Target | How Measured | Review Cadence |
|---|---|---|---|---|

### 3.3 Risks & Watch-outs
List the top 3 risks to achieving the future state:
- The risk
- What would trigger it
- How to mitigate or respond

### 3.4 Executive Summary
Write a concise summary (suitable for a leadership review or a team kickoff) that includes:
- What stream was mapped and why it matters
- The single biggest source of waste or delay found
- The most impactful change in the future state design
- The projected improvement in lead time and PCE
- The first three actions the team should take next week
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT OR FEATURE NAME]` | What is being mapped | "Customer Onboarding" or "Feature Delivery Pipeline" |
| `[DESCRIPTION]` | One-sentence context | "The end-to-end flow from contract signed to customer active in the product" |
| `[CUSTOMER / END USER]` | Who receives the value | "New enterprise customer's admin user" |
| `[TRIGGER]` | What starts the stream | "Contract is marked closed-won in Salesforce" |
| `[OUTCOME]` | Definition of done | "Customer has logged in and completed first key action" |
| `[PROCESS STEPS]` | Each step with time data | See template above — the more data you provide, the sharper the analysis |
| `[STRATEGIC GOAL]` | The improvement target | "Reduce onboarding lead time from 14 days to 3 days" |

## Tips

- **Lead time is what customers feel; process time is what teams see.** The gap between them is where waste lives. A high ratio of wait time to process time is your clearest signal that handoffs and queues are the problem, not team speed.
- You do not need perfect data to start. Rough estimates per step are enough to identify the biggest bottlenecks — precision can come after the first round of improvements.
- Map with the team that does the work, not just from memory. The people in each step know the actual wait times and workarounds better than any document does.
- Rework loops are almost always underestimated. Ask "how often does work come back?" for every step — teams tend to normalize rework they experience daily.
- Resist the urge to redesign everything at once. The Phase 1 quick wins build credibility and momentum for the harder structural changes in Phase 2 and 3.
- After the future state is live, re-map after 90 days. Real flows always differ from designed flows, and the second map reveals what the first redesign missed.
- Value stream mapping works best when paired with customer journey mapping — the VSM shows internal flow efficiency, while the CJM shows how that efficiency (or lack of it) lands with the customer.
