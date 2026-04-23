---
name: ai-pm-prompts
description: >
  A structured library of AI prompts for Product Managers covering the full product lifecycle.
  Use this skill whenever a PM needs help with customer interviews, research synthesis, market
  analysis, competitive intelligence, capability gap analysis, ideation, idea evaluation,
  Kano analysis, MoSCoW prioritization, RICE scoring, stakeholder mapping, RACI matrix,
  DACI decision framework, product strategy canvas, OKR generation, weekly leadership updates,
  sentiment analysis of work items, PRD generation, use case documentation, user story generation,
  user journey mapping, release notes, prototyping, dependency identification, private preview
  planning, value proposition design, Big Rock decomposition, launch gates, architecture diagrams,
  ERD, flowcharts, UML class diagrams, customer meeting summaries, or any product management task.
  Triggers on phrases like "customer discovery", "interview guide", "competitive analysis",
  "gap analysis", "SWOT", "market research", "trend analysis", "ideation", "pre-mortem",
  "RICE scoring", "Kano", "MoSCoW", "synthetic user", "problem statement", "JTBD",
  "stakeholder map", "RACI", "DACI", "decision framework", "strategy canvas", "OKR",
  "weekly update", "leadership update", "sentiment analysis", "Jira sentiment",
  "prioritization", "product strategy", "working backwards", "press release", "PR/FAQ",
  "Amazon press release", "customer value", "ERD", "entity relationship diagram",
  "data model", "database schema", "flowchart", "control flow", "decision flow",
  "dependency map", "dependency identification", "critical path", "RAID log",
  "private preview", "alpha", "beta", "GA readiness", "cohort", "pilot plan",
  "value proposition", "value prop", "jobs to be done", "pain relievers", "gain creators",
  "problem-solution fit", "product-market fit", "business model fit", "value canvas",
  "big rock", "initiative decomposition", "epic breakdown", "MVP scope",
  "use case", "use case documentation", "acceptance criteria", "business rules",
  "user story", "given when then", "gherkin", "story map", "INVEST", "story points",
  "launch gate", "go no-go", "release readiness", "gate review", "launch checklist",
  "customer meeting", "meeting transcript", "meeting summary", "slack update",
  or any product management task.
---

# AI Prompts for Product Managers — Claude Desktop Skill

You have access to a library of 55+ structured PM prompt templates covering the full product lifecycle. When the user asks for help with any product management task, follow the steps below.

---

## How to use this skill

### Step 1 — Identify the right prompt

Match the user's request to the prompt catalog below. Each entry shows the prompt name and the file path where the full template is stored in this skill bundle.

### Step 2 — Read the prompt file

Use the file path to read the prompt template from the skill bundle. The full template contains the exact prompt text, all placeholders, output variants, and usage tips.

### Step 3 — Collect the user's context

The prompt template lists required placeholders (e.g., `[PRODUCT_NAME]`, `[TARGET_SEGMENT]`). Ask the user for each piece of missing context before filling the template.

### Step 4 — Fill and return the prompt

Replace all `[PLACEHOLDERS]` with the user's values. Return the completed, ready-to-use prompt. Offer to run output variants if they would be useful.

---

## Prompt Catalog

### Architecture Diagrams
Generate technical diagrams directly from a codebase.

| Prompt | File path |
|---|---|
| Sequence Diagram from Repo | `prompts/architecture-diagrams/01-sequence-diagram-from-repo.md` |
| UML Class Diagram from Repo | `prompts/architecture-diagrams/02-uml-class-diagram-from-repo.md` |
| Entity Relationship Diagram from Repo | `prompts/architecture-diagrams/03-erd-from-repo.md` |
| Flowchart from Repo | `prompts/architecture-diagrams/04-flowchart-from-repo.md` |

### Communications
Turn raw notes and meeting transcripts into polished leadership messages.

| Prompt | File path |
|---|---|
| Weekly Leadership Update | `prompts/communications/01-weekly-leadership-update.md` |
| Customer Meeting to Team Update + Jira | `prompts/communications/02-customer-meeting-to-team-update.md` |

### Competitive Analysis
Understand market position and close gaps that matter.

| Prompt | File path |
|---|---|
| Positioning and Messaging | `prompts/competitive-analysis/01-positioning-messaging.md` |
| Feature Comparison | `prompts/competitive-analysis/02-feature-comparison.md` |
| Target Customer Analysis | `prompts/competitive-analysis/03-target-customers.md` |
| Capability Gap Analysis | `prompts/competitive-analysis/04-capability-gap-analysis.md` |

