#!/usr/bin/env bash
# Fail if retired product identity appears in key files without an explicit history marker.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PATTERN="Vibe-coding-docs"
FILES=("README.md" "ARCHITECTURE.md" "FAQ.md" "llms.txt" "ROUTES-REGISTRY.md")
fail=0

for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || continue
  line_num=0
  while IFS= read -r line; do
    line_num=$((line_num + 1))
    [[ "$line" == *"$PATTERN"* ]] || continue
    if [[ "$line" != *"history"* && "$line" != *"historical"* ]]; then
      echo "identity-check: FAIL $f:$line_num" >&2
      fail=1
    fi
  done <"$f"
done

if [[ "$fail" -ne 0 ]]; then
  exit 1
fi

echo "identity-check: OK"
