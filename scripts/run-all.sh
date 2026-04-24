#!/usr/bin/env bash
# AgentOS Canonical Orchestration Entrypoint
# STATUS: canonical

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

echo "--- Canonical checks ---"
run "health-check"          bash "$REPO_ROOT/scripts/health-check.sh"
run "validate-architecture" bash "$REPO_ROOT/scripts/validate-architecture.sh"
run "validate-route"        python3 "$REPO_ROOT/scripts/validate-route.py"
run "validate-docs"         python3 "$REPO_ROOT/scripts/validate-docs.py"
run "check-links"           python3 "$REPO_ROOT/scripts/check-links.py"

echo ""
echo "=== Result: $PASS passed, $FAIL failed ==="
if [[ $FAIL -eq 0 ]]; then
  echo "STATUS: PASS"
  exit 0
else
  echo "STATUS: FAIL"
  exit 1
fi
