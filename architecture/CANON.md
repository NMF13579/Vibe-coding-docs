---
# AgentOS — Architecture Canon

status: canonical
last-updated: 2026-04-24

## Primary Architecture

primary model: canonical module routing

agent_startup_entrypoint:
  - llms.txt

human_navigation_entrypoint:
  - START.md
  - ROUTES-REGISTRY.md

architecture_truth:
  - architecture/CANON.md

canonical runtime modules:
  - core-rules/MAIN.md
  - state/MAIN.md
  - workflow/MAIN.md
  - quality/MAIN.md
  - security/MAIN.md

## Architecture Rule

- `llms.txt` is the only agent startup entry.
- `ROUTES-REGISTRY.md` records module ownership and human-facing route reference.
- `START.md` is the primary human entry.
- `architecture/CANON.md` is the architecture truth.
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
