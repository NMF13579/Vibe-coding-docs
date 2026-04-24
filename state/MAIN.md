---
type: canonical
module: state
status: transitional
authority: canonical
when_to_read: always
owner: unassigned
---

# State

## Purpose
Control-plane entry for runtime state usage in the new module model.
This module surfaces the operational state backbone while formal depth still lives in approved legacy sources during migration.

## State authority and roles
- `LAYER-3/STATE.md` remains the formal source of truth for Project / Session / Task state, guards, blockers, and next allowed actions.
- `HANDOFF.md` is a secondary session-transfer snapshot; use it for continuity and recovery, not as authority.
- `LAYER-3/project-status.md` is a tertiary project narrative and risk summary; use it for broad context, not live state.
- `LAYER-3/session-log.md` is a structural session journal with history and transition records; use it to reconstruct sequence, not to define current state.
- If documents conflict, `LAYER-3/STATE.md` wins.
- Do not infer a richer state schema than the sources explicitly define.
- `state/MAIN.md` is canonical for state entry and routing, but not yet the sole deep source.

## Active task and continuity
- Start from `llms.txt`, then follow canonical core rules for session loading.
- After reading context, determine Project / Session / Task state from `LAYER-3/STATE.md`.
- Check `forbidden` and `next_allowed_actions`.
- Report to the user: Project state / Session state / Task state, Active task, Next allowed actions, Blockers.
- Execute the session transition BOOTSTRAP → CONTEXT_LOADED (event: CONTEXT_RESTORED).
- `[BOOTSTRAP COMPLETE]` — only then begin work on the task.
- If `STATE.md` does not exist: "STATE.md not found. State layer initialization required."
- Do not start work until `STATE.md` is created.
- If `active_task` is empty or the session is in handoff, use `HANDOFF.md` to recover transfer context.
- Use `LAYER-3/project-status.md` when project stage, risk, or broad direction is unclear.
- Use `LAYER-3/session-log.md` when the task sequence, prior changes, or transition order must be reconstructed.
- Resume active work by restoring project/session/task from `LAYER-3/STATE.md`, then confirm the transfer context in `HANDOFF.md`.
- Exact field-by-field detail stays direct-read in the formal legacy files.

## Recovery and ambiguity route
- If `HANDOFF.md` and `LAYER-3/STATE.md` disagree, follow `LAYER-3/STATE.md` and reconcile the supporting docs after that.
- If context is stale or incomplete, open `LAYER-3/project-status.md` for project narrative and `LAYER-3/session-log.md` for timeline.
- If the active task, blocker, or transition still cannot be recovered, stop and ask for owner input or direct-read the formal source again.
- Do not guess the current state from partial history.

## Runtime usage for agent
1. Start from `llms.txt`, then load context per `LAYER-1/agent-rules.md`.
2. Read `LAYER-3/STATE.md` first for current formal state, guards, blockers, and next allowed actions.
3. Read `HANDOFF.md` for session transfer context when the session is not already fully active.
4. Use `project-status.md` and `session-log.md` only when the task needs recovery, history, or ambiguity resolution.

## Migration boundary
- This module partially surfaces approved legacy state content from `LAYER-3/STATE.md`, `HANDOFF.md`, `LAYER-3/project-status.md`, and `LAYER-3/session-log.md`.
- Those legacy sources still require direct read for exact state fields, guards, blockers, full transition history, and narrative detail.
- Do not treat the supporting docs as alternate state authority.
- Full relocation of state content is not complete yet and will continue in later PRs.

## Routing
- Read this module always in the core route.
- Continue to `workflow/MAIN.md` for execution protocol tied to state transitions.
- Use `ROUTES-REGISTRY.md` for optional-module triggers.
