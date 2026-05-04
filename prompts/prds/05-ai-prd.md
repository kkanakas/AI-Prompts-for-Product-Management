# AI Product Requirements Document

**Phase:** Writing the PRD
**Purpose:** Generate a comprehensive AI PRD — a living blueprint covering executive summary, problem statement, success metrics, AI features, data requirements, model requirements, UX and human interaction, ethical risk and compliance, milestones, and stakeholders — that product, engineering, data science, and legal teams can execute from and revisit as the product evolves.

## Prompt Template

```
You are a senior product leader writing an AI Product Requirements Document. This is a living blueprint, not a static specification — it will be updated as the model matures, data is validated, and user feedback is incorporated. Using the context below, generate the complete AI PRD.

Product or feature name: [PRODUCT_NAME]
One-line description: [ONE_LINE_DESCRIPTION — what the AI does for the user in plain language]
Stage: [STAGE — e.g., "Discovery", "Pre-build", "In development", "Post-launch iteration"]
Primary author: [AUTHOR]
Last updated: [DATE]

---

# [PRODUCT_NAME] — AI Product Requirements Document

---

## Section 1 — Executive Summary

### 1.1 Product / Feature Overview

| Field | Detail |
|---|---|
| Product / Feature name | [PRODUCT_NAME] |
| Objective | [OBJECTIVE — one sentence: what this AI does and for whom] |
| Business problem | [BUSINESS_PROBLEM — the specific business problem this AI solves] |
| Target users | [TARGET_USERS — who uses this, in what context, and how frequently] |
| Business impact | [BUSINESS_IMPACT — the expected measurable impact on the business — revenue, cost, efficiency, risk] |

### 1.2 Key Success Metrics Summary

| Metric type | Metric | Target | Baseline |
|---|---|---|---|
| Business | [e.g., cost per ticket deflected] | [target] | [current] |
| Business | [e.g., time saved per user per week] | [target] | [current] |
| User / UX | [e.g., task completion rate] | [target] | [current] |
| User / UX | [e.g., AI output acceptance rate] | [target] | [current] |
| AI model | [e.g., accuracy / F1 score] | [target] | [current or N/A if pre-build] |
| AI model | [e.g., latency at p95] | [target] | [current or N/A] |

---

## Section 2 — Problem Statement

### 2.1 Problem Description

[Write 2–3 paragraphs describing the problem this AI product is solving. Be specific about who experiences the problem, how often, and what it costs them. Do not describe the solution yet.]

### 2.2 Current Pain Points

| Pain point | Affected user / team | Frequency | Severity (High / Med / Low) |
|---|---|---|---|
| [e.g., "Agents spend 40 min/day searching for answers manually"] | [Support agents] | [Daily] | [High] |
| [Pain point 2] | | | |
| [Pain point 3] | | | |

### 2.3 Impact on Business

Describe the business impact of NOT solving this problem:
- Revenue impact: [quantify if possible — e.g., "X% of churned accounts cite this as a reason"]
- Operational cost: [e.g., "costs $Y per quarter in manual labor"]
- Risk: [e.g., "compliance exposure if errors continue at current rate"]
- Competitive position: [e.g., "competitors already offer this capability"]

### 2.4 Constraints and Limitations

| Constraint | Type | Impact on solution |
|---|---|---|
| [e.g., "Cannot store PII outside the EU"] | Regulatory | [limits training data sources] |
| [e.g., "Must integrate with existing Salesforce instance"] | Technical | [constrains model output format] |
| [e.g., "Response latency must be < 3 seconds"] | Performance | [limits model complexity] |
| [e.g., "Budget cap of $X/month on inference costs"] | Financial | [shapes model tier selection] |

---

## Section 3 — Objectives and Success Metrics

### 3.1 Primary Objectives

1. [Primary objective — measurable, time-bound, connected to business impact]
2. [Second primary objective]
3. [Third primary objective — maximum 3; if you have more, move them to secondary]

### 3.2 Secondary Objectives

1. [Secondary objective — valuable but not blocking launch]
2. [Secondary objective]

### 3.3 Business Metrics

| Metric | Definition | Measurement method | Target | Review cadence |
|---|---|---|---|---|
| [e.g., Ticket deflection rate] | [% of inbound tickets resolved by AI without human escalation] | [Zendesk tag analysis] | [25% deflection within 90 days of launch] | [Weekly] |
| [Cost per AI-resolved interaction] | | | | |
| [Revenue influenced by AI feature] | | | | |

### 3.4 AI Model Metrics

| Metric | Definition | Acceptable threshold | Measurement method |
|---|---|---|---|
| Accuracy | [correct predictions / total predictions] | [≥ X%] | [holdout test set] |
| Precision | [true positives / (true positives + false positives)] | [≥ X%] | [holdout test set] |
| Recall | [true positives / (true positives + false negatives)] | [≥ X%] | [holdout test set] |
| F1 Score | [harmonic mean of precision and recall] | [≥ X] | [holdout test set] |
| Latency | [end-to-end response time from request to output] | [p95 ≤ Xms] | [production monitoring] |
| Hallucination rate | [% of outputs containing factually incorrect content] | [< X%] | [LLM-as-judge sampling] |
| Confidence calibration | [correlation between model confidence and actual accuracy] | [Brier score ≤ X] | [calibration curve analysis] |

Add or remove rows based on model type. Classification models emphasize precision/recall/F1. Generative models emphasize hallucination rate, groundedness, and relevance.

### 3.5 User / UX Metrics

| Metric | Definition | Target | Measurement method |
|---|---|---|---|
| AI output acceptance rate | [% of AI suggestions the user accepts without modification] | [≥ X%] | [UI event tracking] |
| Task completion rate | [% of sessions where user completes the target task with AI assistance] | [≥ X%] | [funnel analysis] |
| User correction rate | [% of AI outputs the user edits before using] | [≤ X%] | [UI event tracking] |
| Time-to-value | [time from session start to user acting on AI output] | [≤ X seconds] | [session analytics] |
| User trust score | [survey-based trust rating for AI feature] | [≥ X/5] | [in-app survey, quarterly] |

### 3.6 Ethical and Compliance Metrics

| Metric | Definition | Threshold | Review cadence |
|---|---|---|---|
| Demographic parity | [difference in AI outcome rates across user segments] | [< X% gap] | [Monthly] |
| Safety filter trigger rate | [% of requests filtered by content safety guardrails] | [monitor for anomalies] | [Weekly] |
| Harmful output rate | [% of outputs flagged as harmful by human or automated review] | [< X%] | [Weekly] |
| Audit log completeness | [% of AI decisions with complete input/output/model-version logs] | [100%] | [Continuous] |

---

## Section 4 — AI Features

For each distinct AI capability, complete one feature block:

---

### Feature [N]: [FEATURE_NAME]

**Problem solved:** [The specific pain point this feature eliminates]

**Use case / user story:**
> As a **[user type]**, I want **[the AI capability]**, so that **[the outcome I achieve]**.

**AI approach and model type:**
[Describe the AI technique — e.g., "RAG pipeline using a fine-tuned embedding model for retrieval and a hosted LLM for generation", "binary classification using a gradient-boosted tree", "multi-label NLP classifier". Be specific about approach; the exact model can be decided later.]

**Input data and features required:**

| Input | Type | Source | Required / Optional |
|---|---|---|---|
| [e.g., Customer support ticket text] | [Unstructured text] | [Zendesk API] | [Required] |
| [e.g., Account tier] | [Categorical] | [Salesforce CRM] | [Required] |
| [e.g., Product usage events (last 30 days)] | [Time-series] | [Mixpanel] | [Optional] |

**Output and expected behavior:**

| Output | Format | Example | Acceptable quality threshold |
|---|---|---|---|
| [e.g., Suggested reply draft] | [Plain text, max 200 words] | [example output] | [acceptance rate ≥ X%] |
| [e.g., Confidence score] | [Float 0.0–1.0] | [0.87] | [calibrated — Brier ≤ X] |

**Human-in-the-loop points:**

| Trigger condition | Human action required | SLA / time limit | Escalation if not actioned |
|---|---|---|---|
| [e.g., Confidence score < 0.70] | [Agent reviews before sending] | [5 minutes] | [Route to senior agent] |
| [e.g., Sensitive topic detected] | [Supervisor approval] | [10 minutes] | [Auto-escalate to Tier 2] |
| [e.g., Novel input type not in training distribution] | [Flag for data team review] | [24 hours] | [Log to retraining queue] |

**Dependencies and integrations:**

| Dependency | Type | Owner | Status |
|---|---|---|---|
| [e.g., Zendesk webhook] | [API integration] | [Platform team] | [Confirmed / Pending] |
| [e.g., Knowledge base vector store] | [Infrastructure] | [ML Infra team] | [In progress] |
| [e.g., Content safety guardrail API] | [Third-party service] | [Security team] | [Confirmed] |

---

Repeat Feature block for each AI capability in the product.

---

## Section 5 — Data Requirements

### 5.1 Data Types

| Data type | Category | Description | Volume estimate |
|---|---|---|---|
| [e.g., Historical support tickets] | Internal | [Labeled ticket text with resolution outcomes] | [500K records, 3 years] |
| [e.g., Third-party knowledge base] | External | [Industry FAQ corpus from vendor API] | [~2M documents] |
| [e.g., Synthetic edge cases] | Synthetic | [Generated adversarial inputs for safety testing] | [10K records] |

### 5.2 Volume and Quality Requirements

| Dataset | Minimum volume for MVP | Target volume for production | Minimum quality bar |
|---|---|---|---|
| [Dataset name] | [N records / MB] | [N records / MB] | [e.g., "< 5% missing labels, > 90% inter-annotator agreement"] |

### 5.3 Labeling and Cleaning Needs

| Dataset | Labeling required | Cleaning required | Owner | Estimated effort |
|---|---|---|---|---|
| [Dataset name] | [Yes — human annotation / No — pre-labeled / Partial] | [Deduplication, PII removal, normalization] | [Data team] | [X weeks] |

### 5.4 Privacy, Risk, and Governance

| Risk | Description | Mitigation | Owner |
|---|---|---|---|
| PII in training data | [Customer names, emails, or account numbers present in raw data] | [PII scrubbing pipeline before ingestion] | [Data Engineering] |
| Data residency | [Data must not leave [REGION]] | [Regional model deployment and data pipeline isolation] | [Platform / Legal] |
| Consent | [Training on user-generated content may require explicit consent] | [Legal review of ToS; opt-out mechanism] | [Legal / Product] |
| Third-party data license | [External dataset may restrict commercial model training] | [License review before ingestion] | [Legal] |

### 5.5 Bias Risks and Mitigations

| Bias type | Description | Affected group | Mitigation | Monitoring method |
|---|---|---|---|---|
| [e.g., Representation bias] | [Training data over-represents certain customer segments] | [Smaller / newer customer cohorts] | [Stratified sampling; synthetic augmentation] | [Monthly demographic parity check] |
| [e.g., Label bias] | [Annotations reflect annotator assumptions] | [Users from non-English-speaking markets] | [Diverse annotator panel; inter-annotator agreement threshold] | [Annotation audit quarterly] |

### 5.6 Data Sources

| Source | Access method | Data owner | Refresh frequency | Availability confirmed |
|---|---|---|---|---|
| [Zendesk] | [API] | [Customer Success Ops] | [Real-time] | [Yes] |
| [Salesforce CRM] | [Bulk export / API] | [Sales Ops] | [Daily] | [Yes] |
| [Internal knowledge base] | [Crawl / export] | [Product team] | [Weekly] | [Pending] |

---

## Section 6 — Model Requirements

### 6.1 Model Type

[Describe the type of model(s) required — e.g., "A retrieval-augmented generation pipeline: a bi-encoder embedding model for retrieval (candidate: text-embedding-3-large) combined with a generative LLM for response synthesis (candidate: Claude Sonnet or GPT-4o). Final model selection will be made after baseline benchmarking in the Discovery phase."]

### 6.2 Inputs and Features

| Feature | Type | Preprocessing required | Importance (Must / Should / Could) |
|---|---|---|---|
| [Feature name] | [Numeric / Categorical / Text / Image / Time-series] | [Normalization / tokenization / embedding] | [Must] |

### 6.3 Outputs and Predictions

| Output | Type | Format | Downstream consumer |
|---|---|---|---|
| [e.g., Suggested reply] | [Generated text] | [String, max 300 tokens] | [Agent UI — editable text field] |
| [e.g., Confidence score] | [Probability] | [Float 0.0–1.0] | [UI confidence badge; human review trigger] |
| [e.g., Topic classification] | [Multi-label] | [Array of label strings] | [Routing engine] |

### 6.4 Performance Targets

| Metric | MVP threshold | Production target | Measurement method |
|---|---|---|---|
| Accuracy | [≥ X%] | [≥ Y%] | [Holdout test set — [N] samples] |
| Precision | [≥ X%] | [≥ Y%] | [Holdout test set] |
| Recall | [≥ X%] | [≥ Y%] | [Holdout test set] |
| F1 Score | [≥ X] | [≥ Y] | [Holdout test set] |
| Latency (p95) | [≤ X ms] | [≤ Y ms] | [Production load test] |
| Throughput | [≥ X req/sec] | [≥ Y req/sec] | [Production load test] |
| Cost per inference | [≤ $X] | [≤ $Y] | [Cloud billing / token tracking] |

### 6.5 Evaluation Plan

| Evaluation stage | Method | Dataset | Responsible | Pass criteria |
|---|---|---|---|---|
| Offline evaluation | [Holdout test set benchmarking] | [Labeled test set — N samples] | [ML team] | [Meets Section 6.4 MVP thresholds] |
| Human evaluation | [Blind human rating of model outputs — N samples per week] | [Random sample of production outputs] | [QA / Data team] | [Average rating ≥ X on relevance and accuracy] |
| A/B test | [Split traffic: AI-assisted vs. control] | [Live production traffic] | [Product + ML] | [Primary business metric improves ≥ X% at p < 0.05] |
| Red teaming | [Adversarial prompt testing] | [Curated adversarial set] | [Security + ML] | [No P0 safety failures; < X% harmful outputs] |

### 6.6 Retraining and Update Plan

| Trigger | Threshold | Action | Cadence |
|---|---|---|---|
| Model drift | [Performance drops > X% below baseline on key metric] | [Trigger retraining pipeline] | [Monitored weekly] |
| Data drift | [Input distribution shifts significantly from training distribution] | [Flag for review; schedule retraining] | [Monitored monthly] |
| Scheduled refresh | [N/A — time-based] | [Retrain on accumulated production data] | [Quarterly] |
| Incident-triggered | [P0 safety or accuracy failure in production] | [Emergency retrain or rollback] | [On incident] |

---

## Section 7 — UX and Human Interaction

### 7.1 Target User Workflows

For each primary user type, describe the workflow before and after AI integration:

**User type: [USER_TYPE_1]**

| Step | Without AI | With AI | Time saved |
|---|---|---|---|
| [Step 1] | [Manual action] | [AI-assisted action] | [X min] |
| [Step 2] | [Manual action] | [AI-assisted action] | [X min] |

### 7.2 Feature Integration Points

| AI feature | Where it appears in the UI | Entry trigger | Exit / completion state |
|---|---|---|---|
| [Feature N] | [Screen / panel / modal name] | [User action or system event that invokes the AI] | [What the user sees when AI has finished] |

### 7.3 Confidence Scores and Explainability

| AI feature | Confidence displayed? | Display format | Threshold for showing vs. hiding | Explainability provided? |
|---|---|---|---|---|
| [Feature N] | [Yes / No] | [Badge / bar / percentage / label] | [Show if ≥ X%; hide if below] | [Yes — "How did the AI get here?" panel / No] |

Explainability requirement: [Specify whether users need to understand WHY the AI produced an output — e.g., "Support agents must be able to see which KB articles the AI used to draft the reply."]

### 7.4 Feedback Mechanism

| Feedback type | Trigger | UI treatment | Data captured | Use in retraining |
|---|---|---|---|---|
| Explicit thumbs up/down | [After each AI output] | [Inline icon pair below response] | [Rating + AI output + user context] | [Yes — positive/negative labels] |
| Explicit correction | [When user edits AI output] | [Track diff between AI output and final sent version] | [Original output + corrected output] | [Yes — correction pairs for fine-tuning] |
| Implicit acceptance | [User acts on AI output without editing] | [No UI change — tracked via event] | [Output accepted + task outcome] | [Yes — positive reinforcement signal] |
| Explicit flag | [User flags harmful or wrong output] | [Flag icon + optional free-text reason] | [Output + reason + user ID] | [Yes — review queue for safety team] |

### 7.5 Alerts and Notifications

| Alert | Trigger condition | Delivery channel | Recipient | Action required |
|---|---|---|---|---|
| [Low confidence alert] | [AI confidence < X% on high-stakes decision] | [In-app badge] | [User] | [Review before acting] |
| [Model degradation alert] | [Key metric drops > X% week-over-week] | [PagerDuty / Slack #ml-ops] | [ML team + PM] | [Investigate and remediate within SLA] |
| [Data pipeline failure] | [Ingestion job fails] | [Slack #data-alerts] | [Data engineering] | [Restore pipeline within X hours] |

### 7.6 Visualizations and Dashboards

| Dashboard | Audience | Key metrics displayed | Refresh rate | Tool |
|---|---|---|---|---|
| [AI model health] | [ML team + PM] | [Accuracy, latency, drift signals] | [Real-time / daily] | [Datadog / Grafana] |
| [User adoption] | [PM + Design] | [Acceptance rate, correction rate, trust score] | [Daily] | [Mixpanel / Looker] |
| [Business impact] | [Leadership] | [Deflection rate, cost savings, time saved] | [Weekly] | [Looker / Tableau] |

---

## Section 8 — Ethical Risk and Compliance

### 8.1 Bias Mitigation Plan

| Bias risk | Affected group | Mitigation approach | Owner | Review cadence |
|---|---|---|---|---|
| [e.g., Model performs worse for non-English inputs] | [Non-English-speaking users] | [Multilingual training data; language-stratified evaluation] | [ML team] | [Monthly] |
| [e.g., Recommendations favor high-value customers] | [SMB / lower-tier accounts] | [Segment-stratified training; fairness constraint in objective function] | [ML team + Product] | [Quarterly] |

### 8.2 Privacy and Regulatory Compliance

| Requirement | Regulation / policy | Implementation | Owner | Status |
|---|---|---|---|---|
| [PII must not be used in model training without consent] | [GDPR Article 6 / CCPA] | [PII scrubbing pipeline + consent flag in data pipeline] | [Legal + Data Engineering] | [In progress] |
| [Right to explanation for automated decisions] | [GDPR Article 22] | [Explainability panel in UI showing AI reasoning] | [Product + ML] | [Planned] |
| [Data residency — EU data stays in EU] | [GDPR / contractual] | [Regional deployment + data isolation] | [Platform] | [Confirmed] |
| [Model outputs auditable for 7 years] | [SOX / sector regulation] | [Immutable audit log with input/output/model version] | [Platform + Legal] | [Planned] |

### 8.3 Human Oversight and Human-in-the-Loop Design

| Scenario | Oversight mechanism | Responsible human | Response SLA |
|---|---|---|---|
| [Low-confidence AI decision] | [Mandatory human review before action is taken] | [Agent / supervisor] | [5 minutes] |
| [High-stakes or irreversible action] | [Dual approval — AI recommendation + human confirmation] | [Senior agent + manager] | [10 minutes] |
| [Novel or out-of-distribution input] | [Flag to data team; AI declines to act] | [Data / ML team] | [24 hours] |
| [Safety filter triggered] | [Log + notify safety team; suppress output] | [Safety team] | [Immediate] |

### 8.4 Security and Governance

| Risk | Mitigation | Owner | Status |
|---|---|---|---|
| Prompt injection attacks | [Input sanitization; system prompt isolation] | [Security team] | [Planned] |
| Training data poisoning | [Data provenance tracking; anomaly detection on ingestion] | [ML + Security] | [Planned] |
| Model output leakage of training data | [Differential privacy; output filtering] | [ML team] | [Under review] |
| Unauthorized model access | [API key rotation; role-based access to model endpoints] | [Platform / Security] | [Confirmed] |
| Shadow model use | [Approved model registry; ban on unapproved LLM API calls in production] | [Platform + Legal] | [Policy in place] |

### 8.5 Contingency Plans

| Failure scenario | Detection method | Immediate response | Recovery plan | Owner |
|---|---|---|---|---|
| [Model produces harmful outputs at scale] | [Safety filter spike / user flag surge] | [Kill switch — revert to non-AI fallback] | [Retrain on curated safe data; red team before relaunch] | [ML + PM + Safety] |
| [Model accuracy degrades significantly] | [Automated metric alert] | [Increase human review threshold to 100% of outputs] | [Retrain or rollback to prior model version] | [ML team] |
| [Data pipeline fails] | [Ingestion monitoring alert] | [Freeze model inputs; serve cached outputs] | [Restore pipeline; validate data quality before resuming] | [Data Engineering] |
| [Regulatory finding or legal challenge] | [Legal notification] | [Suspend affected feature] | [Compliance remediation plan; legal sign-off before relaunch] | [Legal + PM] |

---

## Section 9 — Milestones and Timeline

| Phase | Key activities | Responsible | Deliverables | Due date | Dependencies |
|---|---|---|---|---|---|
| Discovery | Problem validation, data audit, stakeholder alignment, risk assessment | PM + Data team | Problem statement signed off, data availability confirmed, initial risk register | [DATE] | Stakeholder availability |
| Modeling | Data preparation, baseline model, offline evaluation, prototype | ML team + Data Engineering | Trained baseline model meeting MVP thresholds, evaluation report | [DATE] | Data pipeline complete |
| Validation | Human evaluation, A/B test design, red teaming, UX testing | ML + Product + QA + Security | Evaluation report, red team sign-off, UX test results | [DATE] | Baseline model complete |
| Deployment | Staged rollout (shadow → limited → full), monitoring setup, runbooks | Engineering + ML + Platform | Model in production, monitoring dashboards live, incident runbook | [DATE] | Validation sign-off |
| Monitoring | Ongoing performance tracking, drift detection, retraining cadence | ML + Data + PM | Monthly model health report, retraining schedule, bias audit | [DATE] ongoing | Production deployment |

---

## Section 10 — Stakeholders

| Role | RACI | Name / Team | Responsibilities |
|---|---|---|---|
| Product Manager | Responsible | [NAME / TEAM] | Owns the PRD; drives prioritization; defines success metrics; coordinates cross-functional alignment |
| ML / Data Science | Responsible | [NAME / TEAM] | Model design, training, evaluation, and retraining |
| Data Engineering | Responsible | [NAME / TEAM] | Data pipelines, labeling infrastructure, data quality |
| Engineering | Responsible | [NAME / TEAM] | Feature integration, API development, production deployment |
| UX / Design | Responsible | [NAME / TEAM] | User workflow design, confidence score display, feedback mechanisms |
| Product Leader / Director | Accountable | [NAME] | Final sign-off on scope, resources, and launch gate decisions |
| Legal / Compliance | Consulted | [NAME / TEAM] | Privacy review, regulatory compliance, data license review |
| Security | Consulted | [NAME / TEAM] | Threat model, prompt injection defense, access controls |
| Customer Success | Consulted | [NAME / TEAM] | User research input, pilot customer selection, adoption readiness |
| Finance | Consulted | [NAME / TEAM] | Inference cost approval, ROI tracking |
| Executive Sponsor | Informed | [NAME] | Strategic alignment, escalation path for resourcing decisions |
| End Users (pilot) | Informed | [COHORT DESCRIPTION] | Feedback during validation and pilot phases |

---

## Section 11 — References and Supporting Documentation

| Document | Purpose | Owner | Link / Location |
|---|---|---|---|
| [Data audit report] | [Confirms data availability and quality for training] | [Data team] | [link] |
| [Risk register] | [Full risk inventory with mitigations and owners] | [PM + Legal] | [link] |
| [Model evaluation report] | [Baseline model performance against Section 6.4 targets] | [ML team] | [link] |
| [UX research synthesis] | [User interviews and usability test findings] | [Design] | [link] |
| [Legal / compliance review] | [GDPR, CCPA, sector regulation sign-off] | [Legal] | [link] |
| [Security threat model] | [Adversarial attack surface and mitigations] | [Security] | [link] |
| [Red team report] | [Adversarial prompt test results] | [Security + ML] | [link] |
| [A/B test results] | [Business metric impact from production experiment] | [PM + Data] | [link] |

---

## Document Control

| Field | Detail |
|---|---|
| Version | [v0.1 — Discovery / v1.0 — Pre-build sign-off / v1.x — In-iteration] |
| Status | [Draft / In review / Approved / Superseded] |
| Next review date | [DATE — suggest monthly during active development, quarterly post-launch] |
| Change log | [Date — Author — What changed and why] |
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[PRODUCT_NAME]` | Name of the AI product or feature | `"Aria — AI Support Assistant"` |
| `[ONE_LINE_DESCRIPTION]` | What the AI does for the user in plain language | `"Drafts replies to inbound support tickets and surfaces the most relevant knowledge base articles"` |
| `[STAGE]` | Current stage of the initiative | `"Discovery"` |
| `[AUTHOR]` | Primary author of this PRD | `"Kartik K., Senior PM — Platform"` |
| `[DATE]` | Date of this version | `"2026-05-01"` |
| `[OBJECTIVE]` | One-sentence AI product objective | `"Reduce average handle time for Tier-1 support agents by 40% through AI-assisted response drafting"` |
| `[BUSINESS_PROBLEM]` | The specific business problem | `"Support agents spend 60% of their time on ticket types that follow predictable resolution patterns, driving high cost and slow response times"` |
| `[TARGET_USERS]` | Who uses this and how | `"Tier-1 support agents handling 80+ tickets per day; secondary: end customers on self-serve plan"` |
| `[BUSINESS_IMPACT]` | Expected measurable impact | `"$2.4M annual cost reduction; 40% reduction in average handle time; 15-point CSAT improvement"` |
| `[STAGE_MILESTONES]` | Key dates per phase | `"Discovery: 2026-05-30 / Modeling: 2026-07-15 / Validation: 2026-08-31 / Deployment: 2026-09-30"` |

