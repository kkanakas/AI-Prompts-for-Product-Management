# AI Prompts for Product Managers

> A structured, version-controlled prompt library for Product Managers using GenAI across the product lifecycle.

## Overview

This repo organizes proven PM prompts into a **Claude Code**–compatible skill structure. Each prompt is a standalone markdown template you can copy, customize, and run across Claude, ChatGPT, Gemini, GitHub Copilot, or any other AI assistant.

The library covers the full PM workflow — from customer discovery and competitive analysis through to stakeholder alignment, strategy, and executive communication. Every prompt follows the same structure: context, inputs, and a defined output format so you get consistent, usable results.

The library contains 16 categories, 35+ prompts, and 11 worked examples.

---

## Prompt Catalog

### Architecture Diagrams

Generate technical diagrams directly from your codebase.

| Prompt | What it does |
| --- | --- |
| `01-sequence-diagram-from-repo` | Create a sequence diagram from a code repository |
| `02-uml-class-diagram-from-repo` | Generate a UML class diagram showing classes, attributes, methods, and relationships from a GitHub repository |
| `03-erd-from-repo` | Generate an Entity Relationship Diagram showing entities, attributes, primary/foreign keys, and cardinality from a GitHub repository |
| `04-flowchart-from-repo` | Generate a flowchart capturing control flow, decision points, error paths, and terminal states for a process or feature in a GitHub repository |

### Communications

Turn raw weekly notes into polished, executive-ready messages.

| Prompt | What it does |
| --- | --- |
| `01-weekly-leadership-update` | Generate a structured Teams or Slack weekly update for VP and C-suite audiences |

### Competitive Analysis

Understand your market position and close the gaps that matter.

| Prompt | What it does |
| --- | --- |
| `01-positioning-messaging` | Analyze competitor positioning, value propositions, and SWOT |
| `02-feature-comparison` | Side-by-side feature comparison across competitors |
| `03-target-customers` | Identify and compare competitor target customer segments |
| `04-capability-gap-analysis` | Map gaps between your current capabilities, customer needs, and competitor offerings |

### Customer Discovery

Go deeper with interviews, transcripts, surveys, and work items.

| Prompt | What it does |
| --- | --- |
| `01-interview-guide` | Build a structured interview guide with probing questions and edge case coverage |
| `02-blind-spot-detection` | Identify assumptions and blind spots in your current understanding |
| `03-research-synthesis` | Synthesize findings across multiple research sources |
| `04-problem-refinement` | Sharpen a vague problem statement into specific, testable hypotheses |
| `05-transcript-theme-analysis` | Extract themes and patterns from interview transcripts |
| `06-transcript-deep-dive` | Deep analysis of a single interview transcript |
| `07-jtbd-analysis` | Jobs-to-be-done analysis from customer language |
| `08-survey-open-ended` | Analyze open-ended survey responses at scale |
| `09-survey-segment-comparison` | Compare survey results across customer segments |
| `10-multi-source-patterns` | Surface patterns across multiple research inputs simultaneously |
| `11-sentiment-analysis-in-workitems` | Structured sentiment analysis across Jira issues — flags escalation language, team health signals, and emerging themes |

### Idea Evaluation

Score, stress-test, and prioritize ideas before committing resources.

| Prompt | What it does |
| --- | --- |
| `01-rice-scoring` | Score and rank ideas using the RICE framework |
| `02-pre-mortem` | Identify ways an initiative could fail before it starts |
| `03-assumption-mapping` | Map and rank the assumptions your strategy depends on |
| `04-validation-questions` | Generate the questions you need to answer before building |
| `05-kano-analysis` | Classify features as Must-Have, Performance, Delighter, Indifferent, or Reverse |
| `06-moscow-prioritization` | Facilitate team prioritization using Must / Should / Could / Won't framework |

### Ideation

Generate and evaluate ideas systematically.

| Prompt | What it does |
| --- | --- |
| `01-problem-to-solution` | Generate solution ideas from a problem statement |
| `02-Ideation` | Structured ideation session with divergent and convergent phases |
| `03-scamper-analysis` | Apply the SCAMPER technique to an existing product or feature |
| `04-vrio-analysis` | Assess competitive advantage using the VRIO framework |
| `05-mece-analysis` | Structure a problem space using MECE principles |

### Market Research

Build a rigorous picture of your market and validate your assumptions.

| Prompt | What it does |
| --- | --- |
| `01-structured-market-analysis` | Systematic analysis of market size, dynamics, and trends |
| `02-evidence-and-contradictions` | Surface evidence that supports and contradicts your market thesis |
| `03-comprehensive-market-landscape` | C-suite-ready landscape covering trends, SWOT, PESTLE, and information gaps from public sources |

