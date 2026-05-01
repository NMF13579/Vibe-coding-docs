#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" scripts/validate-task.py tasks/active-task.md
"$PYTHON_BIN" scripts/validate-verification.py reports/verification.md
