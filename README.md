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
│   │   ├── 02-Ideation.md
│   │   ├── 03-scamper-analysis.md
│   │   ├── 04-vrio-analysis.md
│   │   └── 05-mece-analysis.md
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
├── mcp-server/
│   ├── server.py                         # MCP server exposing prompts as tools
│   ├── requirements.txt
│   └── README.md                         # MCP setup & tutorial
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

### With the MCP Server

The `mcp-server/` directory contains a [Model Context Protocol](https://modelcontextprotocol.io) server that exposes every prompt as a callable tool inside Claude Desktop, Claude Code, Cursor, and any other MCP-compatible client.

**Tools exposed:**

| Tool | What it does |
| --- | --- |
| `list_prompts` | List all prompts, optionally filtered by category |
| `get_categories` | List all categories with prompt counts |
| `search_prompts` | Full-text search across titles, purposes, and content |
| `get_prompt` | Return the raw markdown of a prompt |
| `fill_prompt` | Fill placeholders and return a ready-to-use prompt |

**Quick setup:**

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

Or connect via Claude Code CLI:

```bash
claude mcp add pm-prompts /absolute/path/to/mcp-server/.venv/bin/python /absolute/path/to/mcp-server/server.py
```

**Connect to GitHub Copilot (VS Code):**

Create `.vscode/mcp.json` in this workspace root (or open the Command Palette → **MCP: Open User Configuration** for a global config):

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

> Note: VS Code uses `"servers"` as the root key, not `"mcpServers"`.

Then in Copilot Chat, switch to **Agent** mode — MCP tools are only available there. Click the Tools icon in the chat input to confirm `list_prompts`, `search_prompts`, `fill_prompt`, and others are listed.

See [mcp-server/README.md](mcp-server/README.md) for the full setup guide, Claude Code integration, and an MCP tutorial.

## Prompt Engineering Principles

1. **Context → Inputs → Outputs** — Every prompt follows this three-part structure
2. **Be specific** — Generic prompts produce generic outputs
3. **Iterate** — Refine your prompt if the first result isn't right
4. **Admit unknowns** — Tell the AI "I don't know this" rather than guessing

