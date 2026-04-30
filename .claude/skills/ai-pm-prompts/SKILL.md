---
name: ai-pm-prompts
description: >
  A structured library of AI prompts for Product Managers covering the full product lifecycle.
  Use this skill whenever a PM needs help with customer interviews, research synthesis, market
  analysis, competitive intelligence, capability gap analysis, ideation, idea evaluation,
  Kano analysis, MoSCoW prioritization, RICE scoring, stakeholder mapping, RACI matrix,
  DACI decision framework, product strategy canvas, OKR generation, weekly leadership updates,
  sentiment analysis of work items, PRD generation, user journey mapping, release notes,
  prototyping, or any product management research, strategy, or communication task.
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
  "big rock", "initiative decomposition", "epic breakdown", "MVP scope", "critical path",
  "use case", "use case documentation", "actor", "precondition", "main flow", "exception flow",
  "acceptance criteria", "business rules", "functional requirements",
  "user story", "given when then", "gherkin", "story map", "INVEST", "story points",
  "launch gate", "go no-go", "release readiness", "release gate", "gate review",
  "launch checklist", "release criteria", "waiver", "post-release monitoring",
  "customer meeting", "meeting transcript", "meeting notes", "customer update",
  "meeting summary", "slack update", "jira from transcript",
  or any product management task.
---

# AI Prompts for Product Managers

A structured, version-controlled prompt library for Product Managers using GenAI across the full product lifecycle — from customer discovery and competitive analysis through to stakeholder alignment, strategy, and executive communication.

Each prompt follows the same structure: context, inputs, and a defined output format so you get consistent, usable results across Claude, ChatGPT, Gemini, GitHub Copilot, or any AI assistant.

## How to Use

1. Identify the phase you are in (discovery, research, ideation, evaluation, strategy, communication)
2. Find the relevant prompt in `prompts/<category>/`
3. Fill in the `[PLACEHOLDERS]` with your specific context
4. Run the prompt in your preferred AI tool, or use the MCP server to call it directly

## Prompt Library

| Category | Directory | What's Inside |
|---|---|---|
| Architecture Diagrams | `prompts/architecture-diagrams/` | Sequence diagrams, UML class diagrams, Entity Relationship Diagrams, and flowcharts from code repositories |
| Communications | `prompts/communications/` | Weekly leadership updates, customer meeting transcript to Slack update and Jira tickets |
| Competitive Analysis | `prompts/competitive-analysis/` | Positioning, feature comparison, target customers, capability gap analysis |
| Customer Discovery | `prompts/customer-discovery/` | Interview guides, transcript analysis, JTBD, survey analysis, sentiment analysis of work items, pattern finding |
| Idea Evaluation | `prompts/idea-evaluation/` | RICE scoring, pre-mortem, assumption mapping, validation questions, Kano analysis, MoSCoW prioritization |
| Ideation | `prompts/ideation/` | Problem-to-solution generation, SCAMPER, VRIO, MECE analysis |
| Market Research | `prompts/market-research/` | Structured market analysis, cross-referencing sources |
| Metrics | `prompts/metrics/` | Feature success metrics, and AI product metrics frameworks covering latency, task completion, output quality, business value, and trust and safety |
| PRDs | `prompts/prds/` | Product Requirements Documents (Amazon 6-pager style), use case documentation, features and user stories with Given/When/Then criteria |
| Prototyping | `prompts/prototyping/` | Lo-fi wireframe briefs, mid-fi flow specs, clickthrough demo scripts, Wizard of Oz protocols, prompt-powered UI generation, AI feature stubs, agent workflow simulations, API-connected LLM prototypes, narrative prototypes, and data dashboard prototypes |
| Release Notes | `prompts/release-notes-generator/` | Release notes from git commit history |
| Stakeholder Management | `prompts/stakeholder-management/` | RACI matrix, DACI decision framework, stakeholder influence and support analysis |
| Strategy | `prompts/strategy/` | Product strategy canvas, OKR generation, working backwards, Amazon PR/FAQ, dependency identification, private preview planning, value proposition design, Big Rock decomposition, launch gates |
| Synthetic Users | `prompts/synthetic-users/` | Creating and interviewing AI-generated personas |
| Trend Analysis | `prompts/trend-analysis/` | Feedback trend monitoring, industry trend identification |
| User Journey Maps | `prompts/user-journey-maps/` | End-to-end user journey mapping with emotions and opportunities |

## Quick Reference — Most-Used Prompts

| Task | Prompt |
|---|---|
| Run a customer interview | `prompts/customer-discovery/01-interview-guide.md` |
| Analyse sentiment in Jira issues | `prompts/customer-discovery/11-sentiment-analysis-in-workitems` |
| Gap analysis vs. competitors | `prompts/competitive-analysis/04-capability-gap-analysis.md` |
| Prioritize features with Kano | `prompts/idea-evaluation/05-kano-analysis.md` |
| Run a MoSCoW session | `prompts/idea-evaluation/06-moscow-prioritization.md` |
| Map stakeholders and RACI | `prompts/stakeholder-management/01-raci-stakeholder-map.md` |
| Document a decision with DACI | `prompts/stakeholder-management/02-daci-decision-framework.md` |
| Build a product strategy canvas | `prompts/strategy/01-product-strategy-canvas.md` |
| Cascade company OKRs to team OKRs | `prompts/strategy/02-team-okr-generator.md` |
| Write a weekly leadership update | `prompts/communications/01-weekly-leadership-update.md` |
| Turn a customer meeting into a Slack update + Jira tickets | `prompts/communications/02-customer-meeting-to-team-update.md` |
| Write a PRD | `prompts/prds/01-prd-generation.md` |
| Write use case documentation | `prompts/prds/02-use-case-documentation.md` |
| Generate user stories from use cases | `prompts/prds/03-features-and-user-stories.md` |
| Write a working backwards plan | `prompts/strategy/03-working-backwards.md` |
| Write an Amazon-style PR/FAQ | `prompts/strategy/04-amazon-pr-faq.md` |
| Map feature dependencies and critical path | `prompts/strategy/05-dependency-identification.md` |
| Plan a multi-phased private preview | `prompts/strategy/06-private-preview-plan.md` |
| Design a value proposition canvas | `prompts/strategy/07-value-proposition.md` |
| Decompose a Big Rock into epics and features | `prompts/strategy/08-big-rock-decomposition.md` |
| Define and run launch gate reviews | `prompts/strategy/11-launch-gates.md` |

## MCP Server

The `mcp-server/` directory exposes every prompt as a callable tool inside Claude Desktop, Claude Code, GitHub Copilot, and the OpenAI Agents SDK. Once connected, your AI assistant can browse, search, and fill prompts without you leaving the conversation.

See `mcp-server/README.md` for full setup instructions.

## Prompt Engineering Tips

- **Context matters most.** Be specific about your product, users, and constraints. "Research my competitors" produces generic output; naming your product, target customer, and the top three competitors produces actionable analysis.
- **Structure is consistent.** Every prompt follows Context → Inputs → Outputs.
- **Iterate.** If the first output is too generic, add more context and rerun.
- **Admit unknowns.** If you lack data for a section, say so — the AI handles gaps better than guesses.
- **Baselines unlock measurement.** For OKRs and metrics prompts, always include current numbers — a KR without a baseline is a wish, not a target.

## Scripts

- `scripts/run-prompt.sh` — Run a prompt template with variable substitution
- `scripts/list-prompts.sh` — List all available prompts with descriptions
