# Customer Meeting to Team Update

**Phase:** Customer Discovery & Communications
**Purpose:** Transform a raw customer meeting transcript into a structured leadership Slack update and optional Jira ticket descriptions — so the insights from every customer conversation reach the right people quickly, in a format they can act on, without the PM spending an hour writing it up.

## Prompt Template

```
You are a senior product leader converting a customer meeting transcript into a team update and actionable backlog items.

Step 1: Ask the user to paste the meeting transcript.

---

Please paste the transcript from your customer meeting below. Once you share it, I will extract the key insights and generate a structured team update for your leadership audience.

[PASTE TRANSCRIPT HERE]

---

Once the transcript is provided, perform the following analysis:

**Meeting context to extract (if present in the transcript):**
- Customer name and account tier (if mentioned)
- Meeting date and attendees
- Meeting type: [e.g., discovery call, QBR, escalation, product feedback session, exec briefing]

---

## Step 2 — Transcript Analysis

Extract and organize the following from the transcript:

### 1. Customer Environment
Key details about the customer's technical and organizational context:
- Current tools, platforms, or systems in use
- Team structure or scale relevant to the problem area
- Industry, compliance environment, or regulatory constraints mentioned
- Maturity level or sophistication relevant to the solution

### 2. Customer Challenges
The problems they are experiencing today — specifically due to gaps in the current solution or workflow:
- Primary pain point (the most acute problem described)
- Secondary pain points
- Business impact of the problem (cost, risk, time lost, team frustration)
- Workarounds they are currently using
- How long they have had this problem

### 3. Feedback on Our Work
What the customer said — positive, critical, or neutral — about what we are building or have already shipped:
- What they praised or validated
- What they criticized or flagged as insufficient
- Feature or capability gaps they called out explicitly
- Sentiment summary: [Positive / Neutral / Mixed / Negative / Escalation risk]

### 4. Feature and Capability Requests
Specific requests, ideas, or suggestions raised by the customer:

| # | Request | Customer's stated reason | Priority signal | Existing roadmap item? |
|---|---|---|---|---|
| 1 | [feature or capability] | [why they need it] | [High / Med / Low based on language used] | [Yes / No / Unknown] |
| 2 | | | | |
| 3 | | | | |

### 5. Next Steps
Explicit commitments or follow-up actions mentioned in the transcript:

| # | Action | Owner | Due date |
|---|---|---|---|
| 1 | [action] | [PM / CSM / Engineering / Customer] | [date or "TBD"] |
| 2 | | | |

### 6. Strategic Signals
Any broader signals worth flagging to leadership:
- Competitive mentions (which competitors were named and in what context)
- Budget or procurement signals
- Expansion or churn risk indicators
- Escalation language or executive visibility signals
- Potential for case study, reference, or co-development opportunity

---

## Step 3 — Slack Team Update

Generate a structured Slack message for a leadership audience (VP, Director, or C-suite). The update must be scannable in under 90 seconds, under 300 words, and use Slack formatting.

---

*:busts_in_silhouette: Customer Meeting Summary — [CUSTOMER NAME] | [DATE]*

*:mag: Customer Environment*
[2–3 bullet points on the customer's context — team size, current tools, relevant constraints]

*:warning: Key Challenges*
[2–3 bullet points on their primary pain points and business impact — be specific, use their language where possible]

*:speech_balloon: Feedback on Our Work*
[2–3 bullet points on what they said about our product or roadmap — both positive and critical]

*:bulb: Feature Requests*
[2–4 bullet points — one line per request with the customer's stated reason]

*:white_check_mark: Next Steps*
[Bulleted action list with owner and date for each item]

*:bar_chart: Signal*
[1–2 sentences on strategic signals: competitive mentions, churn/expansion risk, or leadership visibility]

*:link: Source*
[Meeting recording / transcript link — or "Transcript pasted below"]

---

## Step 4 — Jira Ticket Generation (Interactive)

After generating the Slack update, ask the following:

---

Would you like me to generate Jira ticket descriptions for the feature requests and action items identified above? (Yes / No)

---

If the answer is Yes, generate a Jira ticket description for each feature request and each PM-owned next step using this format:

---

**Ticket: [FEATURE OR ACTION TITLE]**

**Type:** Story / Task / Bug / Spike
**Source:** Customer feedback — [CUSTOMER NAME], [DATE]
**Priority:** High / Medium / Low

**Summary:**
[One sentence: what needs to be done and why]

**Background:**
[2–3 sentences: what the customer said, what problem it solves, why it matters now. Include the customer's exact language where impactful.]

**Acceptance Criteria:**
- [ ] [Criterion 1 — what done looks like]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Out of scope:**
[What this ticket does NOT cover]

**Customer evidence:**
- Customer: [name or tier]
- Meeting date: [date]
- Verbatim quote (if available): "[quote from transcript]"

**Labels:** `customer-feedback`, `[customer-name]`, `[feature-area]`
**Linked to epic:** [epic name or "TBD"]

---

Repeat this template for each ticket. Order tickets by Priority (High first).
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PASTE TRANSCRIPT HERE]` | The raw transcript from the customer meeting — auto-call notes, Gong/Chorus export, or manual notes | Paste full transcript text |
| `[CUSTOMER NAME]` | Name of the customer or account | `"Acme Corp"` or `"Fortune 500 FSI Customer"` |
| `[DATE]` | Date of the meeting | `"2026-04-22"` |

