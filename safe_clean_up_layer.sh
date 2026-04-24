#!/bin/bash
# safe_clean_up_layer.sh
# Dry-run for LAYER cleanup by default.
# --apply moves ARCHIVE_CANDIDATES into LAYER-archive/ without deleting DELETE_CANDIDATES.

set -e

APPLY_MODE="no"
if [ "${1:-}" = "--apply" ]; then
  APPLY_MODE="yes"
elif [ -n "${1:-}" ]; then
  echo "Unknown argument: $1"
  exit 1
fi

if [ -n "$(git status --short | grep -v 'safe_clean_up_layer.sh')" ]; then
  echo "Working tree is not clean. Aborting."
  exit 1
fi

DELETE_CANDIDATES=(
  "LAYER-1/agent-rules.md"
  "LAYER-1/anti-patterns.md"
  "LAYER-1/audit-quick.md"
  "LAYER-1/audit.md"
  "LAYER-1/context-recovery.md"
  "LAYER-1/cursor-auto-actions.md"
  "LAYER-1/decision-guide.md"
  "LAYER-1/document-governance.md"
  "LAYER-1/error-handling.md"
  "LAYER-1/event-dictionary.md"
  "LAYER-1/instruction-priority.md"
  "LAYER-1/owner.md"
  "LAYER-1/plan-and-scope-gate.md"
  "LAYER-1/session-lifecycle.md"
  "LAYER-1/system-constraints.md"
  "LAYER-1/scope-guard.md"
  "LAYER-1/security.md"
  "LAYER-1/testing-guide.md"
  "LAYER-1/workflow.md"
  "LAYER-2/qa/post-launch-review.md"
  "LAYER-2/qa/release-blockers.md"
  "LAYER-2/qa/test-scenarios.md"
  "LAYER-2/qa/verification-criteria.md"
)

ARCHIVE_CANDIDATES=(
  "LAYER-1/interview-system.md"
  "LAYER-1/self-verification.md"
  "LAYER-1/state-transitions.md"
  "LAYER-1/task-protocol.md"
  "LAYER-2/specs/access-rules.md"
  "LAYER-2/specs/component-states.md"
  "LAYER-2/specs/validation-rules.md"
)

echo "=== DELETE_CANDIDATE files ==="
for f in "${DELETE_CANDIDATES[@]}"; do
  if [ -f "$f" ]; then
    echo "[DELETE] $f"
  fi
done

echo
echo "=== ARCHIVE_CANDIDATE files ==="
for f in "${ARCHIVE_CANDIDATES[@]}"; do
  if [ -f "$f" ]; then
    echo "[ARCHIVE] $f"
  fi
done

if [ "$APPLY_MODE" = "yes" ]; then
  mkdir -p "LAYER-archive"
  for f in "${ARCHIVE_CANDIDATES[@]}"; do
    if [ -f "$f" ]; then
      mv "$f" "LAYER-archive/$(basename "$f")"
    fi
  done

  echo
  echo "=== git status --short ==="
  git status --short
fi
