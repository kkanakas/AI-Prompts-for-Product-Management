#!/usr/bin/env bash
# list-prompts.sh — List all available PM prompts with their titles and phases.
# Usage: ./scripts/list-prompts.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/../prompts"

echo "====================================="
echo " AI PM Prompt Library"
echo "====================================="
echo ""

for phase_dir in "$PROMPTS_DIR"/*/; do
  phase=$(basename "$phase_dir")
  echo "── $phase ──"
  for file in "$phase_dir"*.md; do
    [ -f "$file" ] || continue
    title=$(head -1 "$file" | sed 's/^# //')
    filename=$(basename "$file")
    printf "  %-42s  %s\n" "$filename" "$title"
  done
  echo ""
done
