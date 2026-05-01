---
type: support
module: architecture
status: active
authority: support
when_to_read: on_demand
owner: unassigned
---

# Architecture

## Purpose
Architecture support entry for AgentOS in module-based routing.
This file helps navigation to architecture material and points to the actual architecture truth source.

## When to read
- When the architecture split needs to be understood quickly.
- When a task needs architecture context but not runtime rules.
- When routing, onboarding, or module maturity looks inconsistent.

## Architecture authority
- `architecture/CANON.md` is the canonical architecture truth source.
- `architecture/MAIN.md` is an architecture support entry.
- `architecture/MAIN.md` is not a runtime module.
- `architecture/MAIN.md` must not be added to `llms.txt` bootstrap order.
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
- Do not treat this file as part of the runtime bootstrap.
- Use `ROUTES-REGISTRY.md` only to confirm runtime module ownership and routing reference.
- Use `architecture/CANON.md` when the architecture truth itself is needed.
- Use this file only as on-demand support navigation.
