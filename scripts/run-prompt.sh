#!/usr/bin/env bash
# run-prompt.sh — Extract the prompt template from a file, substitute variables,
#                 and copy to clipboard (or print to stdout).
#
# Usage:
#   ./scripts/run-prompt.sh prompts/customer-discovery/01-interview-guide.md \
#       --problem "onboarding friction" --user-type "SMB owners"
#
# Flags are matched to [PLACEHOLDER] names: --problem → [PROBLEM], --user-type → [USER TYPE]
# Any unmatched placeholders are left as-is for you to fill manually.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <prompt-file> [--variable value ...]"
  echo ""
  echo "Example:"
  echo "  $0 prompts/customer-discovery/01-interview-guide.md \\"
  echo "      --problem 'onboarding friction' --user-type 'SMB owners'"
  exit 1
fi

PROMPT_FILE="$1"
shift

if [ ! -f "$PROMPT_FILE" ]; then
  echo "Error: File not found: $PROMPT_FILE"
  exit 1
fi

# Extract text between ``` fences (the actual prompt template)
TEMPLATE=$(awk '/^```$/{if(in_block){in_block=0;next}else{in_block=1;next}} /^```/{if(in_block){in_block=0;next}else{in_block=1;next}} in_block{print}' "$PROMPT_FILE" | head -80)

if [ -z "$TEMPLATE" ]; then
  echo "Warning: No fenced code block found. Printing full file content."
  TEMPLATE=$(cat "$PROMPT_FILE")
fi

# Apply variable substitutions from command-line flags
OUTPUT="$TEMPLATE"
while [ $# -ge 2 ]; do
  KEY="$1"
  VALUE="$2"
  shift 2

  # Convert --flag-name to [FLAG NAME] placeholder
  PLACEHOLDER=$(echo "$KEY" | sed 's/^--//' | tr '-' ' ' | tr '[:lower:]' '[:upper:]')
  OUTPUT=$(echo "$OUTPUT" | sed "s|\[$PLACEHOLDER\]|$VALUE|g")
done

echo "═══════════════════════════════════════"
echo " Prompt ready — paste into your AI tool"
echo "═══════════════════════════════════════"
echo ""
echo "$OUTPUT"
echo ""

# Copy to clipboard if available
if command -v pbcopy &>/dev/null; then
  echo "$OUTPUT" | pbcopy
  echo "(Copied to clipboard)"
elif command -v xclip &>/dev/null; then
  echo "$OUTPUT" | xclip -selection clipboard
  echo "(Copied to clipboard)"
else
  echo "(Tip: pipe to pbcopy or xclip to copy to clipboard)"
fi