### Customer Discovery
Go deeper with interviews, transcripts, surveys, and work items.

| Prompt | File path |
|---|---|
| Interview Guide | `prompts/customer-discovery/01-interview-guide.md` |
| Blind Spot Detection | `prompts/customer-discovery/02-blind-spot-detection.md` |
| Research Synthesis | `prompts/customer-discovery/03-research-synthesis.md` |
| Problem Refinement | `prompts/customer-discovery/04-problem-refinement.md` |
| Transcript Theme Analysis | `prompts/customer-discovery/05-transcript-theme-analysis.md` |
| Transcript Deep Dive | `prompts/customer-discovery/06-transcript-deep-dive.md` |
| JTBD Analysis | `prompts/customer-discovery/07-jtbd-analysis.md` |
| Survey Open-Ended Analysis | `prompts/customer-discovery/08-survey-open-ended.md` |
| Survey Segment Comparison | `prompts/customer-discovery/09-survey-segment-comparison.md` |
| Multi-Source Patterns | `prompts/customer-discovery/10-multi-source-patterns.md` |
| Sentiment Analysis in Work Items | `prompts/customer-discovery/11-sentiment-analysis-in-workitems` |

### Idea Evaluation
Score, stress-test, and prioritize ideas before committing resources.

| Prompt | File path |
|---|---|
| RICE Scoring | `prompts/idea-evaluation/01-rice-scoring.md` |
| Pre-Mortem | `prompts/idea-evaluation/02-pre-mortem.md` |
| Assumption Mapping | `prompts/idea-evaluation/03-assumption-mapping.md` |
| Validation Questions | `prompts/idea-evaluation/04-validation-questions.md` |
| Kano Analysis | `prompts/idea-evaluation/05-kano-analysis.md` |
| MoSCoW Prioritization | `prompts/idea-evaluation/06-moscow-prioritization.md` |

### Ideation
Generate and evaluate ideas systematically.

| Prompt | File path |
|---|---|
| Problem to Solution | `prompts/ideation/01-problem-to-solution.md` |
| Ideation Session | `prompts/ideation/02-Ideation.md` |
| SCAMPER Analysis | `prompts/ideation/03-scamper-analysis.md` |
| VRIO Analysis | `prompts/ideation/04-vrio-analysis.md` |
| MECE Analysis | `prompts/ideation/05-mece-analysis.md` |

### Market Research
Build a rigorous picture of your market.

| Prompt | File path |
|---|---|
| Structured Market Analysis | `prompts/market-research/01-structured-market-analysis.md` |
| Evidence and Contradictions | `prompts/market-research/02-evidence-and-contradictions.md` |
| Comprehensive Market Landscape | `prompts/market-research/03-comprehensive-market-landscape.md` |

### Metrics
Define what success looks like before you build.

| Prompt | File path |
|---|---|
| Feature Success Metrics | `prompts/metrics/01-feature-success-metrics.md` |

### PRDs and Requirements
Write requirements that engineering teams can act on.

| Prompt | File path |
|---|---|
| PRD Generation | `prompts/prds/01-prd-generation.md` |
| Use Case Documentation | `prompts/prds/02-use-case-documentation.md` |
| Features and User Stories | `prompts/prds/03-features-and-user-stories.md` |

### Prototyping
Specify UI prototypes with enough detail for engineers and designers.

| Prompt | File path |
|---|---|
| UI Prototype Spec | `prompts/prototyping/01-ui-prototype-spec.md` |

### Release Notes
Generate clear, customer-friendly release notes from commit history.

| Prompt | File path |
|---|---|
| Release Notes Generator | `prompts/release-notes-generator/01-release-notes-generator.md` |

### Stakeholder Management
Align people, clarify ownership, and move decisions forward.

| Prompt | File path |
|---|---|
| RACI and Stakeholder Map | `prompts/stakeholder-management/01-raci-stakeholder-map.md` |
| DACI Decision Framework | `prompts/stakeholder-management/02-daci-decision-framework.md` |

### Strategy
Set direction, communicate it, and cascade it to your team.

