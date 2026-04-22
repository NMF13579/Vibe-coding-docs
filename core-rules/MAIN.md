---
type: canonical
module: core-rules
status: draft
authority: canonical
when_to_read: always
owner: unassigned
---

# Core Rules

## Purpose
Canonical entry for governance and behavior rules in the new module structure.
Rule content remains distributed across legacy rule documents during migration.

## Rule backbone (current)
- Single bootstrap entry for agents remains `llms.txt`.
- Behavior after bootstrap is governed by `LAYER-1/agent-rules.md`.
- Instruction priority/conflict handling follows canonical priority model in shared governance docs.
- State authority follows `LAYER-3/STATE.md` as formal control plane.

## Adapters and authority
- Adapters are compatibility layers and are not source of truth.
- Adapter registry is inventory-only and does not control routing/authority.
- Canonical routing/rules stay in bootstrap + core governance documents.

## Safety and boundaries
- Work only after explicit plan confirmation.
- Respect scope guard and do not expand task without owner confirmation.
- Use self-verification and error-handling routes when risk or failure appears.

## Active legacy sources (transition phase)
- `llms.txt`
- `LAYER-1/agent-rules.md`
- `LAYER-1/document-governance.md`
- `LAYER-1/scope-guard.md`, `LAYER-1/error-handling.md`, `LAYER-1/self-verification.md`
- `LAYER-1/adapter-registry.md` (inventory only)

## Migration boundary
- This module defines the core-rule entry and routing backbone.
- Full consolidation of all policy detail will happen in later PRs.

## Routing
- Read this module always after bootstrap routing.
- Continue to `state/MAIN.md` and `workflow/MAIN.md`.
- Open deep rule docs only when specific trigger/risk requires it.
