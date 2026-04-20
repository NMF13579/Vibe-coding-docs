#!/usr/bin/env bash
# Repository integrity diagnostics (read-only). Exit 0 = OK, 1 = FAIL.
set -u
shopt -s nocasematch

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

issues=0
failures=()

add_fail() {
  issues=$((issues + 1))
  failures+=("$1")
}

echo "HEALTH CHECK — Vibe-coding-docs"
echo "────────────────────────────────"

# --- [A] Core files ---
echo "[A] Core files"

if [[ ! -f llms.txt ]]; then
  echo "  ❌ llms.txt — MISSING"
  add_fail "❌ [A] llms.txt — MISSING"
else
  echo "  ✅ llms.txt — OK"
fi

if [[ -f llms.txt ]] && grep -q 'AUTHORITY: PRIMARY' llms.txt; then
  echo "  ✅ llms.txt AUTHORITY — PRIMARY"
else
  echo "  ❌ llms.txt AUTHORITY — NOT PRIMARY OR MISSING"
  add_fail "❌ [A] llms.txt AUTHORITY — NOT PRIMARY"
fi

if [[ -f llms.txt ]] && grep -q 'SOURCE_OF_TRUTH: yes' llms.txt; then
  echo "  ✅ llms.txt SOURCE_OF_TRUTH — yes"
else
  echo "  ❌ llms.txt SOURCE_OF_TRUTH — NOT yes OR MISSING"
  add_fail "❌ [A] llms.txt SOURCE_OF_TRUTH — NOT yes"
fi

if [[ ! -f LAYER-3/STATE.md ]]; then
  echo "  ❌ STATE.md — MISSING"
  add_fail "❌ [A] STATE.md — MISSING"
elif [[ ! -s LAYER-3/STATE.md ]]; then
  echo "  ❌ STATE.md — EMPTY"
  add_fail "❌ [A] STATE.md — EMPTY"
else
  echo "  ✅ STATE.md — OK"
fi

if [[ ! -f HANDOFF.md ]]; then
  echo "  ❌ HANDOFF.md — MISSING"
  add_fail "❌ [A] HANDOFF.md — MISSING"
elif [[ ! -s HANDOFF.md ]]; then
  echo "  ❌ HANDOFF.md — EMPTY"
  add_fail "❌ [A] HANDOFF.md — EMPTY"
else
  echo "  ✅ HANDOFF.md — OK"
fi

if [[ ! -f LAYER-1/adapter-registry.md ]]; then
  echo "  ❌ adapter-registry.md — MISSING"
  add_fail "❌ [A] adapter-registry.md — MISSING"
else
  echo "  ✅ adapter-registry.md — OK"
fi

if [[ ! -f LAYER-1/templates/adapter-template.md ]]; then
  echo "  ❌ adapter-template.md — MISSING"
  add_fail "❌ [A] adapter-template.md — MISSING"
else
  echo "  ✅ adapter-template.md — OK"
fi

# --- [B] Adapter registry ---
echo "[B] Adapter registry"

