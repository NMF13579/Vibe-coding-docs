---
type: canonical
module: adapters
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Adapters

## Purpose
Compatibility layer for specific agent/IDE environments.
Adapters translate canonical routing into platform format and do not define policy.

## When to read
- Open when task depends on a specific runtime/IDE adapter.
- Skip in normal core route when adapter-specific behavior is not needed.

## Canonical constraints
- Adapters are not source of truth.
- Adapters may point to canonical routing only.
- Adapters must not create alternate read order or new bootstrap.

## Active adapter sources (legacy)
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `DOMAIN-ADAPTER.md`
- `LAYER-1/adapter-registry.md`

## Current boundaries
- Adapter files are pointer/compatibility docs.
- Governance and behavior remain in `llms.txt` + `LAYER-1/agent-rules.md`.
- If adapter text conflicts with canonical docs, canonical docs win.

## Migration boundary
- This module is the optional entry for adapter routing.
- Adapter-specific deep guidance remains distributed in existing adapter docs.

## Routing
- Read this module when platform/adapter trigger matches.
- Then open target adapter file and validate against core modules.
- Return to `core-rules/MAIN.md` if authority/routing is unclear.
