# AI Feature Stub

**Phase:** Prototyping
**Purpose:** Generate a library of hardcoded AI outputs and a structured testing protocol for validating whether users trust and act on AI suggestions — before any model is built. Used in Wizard of Oz sessions, clickthrough demos, and coded prototypes where the AI output is simulated rather than generated.

## Prompt Template

```
You are a product manager designing an AI feature stub — a set of hardcoded AI responses that look and feel like real AI output, used to test whether users trust and act on AI suggestions before the model exists. Using the context below, generate a complete stub library and testing protocol.

AI feature being stubbed: [FEATURE_NAME — what the AI is supposed to do, e.g. "suggest the next best action for a support agent", "summarise a contract", "classify a transaction as fraudulent or legitimate"]
Product context: [PRODUCT_CONTEXT — the product, user, and task context]
User action that triggers the AI: [TRIGGER_ACTION — what the user does to invoke the AI, e.g. "opens a ticket", "uploads a document", "initiates a checkout"]
Format of the AI output: [OUTPUT_FORMAT — how the AI response appears in the UI, e.g. "a ranked list of 3 suggestions", "a one-paragraph summary with key points highlighted", "a confidence score badge with a short rationale"]
Prototype or test it will be used in: [PROTOTYPE_TYPE — e.g. "Wizard of Oz session", "v0.dev prototype", "Arcade demo", "Figma clickthrough"]
Trust hypothesis: [TRUST_HYPOTHESIS — what you are trying to learn about user trust, e.g. "users will accept AI suggestions for routine cases without reading the rationale", "users will distrust AI when confidence is below 80%"]

---

## Section 1 — Stub Response Library

Generate a library of [12–15] hardcoded AI responses covering the full confidence and quality spectrum. For each stub:

**Stub [N]: [Short label]**
- Trigger scenario: [the specific input or context that would produce this response in a real AI]
- AI output (exactly as it appears in the UI): [the full text, label, score, or structured output — write it in the voice and format of the real AI feature]
- Confidence level: [High / Medium / Low — or a numeric score if the UI shows one]
- Quality classification: [Correct / Plausible but wrong / Incomplete / Outside scope]
- When to use in testing: [which task or scenario this stub is paired with]
- Expected user reaction: [what you predict the user will do — accept, verify, reject, ask a question]

Ensure the library includes:
- 4–5 high-confidence, correct responses (establishes baseline trust)
- 2–3 high-confidence, plausible-but-wrong responses (tests skepticism — will users catch it?)
- 2–3 medium-confidence, hedged responses (tests tolerance for uncertainty)
- 2 low-confidence or declined responses ("I don't have enough information to answer reliably")
- 1–2 out-of-scope responses (tests graceful degradation)

---

## Section 2 — Output Format Spec

Specify exactly how each AI response should be rendered in the prototype. This spec is handed to the engineer, designer, or code-generation tool.

**Response card structure:**
| Field | Content | Display rules |
|---|---|---|
| AI label | [e.g. "AI Suggestion", "Aria recommends", "Auto-classified"] | Always visible; use a distinct color or icon to signal AI origin |
| Primary output | [the main recommendation, summary, or classification] | Max [N] lines before truncation with "show more" |
| Confidence indicator | [score / bar / label / none] | [only show if above X% / always show / show on hover] |
| Rationale | [1–2 sentence explanation of why the AI made this recommendation] | [always visible / collapsed / on hover] |
| Feedback affordance | [thumbs up / thumbs down / flag / none] | Always visible below the response |
| Action buttons | [Accept / Dismiss / Edit / Reassign] | Primary action is highest visual weight |

**State variants to design:**
- Loading state: [description of the skeleton or spinner shown while the AI "processes"]
- Success state: [the response card as described above]
- Accepted state: [what changes in the UI after the user accepts]
- Dismissed state: [what changes in the UI after the user dismisses]
- Error state: [what shows if the AI cannot generate a response]

---

## Section 3 — Trust Testing Protocol

Use this protocol to test whether users act on AI suggestions during [PROTOTYPE_TYPE] sessions.

**Primary observation: trust signal matrix**

| Behavior | What to log | Trust signal |
|---|---|---|
| User accepts without reading rationale | Y / N | High trust |
| User reads rationale before accepting | Y / N | Moderate trust — verify-then-act |
| User independently verifies before accepting | How they verify | Low trust — AI is a hint, not an answer |
| User ignores or dismisses the suggestion | Y / N | Distrust or irrelevance |
| User catches a plausible-but-wrong response | Y / N | Healthy skepticism |
| User does not catch a plausible-but-wrong response | Y / N | Over-trust — risk signal |
| User explicitly comments on the AI | What they say | Voice-of-user signal |

**Task design:**
For each stub quality level, pair it with a task prompt that creates a realistic decision context. Generate [5–6] task prompts:

| Task | Stub used | What you are testing |
|---|---|---|
| [Task prompt] | [Stub N — high confidence, correct] | Baseline acceptance behavior |
| [Task prompt] | [Stub N — high confidence, wrong] | Whether users catch AI errors |
| [Task prompt] | [Stub N — medium confidence] | Tolerance for uncertainty |
| [Task prompt] | [Stub N — declined] | Response to AI limitations |

**Post-task probes:**
- "How confident were you in the AI's suggestion? What made you more or less confident?"
- "Did you do anything to verify the suggestion before acting on it?"
- "Was there anything the AI missed?"
- "Would you trust this feature in your day-to-day work? What would need to change?"

---

## Section 4 — Stub Maintenance Plan

Stubs become stale as the product and user mental models evolve. Specify:

**When to update the stub library:**
- Before each new round of user testing
- When the production AI model produces outputs significantly different from the stubs
- When user feedback reveals gaps in scenario coverage

**How to transition from stubs to real AI:**
1. Shadow mode: run the real AI in parallel with the stub; compare outputs before surfacing to users
2. Gradual replacement: substitute real AI outputs for stubs one scenario at a time, starting with high-confidence cases
3. Decommission: remove the stub infrastructure once the real AI covers [N]% of scenarios at acceptable quality
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | What the AI is supposed to do | `"Suggest the most relevant knowledge base article and draft a reply for a support agent"` |
| `[PRODUCT_CONTEXT]` | Product, user, and task context | `"B2B SaaS support platform; Tier-1 agents handling 80+ tickets per day"` |
| `[TRIGGER_ACTION]` | What the user does to invoke the AI | `"Agent opens a new inbound support ticket"` |
| `[OUTPUT_FORMAT]` | How the AI response appears in the UI | `"A suggested reply draft with an editable text field, a KB article citation, and a confidence badge"` |
| `[PROTOTYPE_TYPE]` | Where this stub will be used | `"Wizard of Oz session with 6 support agents"` |
| `[TRUST_HYPOTHESIS]` | What you are learning about user trust | `"Agents will send the AI-drafted reply without editing for tickets classified as 'routine'"` |

## Output Variants

**Multimodal AI stub variant** — add to the prompt:
```
The AI output includes non-text elements: [charts / images / structured data / code snippets]. For each stub, specify the visual or structured output alongside the text response. Generate sample chart data (as a JSON array), sample structured outputs (as a table), or sample code snippets as appropriate. These are hardcoded values to embed in the prototype — not real model outputs.
```

**Agentic AI stub variant** — add to the prompt:
```
This AI feature involves multi-step agentic behavior — the AI performs a sequence of actions, not just a single response. For each stub, generate a step-by-step "action trace" that shows what the agent did before producing the output: [Step 1: retrieved X / Step 2: evaluated Y / Step 3: generated Z]. This trace appears in a collapsible "How did the AI get here?" panel in the UI. Users can inspect it to build trust in agentic decisions.
```

## Tips

- The plausible-but-wrong stubs are the most valuable in the library — if users never catch them during testing, you have a trust calibration problem that will be much more expensive to discover in production
- Confidence scores change user behavior dramatically — test with and without them; some users overtrust high scores, others ignore anything below 90%
- Write stubs in the exact voice and format of the final AI — "AI Suggestion: reassign to Tier-2" reads differently than "Based on similar tickets, I recommend escalating this to Tier-2 (87% confidence)" even if the action is the same
- Pair with `05-wizard-of-oz-protocol.md` for live facilitated testing and `06-prompt-powered-ui.md` for embedding stubs into a coded prototype
- Keep the stub library versioned — when the real model launches, compare its outputs to the stubs to measure how closely the prototype predicted real model behavior
