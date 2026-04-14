# Example: Product Strategy Canvas — In-House Legal Contract Management

This is a worked example of the Product Strategy Canvas prompt (`prompts/strategy/01-product-strategy-canvas.md`).

## Filled-In Prompt

```
You are a senior product strategy advisor. I am a Product Manager building a strategy canvas for Clearpath, a contract management platform for in-house legal teams.

Company / Business Context:
Series B SaaS company, $6M ARR, expanding from SMB into mid-market (500–2,000 employee companies), 18-month runway, 35-person team.

Target Customer:
Primary: In-house General Counsel or Senior Legal Counsel at mid-market companies (500–2,000 employees) in the US
Secondary: Sales Operations or RevOps leaders who manage commercial contract volume

Problem We Are Solving:
In-house legal teams at mid-market companies spend 60–70% of their time on contract status follow-ups, version control in email threads, and chasing signatures — not on legal work. They use a patchwork of shared drives, Word redlines, and DocuSign with no single system of record.

Current Solution Landscape:
- Enterprise CLMs (Ironclad, Icertis) — overkill and too expensive for mid-market; 6-month implementations
- DocuSign alone — handles signatures but not negotiation, storage, or visibility
- Shared drives + email — the default; no workflow, no audit trail, no search
- Juro — strong in Europe, SMB-focused, limited enterprise security features

Our Differentiators:
- Deploys in one day — no professional services required
- Built specifically for in-house legal teams, not law firms
- AI-assisted risk flagging trained on commercial contract language
- Transparent per-seat pricing with no implementation fee

Strategic Constraints:
18-month runway, team of 35 (8 in product/engineering), no enterprise sales motion yet, US-only.

12-Month Goal:
Reach $12M ARR by signing 40 mid-market contracts (500–2,000 employee companies) at $25K–$50K ACV.
```

## Generated Output

### 1. Product Vision

We believe in-house legal teams deserve to spend their time on legal judgment — not on chasing contracts through email threads and shared drives.

### 2. Target Customer Profile

| Dimension | Primary Persona | Secondary Persona |
|---|---|---|
| Role & title | General Counsel / Senior Legal Counsel | Head of Sales Ops / RevOps Manager |
| Company type & size | Mid-market US companies, 500–2,000 employees | Same company size; commercial-contract-heavy orgs |
| Primary job to be done | Manage commercial contracts without losing control of versions, deadlines, or approvals | Get contracts out of legal's queue faster to unblock deal closures |
| Biggest frustration today | "I spend more time asking 'where does this stand?' than reviewing contracts" | "Legal is the bottleneck and I have no visibility into what's happening" |
| How they measure success | Reduction in time spent on contract admin; fewer missed renewals; zero compliance surprises | Shorter contract cycle time; fewer escalations to legal |
| Where we find them | Legal operations communities (CLOC), LinkedIn, G2 reviews of Ironclad/Juro | RevOps communities, Salesforce ecosystem events |

### 3. Value Proposition

**Functional value:** Clearpath replaces the email-and-shared-drive patchwork with a single system of record for contract creation, negotiation, approval, and storage — searchable, auditable, and connected to the tools legal and sales already use.

**Emotional value:** Legal teams feel in control and professional rather than reactive and buried. Sales teams feel respected rather than stonewalled.

**Business value:** Mid-market companies reduce contract cycle time by 60%, eliminate missed renewal risk, and pass compliance reviews without scrambling for audit evidence.

**Value Proposition Statement:** For in-house legal teams at mid-market companies who are drowning in contract admin, Clearpath is the contract management platform that gives legal teams full visibility and control from first draft to signed agreement — unlike enterprise CLMs which take six months to implement and cost more than the problem they solve.

### 4. Competitive Positioning Map

**Axes:** Ease of implementation (slow → fast) vs. Depth of legal workflow (basic e-sign → full CLM)

| Player | Position | Why |
|---|---|---|
| Clearpath | Fast implementation + strong legal workflow | Day-one deployment with AI risk flagging and full negotiation workflow |
| Ironclad | Slow implementation + strong legal workflow | 3–6 month enterprise implementations; powerful but complex |
| Juro | Moderate implementation + moderate workflow | Faster than Ironclad but primarily SMB; limited enterprise security |
| DocuSign alone | Fast + shallow | Easy to use but only handles signatures, not negotiation or storage |
| Shared drives + email | Fast + no workflow | Zero implementation cost; zero capability |

**Our defensible position:** The only platform that delivers full contract workflow at implementation speed. Ironclad cannot move down-market without breaking their services model. DocuSign cannot move up-workflow without becoming a CLM.

**Nearest competitive threat:** Juro is expanding upmarket with enterprise security features. We have a 12–18 month window before they close the gap.

**Whitespace:** No player owns the RevOps / Sales Ops buyer alongside legal. Clearpath's dual-persona positioning (legal + sales ops) is uncontested.

### 5. Strategic Bets

