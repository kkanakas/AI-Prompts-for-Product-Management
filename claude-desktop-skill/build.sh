#!/usr/bin/env bash
# Build the Claude Desktop skill ZIP for upload.
# Run from the repo root OR from inside claude-desktop-skill/
# Output: ai-pm-prompts-claude-desktop.zip (placed in repo root)

set -euo pipefail

# Resolve repo root regardless of where the script is run from
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT="$REPO_ROOT/ai-pm-prompts-claude-desktop.zip"

echo "Building Claude Desktop skill ZIP..."
echo "  Repo root : $REPO_ROOT"
echo "  Output    : $OUTPUT"

# Remove previous build
rm -f "$OUTPUT"

# Build the ZIP from repo root so paths inside are relative:
#   SKILL.md             <- Claude Desktop reads this at root
#   prompts/...          <- prompt files readable from within the skill
cd "$REPO_ROOT"

zip -r "$OUTPUT" \
  claude-desktop-skill/SKILL.md \
  prompts/ \
  --exclude "*.DS_Store" \
  --exclude "*/.git/*" \
  --exclude "*/__pycache__/*" \
  --exclude "*.pyc"

# Claude Desktop requires SKILL.md at the ZIP root, not in a subdirectory.
# Repack so SKILL.md sits at root of the archive.
TMPDIR=$(mktemp -d)
unzip -q "$OUTPUT" -d "$TMPDIR"
cp "$TMPDIR/claude-desktop-skill/SKILL.md" "$TMPDIR/SKILL.md"
rm -rf "$TMPDIR/claude-desktop-skill"

rm -f "$OUTPUT"
cd "$TMPDIR"
zip -r "$OUTPUT" . --exclude "*.DS_Store"
cd "$REPO_ROOT"
rm -rf "$TMPDIR"

SIZE=$(du -sh "$OUTPUT" | cut -f1)
echo ""
echo "Done. Built $OUTPUT ($SIZE)"
echo ""
echo "Next steps:"
echo "  1. Open Claude Desktop"
echo "  2. Go to Customize → Skills"
echo "  3. Click + → Create skill → Upload a skill"
echo "  4. Upload: $OUTPUT"
echo "  5. Toggle the skill on"
echo ""
echo "Note: Code execution must be enabled in Claude Desktop settings for skills to work."
echo "      For Team/Enterprise plans, your org admin must enable Skills first."
