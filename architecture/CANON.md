---
# AgentOS — Architecture Canon

status: canonical
last-updated: 2026-04-23

## Primary Architecture
primary model: modular routing

primary entrypoints:
  - START.md
  - llms.txt
  - ROUTES-REGISTRY.md

canonical modules: */MAIN.md pattern

## Legacy Status
The following are transitional compatibility layers, NOT primary architecture:
  - LAYER-1/adapter-registry.md
  - LAYER-1/adapters/*
  - LAYER-1/templates/adapter-template.md

## Canonical Validators
  - scripts/validate-architecture.sh
  - scripts/validate-route.py
  - scripts/validate-docs.py
  - tools/doc-tests/*
  - scripts/run-all.sh
  - scripts/health-check.sh

## Legacy Validators (must NOT represent global system health)
  - scripts/legacy-health-check.sh
  - scripts/validate-adapters.sh
  - scripts/check-identity-drift.sh

## CI Canon
canonical workflows:
  - .github/workflows/health.yml
  - .github/workflows/modular-validators.yml
compatibility/transitional workflow:
  - .github/workflows/adapter-check.yml

Note: `adapter-check.yml` is transitional compatibility workflow and must not redefine global architecture truth.
---
