#!/usr/bin/env bash
# Check that canonical module paths named in llms.txt exist.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LLMS="llms.txt"
[[ -f "$LLMS" ]] || {
  echo "check-llms-graph: missing $LLMS" >&2
  exit 1
}

fail=0
while IFS= read -r rel; do
  [[ -z "$rel" ]] && continue
  if [[ ! -f "$rel" ]]; then
    echo "check-llms-graph: missing file: $rel" >&2
    fail=1
  fi
done < <(grep -oE '`[A-Za-z0-9_-]+/MAIN\.md`' "$LLMS" | tr -d '`' | sort -u)

if [[ "$fail" -ne 0 ]]; then
  exit 1
fi

echo "check-llms-graph: OK"