## Output Variants

**No transcript — notes only** — add to the prompt:
```
I do not have a full transcript. Instead I will provide my meeting notes in bullet form. Treat these notes as the source material and generate the same analysis, Slack update, and Jira tickets as you would from a full transcript. Flag any sections where coverage is thin due to missing notes.
```

**Executive briefing format** — add to the prompt:
```
In addition to the Slack update, generate a one-paragraph executive briefing suitable for a written status report or board update. It should cover: who the customer is, the problem they described, what they said about our product, and what we are doing next. Maximum 100 words. No bullet points.
```

**Multi-customer synthesis** — add to the prompt:
```
I am going to paste transcripts from [N] customer meetings. Analyze all of them together and produce: (1) a cross-customer theme analysis identifying pain points and feature requests mentioned by more than one customer, (2) a single synthesized Slack update that captures the patterns across all meetings, and (3) a consolidated Jira ticket list de-duplicated across customers with a "mentioned by N customers" count on each ticket.
```

**Escalation flag format** — add to the prompt:
```
This meeting had escalation signals. After the standard Slack update, generate a separate escalation summary formatted for a CSM or account executive: customer sentiment score (1–5), primary escalation reason, what the customer said that signals risk, what we committed to in the meeting, and the recommended response timeline.
```

## Tips

- **Use the customer's exact language in Jira tickets** — the verbatim quote field is not optional; engineering teams who see "our analysts spend 4 hours a day on this manually" build differently than teams who see "customer wants automation"
- **Signal section is for leadership, not ops** — the strategic signals (competitive mentions, churn risk, expansion opportunity) are what a VP or GM needs to see; keep them factual and direct, not softened
- **Sentiment summary unlocks CSM action** — the Sentiment field in Step 2 Section 3 is a leading indicator; "Escalation risk" should trigger a CSM follow-up within 24 hours, not just a Slack message
- **Pair with the customer interview guide prompt** — use the interview guide before the meeting to ensure you capture the right information; use this prompt after to turn the notes into action
- **Pair with the sentiment analysis prompt** — if you have a backlog of Jira tickets that mention this customer, run the sentiment analysis prompt on those tickets before the meeting so you walk in knowing the history
- **Pair with the DACI prompt** — if a feature request from this meeting requires a build-vs-defer decision, use the DACI framework to document who makes the call and prevent the request from dying in a backlog
- **300-word Slack limit is a feature, not a constraint** — if leadership needs to read more than 300 words to understand a customer meeting, the message has not been curated; the full analysis lives in the Jira tickets and transcript link
