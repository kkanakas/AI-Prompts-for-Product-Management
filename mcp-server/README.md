# PM Prompts MCP Server

A [Model Context Protocol](https://modelcontextprotocol.io) server that exposes every prompt in this repository as callable tools inside Claude Desktop, Claude Code, GitHub Copilot, OpenAI Agents, and any other MCP-compatible client.

---

## What This Server Does

Without MCP, using these prompts means browsing to a file, copying the template, filling in placeholders manually, and pasting into your AI tool.

With MCP, your AI assistant can:

- **Discover** what prompts exist (`list_prompts`, `get_categories`)
- **Find** the right one for your task (`search_prompts`)
- **Retrieve** the full template (`get_prompt`)
- **Fill it** with your context and hand it back ready to run (`fill_prompt`)

All without leaving the conversation.

### Tools Exposed

| Tool | What it does | Key args |
|---|---|---|
| `list_prompts` | List all prompts, optionally filtered by category | `category` (optional) |
| `get_categories` | List all categories with counts and descriptions | — |
| `search_prompts` | Full-text search across titles, purposes, and content | `query` |
| `get_prompt` | Return the raw markdown of a prompt | `prompt_id` |
| `fill_prompt` | Fill placeholders and return a ready-to-use prompt | `prompt_id`, `variables` dict |

---

## Prerequisites

- **Python 3.10 or later** — check with `python3 --version`
- One of:
  - **venv** (built into Python, no install needed)
  - **uv** (faster alternative — install with `curl -LsSf https://astral.sh/uv/install.sh | sh`)

---

## Setup

Choose **one** of the two environment options below. Both work identically at runtime — `uv` is faster to install and requires no manual activation step.

### Option A — venv (standard Python)

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

Your shell prompt changes to `(.venv)` confirming the environment is active.

To get the absolute path to the Python binary (needed for client configs below):

```bash
which python          # macOS / Linux — copy this path
```

### Option B — uv (recommended)

```bash
cd mcp-server
uv venv
uv pip install -r requirements.txt
```

With `uv`, you reference the server using `uv run` in client configs — no activation step needed.

---

## Test the Server Locally

### Quick smoke test

```bash
# venv
python server.py

# uv
uv run python server.py
```

The server waits silently for MCP messages on stdin — that is expected behavior. Press `Ctrl+C` to exit.

### Interactive browser UI (MCP Inspector)

```bash
npx @modelcontextprotocol/inspector python mcp-server/server.py
```

This opens a browser UI at `localhost:5173` where you can call every tool interactively and inspect the JSON responses.

---

## Connect to Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (create the file if it does not exist). Add the `pm-prompts` block inside `mcpServers`.

With **venv** — point `command` at the venv Python binary so Claude Desktop uses the environment where `mcp` is installed:

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

With **uv** — no venv activation needed, `uv run` handles the environment automatically:

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "python",
        "/absolute/path/to/AI-Prompts-for-Product-Management/mcp-server/server.py"
      ]
    }
  }
}
```

After saving, **restart Claude Desktop**. A hammer icon in the chat input confirms MCP tools are loaded.

---

## Connect to Claude Code (CLI)

### One-line setup

```bash
# venv
claude mcp add pm-prompts /absolute/path/to/mcp-server/.venv/bin/python /absolute/path/to/mcp-server/server.py

# uv
claude mcp add pm-prompts uv -- run --with mcp[cli] python /absolute/path/to/mcp-server/server.py
```

### Project-scoped config (`.claude/settings.json`)

Add this to `.claude/settings.json` in the repo root so the server is available to anyone who clones the repo:

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "./mcp-server/.venv/bin/python",
      "args": ["./mcp-server/server.py"]
    }
  }
}
```

