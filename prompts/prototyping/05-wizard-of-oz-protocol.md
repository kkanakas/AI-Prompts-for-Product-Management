# Wizard of Oz Test Protocol

**Phase:** Prototyping
**Purpose:** Generate a complete Wizard of Oz test plan — roles, trigger/response library, wizard playbook, session guide, and observation framework — for testing AI features or complex interactions before any model or backend is built.

## Prompt Template

```
You are a UX researcher helping me design a Wizard of Oz (WoZ) prototype test. In this test, a human operator (the "wizard") will simulate the AI or backend system in real time while a participant believes they are interacting with a real product. Using the context below, generate the complete test protocol.

Feature or capability being simulated: [FEATURE_NAME — the AI feature or backend capability the wizard will simulate]
Product context: [PRODUCT_CONTEXT — what the product does and how the user interacts with it]
User task to test: [USER_TASK — the specific task the participant will attempt during the session]
Participant profile: [PARTICIPANT_PROFILE — who the test participants are]
Core hypothesis: [HYPOTHESIS — what you need to learn, e.g. "Users will trust AI-generated recommendations enough to act on them without verification"]
Known AI behavior to simulate: [AI_BEHAVIOR — what the AI is supposed to do, e.g. "suggest the next best action", "summarise a document", "classify an issue as high/low priority"]
Test format: [TEST_FORMAT — moderated in-person / moderated remote / unmoderated]
Number of participants: [PARTICIPANT_COUNT]

---

## Section 1 — Role Definitions

**Participant:** [PARTICIPANT_PROFILE]. Believes they are testing a real product. Has no knowledge that a human is generating the AI responses.

**Wizard (AI simulator):** [Who plays this role — usually a PM, engineer, or researcher who knows the system]. Responsible for monitoring the participant's inputs and injecting AI responses in real time.

**Facilitator:** Conducts the session, reads tasks, probes with follow-up questions, and manages the participant's experience. Never breaks the illusion.

**Observer:** Silent note-taker. Logs participant behavior, hesitations, errors, and verbal reactions on the observation rubric.

Wizard and facilitator must NOT be the same person. They need separate communication channels during the session.

---

## Section 2 — Technical Setup

Specify the minimum technical setup needed to run this WoZ session:

**Participant interface:** [What the participant sees and interacts with — e.g. "Figma prototype", "staging environment with a fake AI response panel", "live web app with a hidden admin panel"]

**Wizard interface:** [How the wizard injects responses — e.g. "separate browser tab with a text field that pushes to the participant's screen", "Slack message that the facilitator reads aloud", "pre-built response card the wizard clicks to display"]

**Communication channel (wizard ↔ facilitator):** [How they coordinate without the participant knowing — e.g. "silent Slack DM", "earpiece", "shared Google Doc open on a second monitor facing away from participant"]

**Latency simulation:** [How to make wizard responses feel like realistic AI latency — e.g. "wizard waits 1.5–2 seconds before injecting response", "add a fake loading spinner that auto-dismisses after 2 seconds"]

---

## Section 3 — Wizard Playbook

The wizard playbook is a pre-built lookup table of participant inputs mapped to AI responses. The wizard uses this to respond consistently across all sessions.

For each anticipated input type, specify:

| Participant input / trigger | AI response to inject | Response quality variant | Notes |
|---|---|---|---|
| [e.g. "User submits a support ticket with clear intent"] | [e.g. Confident AI recommendation with 90%+ relevance] | High confidence | [when to use — e.g. "use for first 2 tasks to establish baseline trust"] |
| [e.g. "User submits an ambiguous query"] | [e.g. AI asks a clarifying question] | Hedged / uncertain | [use to test how users respond to AI uncertainty] |
| [e.g. "User submits something outside the AI's scope"] | [e.g. "I don't have enough information to answer this reliably"] | Low confidence / decline | [use to test graceful degradation] |
| [e.g. "User re-submits after editing their input"] | [e.g. Refined recommendation] | Improved | [shows AI learning — use to test willingness to iterate] |

Generate a full playbook with at least 8–10 response variants covering: high-confidence correct responses, high-confidence wrong responses (to test user skepticism), hedged responses, clarifying questions, and graceful declines.

---

## Section 4 — Session Guide

**Pre-session setup (10 min before participant arrives):**
- [ ] Wizard and facilitator run a dry-run using the playbook
- [ ] Confirm wizard ↔ facilitator communication channel is working
- [ ] Load participant's interface to the correct starting state
- [ ] Confirm latency simulation is working
- [ ] Observer observation rubric is printed or open

**Introduction script (read verbatim):**
"Today you'll be testing [PRODUCT_NAME]. We're interested in how you interact with it naturally — there are no right or wrong answers, and nothing you do will break anything. Please think aloud as you go — tell us what you're looking at, what you expect to happen, and how you feel about what you see. Do you have any questions before we start?"

[Do NOT mention the AI feature specifically. Let the participant discover it naturally.]

**Task prompts (read one at a time — do not advance until the participant has finished or abandoned):**

| Task | Prompt (read aloud) | Success criteria | Time limit |
|---|---|---|---|
| 1 | [Task 1 prompt — written as a realistic goal, not an instruction e.g. "You received a complaint from a customer about a delayed order. How would you handle it using this tool?"] | [What the participant does that signals task completion] | [minutes] |
| 2 | [Task 2 prompt] | [Success criteria] | [minutes] |
| 3 | [Task 3 prompt] | [Success criteria] | [minutes] |

Generate 3–5 tasks that span different confidence levels in the wizard playbook.

**Post-task probes (ask after each task):**
- "What did you expect to happen when you [action]?"
- "How confident are you in that result? Why?"
- "Would you act on that suggestion? What would make you more or less confident?"
- "Was there anything surprising about what the AI did?"

**Post-session debrief (do not reveal the wizard until after debriefing):**
- "What was your overall impression of the AI feature?"
- "Were there moments where you doubted the AI? What triggered that?"
- "If this were a real product you used every day, what would need to be different?"

[Reveal the wizard]: "I want to let you know that the AI responses in this session were generated by a human operator in real time. We do this to test user experience before the AI model is built. Does knowing that change anything about your feedback?"

---

## Section 5 — Observation Rubric

Observers log the following signals for each task:

| Signal | What to watch for | How to log |
|---|---|---|
| Trust | Does the participant act on the AI response without verification? | Y / N / Partial |
| Skepticism | Does the participant question or re-verify the AI output? | Note verbatim reaction |
| Confusion | Does the participant pause, re-read, or express uncertainty? | Note the trigger |
| Frustration | Sighs, repeated clicks, verbal expressions of frustration | Note timestamp and trigger |
| Delight | Positive verbal reaction to an AI output | Note verbatim |
| Recovery | Does the participant recover when the AI gives a poor response? | Y / N — note strategy |
| Latency tolerance | Does the participant comment on or seem bothered by response time? | Note threshold |

---

## Section 6 — Analysis Framework

After all sessions, synthesize findings using this framework:

1. **Trust calibration:** Did participants trust high-confidence responses more than hedged ones? Did they ever trust wrong responses?
2. **Recovery patterns:** How did participants respond to poor AI outputs — did they retry, escalate, or abandon?
3. **Latency threshold:** At what response time did participants show impatience or doubt?
4. **Aha moments:** Were there specific AI responses that generated strong positive reactions? What made them land?
5. **Failure modes:** Which wizard responses triggered skepticism or abandonment? What was the common pattern?
6. **Hypothesis verdict:** Did the evidence support or refute [HYPOTHESIS]? What is the confidence level?
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | The AI or backend capability being simulated | `"AI-suggested next best action for support agents"` |
| `[PRODUCT_CONTEXT]` | What the product does | `"B2B customer support platform used by Tier-1 support agents"` |
| `[USER_TASK]` | The task participants will attempt | `"Resolve a customer complaint about a delayed shipment using the AI assistant"` |
| `[PARTICIPANT_PROFILE]` | Who the test participants are | `"Support agents with 6–18 months of tenure, no prior experience with AI assistants"` |
| `[HYPOTHESIS]` | What you need to learn | `"Agents will act on AI suggestions for routine tickets without independent verification"` |
| `[AI_BEHAVIOR]` | What the AI is supposed to do | `"Surface the most relevant knowledge base article and draft a reply the agent can send with one click"` |
| `[TEST_FORMAT]` | How the session is run | `"Moderated remote via Zoom"` |
| `[PARTICIPANT_COUNT]` | Number of test participants | `"6"` |

## Output Variants

**Async / unmoderated variant** — add to the prompt:
```
This is an unmoderated WoZ session. The wizard will not be present in real time. Instead, pre-generate a fixed set of AI responses for every anticipated input and load them into a decision tree the prototype can serve automatically based on keyword matching. Produce the decision tree and a fallback response for inputs that do not match any branch.
```

**AI trust calibration focus** — add to the prompt:
```
The primary goal of this test is to calibrate how much users trust the AI at different confidence levels. Add a fifth wizard response type to the playbook: "confidently wrong" — a high-confidence AI response that contains a factual error. Design two tasks that will trigger this response. Log specifically whether participants catch the error and how they respond.
```

## Tips

- Never let the wizard and facilitator be the same person — the facilitator must be fully present with the participant; a split-attention facilitator misses the behavioral signals that make WoZ valuable
- The latency simulation is often skipped and always regretted — real AI response times affect trust; a wizard who responds instantly creates unrealistic expectations
- Reveal the wizard at the end, after debriefing — post-reveal reactions often contain the most honest feedback about what the AI needs to do better
- Pair with `07-ai-feature-stub.md` when you need static AI outputs for a demo rather than a live-facilitated test
- Run at least 5 participants — WoZ sessions are expensive but the signal density is extremely high; fewer than 5 makes pattern detection unreliable
