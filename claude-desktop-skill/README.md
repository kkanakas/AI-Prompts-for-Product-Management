# Claude Desktop Skill — AI Prompts for Product Managers

This folder contains everything needed to install the PM Prompts library as a skill in **Claude Desktop**.

---

## What this skill does

Once installed, Claude Desktop automatically recognises when you are working on a product management task and activates the skill. You can ask naturally:

```
"Help me run a Kano analysis on these eight features"
"Create a DACI for our mobile strategy decision"
"Build team OKRs from our company OKRs"
"Write a working backwards plan for our new checkout feature"
"Turn my customer meeting notes into a leadership Slack update"
"Define the launch gates for our Q3 GA release"
```

Claude reads the relevant prompt template from the skill bundle, asks you for the context it needs, fills in the placeholders, and returns a ready-to-use prompt.

---

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | Skill definition — tells Claude Desktop what this skill does and how to use it |
| `build.sh` | Script that assembles the uploadable ZIP from the repo's prompt files |
| `README.md` | This file |

The `prompts/` directory lives one level up (at the repo root) and is bundled into the ZIP at build time. The skill reads prompt files from that bundle at runtime.

---

## Installation

### Step 1 — Build the ZIP

Run the build script from anywhere inside the repo:

```bash
bash claude-desktop-skill/build.sh
```

This produces `ai-pm-prompts-claude-desktop.zip` in the repo root. The ZIP contains `SKILL.md` at the root and the full `prompts/` library.

### Step 2 — Upload to Claude Desktop

1. Open **Claude Desktop**
2. Go to **Customize → Skills**
3. Click **+** → **Create skill** → **Upload a skill**
4. Select `ai-pm-prompts-claude-desktop.zip`
5. Toggle the skill **on**

### Step 3 — Verify

Start a new conversation and type:

```
Help me write a weekly leadership update
```

Claude should recognise the request, confirm it is using the PM Prompts skill, and ask for your context.

---

## Requirements

- **Claude Desktop** (Mac or Windows) with a Pro, Team, or Enterprise plan
- **Code execution enabled** — go to Claude Desktop Settings and enable "Code execution and file creation"
- **Team / Enterprise only**: your organisation owner must also enable "Skills" before custom skills can be uploaded

---

## Updating the skill

When new prompts are added to the repository:

1. Pull the latest changes: `git pull`
2. Rebuild the ZIP: `bash claude-desktop-skill/build.sh`
3. In Claude Desktop: go to **Customize → Skills**, find the skill, and re-upload the new ZIP

---

## Difference from Claude Code skill

| | Claude Code | Claude Desktop |
|---|---|---|
| **Install method** | Auto-discovered from `.claude/skills/` | ZIP upload via UI |
| **Activation** | `Skill` tool called by Claude Code | Automatic when trigger phrases detected |
| **Prompt files** | Read from repo directory | Bundled inside the ZIP |
| **Best for** | CLI / IDE workflows, coding sessions | Conversations, writing, planning sessions |

Both skills use the same underlying prompt library — they are two delivery mechanisms for the same content.
