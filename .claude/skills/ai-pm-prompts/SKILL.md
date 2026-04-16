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
| Communications | `prompts/communications/` | Weekly leadership updates for Teams and Slack |
| Competitive Analysis | `prompts/competitive-analysis/` | Positioning, feature comparison, target customers, capability gap analysis |
| Customer Discovery | `prompts/customer-discovery/` | Interview guides, transcript analysis, JTBD, survey analysis, sentiment analysis of work items, pattern finding |
| Idea Evaluation | `prompts/idea-evaluation/` | RICE scoring, pre-mortem, assumption mapping, validation questions, Kano analysis, MoSCoW prioritization |
| Ideation | `prompts/ideation/` | Problem-to-solution generation, SCAMPER, VRIO, MECE analysis |
| Market Research | `prompts/market-research/` | Structured market analysis, cross-referencing sources |
| Metrics | `prompts/metrics/` | Feature success metrics and measurement frameworks |
| PRDs | `prompts/prds/` | Product Requirements Documents (Amazon 6-pager style) |
| Prototyping | `prompts/prototyping/` | UI prototype specs |
| Release Notes | `prompts/release-notes-generator/` | Release notes from git commit history |
| Stakeholder Management | `prompts/stakeholder-management/` | RACI matrix, DACI decision framework, stakeholder influence and support analysis |
| Strategy | `prompts/strategy/` | Product strategy canvas, team OKR generation and cascading, working backwards planning, Amazon PR/FAQ |
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
| Write a PRD | `prompts/prds/01-prd-generation.md` |
| Write a working backwards plan | `prompts/strategy/03-working-backwards.md` |
| Write an Amazon-style PR/FAQ | `prompts/strategy/04-amazon-pr-faq.md` |

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
