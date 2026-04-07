---
name: ai-pm-prompts
description: >
  A structured library of AI prompts for Product Managers, covering the full product lifecycle
  from customer discovery through prototyping. Use this skill whenever a PM needs help with
  customer interviews, research synthesis, market analysis, competitive intelligence, ideation,
  idea evaluation, or solution validation. Triggers on phrases like "customer discovery",
  "interview guide", "competitive analysis", "SWOT", "market research", "trend analysis",
  "ideation", "pre-mortem", "RICE scoring", "synthetic user", "problem statement", "JTBD",
  or any product management research and strategy task.
---

# AI Prompts for Product Managers

A curated prompt library based on the book *AI for Product Managers* by 5D Vision.
Each prompt is a battle-tested template designed for the Context → Inputs → Outputs structure.

## How to Use

1. Pick the workflow phase you're in (discovery, research, ideation, evaluation, prototyping)
2. Read the relevant prompt file from `prompts/<phase>/`
3. Fill in the bracketed `[PLACEHOLDERS]` with your specific context
4. Run the prompt in Claude or paste it into your preferred GenAI tool

## Prompt Library Map

| Phase | Directory | What's Inside |
|---|---|---|
| Customer Discovery | `prompts/customer-discovery/` | Interview guides, transcript analysis, JTBD, survey analysis, pattern finding |
| Synthetic Users | `prompts/synthetic-users/` | Creating and interviewing AI-generated personas |
| Market Research | `prompts/market-research/` | Structured market analysis, cross-referencing sources |
| Competitive Analysis | `prompts/competitive-analysis/` | Positioning, feature comparison, target customers |
| Trend Analysis | `prompts/trend-analysis/` | Feedback trend monitoring, industry trend identification |
| Ideation | `prompts/ideation/` | Problem-to-solution generation, Accelerate/Expand/Simplify |
| Idea Evaluation | `prompts/idea-evaluation/` | RICE scoring, pre-mortem, assumption mapping, validation questions |
| Prototyping | `prompts/prototyping/` | UI prototype prompts, example specs |

## Quick Start

To run a prompt, read the template, fill in your context, and execute. Example:

```bash
# Read the interview guide prompt
cat prompts/customer-discovery/01-interview-guide.md

# Read the competitive positioning prompt
cat prompts/competitive-analysis/01-positioning-messaging.md
```

## Prompt Engineering Tips

- **Structure is king.** Every prompt follows Context → Inputs → Outputs.
- **Context matters most.** Be specific about your product, users, and constraints.
  Don't say "Research my competitors" — say exactly what your product does and who it serves.
- **Iterate.** If the output is too generic, add more context and try again.
- **Say "I don't know."** If you lack data for a section, tell the AI honestly.
  It's better than guessing.

## Scripts

- `scripts/run-prompt.sh` — Helper to run a prompt template with variable substitution
- `scripts/list-prompts.sh` — List all available prompts with descriptions