REG="LAYER-1/adapter-registry.md"
if [[ -f "$REG" ]]; then
  in_section=0
  current_id=""
  while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ "$line" == "## Registered adapters" ]]; then
      in_section=1
      continue
    fi
    if [[ $in_section -eq 1 && "$line" =~ ^##[[:space:]] ]]; then
      break
    fi
    if [[ $in_section -ne 1 ]]; then
      continue
    fi
    if [[ "$line" =~ ^-[[:space:]]+id:[[:space:]]+\`([^\`]+)\` ]]; then
      current_id="${BASH_REMATCH[1]}"
      continue
    fi
    if [[ "$line" =~ ^[[:space:]]*path:[[:space:]]+\`([^\`]+)\` ]]; then
      rel="${BASH_REMATCH[1]}"
      label="${current_id:-?}"
      if [[ -f "$rel" ]]; then
        echo "  ✅ ${label} → ${rel} — OK"
      else
        echo "  ❌ ${label} → ${rel} — FILE NOT FOUND"
        add_fail "❌ [B] ${label} → ${rel} — FILE NOT FOUND"
      fi
    fi
  done < "$REG"
else
  echo "  ❌ registry file missing (skipped path checks)"
fi

# --- [C] Forbidden adapter patterns ---
echo "[C] Forbidden adapter patterns"

adapter_files=()
while IFS= read -r -d '' f; do
  adapter_files+=("$f")
done < <(find LAYER-1/adapters -type f -name '*.md' -print0 2>/dev/null || true)

for f in CLAUDE.md GEMINI.md AGENTS.md; do
  if [[ -f "$f" ]]; then
    adapter_files+=("$f")
  fi
done

found_forbidden=0
# Ignore lines that are anti-pattern documentation only: whole line is `- "phrase"`.
is_quoted_antipattern_line() {
  local line=$1 phrase=$2
  local line_lc phrase_lc
  line_lc=$(printf '%s' "$line" | tr '[:upper:]' '[:lower:]')
  phrase_lc=$(printf '%s' "$phrase" | tr '[:upper:]' '[:lower:]')
  [[ "$line_lc" =~ ^[[:space:]]*-[[:space:]]*\"${phrase_lc}\"[[:space:]]*$ ]]
}

line_has_real_forbidden() {
  local f=$1 needle=$2 quoted_phrase=$3
  local ln=0 line low
  while IFS= read -r line || [[ -n "$line" ]]; do
    ln=$((ln + 1))
    low=$(printf '%s' "$line" | tr '[:upper:]' '[:lower:]')
    [[ "$low" == *"${needle}"* ]] || continue
    if is_quoted_antipattern_line "$line" "$quoted_phrase"; then
      continue
    fi
    return 0
  done <"$f"
  return 1
}

for f in "${adapter_files[@]}"; do
  [[ -f "$f" ]] || continue
  if line_has_real_forbidden "$f" 'start from this file' 'Start from this file' \
    || line_has_real_forbidden "$f" 'follow this order' 'Follow this order' \
    || line_has_real_forbidden "$f" 'primary coordination files' 'Primary coordination files'; then
    found_forbidden=1
    add_fail "❌ [C] forbidden pattern in ${f}"
  fi
done

if [[ $found_forbidden -eq 0 ]]; then
  echo "  ✅ no forbidden patterns found"
else
  echo "  ❌ forbidden pattern(s) found"
fi

# --- [D] Bootstrap size ---
echo "[D] Bootstrap size"

if [[ -f llms.txt ]]; then
  in_req=0
  found_heading=0
  boot_count=0
  while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ $in_req -eq 0 ]]; then
      if [[ "$line" == "### Required at every start" ]]; then
        in_req=1
        found_heading=1
      fi
      continue
    fi
    trimmed="${line#"${line%%[![:space:]]*}"}"
    trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"
    if [[ -z "$trimmed" ]]; then
      continue
    fi
    if [[ "$trimmed" =~ ^###[[:space:]] ]] || [[ "$trimmed" == "###" ]]; then
      break
    fi
    if [[ "${trimmed:0:2}" == "- " ]]; then
      boot_count=$((boot_count + 1))
      continue
    fi
    break
  done < llms.txt

  if [[ $found_heading -eq 0 ]]; then
    echo "  ❌ bootstrap size — FAIL (### Required at every start not found)"
    add_fail "❌ [D] bootstrap — Required section not found in llms.txt"
  elif [[ "$boot_count" -eq 0 ]]; then
    echo "  ❌ bootstrap size — FAIL (0 required bootstrap items)"
    add_fail "❌ [D] bootstrap size — zero items in Required section"
  elif [[ "$boot_count" -le 7 ]]; then
    echo "  ✅ bootstrap size — OK (${boot_count}/7)"
  else
    echo "  ❌ bootstrap size — FAIL (${boot_count} required items, max 7)"
    add_fail "❌ [D] bootstrap size — too many required items (${boot_count})"
  fi
else
  echo "  ❌ bootstrap size — SKIP (llms.txt missing)"
  add_fail "❌ [D] bootstrap size — llms.txt missing"
fi

echo "────────────────────────────────"

if [[ "$issues" -eq 0 ]]; then
  echo "HEALTH: OK"
  echo "Issues found: 0"
  exit 0
fi

echo "HEALTH: FAIL"
echo "Issues found: ${issues}"
for msg in "${failures[@]}"; do
  echo "  ${msg}"
done
exit 1
