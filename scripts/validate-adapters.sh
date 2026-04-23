#!/usr/bin/env bash
# STATUS: legacy-compatibility
# Requires bash >= 4 (macOS ships bash 3.2 by default)
# On macOS: brew install bash, then use /opt/homebrew/bin/bash
if [[ "${BASH_VERSINFO[0]}" -lt 4 ]]; then
  echo "ERROR: validate-adapters.sh requires bash >= 4"
  echo "Your bash: ${BASH_VERSION}"
  echo "Fix: brew install bash"
  echo "Then: /opt/homebrew/bin/bash scripts/validate-adapters.sh ."
  echo ""
  echo "STATUS: SKIPPED (incompatible environment)"
  exit 2
fi
# validate-adapters.sh — Adapter Validator v1.2.1
# Usage: ./validate-adapters.sh [repo_root] [--json]
# Default repo_root: current directory

set -euo pipefail

REPO="${1:-.}"
JSON_MODE=false
[[ "${2:-}" == "--json" ]] && JSON_MODE=true

# ─── Canonical adapter paths ───────────────────────────────────────────────
declare -A REQUIRED_ADAPTERS=(
  [cursor]=".cursor/rules/governed-repo.mdc"
  [copilot]=".github/copilot-instructions.md"
  [agents]="AGENTS.md"
  [zed]=".rules"
)

declare -A OPTIONAL_ADAPTERS=(
  [claude]="CLAUDE.md"
  [gemini]="GEMINI.md"
  [windsurf_rules]=".windsurf/rules"
  [agents_override]="AGENTS.override.md"
)

ZED_COMPAT=(".cursorrules" ".windsurfrules" ".clinerules" ".github/copilot-instructions.md" "AGENTS.md" "CLAUDE.md" "GEMINI.md")

declare -A LEAK_PATTERNS=(
  [ADAPTER_STATE_LEAK]="STATE\.md"
  [ADAPTER_HANDOFF_LEAK]="HANDOFF\.md"
  [ADAPTER_DECISIONS_LEAK]="DECISIONS\.md"
  [ADAPTER_INTENT_LEAK]="INTENT\.md"
  [ADAPTER_LAYER2_LEAK]="LAYER-2"
  [ALT_BOOTSTRAP_LANGUAGE]="(always start by reading|first read the following|begin by loading|start with these instructions)"
  [COMPETING_ROUTING_LIST]="(## Reading Order|## Load Order|## File Order|read these files in order)"
)

# ─── State ─────────────────────────────────────────────────────────────────
ISSUE_COUNT=0
ERROR_COUNT=0
WARNING_COUNT=0
CHECKED_FILES=()
ISSUES=()

# ─── Helpers ───────────────────────────────────────────────────────────────
add_issue() {
  local id="$1" severity="$2" enforcement="$3" code="$4"
  local file="$5" line="$6" message="$7"
  local why="$8" fix_hint="$9" expected="${10}" auto_fixable="${11}" fix_type="${12}"

  ISSUE_COUNT=$((ISSUE_COUNT+1))
  [[ "$severity" == "error" ]] && ERROR_COUNT=$((ERROR_COUNT+1))
  [[ "$severity" == "warning" ]] && WARNING_COUNT=$((WARNING_COUNT+1))

  local line_json="null"
  [[ "$line" != "null" && "$line" =~ ^[0-9]+$ ]] && line_json="$line"

  local expected_json="null"
  [[ "$expected" != "null" ]] && expected_json="\"$(echo "$expected" | sed 's/"/\\"/g')\""

  ISSUES+=("{
      \"id\": \"issue-$(printf '%03d' $ISSUE_COUNT)\",
      \"severity\": \"$severity\",
      \"enforcement\": \"$enforcement\",
      \"code\": \"$code\",
      \"locations\": [{ \"file\": \"$file\", \"line\": $line_json }],
      \"message\": \"$(echo "$message" | sed 's/"/\\"/g')\",
      \"why_it_matters\": \"$(echo "$why" | sed 's/"/\\"/g')\",
      \"fix_hint\": \"$(echo "$fix_hint" | sed 's/"/\\"/g')\",
      \"expected_pattern\": $expected_json,
      \"auto_fixable\": $auto_fixable,
      \"fix_type\": $([ "$fix_type" = "null" ] && echo "null" || echo "\"$fix_type\"")
    }")
}

