# AI Prompts for Product Managers

> A structured, version-controlled prompt library for Product Managers using GenAI across the product lifecycle.


## Overview

This repo organizes proven PM prompts into a **Claude Code**–compatible skill structure. Each prompt is a standalone markdown template you can copy, customize, and run.

## Repository Structure

```
AI-Prompts-for-Product-Management/
├── SKILL.md                          # Skill entry point (for Claude Code)
├── README.md                         # This file
├── prompts/
│   ├── architecture-diagrams/
│   │   └── 01-sequence-diagram-from-repo.md
│   ├── competitive-analysis/
│   │   ├── 01-positioning-messaging.md
│   │   ├── 02-feature-comparison.md
│   │   └── 03-target-customers.md
│   ├── customer-discovery/
│   │   ├── 01-interview-guide.md
│   │   ├── 02-blind-spot-detection.md
│   │   ├── 03-research-synthesis.md
│   │   ├── 04-problem-refinement.md
│   │   ├── 05-transcript-theme-analysis.md
│   │   ├── 06-transcript-deep-dive.md
│   │   ├── 07-jtbd-analysis.md
│   │   ├── 08-survey-open-ended.md
│   │   ├── 09-survey-segment-comparison.md
│   │   └── 10-multi-source-patterns.md
│   ├── idea-evaluation/
│   │   ├── 01-rice-scoring.md
│   │   ├── 02-pre-mortem.md
│   │   ├── 03-assumption-mapping.md
│   │   └── 04-validation-questions.md
│   ├── ideation/
│   │   ├── 01-problem-to-solution.md
│   │   └── Ideation1.md
│   ├── market-research/
│   │   ├── 01-structured-market-analysis.md
│   │   └── 02-evidence-and-contradictions.md
│   ├── metrics/
│   │   └── 01-feature-success-metrics.md
│   ├── prds/
│   │   └── 01-prd-generation.md
│   ├── prototyping/
│   │   └── 01-ui-prototype-spec.md
│   ├── release-notes-generator/
│   │   └── 01-release-notes-generator.md
│   ├── synthetic-users/
│   │   ├── 01-create-synthetic-user.md
│   │   └── 02-interview-synthetic-user.md
│   ├── trend-analysis/
│   │   ├── 01-feedback-trends.md
│   │   └── 02-industry-trends.md
│   └── user-journey-maps/
│       └── 01-user-journey-map.md
├── examples/
│   ├── problem-refinement-example.md
│   └── stock-portfolio-example.md
└── scripts/
    ├── run-prompt.sh
    └── list-prompts.sh
```

## Usage

### Direct copy-paste
Open any prompt file, replace `[PLACEHOLDERS]` with your context, and paste into Claude, ChatGPT, or Gemini.

### With Claude Code
```bash
# Claude Code will auto-detect the SKILL.md and offer these prompts contextually
claude "Help me create an interview guide for my B2B SaaS product"
```

### With the helper script
```bash
./scripts/run-prompt.sh prompts/customer-discovery/01-interview-guide.md \
  --problem "onboarding friction for SMB users" \
  --user-type "small business owners"
```

## Prompt Engineering Principles

1. **Context → Inputs → Outputs** — Every prompt follows this three-part structure
2. **Be specific** — Generic prompts produce generic outputs
3. **Iterate** — Refine your prompt if the first result isn't right
4. **Admit unknowns** — Tell the AI "I don't know this" rather than guessing

