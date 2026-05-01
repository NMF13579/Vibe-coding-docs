#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$TMP_DIR/project"
cd "$TMP_DIR/project"
git init >/dev/null

bash "$REPO_ROOT/install.sh" --minimal

for path in \
  requirements.txt \
  schemas/task.schema.json \
  schemas/verification.schema.json \
  tasks/active-task.md \
  reports/verification.md \
  scripts/validate-task.py \
  scripts/validate-verification.py \
  scripts/run-all.sh
do
  if [ ! -f "$path" ]; then
    echo "FAIL: missing file: $path"
    exit 1
  fi
done

python3 -m venv .venv
VENV_PYTHON="$TMP_DIR/project/.venv/bin/python3"

"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install --quiet -r requirements.txt 2>/dev/null \
  || "$VENV_PYTHON" -m pip install -r requirements.txt

PYTHON_BIN="$VENV_PYTHON" bash scripts/run-all.sh

echo "PASS: install smoke test passed"