Or with `uv`:

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "python",
        "./mcp-server/server.py"
      ]
    }
  }
}
```

Verify the tools are live inside a Claude Code session:

```
/mcp
```

---

## Connect to GitHub Copilot (VS Code)

Create `.vscode/mcp.json` in the repo root (or open the Command Palette → **MCP: Open User Configuration** for a global config shared across all workspaces).

With **venv**:

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

With **uv**:

```json
{
  "servers": {
    "pm-prompts": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "python",
        "/absolute/path/to/AI-Prompts-for-Product-Management/mcp-server/server.py"
      ]
    }
  }
}
```

> **Note:** VS Code uses `"servers"` as the root key, not `"mcpServers"`.

After saving, open Copilot Chat and switch to **Agent** mode — MCP tools are only available in Agent mode, not Chat mode. Click the **Tools** icon in the chat input to confirm `list_prompts`, `search_prompts`, `fill_prompt`, and others appear in the list.

---

## Connect to OpenAI (Agents SDK)

The [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) supports MCP servers natively via `MCPServerStdio`.

### Install the SDK

```bash
# venv
pip install openai-agents

# uv
uv add openai-agents
```

### Example agent script

```python
import asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main():
    server = MCPServerStdio(
        command="python",                          # or "uv"
        args=["/absolute/path/to/mcp-server/server.py"],
        # If using uv:
        # args=["run", "--with", "mcp[cli]", "python", "/absolute/path/to/mcp-server/server.py"]
    )

    async with server:
        agent = Agent(
            name="PM Assistant",
            instructions="You are a product management assistant. Use the pm-prompts tools to find and fill prompt templates when the user needs help with PM tasks.",
            mcp_servers=[server],
        )
        result = await Runner.run(
            agent,
            "Find me the best prompt for running a Kano analysis on a new feature set."
        )
        print(result.final_output)

asyncio.run(main())
```

### OpenAI Responses API (remote MCP)

The OpenAI Responses API supports **remote** MCP servers over HTTPS. To use this server with the Responses API, expose it over SSE using a proxy:

```bash
pip install mcp-proxy
mcp-proxy --port 8000 python mcp-server/server.py
```

Then reference it in your API call:

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-4o",
    tools=[{
        "type": "mcp",
        "server_url": "http://localhost:8000/sse",
        "server_label": "pm-prompts"
    }],
    input="Find and fill the OKR generator prompt for a growth team."
)
```

---

## Example Conversations

Once connected, talk to your AI assistant naturally — it will call the right tools automatically.

### Customer Discovery

> "I need to do customer discovery for a B2B invoicing tool. Find the right prompt and fill it in for me."

Calls `search_prompts("customer discovery")`, then `fill_prompt("customer-discovery/01-interview-guide", {"[PROBLEM]": "invoicing friction for SMB owners", "[USER TYPE]": "freelancers and small business owners"})` and returns a ready-to-use interview guide.

> "Analyse the sentiment in these Jira issues and tell me where the team is struggling."

Calls `get_prompt("customer-discovery/10-sentiment-analysis-in-workitems")` and returns the structured sentiment analysis template — paste your Jira export directly into the prompt.

### Competitive Analysis

> "Run a capability gap analysis between us and our top three competitors."

Calls `fill_prompt("competitive-analysis/04-capability-gap-analysis", {"[PRODUCT NAME]": "...", "[TARGET CUSTOMER]": "...", "[LIST YOUR CURRENT CAPABILITIES]": "..."})` and returns a full gap matrix with Critical, Opportunity, Parity, and Differentiator classifications.

> "What positioning prompts do you have?"

Calls `list_prompts("competitive-analysis")` and lists positioning & messaging, feature comparison, target customers, and capability gap analysis.

### Idea Evaluation & Prioritization

> "What prompts do you have for evaluating ideas?"

Calls `list_prompts("idea-evaluation")` and lists RICE scoring, pre-mortem, assumption mapping, validation questions, Kano analysis, and MoSCoW prioritization.

> "Run a Kano analysis on these eight features I'm considering for our Q3 release."

Calls `fill_prompt("idea-evaluation/05-kano-analysis", {"[PRODUCT NAME]": "...", "[FEATURE 1]": "...", ...})` and returns each feature classified as Basic, Performance, Delighter, Indifferent, or Reverse — with an investment priority tier list.

> "Help my team prioritize these capabilities for the next sprint using MoSCoW."

Calls `fill_prompt("idea-evaluation/06-moscow-prioritization", {"[INITIATIVE OR RELEASE SCOPE]": "Q3 sprint", "[CAPABILITY 1]": "...", "[GOAL OF THIS INITIATIVE]": "...", "[CONSTRAINTS]": "6-week window, 3 engineers"})` and returns a full MoSCoW table, scope health check, and team alignment talking points.

