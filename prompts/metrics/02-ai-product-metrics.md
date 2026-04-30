# AI Product Metrics Framework

**Phase:** Metrics
**Purpose:** Generate a comprehensive metrics framework for an AI-driven product that goes beyond ML model accuracy, covering operational performance, user experience, business value, and trust and safety — the dimensions that determine whether an AI product succeeds in production.

## Prompt Template

```
You are a senior product manager building a metrics framework for an AI-driven product. Using the context below, generate a structured set of metrics across six dimensions. For each metric, provide the full specification a data or engineering team would need to instrument and track it.

Product name: [PRODUCT_NAME]
Product description: [PRODUCT_DESCRIPTION — what the AI does, how users interact with it, and what task it is performing on their behalf]
Target users: [TARGET_USERS — who uses this product and in what context]
AI modality: [AI_MODALITY — e.g., "LLM-based chat assistant", "recommendation engine", "document summarisation", "code generation", "image classification", "RAG pipeline"]
Primary business outcome: [BUSINESS_OUTCOME — e.g., "reduce time-to-answer for support agents", "increase developer productivity", "automate invoice processing"]
Current instrumentation: [CURRENT_INSTRUMENTATION — what is already measured, or "none"]
Known risks: [KNOWN_RISKS — e.g., "hallucinations in regulated domain", "high latency on mobile", "user distrust of AI recommendations", or "none identified"]

---

## Section 1 — Operational Performance Metrics

These metrics measure whether the AI system is fast, reliable, and cost-efficient enough to use in production.

For each metric below, provide:
- **Definition:** what it measures
- **Formula or data source:** how it is calculated or where the data comes from
- **Recommended target or threshold:** a starting benchmark appropriate for [AI_MODALITY]
- **Alert threshold:** the value that should trigger an on-call or engineering response
- **Why it matters for [PRODUCT_NAME]:** connect it to the primary business outcome

Generate metrics for:
1. Response latency — P50, P95, and P99 end-to-end latency from request to response delivered to user
2. Time to first token (TTFT) — for streaming responses, the latency until the first token appears
3. Throughput — requests processed per second or per minute at peak load
4. Availability / uptime — percentage of time the AI feature is fully functional
5. Error rate — percentage of requests that return an error, time out, or fall back to a non-AI path
6. Cost per request — fully-loaded inference cost per API call, including token usage and infrastructure
7. Token efficiency — average input and output token count per request; flag requests that are outliers

---

## Section 2 — Task Completion and User Experience Metrics

These metrics measure whether users are able to accomplish what they came to do with the AI, and how much effort it takes.

Generate metrics for:
1. Task completion rate — percentage of sessions where the user achieved their goal without abandoning or escalating
2. Task abandonment rate — percentage of sessions where the user stopped interacting before completing the task; break down by exit point if possible
3. AI output acceptance rate — for surfaces where users can accept, reject, or edit AI output (suggestions, drafts, recommendations): percentage accepted without modification
4. User correction rate — percentage of AI outputs the user modifies before using; a proxy for output quality from the user's perspective
5. Retry / regeneration rate — how often users re-submit the same request or ask for a different answer; indicates dissatisfaction with the first response
6. Time-to-value — time from session start to the moment the user acts on an AI output for the first time
7. Human-in-the-loop escalation rate — how often the AI defers, routes to a human, or the user overrides the AI to contact a human directly
8. Session depth — average number of turns or interactions per session; distinguish between depth caused by engagement vs. depth caused by the AI failing to answer correctly

For each metric include: definition, measurement method, recommended baseline-setting approach, and connection to [BUSINESS_OUTCOME].

---

## Section 3 — Output Quality Metrics

These metrics measure the quality of AI-generated content beyond binary accuracy. They are particularly important for generative AI, RAG pipelines, and LLM-based products.

Generate metrics for:
1. Groundedness / faithfulness rate — for RAG or context-grounded systems: percentage of responses that do not introduce facts outside the provided context; measured via automated LLM-as-judge or human sampling
2. Hallucination rate — percentage of responses that contain factually incorrect or fabricated information; define the sampling and evaluation method appropriate for [AI_MODALITY]
3. Relevance score — how well the response addresses the user's actual intent; measured via thumbs up/down, implicit signals (acceptance rate), or LLM-as-judge
4. Response completeness — percentage of responses that fully address the user's request without requiring a follow-up to extract the rest of the answer
5. Consistency rate — for repeated or semantically equivalent queries: percentage of responses that are substantively consistent; measures model reliability
6. Confidence calibration — where the model expresses a confidence level or certainty: correlation between stated confidence and actual correctness; well-calibrated models express uncertainty when they are likely to be wrong
7. Format compliance rate — for structured output use cases (JSON, tables, specific templates): percentage of responses that conform to the required format without post-processing fixes

---

## Section 4 — Business Value Metrics

These metrics connect AI product performance to the outcomes the business cares about. They are the metrics most likely to appear in an executive review.

Generate metrics for:
1. AI-assisted vs. unassisted outcome comparison — for the primary task [PRODUCT_NAME] performs: compare the quality, speed, or cost of outcomes for users with AI assistance vs. without (A/B or pre/post)
2. Time saved per user — average time reduction in completing [BUSINESS_OUTCOME] task with AI vs. baseline; expressed in minutes per task and annualised per user
3. Cost deflection or cost avoidance — reduction in human effort, support volume, or operational cost attributable to AI handling the task
4. Feature adoption rate — percentage of target users who actively use the AI feature at least once per week; distinguish first-time activation from sustained use
5. AI-influenced retention — difference in retention rate between users who engage with the AI feature vs. those who do not; segment by cohort
6. Revenue or conversion impact — for AI features on a commercial path: change in conversion, upsell, or renewal attributable to AI feature adoption
7. Return on AI (ROAi) — ratio of value generated (time saved + cost avoided + revenue impact) to total cost of running the AI feature (inference + engineering + data)

---

## Section 5 — Trust and Safety Metrics

These metrics measure whether users trust the AI and whether the system is behaving safely, fairly, and within policy.

Generate metrics for:
1. User trust score — survey-based or behavioural proxy for whether users trust the AI's outputs; recommended survey question and behavioural proxy signal for [PRODUCT_NAME]
2. AI output rejection rate — percentage of AI outputs users explicitly reject, dismiss, flag, or report; a direct signal of distrust or quality failure
3. Safety filter trigger rate — percentage of requests filtered, blocked, or modified by safety guardrails; distinguish between legitimate filtering and over-triggering (false positives)
4. Harmful output rate — rate at which the AI produces outputs that violate safety, compliance, or content policies; requires a definition of "harmful" specific to [KNOWN_RISKS] and the regulatory context of [PRODUCT_NAME]
5. Demographic parity — for AI features that make recommendations or decisions affecting users: measure whether outcomes (acceptance rate, task completion, error rate) differ significantly across user segments (role, region, plan tier, language)
6. Sensitive data exposure rate — rate at which AI outputs contain or infer personally identifiable information (PII) or confidential data that should not have been surfaced
7. Model drift signal — statistical measure of distribution shift in inputs or outputs over time that may indicate the model is degrading relative to the real-world use cases it was trained or prompted for

---

## Section 6 — Counter-Metrics and Guardrails

For each of the following risks, identify the counter-metric that prevents the primary metrics from being optimised in the wrong direction:

1. Optimising acceptance rate at the expense of quality (users accept bad output because they do not know it is wrong)
2. Reducing latency at the expense of output completeness or accuracy
3. Increasing task completion rate by making it too easy for users to skip steps the AI should handle carefully
4. Reducing cost per request by degrading context quality (shorter prompts, fewer retrieved chunks)
5. Inflating time-saved estimates by attributing unrelated productivity gains to the AI feature

For each counter-metric, specify: what it measures, how it is tracked, and at what threshold it should trigger a review of the primary metric.

---

## Section 7 — Metrics Rollout Plan

Produce a phased instrumentation plan in three stages:

**Stage 1 — Launch (Day 0–30):** The minimum set of metrics needed to safely ship and monitor the AI feature in production. Prioritise operational health, error rates, and a single user experience signal.

**Stage 2 — Learning (Day 31–90):** Add quality, trust, and task completion metrics as usage grows and baseline data accumulates. Flag which metrics require a minimum sample size before they are actionable.

**Stage 3 — Optimisation (Day 91+):** Business value metrics, demographic parity checks, and model drift monitoring. These require longer observation windows and integration with business reporting systems.

For each stage, output a table:

| Metric | Category | Instrumentation required | Owner (PM / Eng / Data / Safety) | Priority |
|---|---|---|---|---|
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT_NAME]` | Name of the AI-driven product or feature | `"Aria — AI Support Assistant"` |
| `[PRODUCT_DESCRIPTION]` | What the AI does, how users interact with it, and what task it performs | `"LLM-powered chat assistant that answers customer support questions by retrieving from a knowledge base and generating natural-language responses"` |
| `[TARGET_USERS]` | Who uses the product and in what context | `"Tier-1 support agents handling 80+ tickets per day; secondary audience is end customers on self-serve plan"` |
| `[AI_MODALITY]` | The type of AI system | `"RAG pipeline with GPT-4o, retrieval from Confluence knowledge base, streamed responses via chat UI"` |
| `[BUSINESS_OUTCOME]` | The primary outcome the product is meant to drive | `"Reduce average handle time for support tickets by 40% and deflect 25% of inbound tickets to self-serve"` |
| `[CURRENT_INSTRUMENTATION]` | What is already being tracked | `"Basic API error rate and uptime via Datadog; no product-level AI metrics in place"` |
| `[KNOWN_RISKS]` | Risks already identified by the team | `"Hallucinations in responses about billing and legal terms; latency spikes during peak hours; agent distrust of AI suggestions"` |