| Bet | What we are doing | What we are NOT doing | Why this is the right trade-off |
|---|---|---|---|
| Own mid-market before expanding | Laser-focused on 500–2,000 employee US companies | Not pursuing enterprise (5,000+) or international in the next 12 months | Mid-market is underserved; enterprise requires a sales and implementation motion we cannot afford yet |
| Self-serve implementation as a moat | Investing in deployment simplicity and in-app onboarding | Not building a professional services team | Services revenue is low-margin and slows product-led growth; our speed advantage is only defensible if we keep engineering it |
| Dual-persona go-to-market | Targeting legal and RevOps simultaneously | Not building separate products for each | RevOps is often the economic buyer; legal is the champion — we need both to close mid-market deals efficiently |
| AI risk flagging as a wedge | Shipping AI-assisted clause risk flagging this quarter | Not trying to build a full AI contract lawyer | One sharp, accurate capability builds trust faster than a broad AI feature set that is unreliable |
| Product-led growth with enterprise upsell | Free trial → team plan → enterprise deal | Not leading with outbound enterprise sales | Our 35-person team cannot support a complex sales motion; PLG generates qualified pipeline at lower CAC |

### 6. Key Capabilities Required

| Capability | Current State | Build / Buy / Partner |
|---|---|---|
| Contract workflow engine (create, negotiate, approve, sign) | Have it | Extend — add obligation tracking and renewal alerts |
| AI clause risk flagging | Partially have it (prototype) | Build — train on mid-market commercial contracts |
| Role-based access controls and audit log | Gap | Build — required for mid-market security reviews |
| CRM integration (Salesforce, HubSpot) | Gap | Partner — native integration via API; critical for RevOps persona |
| Self-serve onboarding and in-app setup | Partially have it | Build — must reach day-one value without customer success intervention |

### 7. Success Metrics

| Horizon | Metric | Target | Why it matters |
|---|---|---|---|
| Leading (3 months) | Trial-to-paid conversion rate | 25% (from current 14%) | Proves the self-serve motion is working before we can see ARR impact |
| Leading (3 months) | Time-to-first-contract (new accounts) | Under 2 hours | Validates the day-one implementation claim |
| Growth (6–12 months) | Mid-market ACV deals signed | 40 contracts at $25K–$50K ACV | Core revenue target for the year |
| Growth (6–12 months) | Net Revenue Retention | >110% | Confirms customers are expanding, not churning |
| Strategic (12–24 months) | % revenue from RevOps-influenced deals | >35% | Validates the dual-persona GTM strategy |
| Strategic (12–24 months) | ARR | $12M | Proves mid-market ICP and positions for Series C |

### 8. Risks & Strategic Assumptions

| Assumption | What would invalidate it | 90-day test |
|---|---|---|
| Mid-market legal teams will buy without an enterprise sales rep | Deals consistently stall at security review or procurement approval without human support | Run 10 mid-market PLG trials end-to-end; measure where they stall and whether async support resolves blocks |
| RevOps and legal can be sold together in one motion | RevOps buyers defer entirely to legal; two separate buying processes emerge | Track whether RevOps is in the first call on the next 20 deals; measure deal velocity with vs. without RevOps champion |
| Day-one implementation is a durable differentiator | Juro or Ironclad launch a simplified onboarding track targeting mid-market | Monitor Juro's product announcements and G2 reviews for implementation speed improvements quarterly |
| AI risk flagging is accurate enough to build trust, not erode it | Customer feedback shows false positives reducing confidence in the feature | Track feature adoption rate and NPS for AI risk flagging specifically in the first 30 days post-launch |

### 9. One-Page Summary

**Vision:** In-house legal teams deserve to spend their time on legal judgment — not on chasing contracts through email threads and shared drives.

**Who we serve and what we solve:** General Counsel and RevOps leaders at mid-market US companies (500–2,000 employees) who are losing hours every week to contract admin, missed renewals, and compliance scrambles. We give them a single system of record that replaces the email-and-shared-drive patchwork — and deploys in a day.

**Our differentiated position:** The only platform that delivers full contract workflow at implementation speed — Ironclad's capability without Ironclad's six-month implementation.

**Three strategic bets:**
- Own mid-market before moving upmarket or international
- Keep self-serve implementation as a durable moat by continuing to engineer it
- Sell to legal and RevOps simultaneously — the dual-persona GTM is uncontested

**How we measure success in 12 months:** 40 mid-market contracts signed at $25K–$50K ACV; Net Revenue Retention above 110%.

**Biggest assumption we are betting on:** Mid-market legal teams will buy and activate without a dedicated enterprise sales motion — if that assumption is wrong, we will need to build a sales team six months earlier than planned.

## What to Notice

- The company stage and constraints were specific (35-person team, 18-month runway) — this produced targeted strategic bets rather than generic advice
- Strategic bets explicitly name what the team is *not* doing, which is the harder and more valuable part of strategy
- The 90-day tests in the Risks section are concrete and actionable, not just descriptions of risk
- The One-Page Summary is genuinely self-contained — a VP could read only that section and have the full strategic picture