### Stakeholder Management

> "Build a RACI matrix for my upcoming platform migration."

Calls `fill_prompt("stakeholder-management/01-raci-stakeholder-map", {"[INITIATIVE]": "Platform migration", "[LIST STAKEHOLDERS]": "Sarah — VP Eng; James — Head of Sales; ..."})` and returns a RACI table, influence and support matrix, engagement strategy, and risk flags.

### Communications

> "I need to send a weekly update to my VP. Here are my rough notes for the week."

Calls `fill_prompt("communications/01-weekly-leadership-update", {"[AUDIENCE]": "VP of Product", "[PRODUCT OR INITIATIVE NAME]": "...", "[DATE]": "...", "[BULLET LIST — completed]": "..."})` and returns a formatted Teams or Slack message under 250 words, ready to send.

### Strategy

> "Help me build a product strategy canvas for our new enterprise tier."

Calls `fill_prompt("strategy/01-product-strategy-canvas", {"[PRODUCT NAME]": "...", "[TARGET CUSTOMER]": "Enterprise IT teams", "[PROBLEM WE ARE SOLVING]": "...", "[12-MONTH GOAL]": "..."})` and returns a nine-section canvas including vision, value proposition, competitive positioning map, strategic bets, and OKRs.

> "Help me build team OKRs that cascade from our company OKRs."

Calls `fill_prompt("strategy/02-team-okr-generator", {"[COMPANY OKRS]": "O1: Grow ARR to $12M. KR1: ...", "[TEAM NAME]": "Growth Team", "[BASELINE METRICS]": "activation rate: 38%"})` and returns 2–3 well-formed Objectives with Key Results, an OKR health check flagging any activity KRs or missing baselines, and a ready-to-send team announcement.

### Browsing and Discovery

> "What categories of PM prompts do you have?"

Calls `get_categories()` and lists all 16 categories with prompt counts and descriptions — from customer discovery and competitive analysis to strategy, stakeholder management, and communications.

> "Show me everything in the strategy category."

Calls `list_prompts("strategy")` and returns the product strategy canvas and team OKR generator with IDs, phases, and purposes.

---

## Extending the Server

### Add a new tool

```python
@mcp.tool()
def export_prompt_as_notion(prompt_id: str) -> str:
    """Export a filled prompt formatted for Notion."""
    prompt = _find_prompt(prompt_id)
    # ... your logic
    return result
```

### Add a new prompt category

Add a new folder and `.md` files under `prompts/` — the server discovers them automatically at startup via `rglob("*.md")`. Then add the new category slug and description to `CATEGORY_DESCRIPTIONS` in `server.py`.

---

## How This Server Was Built

### What is MCP?

MCP (Model Context Protocol) is an open standard that lets AI assistants call external tools at runtime. Think of it as a typed API layer between the assistant and your data sources.

```
You ─── ask AI ─── AI calls MCP tool ─── server reads .md file ─── returns prompt
```

### Anatomy of an MCP Server (Python)

An MCP server has three parts:

**1. The transport layer** — `FastMCP` handles stdio transport automatically:

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("PM Prompts")
```

**2. Tools** — Python functions decorated with `@mcp.tool()`. The docstring is what the AI reads to decide when to call the tool:

```python
@mcp.tool()
def list_prompts(category: str = "") -> str:
    """List all available PM prompt templates, optionally filtered by category."""
    ...
    return json.dumps(result)
```

**3. The entry point:**

```python
if __name__ == "__main__":
    mcp.run()
```

### Design Decisions

| Decision | Rationale |
| --- | --- |
| Parse files at startup, not per-call | Prompts are static; parsing once is faster |
| 5 focused tools | Each does one job — list, search, categorize, get, fill |
| Partial-match fallback in `_find_prompt` | "interview guide" works, not just the exact file ID |
| Bracket notation optional in `fill_prompt` | `"PROBLEM"` and `"[PROBLEM]"` both resolve correctly |
| Return markdown from `fill_prompt` | Renders cleanly in Claude, Copilot, and most AI clients |
