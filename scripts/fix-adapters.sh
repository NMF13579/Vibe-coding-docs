#!/usr/bin/env bash
# Add minimal canonical routing hints to adapter files.
set -euo pipefail

REPO="${1:-.}"
FILES=("AGENTS.md" "CLAUDE.md" "GEMINI.md")
TEXT='Read `llms.txt` first. Use `ROUTES-REGISTRY.md` for canonical module ownership.'

for file in "${FILES[@]}"; do
  path="$REPO/$file"
  [[ -f "$path" ]] || continue
  if ! grep -q "llms.txt" "$path"; then
    printf '\n%s\n' "$TEXT" >> "$path"
    echo "updated $file"
  fi
done