### Metrics

Define what success looks like before you build.

| Prompt | What it does |
| --- | --- |
| `01-feature-success-metrics` | Define leading and lagging success metrics for a feature |

### PRDs

Write product requirements documents that engineering teams can act on.

| Prompt | What it does |
| --- | --- |
| `01-prd-generation` | Generate a structured PRD in Amazon 6-pager style |

### Prototyping

Specify UI prototypes with enough detail for engineers and designers.

| Prompt | What it does |
| --- | --- |
| `01-ui-prototype-spec` | Generate a detailed UI prototype specification |

### Release Notes

Generate clear, customer-friendly release notes from commit history.

| Prompt | What it does |
| --- | --- |
| `01-release-notes-generator` | Generate release notes from a git commit log |

### Stakeholder Management

Align people, clarify ownership, and move decisions forward.

| Prompt | What it does |
| --- | --- |
| `01-raci-stakeholder-map` | Build a RACI matrix and stakeholder influence map with engagement strategies |
| `02-daci-decision-framework` | Document a product decision with clear Driver, Approver, Contributors, and Informed roles — prevents decision paralysis and revisiting |

### Strategy

Set direction, communicate it clearly, and cascade it to your team.

| Prompt | What it does |
| --- | --- |
| `01-product-strategy-canvas` | Build a nine-section strategy canvas covering vision, value proposition, competitive positioning, strategic bets, and success metrics |
| `02-team-okr-generator` | Cascade company OKRs into well-formed, measurable team OKRs with a health check and team communication draft |
| `03-working-backwards` | Write a working backwards plan — internal press release, customer FAQs, value statement, and success metrics — anchored in customer outcome before any build begins |
| `04-amazon-pr-faq` | Write a full Amazon-style Press Release and FAQ document — the discipline of announcing a finished product before building it, to force clarity on customer value before any code is written |
| `05-dependency-identification` | Identify and categorize all dependencies for a feature initiative across team, technical, product, regulatory, third-party, and timeline dimensions — with a risk-ranked dependency map and critical path |

### Synthetic Users

Create and interview AI-generated personas grounded in real customer data.

| Prompt | What it does |
| --- | --- |
| `01-create-synthetic-user` | Create a detailed synthetic user persona |
| `02-interview-synthetic-user` | Run a simulated interview with a synthetic user |

### Trend Analysis

Stay ahead of what is changing in your market and your feedback data.

| Prompt | What it does |
| --- | --- |
| `01-feedback-trends` | Identify trends and shifts in customer feedback over time |
| `02-industry-trends` | Analyze broader industry trends relevant to your product |

### User Journey Maps

Visualize the end-to-end customer experience.

| Prompt | What it does |
| --- | --- |
| `01-user-journey-map` | Create a detailed user journey map with emotions, touchpoints, and opportunities |

---

## Examples

Worked examples showing filled-in prompts and generated outputs — useful for understanding what each prompt produces before using it.

| Example | Prompt it demonstrates |
| --- | --- |
| [problem-refinement-example](examples/problem-refinement-example.md) | `customer-discovery/04-problem-refinement` |
| [stock-portfolio-example](examples/stock-portfolio-example.md) | `prototyping/01-ui-prototype-spec` |
| [sentiment-analysis-workitems-example](examples/sentiment-analysis-workitems-example.md) | `customer-discovery/11-sentiment-analysis-in-workitems` |
| [capability-gap-analysis-example](examples/capability-gap-analysis-example.md) | `competitive-analysis/04-capability-gap-analysis` |
| [kano-analysis-example](examples/kano-analysis-example.md) | `idea-evaluation/05-kano-analysis` |
| [moscow-prioritization-example](examples/moscow-prioritization-example.md) | `idea-evaluation/06-moscow-prioritization` |
| [raci-stakeholder-map-example](examples/raci-stakeholder-map-example.md) | `stakeholder-management/01-raci-stakeholder-map` |
| [weekly-leadership-update-example](examples/weekly-leadership-update-example.md) | `communications/01-weekly-leadership-update` |
| [product-strategy-canvas-example](examples/product-strategy-canvas-example.md) | `strategy/01-product-strategy-canvas` |
| [team-okr-generator-example](examples/team-okr-generator-example.md) | `strategy/02-team-okr-generator` |
| [daci-decision-framework-example](examples/daci-decision-framework-example.md) | `stakeholder-management/02-daci-decision-framework` |
| [working-backwards-example](examples/working-backwards-example.md) | `strategy/03-working-backwards` |
| [amazon-pr-faq-example](examples/amazon-pr-faq-example.md) | `strategy/04-amazon-pr-faq` |

