---
type: canonical
module: adapters
status: transitional
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
- Bootstrap remains `llms.txt`; adapters must not create alternate startup paths or read order.
- Adapters may translate canonical instructions into platform-specific entry formatting, but not policy.
- Adapters must stay compatible with canonical routing and core modules.
- Adapter text must not weaken validator policy or invent new governance rules.
- Root adapter files are wrappers for the canonical route, not alternate bootstrap points.

## Adapter roles and authority
- `LAYER-1/adapter-registry.md` is a read-only inventory for discovery, not routing or authority.
- `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` are platform entry wrappers; they defer to canonical bootstrap and core routing.
- `DOMAIN-ADAPTER.md` shows how a domain-specific adapter pattern is shaped, but it is not a replacement for core routing or governance.
- Adapter files may describe platform-specific loading or presentation details, but not canonical policy.
- If adapter text conflicts with canonical docs, canonical docs win.
- Adapter entry files are compatibility/interface layers, not primary entry points.

## Active adapter sources (legacy)
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `DOMAIN-ADAPTER.md`
- `LAYER-1/adapter-registry.md`

## Registry and discovery
- `LAYER-1/adapter-registry.md` may list adapters with metadata so agents and humans can discover available wrappers.
- The registry is a map of adapter locations and status, not a controller for reading order or authority.
- The registry may describe compatibility hints, but it must not become a bootstrap or policy source.
- If registry details and canonical docs conflict, canonical docs win.

## Current boundaries
- Adapter files are pointer/compatibility docs, not bootstrap or policy sources.
- Governance and behavior remain in `llms.txt` + `LAYER-1/agent-rules.md`.
- Adapter guidance must stay compatible with the validator classes and roles already defined in `scripts/VALIDATORS.md`.
- Platform-specific tuning tips and examples remain direct-read detail in the legacy adapter files.

## Compatibility behavior
- Adapters may redirect the user or agent into the canonical route for their platform.
- Adapters may set local formatting, wording, or entry hints that help a specific runtime.
- Adapters must not change canonical ordering, ownership, or authority.
- Adapters must not become a place to define new workflow, state, or governance logic.
- Validation guidance stays bounded by the existing adapter-spec and validator policy; adapters do not rewrite that policy.
- Adapter behavior must remain compatible with existing validator classes and roles; adapters do not redefine them.

## Migration boundary
- This module partially surfaces approved legacy adapter-layer content from `LAYER-1/adapter-registry.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `DOMAIN-ADAPTER.md`.
- Those legacy sources still require direct read for platform-specific examples, entry wording, domain adaptation detail, and validator-boundary nuance.
- `adapters/MAIN.md` is canonical for adapter entry/routing guidance, but not yet the sole deep source.
- Do not treat adapter files as alternate bootstrap or authority.

## Routing
- Read this module when platform/adapter trigger matches.
- Then open the target adapter file and validate against core modules.
- Return to `core-rules/MAIN.md` if authority or routing is unclear.
