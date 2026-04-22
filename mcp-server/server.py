#!/usr/bin/env python3
"""
PM Prompts MCP Server

Exposes the AI Prompts for Product Management library as MCP tools so that
any MCP-compatible client (Claude Desktop, Claude Code, Cursor, etc.) can
browse, retrieve, and fill prompt templates without leaving the assistant.
"""

import json
import re
from collections import Counter
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PM Prompts")

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

CATEGORY_DESCRIPTIONS = {
    "architecture-diagrams": "Sequence diagrams, UML class diagrams, Entity Relationship Diagrams, and flowcharts from code repositories",
    "communications": "Executive updates, weekly leadership messages, stakeholder communications",
    "competitive-analysis": "Positioning, feature comparison, target customers, capability gap analysis",
    "customer-discovery": "Interview guides, transcript analysis, JTBD, survey analysis, sentiment analysis, pattern finding",
    "idea-evaluation": "RICE scoring, pre-mortem, assumption mapping, validation questions, Kano analysis, MoSCoW prioritization",
    "ideation": "Problem-to-solution generation, SCAMPER, VRIO, MECE analysis",
    "market-research": "Structured market analysis, cross-referencing sources",
    "metrics": "Feature success metrics and measurement frameworks",
    "prds": "Product Requirements Documents (Amazon 6-pager style), use case documentation, features and user stories with Given/When/Then acceptance criteria and sprint planning",
    "prototyping": "UI prototype specs",
    "release-notes-generator": "Generating release notes from commit history",
    "stakeholder-management": "RACI matrix, DACI decision framework, stakeholder mapping, influence and support analysis",
    "strategy": "Product strategy canvas, OKR generation, working backwards, Amazon PR/FAQ, dependency identification, private preview planning, value proposition design, Big Rock decomposition, launch gates",
    "synthetic-users": "Creating and interviewing AI-generated personas",
    "trend-analysis": "Feedback trend monitoring, industry trend identification",
    "user-journey-maps": "User journey mapping",
}


def parse_prompt_file(file_path: Path) -> dict:
    """Parse a prompt markdown file and extract structured metadata."""
    content = file_path.read_text()

    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else file_path.stem

    phase_match = re.search(r"\*\*Phase:\*\* (.+)$", content, re.MULTILINE)
    phase = phase_match.group(1).strip() if phase_match else "Unknown"

    purpose_match = re.search(r"\*\*Purpose:\*\* (.+)$", content, re.MULTILINE)
    purpose = purpose_match.group(1).strip() if purpose_match else ""

    # Pull every fenced code block — most prompts have one template, some have multiple
    templates = re.findall(r"```\n(.*?)```", content, re.DOTALL)

    # Parse the Placeholders table if present
    placeholders: dict[str, str] = {}
    placeholder_section = re.search(
        r"## Placeholders\n(.*?)(?=^##|\Z)", content, re.DOTALL | re.MULTILINE
    )
    if placeholder_section:
        rows = re.findall(
            r"\| `(\[[^\]]+\])` \| (.+?) \|", placeholder_section.group(1)
        )
        for var, desc in rows:
            placeholders[var] = desc.strip()

    return {
        "id": str(file_path.relative_to(PROMPTS_DIR)).replace(".md", ""),
        "title": title,
        "phase": phase,
        "purpose": purpose,
        "category": file_path.parent.name,
        "templates": templates,
        "placeholders": placeholders,
        "raw_content": content,
    }


def load_all_prompts() -> list[dict]:
    prompts = []
    for md_file in sorted(PROMPTS_DIR.rglob("*.md")):
        try:
            prompts.append(parse_prompt_file(md_file))
        except Exception as exc:
            print(f"Warning: could not parse {md_file}: {exc}")
    return prompts


ALL_PROMPTS = load_all_prompts()
PROMPTS_BY_ID = {p["id"]: p for p in ALL_PROMPTS}


def _find_prompt(prompt_id: str) -> dict | None:
    """Return a prompt by exact ID or fall back to a partial title/id match."""
    if prompt_id in PROMPTS_BY_ID:
        return PROMPTS_BY_ID[prompt_id]
    needle = prompt_id.lower()
    matches = [
        p
        for p in ALL_PROMPTS
        if needle in p["id"].lower() or needle in p["title"].lower()
    ]
    return matches[0] if matches else None


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_prompts(category: str = "") -> str:
    """
    List all available PM prompt templates, optionally filtered by category.

    Args:
        category: Optional category slug, e.g. 'customer-discovery', 'ideation',
                  'idea-evaluation', 'market-research', 'competitive-analysis',
                  'trend-analysis', 'synthetic-users', 'prds', 'metrics',
                  'prototyping', 'release-notes-generator', 'user-journey-maps',
                  'architecture-diagrams', 'communications', 'stakeholder-management',
                  'strategy'. Leave empty to list all 55+ prompts across 16 categories.

    Returns:
        JSON array — each item has: id, title, phase, purpose, category.
        Use the id value with get_prompt() or fill_prompt().
    """
    prompts = ALL_PROMPTS
    if category:
        slug = category.lower().replace(" ", "-")
        prompts = [p for p in prompts if p["category"].lower() == slug]

    return json.dumps(
        [
            {
                "id": p["id"],
                "title": p["title"],
                "phase": p["phase"],
                "purpose": p["purpose"],
                "category": p["category"],
            }
            for p in prompts
        ],
        indent=2,
    )


