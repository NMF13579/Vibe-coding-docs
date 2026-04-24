---
type: canonical
module: architecture
status: transitional
authority: canonical
when_to_read: always
owner: unassigned
---

# Architecture

## Purpose
Canonical architecture entry for AgentOS in module-based routing.
This module routes architecture reading and points to the actual architecture truth source.

## When to read
- When the architecture split needs to be understood quickly.
- When a task needs the architecture route but not deep architectural detail.
- When routing, onboarding, or module maturity looks inconsistent.

## Architecture authority
- `architecture/CANON.md` is the canonical architecture truth source.
- `architecture/MAIN.md` is the operational architecture entry and routing layer.
- `ARCHITECTURE.md` is supporting architecture detail.
- If this module and `architecture/CANON.md` conflict, `architecture/CANON.md` wins.

## Current deep sources
- `ARCHITECTURE.md` is the deep architecture detail source.
- Read it only when the route or canon summary is not enough.

## Migration boundary
- This module surfaces the architecture entry and routing split.
- The truth lives in `architecture/CANON.md`.
- Detailed architecture stays in `ARCHITECTURE.md`.
- Do not treat this module as a second canon.

## Routing
- Read this module in the core route after `core-rules/MAIN.md` and `state/MAIN.md`.
- Use `ROUTES-REGISTRY.md` for module navigation.
- Use `architecture/CANON.md` when the architecture truth itself is needed.
