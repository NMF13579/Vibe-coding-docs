#!/usr/bin/env bash
# AgentOS Canonical Orchestration Entrypoint
# STATUS: canonical
# This is the single command that represents: "is the system healthy?"
# Runs canonical checks first. Legacy checks are informational and non-blocking.

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PASS=0
FAIL=0

echo "=== AgentOS run-all.sh ==="
echo ""

run() {
  local label="$1"; shift
  if "$@" > /dev/null 2>&1; then
    echo "  OK  $label"
    PASS=$((PASS + 1))
  else
    echo "  FAIL  $label"
    FAIL=$((FAIL + 1))
  fi
}

echo "--- Canonical checks (blocking) ---"
run "health-check"          bash "$REPO_ROOT/scripts/health-check.sh"
run "validate-architecture" bash "$REPO_ROOT/scripts/validate-architecture.sh"
run "validate-route"        python3 "$REPO_ROOT/scripts/validate-route.py"
run "validate-docs"         python3 "$REPO_ROOT/scripts/validate-docs.py"

echo ""
echo "--- Legacy compatibility (informational, non-blocking) ---"
if [[ "${BASH_VERSINFO[0]}" -ge 4 ]]; then
  bash "$REPO_ROOT/scripts/validate-adapters.sh" . > /dev/null 2>&1 \
    && echo "  OK  validate-adapters (legacy)" \
    || echo "  WARN  validate-adapters (legacy) — issues found, non-blocking"
else
  echo "  SKIP  validate-adapters (legacy) — requires bash>=4"
fi

bash "$REPO_ROOT/scripts/legacy-health-check.sh" > /dev/null 2>&1 \
  && echo "  OK  legacy-health-check (informational)" \
  || echo "  WARN  legacy-health-check (informational) — non-blocking"

echo ""
echo "=== Result: $PASS passed, $FAIL failed ==="
if [[ $FAIL -eq 0 ]]; then
  echo "STATUS: PASS"
  exit 0
else
  echo "STATUS: FAIL"
  exit 1
fi
