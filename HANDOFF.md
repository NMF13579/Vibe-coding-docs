<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- SOURCE_OF_TRUTH: no -->

# HANDOFF.md — Session Handoff Contract

HANDOFF is session context only.
It does not override canonical modules.

## Terminal Snapshot

- Startup route: `llms.txt` -> `state/MAIN.md` -> `workflow/MAIN.md`.
- Current blockers: none recorded here.
- Use `core-rules/MAIN.md` for authority conflicts.
- Use `quality/MAIN.md` before claiming completion.
- Use `security/MAIN.md` when sensitive data or access boundaries are involved.

## Next Agent First Step

1. Read `llms.txt`.
2. Confirm state through `state/MAIN.md`.
3. Confirm execution boundary through `workflow/MAIN.md`.
4. Continue only inside the owner-confirmed task.

## Persistent Context

Project type: AgentOS — governed workspace for AI-agent-driven development.
Stack: Markdown, GitHub, agent environments.
Architecture: canonical module routing.
Primary route: `llms.txt` and `ROUTES-REGISTRY.md`.
