# API-Connected Prototype Spec

**Phase:** Prototyping
**Purpose:** Generate a complete specification for connecting a real LLM API to a rough front-end prototype — covering system prompt design, conversation schema, frontend component requirements, and a test scenario matrix — so PMs can test actual model behavior with users before investing in a full build.

## Prompt Template

```
You are a product manager building an API-connected prototype — a rough front-end wired to a real LLM API (OpenAI, Anthropic, Google Gemini, or similar) to test actual model behavior with users. This is not production code. The goal is to learn whether the model performs well enough for users to trust and act on its outputs. Using the context below, generate the complete prototype specification.

AI feature being tested: [FEATURE_NAME — what the AI is supposed to do for the user]
LLM provider and model: [LLM — e.g. "Anthropic Claude Sonnet", "OpenAI GPT-4o", "Google Gemini 1.5 Pro"]
User interaction pattern: [INTERACTION_PATTERN — e.g. "single-turn: user inputs X, AI outputs Y", "multi-turn chat", "document upload then Q&A", "background processing with result display"]
User task to support: [USER_TASK — what the user is trying to accomplish]
Inputs the user provides: [USER_INPUTS — what the user types, uploads, or selects]
Expected AI output format: [OUTPUT_FORMAT — e.g. "structured JSON parsed into a card UI", "free-text response in a chat bubble", "a ranked list with explanations", "a filled document template"]
What success looks like: [SUCCESS_CRITERIA — how you will know the model is performing well enough in testing]
What failure looks like: [FAILURE_CRITERIA — hallucination patterns, refusals, or output quality issues that would block launch]

---

## Section 1 — System Prompt Design

Write the production-candidate system prompt for this prototype. The system prompt must:

1. Define the AI's role and persona in one sentence
2. State the task it is performing and the output format it must produce
3. Specify any constraints (what it must never do, what it must always do)
4. Define how it handles out-of-scope inputs
5. Specify the tone and response length

**System prompt:**
```
[Generate the full system prompt here]
```

**Prompt engineering notes:**
- Variables to inject at runtime: [list any placeholders like {user_name}, {context_document}, {product_name} that will be substituted before sending]
- Context window budget: [how much of the context window is reserved for system prompt vs. user message vs. retrieved context vs. conversation history]
- Temperature setting: [recommended temperature and why — lower for factual/structured output, higher for creative tasks]

---

## Section 2 — Conversation Schema

Define the message structure for the API call.

**Request schema:**
```json
{
  "model": "[LLM model ID]",
  "system": "[system prompt from Section 1]",
  "messages": [
    {"role": "user", "content": "[USER_INPUTS]"}
  ],
  "max_tokens": [N],
  "temperature": [X]
}
```

**For multi-turn interactions:** specify how conversation history is managed:
- Maximum turns to retain in context: [N]
- Summarization strategy if history exceeds context window: [truncate oldest / summarize / sliding window]
- How user context (account data, prior sessions) is injected: [prepended to system prompt / injected as a tool result / not used]

**Response handling:**
- Expected response format: [raw text / JSON / markdown / structured output with schema]
- Parsing logic: [how to extract the display content from the raw API response]
- Error responses to handle: [rate limit, context length exceeded, content policy refusal, timeout]

---

## Section 3 — Frontend Component Specification

Specify the minimum UI needed to test this prototype. This spec is used with a vibe-coding tool (v0.dev, Claude Artifacts, Lovable) or handed to an engineer.

**Input components:**
| Component | Type | Placeholder / label | Validation | On submit |
|---|---|---|---|---|
| [e.g. Text input] | [text / textarea / file upload / dropdown] | [label] | [required / max length / file type] | [send to API] |

**Output components:**
| Component | Displays | Loading state | Error state |
|---|---|---|---|
| [e.g. Response card] | [AI output field] | [skeleton / spinner / "Thinking…"] | [error message + retry button] |

**Interaction flow:**
1. User [action] → [input component]
2. Prototype sends API request with [USER_INPUTS] + system prompt
3. Loading state shown: [description]
4. API response received → [parsing logic from Section 2]
5. Output rendered in [output component]
6. User can [accept / copy / edit / ask a follow-up / start over]

**Feedback affordance:**
Include a simple feedback capture on every AI response: thumbs up / thumbs down + optional free-text comment. Log these to a local file or simple database during testing sessions.

---

## Section 4 — Test Scenario Matrix

Generate a set of test scenarios that cover the expected range of inputs users will provide. For each scenario, include the input, the expected output quality, and the evaluation criterion.

| Scenario | User input | Expected output quality | Evaluation criterion | Pass / Fail threshold |
|---|---|---|---|---|
| [Label] | [Specific input text or file] | [High / Medium / Low confidence, correct] | [How to evaluate — human review / regex / LLM-as-judge] | [What passes] |
| [Label — edge case] | [Input near the boundary of what the AI can handle] | [Hedged or declining response] | [Evaluation method] | [Graceful decline accepted] |
| [Label — adversarial] | [Input designed to trigger a failure mode] | [Safe refusal or error recovery] | [Does not produce [FAILURE_CRITERIA]] | [No hallucination / no unsafe output] |

Generate 8–10 scenarios including: core use cases (3–4), edge cases (2–3), out-of-scope inputs (1–2), and adversarial inputs (1–2).

---

## Section 5 — Quality Evaluation Framework

Define how output quality will be assessed during prototype testing:

**Automated checks (run on every response):**
- Format compliance: [does the response match [OUTPUT_FORMAT]? Yes / No]
- Length compliance: [is the response within acceptable length bounds?]
- Forbidden content: [does the response contain any strings or patterns that indicate a failure mode?]

**Human evaluation (sampled — assess [N]% of responses):**
| Dimension | Rating scale | What a "5" looks like | What a "1" looks like |
|---|---|---|---|
| Accuracy | 1–5 | Factually correct, no fabrications | Contains clearly wrong facts |
| Relevance | 1–5 | Directly addresses the user's input | Generic or off-topic |
| Completeness | 1–5 | Fully answers the question | Missing key information |
| Format | 1–5 | Matches [OUTPUT_FORMAT] exactly | Wrong structure or unparseable |
| Trust | 1–5 | User would act on this without verification | User would distrust or ignore this |

**Success gate:**
The prototype is ready to advance to full build when: average human evaluation score ≥ [X] across all dimensions on [N] sampled responses, AND [FAILURE_CRITERIA] triggers fewer than [Y]% of the time across the test scenario matrix.

---

## Section 6 — Prototype Deployment Checklist

Before testing this prototype with users:
- [ ] API key stored in environment variable — not hardcoded in the prototype
- [ ] Rate limiting handled — prototype does not allow users to spam API calls
- [ ] Feedback logging is working — every response and user rating is captured
- [ ] Test scenario matrix has been run manually — all 8–10 scenarios produce acceptable output
- [ ] Adversarial scenarios tested — prototype handles out-of-scope and adversarial inputs gracefully
- [ ] Cost estimate confirmed — prototype usage during testing will not exceed [budget]
- [ ] Data handling reviewed — no user PII is sent to the LLM without explicit consent
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | What the AI does for the user | `"Summarise a customer support ticket and suggest the three most relevant knowledge base articles"` |
| `[LLM]` | LLM provider and model | `"Anthropic Claude Sonnet 4.6"` |
| `[INTERACTION_PATTERN]` | How the user interacts | `"Single-turn: agent pastes ticket text, AI returns summary + ranked article list"` |
| `[USER_TASK]` | What the user is trying to accomplish | `"Resolve an inbound support ticket in under 3 minutes"` |
| `[USER_INPUTS]` | What the user provides | `"Ticket subject line, ticket body text (up to 2000 characters)"` |
| `[OUTPUT_FORMAT]` | Expected AI response format | `"JSON with fields: summary (string), articles (array of {title, url, relevance_score})"` |
| `[SUCCESS_CRITERIA]` | How you know the model is performing well | `"Recommended article is in the agent's accepted resolution 70%+ of the time; summary is accurate and under 80 words"` |
| `[FAILURE_CRITERIA]` | Output quality issues that block launch | `"Hallucinated article titles, summaries that contradict the ticket content, or refusals on routine support queries"` |

## Output Variants

**RAG prototype variant** — add to the prompt:
```
This prototype uses Retrieval Augmented Generation (RAG). Add a retrieval layer specification: (1) the document corpus to index, (2) the embedding model, (3) the retrieval query strategy (how the user's input is converted to a retrieval query), (4) the number of chunks to retrieve, (5) how retrieved chunks are injected into the system prompt, and (6) how to surface citations in the UI so users can verify the source of AI claims.
```

**Streaming response variant** — add to the prompt:
```
The AI response should stream token-by-token to the UI rather than appearing all at once. Add streaming implementation notes: how to handle partial JSON (if the output is structured), minimum token buffer before rendering begins, and how to handle a streaming interruption gracefully (partial response vs. retry vs. error).
```

## Tips

- The system prompt in Section 1 is the highest-leverage artifact in this spec — a poorly written system prompt will produce inconsistent output that makes it impossible to know if the model is capable or just poorly prompted; spend 30% of prototype build time here
- Test adversarial scenarios before showing the prototype to users — a single unexpected failure in a user session destroys trust in both the AI and the team
- Cost estimation is routinely skipped and always a problem — calculate expected token usage per session and multiply by participant count before a testing round; API costs can surprise
- Pair with `07-ai-feature-stub.md` to run initial user tests with hardcoded outputs before wiring the real API — this separates UX validation from model quality validation
- Pair with `02-ai-product-metrics.md` to define the quality and trust metrics this prototype is designed to measure
