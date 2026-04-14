# RACI Stakeholder Map Generator

**Phase:** Stakeholder Management
**Purpose:** Build a RACI matrix and stakeholder influence map to identify supporters, detractors, and the right engagement strategy for a product initiative.

## Prompt Template

```
You are a senior product strategy advisor. I am a Product Manager leading [INITIATIVE] at [COMPANY/TEAM CONTEXT].

I need to build a stakeholder map and RACI matrix to align the right people, surface potential blockers early, and plan my engagement approach.

Here are the key stakeholders I am working with:
[LIST STAKEHOLDERS — name, role, and team for each person]

Using this information, produce the following:

## 1. RACI Matrix
Create a table mapping each stakeholder to one of these roles for this initiative:
- **Responsible** – does the work
- **Accountable** – owns the outcome (one person only)
- **Consulted** – provides input before decisions
- **Informed** – kept up to date on progress

Key activities to map against:
- [ACTIVITY 1 — e.g. "Define requirements"]
- [ACTIVITY 2 — e.g. "Approve scope"]
- [ACTIVITY 3 — e.g. "Build and deliver"]
- [ACTIVITY 4 — e.g. "Go-to-market / launch"]
- [ACTIVITY 5 — e.g. "Post-launch review"]

## 2. Influence & Support Matrix
For each stakeholder, assess:
- **Influence level** – High / Medium / Low (their ability to accelerate or block this initiative)
- **Support stance** – Champion / Supporter / Neutral / Skeptic / Detractor
- **Primary concern or motivation** – what do they care about most?

Present this as a table.

## 3. Engagement Strategy
For each stakeholder, recommend:
- Preferred communication cadence (e.g. weekly sync, async update, monthly review)
- Key message to lead with, tailored to their concern
- One specific action to move a Skeptic or Detractor toward Neutral or Supporter

## 4. Risk Flags
Identify:
- Any gaps in accountability (activities with no clear owner)
- Stakeholders with high influence but low support — these are your top engagement risks
- Any missing stakeholders I should consider adding

## 5. Executive Summary
A 3–4 sentence summary of the stakeholder landscape: who is driving this forward, where the resistance is, and the most important relationship to invest in first.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[INITIATIVE]` | The product initiative or decision you need alignment on | "Redesigning the onboarding flow for enterprise customers" |
| `[COMPANY/TEAM CONTEXT]` | Your org, team, or product area | "B2B SaaS company, 200-person engineering org" |
| `[LIST STAKEHOLDERS]` | Name, role, and team for each person | "Sarah — VP Engineering; James — Head of Sales; Priya — Customer Success Lead" |
| `[ACTIVITY 1–5]` | The key activities or decisions in your initiative | "Define requirements, Approve budget, Build feature, Launch to customers" |

## Tips

- Be explicit about who has budget authority — this often determines who is truly Accountable
- If you have existing signals about someone's stance (past feedback, prior decisions), include them so the AI can refine the engagement strategy
- Run this early in the initiative, before you need alignment — not after resistance surfaces
- Revisit the map at each major milestone; stances shift as the initiative evolves