---

## Repository Structure

```text
AI-Prompts-for-Product-Management/
├── SKILL.md                          # Skill definition (root copy)
├── README.md                         # This file
├── .claude/
│   └── skills/
│       └── ai-pm-prompts/
│           └── SKILL.md             # Project-scoped skill (auto-loaded by Claude Code)
├── .cursor/
│   └── rules/
│       └── pm-prompts.mdc          # Cursor rule (auto-detected)
├── prompts/
│   ├── architecture-diagrams/
│   │   ├── 01-sequence-diagram-from-repo.md
│   │   ├── 02-uml-class-diagram-from-repo.md
│   │   ├── 03-erd-from-repo.md
│   │   └── 04-flowchart-from-repo.md
│   ├── communications/
│   │   └── 01-weekly-leadership-update.md
│   ├── competitive-analysis/
│   │   ├── 01-positioning-messaging.md
│   │   ├── 02-feature-comparison.md
│   │   ├── 03-target-customers.md
│   │   └── 04-capability-gap-analysis.md
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
│   │   ├── 10-multi-source-patterns.md
│   │   └── 11-sentiment-analysis-in-workitems
│   ├── idea-evaluation/
│   │   ├── 01-rice-scoring.md
│   │   ├── 02-pre-mortem.md
│   │   ├── 03-assumption-mapping.md
│   │   ├── 04-validation-questions.md
│   │   ├── 05-kano-analysis.md
│   │   └── 06-moscow-prioritization.md
│   ├── ideation/
│   │   ├── 01-problem-to-solution.md
│   │   ├── 02-Ideation.md
│   │   ├── 03-scamper-analysis.md
│   │   ├── 04-vrio-analysis.md
│   │   └── 05-mece-analysis.md
│   ├── market-research/
│   │   ├── 01-structured-market-analysis.md
│   │   ├── 02-evidence-and-contradictions.md
│   │   └── 03-comprehensive-market-landscape.md
│   ├── metrics/
│   │   └── 01-feature-success-metrics.md
│   ├── prds/
│   │   └── 01-prd-generation.md
│   ├── prototyping/
│   │   └── 01-ui-prototype-spec.md
│   ├── release-notes-generator/
│   │   └── 01-release-notes-generator.md
│   ├── stakeholder-management/
│   │   ├── 01-raci-stakeholder-map.md
│   │   └── 02-daci-decision-framework.md
│   ├── strategy/
│   │   ├── 01-product-strategy-canvas.md
│   │   ├── 02-team-okr-generator.md
│   │   ├── 03-working-backwards.md
│   │   ├── 04-amazon-pr-faq.md
│   │   └── 05-dependency-identification.md
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
│   ├── stock-portfolio-example.md
│   ├── sentiment-analysis-workitems-example.md
│   ├── capability-gap-analysis-example.md
│   ├── kano-analysis-example.md
│   ├── moscow-prioritization-example.md
│   ├── raci-stakeholder-map-example.md
│   ├── weekly-leadership-update-example.md
│   ├── product-strategy-canvas-example.md
│   ├── team-okr-generator-example.md
│   ├── daci-decision-framework-example.md
│   ├── working-backwards-example.md
│   └── amazon-pr-faq-example.md
├── mcp-server/
│   ├── server.py                         # MCP server exposing prompts as tools
│   ├── requirements.txt
│   └── README.md                         # MCP setup & tutorial
└── scripts/
    ├── run-prompt.sh
    └── list-prompts.sh
```

---

## Usage

### Install as a Claude Code Skill

The skill is already installed for project-scoped use — `.claude/skills/ai-pm-prompts/SKILL.md` is included in this repo. When you open this directory in Claude Code, the skill is detected automatically with no setup required.

Skills are discovered automatically from the `.claude/skills/` directory — no CLI command is needed.

**To make the skill available globally across all your projects:**

Copy it into your personal Claude skills directory:

```bash
mkdir -p ~/.claude/skills/ai-pm-prompts
cp .claude/skills/ai-pm-prompts/SKILL.md ~/.claude/skills/ai-pm-prompts/SKILL.md
```

Claude Code loads it automatically from that point forward — no restart required.

**Use it naturally:**

```text
"Help me run a Kano analysis on these eight features"
"Create a DACI for our mobile strategy decision"
"Build team OKRs from our company OKRs"
"Write a weekly leadership update for my VP"
```

Claude Code reads the `SKILL.md` description and trigger phrases to decide when to activate the skill, then guides you through filling the relevant prompt with your context.

---

### Install in Claude Desktop

Claude Desktop installs skills via a ZIP upload through the UI.