## Output Variants

**Executive summary variant** — add to the prompt:
```
After completing all seven sections, produce a one-page executive summary: the top 5 metrics that matter most for [PRODUCT_NAME] at this stage of development, the single leading indicator of AI product health, the one metric most likely to surface a trust or safety failure early, and the metric the business cares most about. Format as a table with: metric name, current status (green / amber / red — use amber for "not yet instrumented"), owner, and next action.
```

**Early-stage / pre-launch variant** — add to the prompt:
```
[PRODUCT_NAME] has not yet launched. Reframe the output as a pre-launch instrumentation checklist. For each metric in Sections 1–3, specify: (a) what must be instrumented before launch, (b) what can be added in the first 30 days post-launch, and (c) what is deferred to 90 days. Flag any metric where the absence of instrumentation at launch would prevent safe operation.
```

**LLM-as-judge evaluation variant** — add to the prompt:
```
For each quality metric in Section 3 that can be evaluated automatically, write an LLM-as-judge prompt that a secondary model can use to score the primary model's output. Each judge prompt should include: the evaluation criteria, a 1–5 scoring rubric, an instruction to return a JSON object with `score`, `rationale`, and `pass` (boolean based on threshold), and an example of a passing and a failing output.
```

**Regulated-industry variant** — add to the prompt:
```
[PRODUCT_NAME] operates in a regulated industry: [INDUSTRY — e.g., healthcare, financial services, legal]. Extend the trust and safety section to include: explainability requirements (can the AI's reasoning be audited?), audit trail completeness (is every AI decision logged with inputs, outputs, and model version?), human override rate and documentation (every override must be traceable), and any sector-specific compliance thresholds. Flag which metrics are legally required vs. best practice.
```