check_redirect() {
  local file="$1"
  grep -qE "llms\.txt" "$REPO/$file" 2>/dev/null && return 0
  return 1
}

check_agent_rules() {
  local file="$1"
  grep -qE "LAYER-1/agent-rules\.md" "$REPO/$file" 2>/dev/null && return 0
  return 1
}

check_meta() {
  local file="$1" tag="$2"
  grep -qF "$tag" "$REPO/$file" 2>/dev/null && return 0
  return 1
}

check_leaks() {
  local file="$1"
  local abs="$REPO/$file"
  for code in "${!LEAK_PATTERNS[@]}"; do
    local pattern="${LEAK_PATTERNS[$code]}"
    if grep -qiE "$pattern" "$abs" 2>/dev/null; then
      local line
      line=$(grep -inE "$pattern" "$abs" | head -1 | cut -d: -f1)
      add_issue "" "error" "hard" "$code" \
        "$file" "$line" \
        "Adapter contains forbidden reference: $code" \
        "Adapters must stay minimal and must not include internal document references." \
        "Remove the reference and keep only the minimal redirect." \
        "null" "false" "null"
    fi
  done
}

validate_adapter() {
  local file="$1"
  local abs="$REPO/$file"
  [[ ! -f "$abs" ]] && return
  CHECKED_FILES+=("$file")

  if ! check_redirect "$file"; then
    add_issue "" "error" "hard" "MISSING_LLMS_REDIRECT" \
      "$file" "1" \
      "Adapter does not redirect to llms.txt" \
      "The adapter must point to the canonical bootstrap entry point." \
      "Add: Read \`llms.txt\` and follow it." \
      "Read \`llms.txt\` and follow it. For behavior after load, use \`LAYER-1/agent-rules.md\`." \
      "true" "insert"
  fi

  if ! check_agent_rules "$file"; then
    add_issue "" "error" "hard" "MISSING_AGENT_RULES_REDIRECT" \
      "$file" "null" \
      "Adapter does not reference LAYER-1/agent-rules.md" \
      "After bootstrap, the AI needs to know where behavior rules are defined." \
      "Add: For behavior after load, use \`LAYER-1/agent-rules.md\`." \
      "null" "true" "insert"
  fi

  if ! check_meta "$file" "ROLE: ADAPTER ENTRYPOINT"; then
    add_issue "" "warning" "soft" "MISSING_META_ROLE" \
      "$file" "1" \
      "Missing ROLE: ADAPTER ENTRYPOINT meta tag" \
      "Meta tags enable automated structural checks." \
      "Add <!-- ROLE: ADAPTER ENTRYPOINT --> at the top of the file." \
      "<!-- ROLE: ADAPTER ENTRYPOINT -->" \
      "true" "insert"
  fi

  if ! check_meta "$file" "AUTHORITY: NON-AUTHORITY"; then
    add_issue "" "warning" "soft" "MISSING_META_AUTHORITY" \
      "$file" "null" \
      "Missing AUTHORITY: NON-AUTHORITY meta tag" \
      "This tag signals that the file is not a governance authority." \
      "Add <!-- AUTHORITY: NON-AUTHORITY --> at the top of the file." \
      "<!-- AUTHORITY: NON-AUTHORITY -->" \
      "true" "insert"
  fi

  if ! check_meta "$file" "SOURCE_OF_TRUTH: no"; then
    add_issue "" "warning" "soft" "MISSING_META_SOT" \
      "$file" "null" \
      "Missing SOURCE_OF_TRUTH: no meta tag" \
      "This tag distinguishes adapters from authoritative system files." \
      "Add <!-- SOURCE_OF_TRUTH: no --> at the top of the file." \
      "<!-- SOURCE_OF_TRUTH: no -->" \
      "true" "insert"
  fi

  check_leaks "$file"
}