**Step 1 — Create the skill ZIP:**

```bash
zip -r ai-pm-prompts.zip SKILL.md prompts/ examples/
```

**Step 2 — Upload the skill:**

1. Open Claude Desktop
2. Go to **Customize → Skills**
3. Click the **+** button → **Create skill**
4. Select **Upload a skill**
5. Upload `ai-pm-prompts.zip`
6. Toggle the skill **on**

The skill will now appear in Claude Desktop and will be suggested automatically when you ask about customer discovery, prioritization, stakeholder mapping, OKRs, strategy, or any other PM task covered by the library.

> **Note:** Code execution must be enabled in Claude Desktop settings for skills to function. For Team or Enterprise plans, your organisation owner must enable "Code execution and file creation" and "Skills" before custom skills can be uploaded.

---

### Install in Cursor

Cursor uses **rules** (`.mdc` files in `.cursor/rules/`) instead of skills. This repo ships with a pre-built rule that teaches Cursor's AI agent the full prompt catalog.

**Project-scoped (automatic) — no setup required:**

The rule file is already included at `.cursor/rules/pm-prompts.mdc`. When you open this repo in Cursor, it is detected automatically. Just start a conversation:

```text
"Help me run a RICE scoring session for these five features"
"Create a competitive gap analysis against Datadog and Splunk"
"Build a PESTLE analysis for our European expansion"
```

Cursor reads the rule's description and trigger phrases to decide when to activate it, then finds the right prompt template, fills in your context, and returns a ready-to-use prompt.

**Global (available across all your projects):**

Copy the rule into your personal Cursor rules directory so it works in every workspace:

```bash
mkdir -p ~/.cursor/rules
cp .cursor/rules/pm-prompts.mdc ~/.cursor/rules/pm-prompts.mdc
```

Cursor loads global rules automatically — no restart required.

> **How Cursor rules differ from Claude Code skills:** Claude Code uses `SKILL.md` with YAML frontmatter; Cursor uses `.mdc` files with `description`, `globs`, and `alwaysApply` fields. Both achieve the same goal — giving the AI agent persistent context about when and how to use this prompt library.

---

### Direct copy-paste

Open any prompt file, replace `[PLACEHOLDERS]` with your context, and paste into Claude, ChatGPT, Gemini, or Copilot.

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

### With the MCP Server

The `mcp-server/` directory contains a [Model Context Protocol](https://modelcontextprotocol.io) server that exposes every prompt as a callable tool inside Claude Desktop, Claude Code, GitHub Copilot, the OpenAI Agents SDK, and any other MCP-compatible client.

**Tools exposed:**

| Tool | What it does |
| --- | --- |
| `list_prompts` | List all prompts, optionally filtered by category |
| `get_categories` | List all categories with prompt counts and descriptions |
| `search_prompts` | Full-text search across titles, purposes, and content |
| `get_prompt` | Return the raw markdown of a prompt |
| `fill_prompt` | Fill placeholders and return a ready-to-use prompt |

**Quick setup — venv:**

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
pip install -r requirements.txt
```

**Quick setup — uv (faster, no activation step):**

```bash
cd mcp-server
uv venv
uv pip install -r requirements.txt
```

**Connect to Claude Desktop** — add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "/absolute/path/to/mcp-server/.venv/bin/python",
      "args": ["/absolute/path/to/AI-Prompts-for-Product-Management/mcp-server/server.py"]
    }
  }
}
```

**Connect via Claude Code CLI:**

```bash
claude mcp add pm-prompts /absolute/path/to/mcp-server/.venv/bin/python /absolute/path/to/mcp-server/server.py
```

**Connect to GitHub Copilot (VS Code)** — create `.vscode/mcp.json`:

```json
{
  "servers": {
    "pm-prompts": {
      "type": "stdio",
      "command": "/absolute/path/to/mcp-server/.venv/bin/python",
      "args": ["/absolute/path/to/AI-Prompts-for-Product-Management/mcp-server/server.py"]
    }
  }
}
```

> Note: VS Code uses `"servers"` as the root key, not `"mcpServers"`. Switch Copilot Chat to **Agent** mode — MCP tools are only available there.

See [mcp-server/README.md](mcp-server/README.md) for the full setup guide including `uv` configs, OpenAI Agents SDK integration, and an MCP tutorial.

---

## Prompt Engineering Principles

1. **Context → Inputs → Outputs** — Every prompt follows this three-part structure
2. **Be specific** — Generic prompts produce generic outputs
3. **Iterate** — Refine your prompt if the first result isn't right
4. **Admit unknowns** — Tell the AI "I don't know this" rather than guessing
