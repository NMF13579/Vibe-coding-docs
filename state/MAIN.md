---
type: canonical
module: state
status: draft
authority: canonical
when_to_read: always
owner: unassigned
---

# State

## Purpose
Control-plane entry for runtime state usage in the new module model.
Formal state authority is still anchored in legacy state documents during migration.

## Formal state model (current)
- `LAYER-3/STATE.md` is the formal source of truth for Project / Session / Task state.
- It also defines guards, blockers, and next allowed actions.
- On conflict with handoff or narrative docs, formal state wins.

## How this differs from HANDOFF and narrative docs
- `HANDOFF.md` is a session context snapshot (secondary), not formal state authority.
- `LAYER-3/project-status.md` and `LAYER-3/session-log.md` are narrative/history context.
- This module does not replace those files yet; it routes to them by purpose.

## Runtime usage for agent
1. Start from `llms.txt`, then load context per `LAYER-1/agent-rules.md`.
2. Read `LAYER-3/STATE.md` first for current formal state and guards.
3. Read `HANDOFF.md` for session transfer context.
4. Use narrative docs only when task/context requires deeper history.

## Active legacy sources (transition phase)
- `LAYER-3/STATE.md` (formal state)
- `HANDOFF.md` (session context)
- `LAYER-3/project-status.md` and `LAYER-3/session-log.md` (narrative/history)

## Migration boundary
- This module is now the canonical entry for state routing.
- Full relocation of state content is not complete yet and will continue in later PRs.

## Routing
- Read this module always in core route.
- Continue to `workflow/MAIN.md` for execution protocol tied to state transitions.
- Use `ROUTES-REGISTRY.md` for optional-module triggers.
