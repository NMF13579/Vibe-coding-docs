#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validate-docs.py
python3 scripts/validate-route.py
python3 scripts/check-links.py
