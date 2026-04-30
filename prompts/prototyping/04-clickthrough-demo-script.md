# Clickthrough Demo Script

**Phase:** Prototyping
**Purpose:** Generate a scene-by-scene demo script and storyboard for a clickthrough product demo built in Arcade, Loom, Demostack, or a similar storytelling tool — used for sales enablement, executive presentations, and marketing without requiring a live product.

## Prompt Template

```
You are a product storyteller helping me script a clickthrough product demo. The demo will be recorded or built as an interactive walkthrough in a tool like Arcade, Demostack, or Loom. It should feel like a real product in use, not a slide deck. Using the context below, generate the complete demo script.

Product or feature name: [PRODUCT_NAME]
Demo audience: [AUDIENCE — e.g. "VP of Sales prospect", "internal exec review", "marketing landing page", "conference keynote"]
Viewer's primary question: [VIEWER_QUESTION — the question the viewer needs answered by the end, e.g. "Can this replace our current tool?", "How does the AI feature work?", "What does onboarding look like?"]
Persona in the demo: [PERSONA — the character using the product in the demo, e.g. "Alex, a sales manager at a 200-person SaaS company"]
Problem to establish: [PROBLEM — the pain or friction the persona experiences before using the product]
Key capability to showcase: [KEY_CAPABILITY — the one or two things that must land for this demo to succeed]
Demo length target: [DEMO_LENGTH — e.g. "90 seconds", "3 minutes", "5 minutes"]
CTA at the end: [CTA — what you want the viewer to do after watching, e.g. "Book a demo", "Start a free trial", "Approve the roadmap item"]

---

## Section 1 — Demo Narrative Arc

Write a three-act narrative arc for the demo:

**Act 1 — Problem (15–20% of demo length):**
Establish the world before your product. Show the friction, the inefficiency, or the risk. Make the viewer nod. Do not show your product yet.

**Act 2 — Resolution (60–70% of demo length):**
Introduce the persona using the product to solve the problem. Show the key capability in action. Make the "before" feel obviously worse than the "after."

**Act 3 — Outcome (15–20% of demo length):**
Show the result — the metric, the saved time, the avoided risk. Land the CTA.

---

## Section 2 — Scene-by-Scene Storyboard

For each scene, produce:

**Scene [N]: [Scene title]**
- Screen shown: [what the viewer sees — specific UI screen, element, or state]
- Narration / caption: [the exact words spoken or shown as text overlay — write in the voice of [PERSONA]'s story, not a feature list]
- Cursor / click action: [what the presenter clicks, highlights, or types — be specific]
- Callout or annotation: [any tooltip, highlight box, or annotation to draw the viewer's eye]
- Duration: [estimated seconds for this scene]
- Transition to next scene: [click / auto-advance / pause for narration]

Generate scenes for all three acts. Aim for [DEMO_LENGTH] total duration.

---

## Section 3 — Narration Script

Write the full narration as a continuous script the presenter reads aloud or records as voiceover. Format it as:

[Scene 1 narration]
[Scene 2 narration]
...

Voice guidelines:
- First person from [PERSONA]'s perspective where possible ("I used to spend an hour on this every Monday…")
- Concrete and specific — name numbers, time saved, and outcomes; never say "seamlessly" or "easily"
- Present tense — the viewer is watching it happen now
- No feature names as the lead — lead with the outcome, follow with the capability

---

## Section 4 — Highlight Callouts

List the 3–5 specific UI moments that deserve a zoom, highlight box, or annotation in the recording tool:

| Scene | Element to highlight | Why it matters to [AUDIENCE] |
|---|---|---|
| [N] | [specific UI element] | [the insight the viewer needs to take away] |

---

## Section 5 — Demo Variants

Produce a short description (2–3 sentences) of how to adapt this demo for two additional audiences:

**Variant A — [AUDIENCE_VARIANT_A, e.g. "technical buyer / IT admin"]:**
[What to show differently, what to cut, what to add]

**Variant B — [AUDIENCE_VARIANT_B, e.g. "end user / individual contributor"]:**
[What to show differently, what to cut, what to add]

---

## Section 6 — Production Checklist

Generate a checklist for building the demo in [RECORDING_TOOL]:
- [ ] Sample data loaded — no placeholder text visible in any scene
- [ ] All scenes scripted before recording begins
- [ ] Screen resolution set consistently across all scenes
- [ ] Narration recorded in one take per act (or per scene) — no spliced audio
- [ ] Callouts and annotations added in post
- [ ] CTA screen or end card built
- [ ] Demo reviewed by someone who has never seen the product — does the problem land before the solution is shown?
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT_NAME]` | Product or feature being demoed | `"Aria — AI Support Assistant"` |
| `[AUDIENCE]` | Who will watch the demo | `"VP of Customer Success at a mid-market SaaS company"` |
| `[VIEWER_QUESTION]` | The primary question in the viewer's head | `"Can this reduce my team's ticket volume without sacrificing CSAT?"` |
| `[PERSONA]` | The character using the product in the demo | `"Jordan, a Support Team Lead managing 12 agents"` |
| `[PROBLEM]` | The friction or pain established in Act 1 | `"Jordan's team spends 40% of their time answering the same 20 questions every week"` |
| `[KEY_CAPABILITY]` | The one or two things that must land | `"AI auto-draft reduces handle time; knowledge base auto-syncs without manual updates"` |
| `[DEMO_LENGTH]` | Target run time | `"3 minutes"` |
| `[CTA]` | What the viewer should do after watching | `"Book a 30-minute live demo"` |
| `[AUDIENCE_VARIANT_A]` | Alternative audience for Variant A | `"IT admin / security reviewer"` |
| `[AUDIENCE_VARIANT_B]` | Alternative audience for Variant B | `"Individual support agent"` |
| `[RECORDING_TOOL]` | Tool used to record or build the demo | `"Arcade"` |

## Output Variants

**Self-serve interactive demo variant** — add to the prompt:
```
This demo will be self-serve — the viewer drives it with clicks, not a presenter. Rewrite the narration as tooltip text and inline annotations. Each annotation should be one sentence maximum. Add branching instructions: after Scene 3, offer the viewer two paths ("See how it works for managers" / "See how it works for agents") and script both branches.
```

**Exec slide embed variant** — add to the prompt:
```
Condense the demo into a 60-second version suitable for embedding in a board or executive review deck. Cut to: one Act 1 scene (the problem), two Act 2 scenes (the key capability in action), one Act 3 scene (the outcome metric). Remove all narration — replace with three on-screen captions of eight words or fewer each.
```

## Tips

- Lead with the problem, not the product — viewers need to feel the pain before they care about the solution; if you open on a feature, you have already lost them
- Use real-sounding sample data — "Acme Corp" and "test@test.com" destroy believability instantly; name the persona's company and use realistic numbers
- Script before recording — improvised demos run long, skip key moments, and require expensive re-records
- The callout list in Section 4 is your editing guide — if a moment is not on the list, it probably does not need a zoom
- Pair with `07-ai-feature-stub.md` if the demo includes an AI feature that does not yet exist — use the stub to generate realistic-looking AI outputs for the demo
