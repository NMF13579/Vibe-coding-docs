#!/usr/bin/env bash
# AgentOS Canonical Health Check
# STATUS: canonical
# Validates modular architecture — the current primary architecture.
# HEALTH: OK is only possible after checking the modular control plane.

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ERRORS=0
CANONICAL_MODULES=(
  "core-rules/MAIN.md"
  "state/MAIN.md"
  "workflow/MAIN.md"
  "quality/MAIN.md"
  "security/MAIN.md"
)

echo "=== AgentOS Health Check (Canonical) ==="
echo ""

check_file() {
  local path="$1"
  local label="$2"
  if [[ -f "$REPO_ROOT/$path" ]]; then
    echo "  OK  $label"
  else
    echo "  FAIL  MISSING: $label ($path)"
    ERRORS=$((ERRORS + 1))
  fi
}

echo "--- Control plane entrypoints ---"
check_file "START.md"            "START.md"
check_file "llms.txt"            "llms.txt"
check_file "ROUTES-REGISTRY.md"  "ROUTES-REGISTRY.md"
check_file "architecture/CANON.md" "architecture/CANON.md"

echo ""
echo "--- Canonical runtime modules ---"
for module in "${CANONICAL_MODULES[@]}"; do
  if [[ -f "$REPO_ROOT/$module" ]]; then
    echo "  OK  $module exists"
  else
    echo "  FAIL  Missing runtime module: $module"
    ERRORS=$((ERRORS + 1))
  fi

  if grep -Fq "$module" "$REPO_ROOT/llms.txt"; then
    echo "  OK  $module listed in llms.txt"
  else
    echo "  FAIL  $module missing from llms.txt"
    ERRORS=$((ERRORS + 1))
  fi

  if grep -Fq "$module" "$REPO_ROOT/ROUTES-REGISTRY.md"; then
    echo "  OK  $module listed in ROUTES-REGISTRY.md"
  else
    echo "  FAIL  $module missing from ROUTES-REGISTRY.md"
    ERRORS=$((ERRORS + 1))
  fi
done

echo ""
echo "--- Canonical validators ---"
if bash "$REPO_ROOT/scripts/validate-architecture.sh" > /dev/null 2>&1; then
  echo "  OK  validate-architecture.sh"
else
  echo "  FAIL  validate-architecture.sh"
  ERRORS=$((ERRORS + 1))
fi

if python3 "$REPO_ROOT/scripts/validate-route.py" > /dev/null 2>&1; then
  echo "  OK  validate-route.py"
else
  echo "  FAIL  validate-route.py"
  ERRORS=$((ERRORS + 1))
fi

if python3 "$REPO_ROOT/scripts/validate-docs.py" > /dev/null 2>&1; then
  echo "  OK  validate-docs.py"
else
  echo "  FAIL  validate-docs.py"
  ERRORS=$((ERRORS + 1))
fi

echo ""
if [[ $ERRORS -eq 0 ]]; then
  echo "HEALTH: OK — modular architecture validated"
  exit 0
else
  echo "HEALTH: FAIL — $ERRORS issue(s) found"
  exit 1
fi