# ─── Main ──────────────────────────────────────────────────────────────────

for key in "${!REQUIRED_ADAPTERS[@]}"; do
  file="${REQUIRED_ADAPTERS[$key]}"
  if [[ ! -f "$REPO/$file" ]]; then
    add_issue "" "error" "hard" "REQUIRED_ADAPTER_MISSING" \
      "$file" "null" \
      "Required adapter file is absent: $file" \
      "Without it, the target platform will not load the repository instructions." \
      "Create the file at $file and add the minimal redirect to llms.txt." \
      "null" "false" "null"
  else
    validate_adapter "$file"
  fi
done

for key in "${!OPTIONAL_ADAPTERS[@]}"; do
  file="${OPTIONAL_ADAPTERS[$key]}"
  if [[ -f "$REPO/$file" ]]; then
    add_issue "" "warning" "soft" "OPTIONAL_ADAPTER_PRESENT" \
      "$file" "null" \
      "Optional adapter file found: $file" \
      "It may contain outdated or conflicting instructions." \
      "Review manually. Remove if unnecessary or add standard redirect." \
      "null" "false" "null"
    validate_adapter "$file"
  fi
done

ZED_FOUND=()
for f in "${ZED_COMPAT[@]}"; do
  [[ -f "$REPO/$f" ]] && ZED_FOUND+=("$f")
done
if [[ ${#ZED_FOUND[@]} -gt 1 ]]; then
  add_issue "" "warning" "soft" "ZED_COMPAT_CONFLICT" \
    "${ZED_FOUND[0]}" "null" \
    "Multiple Zed-compatible instruction files detected" \
    "Zed may load an unexpected instruction file." \
    "Keep only one primary Zed-compatible file." \
    "null" "false" "null"
fi

# ─── Output ────────────────────────────────────────────────────────────────
STATUS="pass"
[[ $ERROR_COUNT -gt 0 ]] && STATUS="fail"
[[ $WARNING_COUNT -gt 0 && "$STATUS" == "pass" ]] && STATUS="warn"

if $JSON_MODE; then
  checked_json=$(printf '"%s", ' "${CHECKED_FILES[@]:-}" | sed 's/, $//')
  issues_json=$(printf '%s,\n' "${ISSUES[@]:-}" | sed '$ s/,$//')
  cat << JSON
{
  "validator": {
    "name": "adapter-validator",
    "version": "1.2.1",
    "mapping_version": "1.2.1"
  },
  "status": "$STATUS",
  "summary": {
    "errors": $ERROR_COUNT,
    "warnings": $WARNING_COUNT,
    "checked_files": [$checked_json]
  },
  "issues": [
$issues_json
  ]
}
JSON
else
  echo "═══════════════════════════════════════"
  echo "  Adapter Validator v1.2.1"
  echo "  Repo: $REPO"
  echo "═══════════════════════════════════════"
  if [[ ${#ISSUES[@]} -eq 0 ]]; then
    echo "✅ All adapters valid. No issues found."
  else
    echo "Found $ISSUE_COUNT issue(s): $ERROR_COUNT error(s), $WARNING_COUNT warning(s)"
    echo ""
    for issue in "${ISSUES[@]}"; do
      code=$(echo "$issue" | grep -o '"code": "[^"]*"' | head -1 | cut -d'"' -f4)
      file=$(echo "$issue" | grep -o '"file": "[^"]*"' | head -1 | cut -d'"' -f4)
      msg=$(echo "$issue" | grep -o '"message": "[^"]*"' | head -1 | cut -d'"' -f4)
      enf=$(echo "$issue" | grep -o '"enforcement": "[^"]*"' | head -1 | cut -d'"' -f4)
      [[ "$enf" == "hard" ]] && icon="❌" || icon="⚠️ "
      echo "$icon [$code] $file"
      echo "   $msg"
      echo ""
    done
  fi
  echo "Status: $STATUS"
  echo "═══════════════════════════════════════"
  [[ $ERROR_COUNT -gt 0 ]] && exit 1
  exit 0
fi