## Tips

- **Instrument latency before anything else.** Latency issues are the most common reason AI features get turned off after launch — a slow AI is a distrusted AI. P95 and P99 are more important than P50 for interactive use cases.
- **Acceptance rate is your fastest quality proxy.** You may not have a ground-truth label for every AI output, but you can always measure whether users acted on it. A declining acceptance rate is an early warning signal before quality formally degrades.
- **Separate "did the user complete the task" from "did the AI complete the task."** Users sometimes finish tasks despite the AI failing. Track both independently — the gap between them is your measure of AI contribution.
- **Set baselines before launch, not after.** Record pre-AI task completion time, escalation rate, and user satisfaction scores during any beta or shadow-mode period. Post-launch comparisons are meaningless without a baseline.
- **Trust is a lagging indicator — watch rejection rate instead.** By the time a user trust score drops, the problem is already widespread. Rejection rate and correction rate are earlier signals.
- **Counter-metrics prevent Goodhart's Law.** Every primary metric can be gamed or optimised toward the wrong outcome. Run Sections 1–5 alongside Section 6, not as an afterthought.
- **Pair with the Feature Success Metrics prompt** for AI features that are part of a broader product — use this prompt for the AI-specific layer and `01-feature-success-metrics.md` for the feature-level rollout metrics.
- **Revisit Section 7 at each quarterly review.** Metrics that were "Stage 3" at launch may become critical after an incident or as the model is fine-tuned. Escalate metrics that are providing signal earlier than expected.
