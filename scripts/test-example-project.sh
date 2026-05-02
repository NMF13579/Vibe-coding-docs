#!/usr/bin/env bash
set -euo pipefail

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXAMPLE_DIR="$REPO_ROOT/examples/simple-project"

if [ ! -d "$EXAMPLE_DIR" ]; then
  echo "FAIL: example project not found"
  exit 1
fi

cp -R "$EXAMPLE_DIR" "$TMP_DIR/simple-project"

cd "$TMP_DIR/simple-project"
git init >/dev/null

bash run-example.sh

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

python3 -m venv --system-site-packages .venv
. .venv/bin/activate

bash run-example.sh
bash scripts/run-all.sh

echo "PASS: example project validation passed"
