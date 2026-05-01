---
type: canonical
module: state
status: canonical
authority: canonical
when_to_read: always
owner: unassigned
---

# State

## Purpose

Canonical control plane for project, session, and task state.
This module owns state lifecycle, events, recovery, and transition boundaries.

## State Authority

- State rules must be read from this module before execution begins.
- `state/MAIN.md` owns state rules, lifecycle, events, guards, and recovery.
- It does not store project-specific current state unless explicitly stated.
- Session transfer notes are supporting context only; they do not override state rules.
- Narrative project notes are supporting context only; they do not define current state.
- If state facts conflict, use the formal state fields and stop if the conflict changes the next action.
- If current state is missing, incomplete, or contradictory, the agent must report that and ask the owner.
- Do not infer a richer state schema than the current canonical rules define.

## State Shape

Use this minimum state shape when reporting or recovering state:

```yaml
project_state:
session_state:
task_state:
active_task:
blockers:
next_allowed_actions:
last_verified_step:
owner_confirmation_required:
```

## Lifecycle

- Project lifecycle: `INIT` -> `DISCOVERY` -> `PLANNING` -> `DEVELOPMENT` -> `REVIEW` -> `RELEASE_READY` -> `MAINTENANCE`.
- Session lifecycle: `BOOTSTRAP` -> `CONTEXT_LOADED` -> `AWAITING_CONFIRMATION` -> `EXECUTING` -> `VERIFYING` -> `HANDOFF`.
- Task lifecycle: `DRAFT` -> `PLANNED` -> `IN_PROGRESS` -> `REVIEW` -> `DONE`.
- Blocked work uses `BLOCKED` until the blocker is removed.
- Failed or unsafe work uses `ERROR` or `ROLLED_BACK` until recovery is complete.

## State Events

- `CONTEXT_RESTORED` marks session context loaded after bootstrap.
- `PLAN_PRESENTED` marks that the owner has received the plan.
- `USER_APPROVED` marks explicit owner confirmation.
- `TASK_IMPLEMENTED` marks implementation completion.
- `VERIFICATION_PASSED` marks successful verification.
- `BLOCKER_FOUND` marks a blocked task state.
- `BLOCKER_RESOLVED` marks removal of a known blocker.
- `ERROR_DETECTED` marks a classified failure.
- `ROLLBACK_COMPLETED` marks completed recovery after rollback.
- `SESSION_ENDED` marks the end of a session.

## Transition Boundaries

- Every transition requires a guard check before it is allowed.
- If a guard fails, stop the transition and report the reason.
- Execution cannot skip `CONTEXT_LOADED`.
- A blocked or failed transition must not be treated as normal continuation.
- Illegal transitions must not be executed unless explicitly revalidated and approved by the owner.
- Error and recovery transitions are exceptional, not ordinary flow.

## Recovery

- If context is stale, incomplete, or contradictory, stop and recover state before continuing.
- If the active task, blocker, or next transition cannot be recovered, ask the owner for input.
- If the same task remains unfinished across several sessions, warn the owner and ask whether to split it or continue.
- After recovery, continue only once the restored context is confirmed.
- Do not guess current state from partial history.

## Runtime Usage

1. Start from `llms.txt`.
2. Load the five canonical modules.
3. Identify project, session, and task state.
4. Check blockers and next allowed actions.
5. Report state, active task, next allowed actions, and blockers before execution.
6. Continue to `workflow/MAIN.md` for the execution sequence.
