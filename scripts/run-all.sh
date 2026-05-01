#!/usr/bin/env bash
# =============================================================
# LEGACY SCRIPT - do not use for M12+ flow
# This script validates tasks/active-task.md as a TASK contract
# and is incompatible with active-pointer format.
#
# Current validator:
#   python3 scripts/agentos-validate.py all
# =============================================================
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" scripts/validate-task.py tasks/active-task.md
"$PYTHON_BIN" scripts/validate-verification.py reports/verification.md
