---
# AgentOS — Architecture Canon

status: canonical
last-updated: 2026-04-24

## Primary Architecture

primary model: canonical module routing

primary entrypoints:
  - llms.txt
  - ROUTES-REGISTRY.md

canonical runtime modules:
  - core-rules/MAIN.md
  - state/MAIN.md
  - workflow/MAIN.md
  - quality/MAIN.md
  - security/MAIN.md

## Architecture Rule

- `llms.txt` is the only agent startup entry.
- `ROUTES-REGISTRY.md` records module ownership.
- The five canonical modules define runtime behavior.
- Adapter, support, note, and archive files are not runtime authority.
- If a non-canonical file conflicts with a canonical module, the canonical module wins.

## Canonical Validators

  - scripts/validate-architecture.sh
  - scripts/validate-route.py
  - scripts/validate-docs.py
  - tools/doc-tests/*
  - scripts/run-all.sh
  - scripts/health-check.sh

## CI Canon

canonical workflows:
  - .github/workflows/health.yml
  - .github/workflows/modular-validators.yml

Wrapper checks may validate entry files, but they must not redefine architecture truth.
---
