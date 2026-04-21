#!/usr/bin/env bash
# Fail if llms.txt references missing repo paths in bootstrap graph sections.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LLMS="llms.txt"
[[ -f "$LLMS" ]] || {
  echo "check-llms-graph: missing $LLMS" >&2
  exit 1
}

declare -A SEEN=()
fail=0

record_missing() {
  local rel="$1"
  printf '%s\n' "check-llms-graph: FAIL missing file: $rel" >&2
  fail=1
}

check_one() {
  local rel="$1"
  rel="${rel#./}"
  [[ -z "$rel" ]] && return 0
  [[ -n "${SEEN[$rel]:-}" ]] && return 0
  SEEN[$rel]=1

  if [[ "$rel" == *TASK-XXX* ]]; then
    return 0
  fi

  if [[ ! -e "$rel" ]]; then
    record_missing "$rel"
  fi
}

# Backtick-enclosed repo paths only (ignore bare STATE.md etc. in prose)
extract_backticks() {
  grep -h -oE '`(LAYER-[123]/[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*\.(md|mdc)|HANDOFF\.md|ARCHITECTURE\.md|tasks/[A-Za-z0-9_.-]+\.md)`' "$@" 2>/dev/null | tr -d '`' || true
}

# Layered or root single-segment .md (HANDOFF.md, ARCHITECTURE.md) from bullet lines
extract_bullet_paths() {
  for f in "$@"; do
    while IFS= read -r line; do
      [[ "$line" =~ ^- ]] || continue
      while IFS= read -r m; do
        [[ -n "$m" ]] && printf '%s\n' "$m"
      done < <(printf '%s\n' "$line" | grep -oE '(LAYER-[123]/[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*\.(md|mdc))|(HANDOFF\.md|ARCHITECTURE\.md)' || true)
    done <"$f"
  done
}

# Situation routes: third column — split on → and spaces, keep path-like tokens
extract_table_paths() {
  for f in "$@"; do
    while IFS= read -r line; do
      [[ "$line" =~ ^\| ]] || continue
      [[ "$line" =~ Ситуация ]] && continue
      [[ "$line" =~ ^\|[[:space:]]*--- ]] && continue
      cell=$(printf '%s\n' "$line" | awk -F'|' '{print $3}' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
      [[ -z "$cell" ]] && continue
      printf '%s\n' "$cell" | tr '→' ' ' | tr ' ' '\n' | grep -E '^LAYER-[123]/[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*\.(md|mdc)$|^HANDOFF\.md$' || true
    done <"$f"
  done
}

# Canonical sources bullets: path tokens
extract_canonical_paths() {
  for f in "$@"; do
    while IFS= read -r line; do
      [[ "$line" =~ ^- ]] || continue
      printf '%s\n' "$line" | grep -oE 'LAYER-[123]/[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*\.(md|mdc)|HANDOFF\.md|ARCHITECTURE\.md' || true
    done <"$f"
  done
}

TMP_REQ=$(mktemp)
TMP_RO=$(mktemp)
TMP_SIT=$(mktemp)
TMP_CAN=$(mktemp)
trap 'rm -f "$TMP_REQ" "$TMP_RO" "$TMP_SIT" "$TMP_CAN"' EXIT

awk '/^### Required at every start/,/^### Read only if needed/{if(/^### Read only if needed/)exit; print}' "$LLMS" >"$TMP_REQ"
awk '/^### Read only if needed/,/^---$/{if(/^---$/){if(seen++)exit}; print}' "$LLMS" >"$TMP_RO"
awk '/^## Situation routes/,/^---$/{if(/^---$/){if(seen++)exit}; print}' "$LLMS" >"$TMP_SIT"
awk '/^## Canonical sources/,/^---$/{if(/^---$/){if(seen++)exit}; print}' "$LLMS" >"$TMP_CAN"

while IFS= read -r p; do check_one "$p"; done < <(extract_backticks "$TMP_REQ" "$TMP_RO")
while IFS= read -r p; do check_one "$p"; done < <(extract_bullet_paths "$TMP_REQ" "$TMP_RO")
while IFS= read -r p; do check_one "$p"; done < <(extract_backticks "$TMP_SIT")
while IFS= read -r p; do check_one "$p"; done < <(extract_table_paths "$TMP_SIT")
while IFS= read -r p; do check_one "$p"; done < <(extract_canonical_paths "$TMP_CAN")

if [[ "$fail" -ne 0 ]]; then
  echo "check-llms-graph: fix missing paths or adjust llms.txt sections." >&2
  exit 1
fi

echo "check-llms-graph: OK"
