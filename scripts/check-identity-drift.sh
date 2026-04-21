#!/usr/bin/env bash
# Fail if legacy product/repo identity appears in key files without an explicit historical marker on the same line.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Legacy identity: old product name (with optional extra hyphens in badges) or old GitHub paths.
readonly DRIFT_PATTERN='[Vv]ibe-+[Cc]oding-+[Dd]ocs|github\.com/NMF13579/Vibe-coding-docs|raw\.githubusercontent\.com/NMF13579/Vibe-coding-docs'

# Same line must contain one of these if DRIFT_PATTERN matches (explicit historical / disclaimer context).
readonly HIST_PATTERN='[Hh]istorical|[Ии]сторич|[Рр]анее репозитор|not current product name|[Пп]режнее имя|[Ll]egacy name|[Oo]ld name|[Ff]ormerly'

fail=0

check_file() {
  local f="$1"
  local line_num=0

  [[ -f "$f" ]] || {
    echo "identity-check: skip missing file: $f" >&2
    return 0
  }

  while IFS= read -r line || [[ -n "$line" ]]; do
    line_num=$((line_num + 1))
    if printf '%s\n' "$line" | grep -qE "$DRIFT_PATTERN"; then
      if ! printf '%s\n' "$line" | grep -qE "$HIST_PATTERN"; then
        printf '%s\n' "identity-check: FAIL $f:$line_num (legacy identity without historical marker on same line)" >&2
        printf '%s\n' "$line" >&2
        fail=1
      fi
    fi
  done <"$f"
}

check_file README.md
check_file ARCHITECTURE.md
check_file llms.txt
check_file HANDOFF.md
check_file install.sh

if [[ "$fail" -ne 0 ]]; then
  echo "identity-check: add an explicit historical disclaimer on the same line, or remove legacy identity from key files." >&2
  exit 1
fi

echo "identity-check: OK"
