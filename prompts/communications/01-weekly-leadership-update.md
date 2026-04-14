# Weekly Leadership Update Generator

**Phase:** Communications
**Purpose:** Transform raw weekly team notes into a crisp, executive-ready Microsoft Teams or Slack message that surfaces progress, risks, and decisions needed — without burying leadership in detail.

## Prompt Template

```
You are a senior communications advisor helping a Product Manager write a weekly leadership update.

My audience is [AUDIENCE — e.g. VP of Product, C-suite, senior leadership team]. They care about outcomes, risks, and decisions — not task lists or technical detail.

Here is my raw input for this week:

**Product / Initiative:** [PRODUCT OR INITIATIVE NAME]
**Week ending:** [DATE]

**What we shipped or completed this week:**
[BULLET LIST — features released, milestones hit, experiments launched, key decisions made]

**What we are working on next week:**
[BULLET LIST — priorities, planned releases, upcoming decisions]

**Risks or blockers:**
[BULLET LIST — anything slowing the team, dependencies at risk, issues escalated]

**Metrics or signals worth highlighting:**
[ANY DATA — usage numbers, customer feedback, NPS, pipeline impact, support volume]

**Decisions or support needed from leadership:**
[LIST anything you need a decision on, unblocking, or visibility into]

Using this input, write a weekly update message formatted for Microsoft Teams or Slack with the following structure:

---

📅 **Weekly Product Update — [PRODUCT OR INITIATIVE NAME] | Week of [DATE]**

**✅ This Week**
[3–5 bullet points. Lead with outcomes, not tasks. Use past tense. One line each. Bold the most important result.]

**🔜 Next Week**
[3–4 bullet points. Frame as intentions or commitments, not a to-do list.]

**⚠️ Risks & Blockers**
[2–3 bullet points. Be direct. If there is nothing to flag, write "None this week." Do not omit this section.]

**📊 Signal of the Week**
[1–2 sentences. One key metric, customer quote, or trend that tells leadership how the product is performing. Skip if no meaningful data is available.]

**🙋 Decisions Needed**
[Bulleted list of any asks from leadership — approvals, unblocking, visibility. If none, write "No decisions needed this week."]

---

Tone guidelines:
- Write at a VP reading level: confident, direct, no jargon
- Keep the entire message under 250 words
- Avoid passive voice and filler phrases like "we are working towards" or "continued progress on"
- If a risk is real, name it plainly — do not soften it into invisibility
- Do not use acronyms unless they were in my input
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[AUDIENCE]` | Who will read this message | "VP of Product and the CTO" |
| `[PRODUCT OR INITIATIVE NAME]` | What the update is about | "Mobile Checkout Redesign" |
| `[DATE]` | Week ending date | "April 18, 2025" |
| `[BULLET LIST — completed]` | Raw notes on what the team finished | "Shipped A/B test for new cart flow to 10% of users" |
| `[BULLET LIST — next week]` | Rough plan for the coming week | "Full rollout of cart flow if metrics hold" |
| `[RISKS OR BLOCKERS]` | Anything slowing the team | "Data pipeline delay from platform team pushing analytics by 5 days" |
| `[METRICS OR SIGNALS]` | Any numbers or customer feedback | "Checkout completion rate up 3pts in test cohort" |
| `[DECISIONS NEEDED]` | What you need from leadership | "Approval to extend A/B test budget by $10K" |

## Tips

- Paste your raw Jira sprint notes, standup summaries, or bullet-point brain dump directly — the prompt will clean it up
- If you have nothing for a section, write "none" — the AI will handle it gracefully
- Run this on Friday afternoon while the week is fresh; edit the output before sending
- Customize the emoji set to match your company's Teams/Slack culture, or remove emojis entirely for more formal cultures
- For monthly or quarterly updates, expand the "This Week" and "Next Week" sections to "This Month" and "Next Month" and increase the word limit to 400