## Output Variants

**Discovery stage (abbreviated)** — add to the prompt:
```
This PRD is at the Discovery stage — the model does not yet exist. Complete Sections 1–3 (Executive Summary, Problem Statement, and Objectives/Metrics) in full. For Sections 4–8 (AI Features, Data, Model, UX, Ethics), generate a structured "known / unknown / assumption" table for each section rather than complete specifications — this surfaces what needs to be answered before the build stage begins. Sections 9–11 should be stubs only.
```

**Executive briefing variant** — add to the prompt:
```
After generating the full PRD, produce a one-page executive briefing: product name, business problem (2 sentences), AI approach (1 sentence), top 3 success metrics with baselines and targets, top 3 risks, launch date, and the single most important decision leadership must make this week to keep the timeline. Format as a table suitable for a steering committee pre-read.
```

**Living document update variant** — add to the prompt:
```
This is an update to an existing AI PRD. The previous version is pasted below. Review the existing document against the new context provided above, then: (1) update any section where the new context changes the content, (2) add a change log entry for each section modified with the date, author, and reason for the change, (3) flag any section where the new context introduces a conflict or ambiguity that needs a decision. Do not regenerate unchanged sections — only output the sections that changed plus the updated change log.
[PASTE_PREVIOUS_VERSION]
```

