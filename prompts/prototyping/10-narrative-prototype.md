# Narrative Prototype

**Phase:** Prototyping
**Purpose:** Generate a future-state narrative prototype — a written walkthrough of a product experience that does not yet exist — used to validate strategic direction, align stakeholders, and test user desirability before any design or engineering investment. Popular in Amazon-style working-backwards cultures and for AI features that are hard to visualize in wireframes.

## Prompt Template

```
You are a product storyteller helping me write a narrative prototype — a vivid, first-person account of a user experiencing a product or feature that does not yet exist. The goal is to make the future state feel real enough that stakeholders can react to it and users can evaluate whether it solves their problem. Using the context below, generate the complete narrative prototype.

Feature or product being prototyped: [FEATURE_NAME]
Target user persona: [PERSONA — name, role, context, and the core problem they face today]
Today's experience (the painful before): [BEFORE_STATE — describe the current workflow, friction, and cost in specific terms]
Future state (the improved after): [AFTER_STATE — what is fundamentally different when the product exists]
The moment of magic: [MAGIC_MOMENT — the single interaction or outcome that makes the user say "I can't go back to the old way"]
Narrative format: [NARRATIVE_FORMAT — choose one: "day-in-the-life walkthrough" / "before-and-after comparison" / "first use story" / "a week later story"]
Audience for this narrative: [AUDIENCE — e.g. "executive stakeholders at a strategy review", "users in a concept test", "engineering team at a kickoff", "investors"]

---

## Section 1 — Scene Setting

Write a 2–3 paragraph scene-setter that establishes:
- Who [PERSONA] is and what their world looks like
- The specific job or task that is painful today
- The emotional and professional stakes — what goes wrong when this problem is not solved, and what it costs them

Do not introduce the product yet. The reader must feel the problem before they are shown the solution.

---

## Section 2 — The Narrative

Write the full [NARRATIVE_FORMAT] narrative in first-person from [PERSONA]'s perspective. The narrative must:

- Be specific and concrete — name the tool, the meeting, the number, the colleague
- Show the product in use, not as a description of features — the reader should experience it, not be told about it
- Include at least one moment of surprise or delight — something the user did not expect but immediately valued
- Show the [MAGIC_MOMENT] as the emotional high point of the narrative
- End with a tangible outcome — a metric improved, a decision made faster, a risk avoided, a conversation that became easier

Length: [NARRATIVE_LENGTH — e.g. "400–600 words", "2 pages", "5-minute read"]

Write in present tense. No feature names as subject nouns — the user is the subject.

---

## Section 3 — "What Changed" Callouts

After the narrative, produce a structured list of the specific changes between the before and after state. These are the design constraints and requirements implied by the narrative.

| What changed | Before | After | Implied requirement |
|---|---|---|---|
| [Specific interaction or outcome] | [How it worked before] | [How it works in the narrative] | [What the product must do to enable this] |

Generate 6–8 rows. These become the first draft of functional requirements.

---

## Section 4 — Stakeholder Validation Questions

Write 5–7 questions to ask stakeholders or users immediately after they read or hear the narrative. These questions test whether the narrative lands and surfaces objections before any design or engineering begins.

**For desirability (does the user want this?):**
- [Question]
- [Question]

**For credibility (does the user believe it's possible?):**
- [Question]

**For clarity (did they understand the core value?):**
- [Question]

**For prioritization (is this the right problem to solve?):**
- [Question]
- [Question]

**The single most important question for [AUDIENCE]:**
[The one question whose answer would most change the direction of this initiative]

---

## Section 5 — Anti-Narrative (The Skeptic's Read)

Write a short counter-narrative (150–200 words) from the perspective of a skeptical stakeholder who has read the narrative and is unconvinced. The skeptic should raise the 2–3 strongest objections a reasonable person would have:

- [Objection 1 — e.g. "users already have a workflow that works; why would they change?"]
- [Objection 2 — e.g. "this assumes the AI will be accurate enough to trust, which we haven't validated"]
- [Objection 3 — e.g. "the narrative glosses over the data privacy concerns of [PERSONA]'s industry"]

For each objection, write a one-sentence response that either addresses it or acknowledges it as a genuine open question to resolve before building.

---

## Section 6 — Narrative Test Plan

Specify how to use this narrative as a research instrument:

**Format:** [Read aloud by facilitator / sent as written doc / presented as a slide / recorded as a narrated video]

**Audience and session structure:**
- Session length: [minutes]
- Number of participants: [N]
- Stimulus: [how to present the narrative — full read / summary / key excerpts]

**Reaction capture:**
After presenting the narrative, capture:
1. Immediate gut reaction (before questions): "In one word, how does this make you feel?"
2. Desirability score: "On a scale of 1–10, how much would you want this? What would move your score up?"
3. Open questions from Section 4
4. "What would need to be true for you to trust this enough to change your current workflow?"

**Success signal:** [What reaction or response confirms the narrative has landed — e.g. "participant asks when it will be available", "score of 8+ on desirability", "no objections to the magic moment"]
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Feature or product being prototyped | `"AI-assisted annual performance review drafting"` |
| `[PERSONA]` | Target user with name, role, and context | `"Priya, an engineering manager at a 600-person SaaS company who manages 8 direct reports"` |
| `[BEFORE_STATE]` | Current painful workflow | `"Priya spends 4–6 hours each review cycle staring at a blank document, trying to recall specific examples from 12 months ago while juggling her normal sprint load"` |
| `[AFTER_STATE]` | The improved future | `"Priya opens the review tool, sees a pre-drafted review grounded in actual work artifacts from the year, and spends 30 minutes refining rather than 6 hours creating"` |
| `[MAGIC_MOMENT]` | The single high-impact interaction | `"The AI surfaces a specific incident from 9 months ago that Priya had forgotten — and it's exactly the example she needed to make the review fair and credible"` |
| `[NARRATIVE_FORMAT]` | Style of the narrative | `"First use story"` |
| `[AUDIENCE]` | Who will read or hear this | `"CHRO and VP Engineering at a strategy review"` |
| `[NARRATIVE_LENGTH]` | Target length | `"500 words"` |

## Output Variants

**Press release format** — add to the prompt:
```
Write the narrative as an Amazon-style internal press release rather than a first-person walkthrough. Include: headline (one sentence, customer benefit), subheadline (the problem solved), three paragraphs (the problem, the solution, a customer quote), a "Getting Started" section, and a FAQ with 3–5 questions a skeptical executive or engineer would ask. Pair this with the "What Changed" callouts and validation questions from Sections 3 and 4.
```

**Video script format** — add to the prompt:
```
Write the narrative as a 90-second video script for a concept video. Format as: [00:00–00:15] Scene description + narration / [00:15–00:45] Core product interaction scenes with screen description + voiceover / [00:45–01:15] Outcome + emotional resolution / [01:15–01:30] CTA. Include on-screen text callouts and visual direction notes for each scene.
```

**Multi-persona format** — add to the prompt:
```
Write two versions of the narrative for two different personas who interact with the same product in different ways: [PERSONA_1] experiences it as the primary user; [PERSONA_2] experiences it as a stakeholder who receives the output. Show how the product creates value for both, and identify where their experiences intersect.
```

## Tips

- The before-state scene-setting is the most commonly rushed section and the most important — if the reader does not feel the problem, the solution will feel like a nice-to-have rather than a must-have
- Specificity is what separates a compelling narrative prototype from a generic product description — "saves time" is forgettable; "gets 90 minutes back on a Tuesday" is not
- The anti-narrative in Section 5 is a discipline tool — writing the strongest version of the objections yourself prevents stakeholders from dismissing the narrative as one-sided advocacy
- Pair with `04-amazon-pr-faq.md` for the press release variant and `05-wizard-of-oz-protocol.md` when the narrative is ready to be tested as a live session rather than a written document
- For AI features, the magic moment in the narrative almost always reveals the trust requirement — the moment where the user acts on the AI's output is the moment you need to design most carefully
