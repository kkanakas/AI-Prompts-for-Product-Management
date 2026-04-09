# PM Prompts MCP Server

A [Model Context Protocol](https://modelcontextprotocol.io) server that exposes every prompt in this repository as callable tools inside Claude Desktop, Claude Code, Cursor, and any other MCP-compatible client.

---

## Tutorial: How This MCP Server Was Built

### What is MCP?

MCP (Model Context Protocol) is an open standard that lets AI assistants call external tools and resources at runtime. Instead of copy-pasting a prompt template from a file, the assistant calls a tool, gets the template back, and uses it directly in the conversation.

```
You ─── ask Claude ─── Claude calls MCP tool ─── server reads .md file ─── returns prompt
```

Think of it as a typed API layer between Claude and your file system (or any other data source).

---

### Why Build One for This Repo?

Without MCP, using these prompts requires you to:
1. Browse to the right file
2. Copy the template
3. Fill in the placeholders manually
4. Paste into Claude

With MCP, Claude can:
- **discover** what prompts exist (`list_prompts`, `get_categories`)
- **find** the right one for your task (`search_prompts`)
- **retrieve** the full template (`get_prompt`)
- **fill it** with your context and hand it back ready to run (`fill_prompt`)

All without leaving the conversation.

---

### Anatomy of an MCP Server (Python)

An MCP server has three parts:

#### 1. The transport layer
MCP servers communicate over **stdio** (default) or SSE. `FastMCP` from the
`mcp` package handles this automatically — you never write transport code.

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("PM Prompts")   # "PM Prompts" is the server name shown in the client
```

#### 2. Tools
Tools are Python functions decorated with `@mcp.tool()`. The docstring becomes
the tool description Claude uses to decide when to call it. Type annotations
become the JSON Schema the client validates against.

```python
@mcp.tool()
def list_prompts(category: str = "") -> str:
    """
    List all available PM prompt templates, optionally filtered by category.
    ...
    """
    ...
    return json.dumps(result)
```

Rules of thumb:
- **Return strings.** Even structured data — serialize it with `json.dumps`.
- **Write detailed docstrings.** Claude reads them to decide whether to call your tool.
- **Keep each tool focused.** One tool = one job.

#### 3. The entry point

```python
if __name__ == "__main__":
    mcp.run()   # starts the stdio server
```

That's it. `mcp.run()` reads from stdin and writes to stdout in the MCP wire format.

---

### Design Decisions for This Server

| Decision | Rationale |
|---|---|
| Parse files at startup, not per-call | Prompts are static; parsing once is faster |
| Expose 5 focused tools | `list`, `search`, `get_categories`, `get_prompt`, `fill_prompt` — each does one thing |
| Partial-match fallback in `_find_prompt` | Forgiving — "interview guide" works, not just the exact ID |
| Bracket notation optional in `fill_prompt` | `"PROBLEM"` and `"[PROBLEM]"` both work |
| Return markdown from `fill_prompt` | Claude can render it nicely back to the user |

---

### Tool Reference

| Tool | What it does | Key args |
|---|---|---|
| `list_prompts` | List all prompts (or filter by category) | `category` (optional) |
| `get_categories` | List all categories with counts | — |
| `search_prompts` | Full-text search across titles, purposes, content | `query` |
| `get_prompt` | Return the raw markdown of a prompt | `prompt_id` |
| `fill_prompt` | Fill placeholders and return a ready-to-use prompt | `prompt_id`, `variables` dict |

---

## Setup

### 1. Install the dependency

```bash
cd mcp-server
pip install -r requirements.txt
```

Or with `uv` (faster):

```bash
uv pip install -r requirements.txt
```

### 2. Test it locally

```bash
python server.py
```

The server waits for MCP messages on stdin. You won't see output until a client connects — that's normal.

You can also use the MCP inspector:

```bash
npx @modelcontextprotocol/inspector python mcp-server/server.py
```

This opens a browser UI where you can call every tool interactively.

---

## Connect to Claude Desktop

Add this block to `~/Library/Application Support/Claude/claude_desktop_config.json`
(create the file if it doesn't exist):

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "python",
      "args": ["/absolute/path/to/AI-Prompts-for-Product-Management/mcp-server/server.py"]
    }
  }
}
```

Replace the path with the actual absolute path on your machine, then restart Claude Desktop.

**Using `uv` (recommended for isolation):**

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "python",
        "/absolute/path/to/mcp-server/server.py"
      ]
    }
  }
}
```

---

## Connect to Claude Code (CLI)

```bash
claude mcp add pm-prompts python /absolute/path/to/mcp-server/server.py
```

Or add it to your project's `.claude/settings.json`:

```json
{
  "mcpServers": {
    "pm-prompts": {
      "command": "python",
      "args": ["./mcp-server/server.py"]
    }
  }
}
```

Then in a Claude Code session, the tools appear automatically. You can verify with:

```
/mcp
```

---

## Example Conversations

Once connected, you can talk to Claude naturally:

> "I need to do customer discovery for a B2B invoicing tool. Find the right prompt and fill it in for me."

Claude will call `search_prompts("customer discovery")`, then `fill_prompt("customer-discovery/01-interview-guide", {...})` and return the ready-to-use prompt.

> "What PM prompts do you have for evaluating ideas?"

Claude calls `list_prompts("idea-evaluation")` and lists RICE scoring, pre-mortem, assumption mapping, and validation questions.

> "Show me the PRD template."

Claude calls `get_prompt("prds/01-prd-generation")` and returns the full Amazon 6-pager template.

---

## Extending the Server

To add a new tool, add a decorated function to `server.py`:

```python
@mcp.tool()
def export_prompt_as_notion(prompt_id: str) -> str:
    """Export a filled prompt to Notion-compatible markdown."""
    prompt = _find_prompt(prompt_id)
    # ... your logic
    return result
```

To support a new prompt category, just add a new folder and `.md` files under
`prompts/` — the server discovers them automatically at startup.
