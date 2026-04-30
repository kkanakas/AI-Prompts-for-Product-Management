# Prompt-Powered UI Generator

**Phase:** Prototyping
**Purpose:** Generate a ready-to-paste prompt for v0.dev, Claude (Artifacts), Lovable, Replit, or Base44 that produces a working, visually realistic UI prototype in minutes — without an engineer. Designed for PMs who need a functional screen to validate ideas with users or stakeholders before any design or development investment.

## Prompt Template

```
You are helping me write a code-generation prompt for a vibe-coding tool (v0.dev, Claude Artifacts, Lovable, or similar). My goal is to generate a working, visually realistic UI prototype I can use for user testing or stakeholder demos — not production code. Using the context below, produce the complete prompt I should paste into the tool.

Screen or feature to build: [SCREEN_NAME — e.g. "dashboard", "onboarding step 2", "AI suggestion panel"]
Product type: [PRODUCT_TYPE — e.g. "B2B SaaS analytics tool", "consumer mobile app", "internal ops dashboard"]
Primary user action on this screen: [PRIMARY_ACTION — the one thing the user comes to this screen to do]
Key components needed: [COMPONENTS — list the UI elements required, e.g. "data table with sorting", "AI suggestion card with accept/reject", "sidebar navigation", "chart"]
Sample data to include: [SAMPLE_DATA — describe realistic placeholder content, e.g. "5 rows of order data with status badges", "3 AI recommendations with confidence scores", "a 30-day line chart for revenue"]
Visual style: [VISUAL_STYLE — e.g. "clean enterprise SaaS like Linear or Notion", "consumer app like Airbnb", "data-dense dashboard like Datadog", "no specific preference"]
Interactions to wire up: [INTERACTIONS — e.g. "clicking a row opens a detail panel", "accept button changes card state to confirmed", "filter dropdown updates the table"]
What this prototype will be used for: [PROTOTYPE_PURPOSE — e.g. "moderated user test", "exec stakeholder review", "sales demo", "internal alignment"]

---

## Output: Code-Generation Prompt

Produce the prompt I should paste into the vibe-coding tool. The prompt must:

1. State the output goal explicitly — "Build a working React prototype for [PROTOTYPE_PURPOSE]. This is not production code — prioritize visual realism and interactivity over code quality."

2. Specify the tech stack simply — React with Tailwind CSS (or shadcn/ui) unless [VISUAL_STYLE] requires otherwise. No backend, no API calls — all data is hardcoded.

3. Define the component inventory precisely — list every component with its content, states, and behavior. Be more specific than "a table" — specify columns, row count, and what clicking a row does.

4. Describe the sample data in detail — provide the exact values to hardcode, not just the shape. Realistic data (real company names, plausible numbers, sensible statuses) makes the prototype feel trustworthy in demos and tests.

5. Specify interaction behavior — for each interactive element, describe the exact state change: what is the before state, what triggers the change, what is the after state.

6. Set visual constraints — describe the layout (sidebar + main content, top nav + cards, split pane), color palette cues, and any component library to use.

7. End with: "Do not add authentication, routing, or database logic. Do not explain the code. Output only the working prototype."

---

## Iteration Prompts

After the initial output, generate three follow-up prompts I can use to refine the prototype:

**Iteration 1 — Add a missing state:**
[Prompt to add the empty state, loading state, or error state most likely to be needed in testing]

**Iteration 2 — Add an interaction:**
[Prompt to wire up the next most important interaction not included in the initial build]

**Iteration 3 — Adjust visual fidelity:**
[Prompt to make the prototype look more polished or more closely match [VISUAL_STYLE] — e.g. adjust typography, spacing, color, or iconography]

---

## Prototype Test Readiness Checklist

Before using this prototype in a user test or stakeholder demo:
- [ ] Sample data looks realistic — no "Lorem ipsum", "test@test.com", or "Company A"
- [ ] Primary action ([PRIMARY_ACTION]) works end-to-end without breaking
- [ ] The prototype opens in a browser without errors
- [ ] All interactive elements in [INTERACTIONS] are wired up or clearly marked as "not yet built"
- [ ] The prototype has been walked through once by someone who did not build it
- [ ] Prototype URL or file is shareable before the session starts
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[SCREEN_NAME]` | The screen or feature being built | `"AI-assisted ticket routing dashboard"` |
| `[PRODUCT_TYPE]` | Type of product | `"B2B SaaS customer support platform"` |
| `[PRIMARY_ACTION]` | The one thing users come to this screen to do | `"Review AI-suggested ticket assignments and accept or reassign"` |
| `[COMPONENTS]` | UI elements needed | `"Ticket queue table, AI suggestion card with confidence score, accept / reassign buttons, status filter"` |
| `[SAMPLE_DATA]` | Realistic placeholder content | `"8 open tickets with customer names, issue categories, AI-suggested assignees, and confidence scores between 72% and 97%"` |
| `[VISUAL_STYLE]` | Desired look and feel | `"Clean enterprise SaaS — think Linear or Intercom. Neutral color palette, generous whitespace."` |
| `[INTERACTIONS]` | Interactions to wire up | `"Accept button changes ticket row to 'Assigned' state. Reassign opens an agent picker modal."` |
| `[PROTOTYPE_PURPOSE]` | How the prototype will be used | `"Moderated usability test with 6 support team leads"` |

## Output Variants

**Mobile prototype variant** — add to the prompt:
```
This prototype is for a native mobile experience. Constrain the output to a 390px wide viewport. Use touch-first interaction patterns: tap targets minimum 44px, bottom sheet instead of modal, swipe gestures where appropriate. Output the prototype as a single scrollable mobile screen, not a desktop layout.
```

**Multi-screen flow variant** — add to the prompt:
```
Build a multi-screen prototype covering the full user flow from [FLOW_START] to [FLOW_END]. Use React Router to link the screens. Build [N] screens: [list screen names]. Each screen transition should be triggered by the primary CTA on the previous screen. Include a "back" button on all screens after the first.
```

**AI feature showcase variant** — add to the prompt:
```
This prototype includes an AI feature. Build the AI response as a timed reveal: when the user submits input, show a 1.5-second loading animation (pulsing skeleton), then replace it with the AI output. Make the AI output feel considered — not instant. Include a "thumbs up / thumbs down" feedback affordance below every AI response.
```

## Tips

- Specificity in sample data is the single biggest lever for prototype quality — "8 support tickets for SaaS companies with names like Meridian Analytics and Cascade Retail, issue types like 'billing dispute' and 'API timeout', and confidence scores between 72% and 97%" produces dramatically better output than "some sample data"
- Ask the tool to output a single file first — multi-file outputs are harder to iterate on and share; start with a single `App.jsx` and refactor only if the prototype is being used long-term
- The iteration prompts are as important as the initial prompt — most good prototypes take 2–3 refinement rounds; generate them upfront so you know where to take it
- For AI feature prototypes, the loading state is not optional — users form their trust assessment during the wait; a prototype that returns AI output instantly trains users to expect unrealistic speed
- Pair with `07-ai-feature-stub.md` to generate the hardcoded AI outputs before pasting into the code-generation prompt
