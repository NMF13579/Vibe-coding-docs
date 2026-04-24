#!/usr/bin/env bash
# Validate that adapter files point back to canonical routing.
set -euo pipefail

REPO="${1:-.}"
ERRORS=0
FILES=("AGENTS.md" "CLAUDE.md" "GEMINI.md")

for file in "${FILES[@]}"; do
  path="$REPO/$file"
  [[ -f "$path" ]] || continue
  if ! grep -q "llms.txt" "$path"; then
    echo "adapter-check: $file must reference llms.txt" >&2
    ERRORS=$((ERRORS + 1))
  fi
  if ! grep -q "ROUTES-REGISTRY.md" "$path"; then
    echo "adapter-check: $file must reference ROUTES-REGISTRY.md" >&2
    ERRORS=$((ERRORS + 1))
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  exit 1
fi

echo "adapter-check: OK"