| Prompt | File path |
|---|---|
| Product Strategy Canvas | `prompts/strategy/01-product-strategy-canvas.md` |
| Team OKR Generator | `prompts/strategy/02-team-okr-generator.md` |
| Working Backwards | `prompts/strategy/03-working-backwards.md` |
| Amazon PR/FAQ | `prompts/strategy/04-amazon-pr-faq.md` |
| Dependency Identification | `prompts/strategy/05-dependency-identification.md` |
| Private Preview Plan | `prompts/strategy/06-private-preview-plan.md` |
| Value Proposition Design | `prompts/strategy/07-value-proposition.md` |
| Big Rock Decomposition | `prompts/strategy/08-big-rock-decomposition.md` |
| TCO / CBA / NPV Model | `prompts/strategy/09-tco-cba-npv-model.md` |
| Value Stream Mapping | `prompts/strategy/10-value-stream-mapping.md` |
| Launch Gates | `prompts/strategy/11-launch-gates.md` |

### Synthetic Users
Create and interview AI-generated personas.

| Prompt | File path |
|---|---|
| Create Synthetic User | `prompts/synthetic-users/01-create-synthetic-user.md` |
| Interview Synthetic User | `prompts/synthetic-users/02-interview-synthetic-user.md` |

### Trend Analysis
Stay ahead of what is changing in your market and feedback data.

| Prompt | File path |
|---|---|
| Feedback Trends | `prompts/trend-analysis/01-feedback-trends.md` |
| Industry Trends | `prompts/trend-analysis/02-industry-trends.md` |

### User Journey Maps
Visualize the end-to-end customer experience.

| Prompt | File path |
|---|---|
| User Journey Map | `prompts/user-journey-maps/01-user-journey-map.md` |

---

## Quick Reference — Most-Used Prompts

| Task | File path |
|---|---|
| Run a customer interview | `prompts/customer-discovery/01-interview-guide.md` |
| Analyse a customer meeting transcript | `prompts/communications/02-customer-meeting-to-team-update.md` |
| Gap analysis vs. competitors | `prompts/competitive-analysis/04-capability-gap-analysis.md` |
| Prioritize features with Kano | `prompts/idea-evaluation/05-kano-analysis.md` |
| Run a MoSCoW session | `prompts/idea-evaluation/06-moscow-prioritization.md` |
| Map stakeholders and RACI | `prompts/stakeholder-management/01-raci-stakeholder-map.md` |
| Document a decision with DACI | `prompts/stakeholder-management/02-daci-decision-framework.md` |
| Build a product strategy canvas | `prompts/strategy/01-product-strategy-canvas.md` |
| Cascade company OKRs to team OKRs | `prompts/strategy/02-team-okr-generator.md` |
| Write a weekly leadership update | `prompts/communications/01-weekly-leadership-update.md` |
| Write a PRD | `prompts/prds/01-prd-generation.md` |
| Write use case documentation | `prompts/prds/02-use-case-documentation.md` |
| Generate user stories | `prompts/prds/03-features-and-user-stories.md` |
| Write a working backwards plan | `prompts/strategy/03-working-backwards.md` |
| Write an Amazon-style PR/FAQ | `prompts/strategy/04-amazon-pr-faq.md` |
| Map feature dependencies | `prompts/strategy/05-dependency-identification.md` |
| Plan a private preview | `prompts/strategy/06-private-preview-plan.md` |
| Design a value proposition | `prompts/strategy/07-value-proposition.md` |
| Decompose a Big Rock | `prompts/strategy/08-big-rock-decomposition.md` |
| Define and run launch gates | `prompts/strategy/11-launch-gates.md` |
| Generate an ERD from a repo | `prompts/architecture-diagrams/03-erd-from-repo.md` |
| Generate a flowchart from a repo | `prompts/architecture-diagrams/04-flowchart-from-repo.md` |

---

## Interaction Pattern

When the user asks for help with a PM task:

1. **Identify** the best matching prompt from the catalog above
2. **Confirm** with the user: "I'll use the [prompt name] template — does that sound right?"
3. **Read** the prompt file to get the full template and placeholder list
4. **Ask** for any missing context: "To fill this template I need: [list placeholders]"
5. **Fill** all placeholders with the user's values
6. **Return** the completed prompt, clearly formatted and ready to use
7. **Offer** output variants: "This prompt also has variants for [X] and [Y] — would either be useful?"

If the user is unsure what they need, ask: "What stage are you at — discovery, strategy, requirements, communication, or go-to-market? And what's the core thing you're trying to produce today?"