@mcp.tool()
def get_categories() -> str:
    """
    Return all prompt categories with their prompt counts and descriptions.

    Returns:
        JSON object mapping category slug → { count, description }.
    """
    counts = Counter(p["category"] for p in ALL_PROMPTS)
    result = {
        cat: {
            "count": counts[cat],
            "description": CATEGORY_DESCRIPTIONS.get(cat, ""),
        }
        for cat in sorted(counts)
    }
    return json.dumps(result, indent=2)


@mcp.tool()
def search_prompts(query: str) -> str:
    """
    Search PM prompts by keyword across titles, purposes, phases, and content.

    Args:
        query: Search term, e.g. 'JTBD', 'competitive', 'metrics', 'interview',
               'RICE', 'pre-mortem', 'synthetic user'.

    Returns:
        JSON array of matching prompts sorted by relevance score.
    """
    needle = query.lower()
    scored = []
    for p in ALL_PROMPTS:
        score = 0
        if needle in p["title"].lower():
            score += 4
        if needle in p["purpose"].lower():
            score += 3
        if needle in p["phase"].lower():
            score += 2
        if needle in p["category"].lower():
            score += 2
        if needle in p["raw_content"].lower():
            score += 1
        if score:
            scored.append((score, p))

    scored.sort(key=lambda x: x[0], reverse=True)

    if not scored:
        return json.dumps({"message": f"No prompts found matching '{query}'", "results": []})

    return json.dumps(
        [
            {
                "id": p["id"],
                "title": p["title"],
                "phase": p["phase"],
                "purpose": p["purpose"],
                "category": p["category"],
            }
            for _, p in scored
        ],
        indent=2,
    )


@mcp.tool()
def get_prompt(prompt_id: str) -> str:
    """
    Return the full markdown content of a specific PM prompt template.

    Args:
        prompt_id: The prompt ID returned by list_prompts() or search_prompts(),
                   e.g. 'customer-discovery/01-interview-guide'.
                   Partial matches on ID or title also work.

    Returns:
        Full markdown file: title, phase, purpose, template text(s),
        placeholders table, and usage tips.
    """
    prompt = _find_prompt(prompt_id)
    if not prompt:
        available = "\n".join(p["id"] for p in ALL_PROMPTS)
        return f"Prompt '{prompt_id}' not found.\n\nAvailable IDs:\n{available}"
    return prompt["raw_content"]


@mcp.tool()
def fill_prompt(prompt_id: str, variables: dict) -> str:
    """
    Fill in a PM prompt template with your specific context and return a
    ready-to-use prompt string.

    Args:
        prompt_id: The prompt ID, e.g. 'customer-discovery/01-interview-guide'.
                   Partial matches on ID or title also work.
        variables: Key-value pairs mapping placeholder names to your values.
                   Bracket notation is optional — both '[PROBLEM]' and 'PROBLEM'
                   are accepted.
                   Example:
                     {
                       "[PROBLEM]": "onboarding friction for SMB users",
                       "[USER TYPE]": "small business owners"
                     }

    Returns:
        The filled prompt text plus a note about any placeholders still missing.
    """
    prompt = _find_prompt(prompt_id)
    if not prompt:
        return f"Prompt '{prompt_id}' not found. Use list_prompts() to see available IDs."

    if not prompt["templates"]:
        return f"No template block found in '{prompt_id}'. Check get_prompt() for the raw content."

    # Use the first template; most prompts have one, a few have labelled variants
    filled = prompt["templates"][0]

    for key, value in variables.items():
        placeholder = key if key.startswith("[") else f"[{key}]"
        filled = filled.replace(placeholder, str(value))

    remaining = sorted(set(re.findall(r"\[[A-Z_\s/]+\]", filled)))

    output = f"# {prompt['title']}\n\n## Ready-to-Use Prompt\n\n```\n{filled.strip()}\n```"

    if remaining:
        output += (
            f"\n\n> **Still needs values for:** {', '.join(f'`{r}`' for r in remaining)}"
        )

    if prompt["placeholders"]:
        rows = "\n".join(
            f"| `{var}` | {desc} |" for var, desc in prompt["placeholders"].items()
        )
        output += f"\n\n## Placeholder Reference\n\n| Variable | Description |\n|---|---|\n{rows}"

    return output


if __name__ == "__main__":
    mcp.run()