**Regulatory / high-risk AI variant** — add to the prompt:
```
This AI product operates in a regulated industry or involves high-risk automated decision-making: [INDUSTRY — e.g., healthcare, financial services, insurance, HR/hiring]. Extend Section 8 (Ethical Risk and Compliance) to include: (1) applicable regulation and specific articles that govern this AI system, (2) whether this system falls under the EU AI Act high-risk classification and the required conformity assessment, (3) the explainability standard required by regulation (not just best practice), (4) the human oversight mandate and documentation required for audit, and (5) the incident reporting obligations if the model causes harm.
```

## Tips

- **This is a living document, not a contract** — version it explicitly (v0.1 Discovery → v1.0 Pre-build → v1.x Iteration); the model requirements, data requirements, and success metrics will change as you learn; the PRD should reflect current best understanding, not lock in decisions you cannot yet make
- **Write the problem statement before any other section** — if you cannot write a crisp Section 2 without referencing your proposed solution, the problem is not well-understood yet; the problem statement should be independently true regardless of whether you build this AI
- **Baselines are mandatory for every metric** — a metric without a baseline is a wish, not a target; if you do not have a baseline yet, write "to be established in Discovery" and assign an owner and date
- **Human-in-the-loop design is a product decision, not a safety afterthought** — the trigger conditions, SLAs, and escalation paths in Sections 4 and 7 are core product features; design them with the same rigor as the AI outputs themselves
- **The contingency plan in Section 8.5 must be executable on day one of launch** — every AI product needs a kill switch and a defined rollback path before going to production; if you cannot describe the recovery plan, you are not ready to ship
- **Pair with `02-ai-product-metrics.md`** for a deeper breakdown of operational, quality, business, and trust metrics — use that prompt to generate the full metrics framework, then reference the key metrics in Sections 3 and 6 of this PRD
- **Pair with `05-wizard-of-oz-protocol.md`** for the AI feature validation phase — before the model exists, a WoZ test can validate whether users trust and act on AI outputs, giving you real behavioral data to inform the model requirements in Section 6
- **Pair with `08-agent-workflow-simulation.md`** if any feature in Section 4 involves multi-step agentic behavior — map the workflow before writing the feature block to surface missing handoff points and error paths
