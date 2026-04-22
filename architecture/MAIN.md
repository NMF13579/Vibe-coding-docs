---
type: canonical
module: architecture
status: draft
authority: canonical
when_to_read: always
owner: unassigned
---

# Architecture

## Purpose
Canonical architecture entry for AgentOS in module-based routing.
Defines how bootstrap, routing hub, modules, and legacy layers coexist during migration.

## System model (current)
- AgentOS is a governed workspace for AI-agent-driven development.
- Agent bootstrap remains `llms.txt`; human start remains `START.md`.
- `ROUTES-REGISTRY.md` is the central routing hub for module navigation.
- Core modules are mandatory route; optional modules are trigger-based.

## Modules vs legacy layers
- New primary UX is module-based routing (core -> optional -> deep docs).
- Legacy `LAYER-1/`, `LAYER-2/`, `LAYER-3/` remain active source layers during transition.
- Migration is incremental: module entries first, content relocation later.

## State, adapters, and authority
- Formal state authority remains `LAYER-3/STATE.md`.
- `HANDOFF.md` remains secondary session context.
- Adapters are interface layers and must not define policy authority.
- Memory-bank is legacy compatibility, not a second canonical memory plane.

## Where architectural canon lives now
- Primary detailed architecture source: `ARCHITECTURE.md`.
- Related architecture decisions and constraints: `LAYER-3/DECISIONS.md`.
- Governance metadata/lifecycle: `LAYER-1/document-governance.md`.

## Active legacy sources (transition phase)
- `ARCHITECTURE.md`
- `LAYER-3/DECISIONS.md`
- `LAYER-1/document-governance.md`
- `llms.txt`, `LAYER-1/agent-rules.md`

## Migration boundary
- This module defines canonical architecture entry and transition model.
- Detailed architecture sections remain in legacy docs until staged migration PRs.

## Routing
- Read this module always in core route.
- Continue to `workflow/MAIN.md` for execution semantics.
- Use `ROUTES-REGISTRY.md` for optional module entry decisions.
