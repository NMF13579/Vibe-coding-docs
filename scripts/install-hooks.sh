#!/usr/bin/env bash
set -euo pipefail
git config core.hooksPath .githooks
echo "PASS: Git hooks installed"
