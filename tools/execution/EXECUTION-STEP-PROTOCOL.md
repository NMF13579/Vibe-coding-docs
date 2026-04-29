# Execution Step Protocol

## 1. Purpose

`EXECUTION-STEP-PROTOCOL.md` defines execution behavior for an agent working inside an execution session.

Execution step protocol guides implementation behavior.
It does not create sessions.
It does not verify completion.
It does not mark task done.

## 2. Preconditions

Agent may use this protocol only when all conditions are true:

- execution session exists
- `session.status == in_progress`
- `session.readiness_result == PASS`
- `session.stop_reason` is empty
- `source_contract` exists
- `active_task_snapshot` exists

If any condition is not met:

- STOP
- do not implement
- report `protocol_blocked`

## 3. Required Inputs

Agent must read:

1. execution session file
2. `active_task_snapshot` inside session
3. `source_contract` from session
4. `source_task` from session, if needed

Agent must not use as authority:

- random task file
- stale queue entry
- human description outside `source_contract`
- previous session file

Primary execution authority:

- `source_contract`

## 4. Execution Authority

`source_contract` is authoritative for:

- goal
- acceptance criteria
- in_scope
- out_of_scope
- verification plan
- risk / rollback notes, if present

Execution session is authoritative for:

- `session_id`
- `active_task_snapshot`
- `readiness_result`
- `status`
- `changed_files` evidence
- `verification_evidence` evidence

Agent must not expand scope on its own.

## 5. Step-by-Step Protocol

Step 1 — Read execution session  
Step 2 — Confirm status is `in_progress`  
Step 3 — Read `source_contract`  
Step 4 — Extract goal, acceptance criteria, `in_scope`, `out_of_scope`  
Step 5 — Produce minimal execution plan  
Step 6 — Check plan against `in_scope` / `out_of_scope`  
Step 7 — If plan violates scope: STOP with `scope_violation` candidate  
Step 8 — Make only scoped changes  
Step 9 — Record changed files  
Step 10 — Prepare verification commands from `source_contract`  
Step 11 — Do not declare completion

At this stage, `record changed files` may be manual/documented behavior.
Script-based session updates are future work.
Agent must output changed files list in its response before stopping.
This list must not be automatically written into session file by this protocol. That behavior is reserved for future tooling.

## 6. Minimal Execution Plan

Before edits, agent must prepare:

## Execution Plan
Goal:
- ...
Allowed files / areas:
- ...
Forbidden files / areas:
- ...
Planned changes:
- ...
Expected verification:
- ...

Rules:

- plan must be derived from `source_contract`
- plan must not add scope
- plan must not add new acceptance criteria
- plan must not remove verification requirements

## 7. Scope Rules

`in_scope` defines allowed work area.  
`out_of_scope` defines forbidden work area.

If `in_scope` is missing or unclear:

- treat as PARTIAL / unclear
- do not broaden scope silently
- ask for clarification or stop

If `out_of_scope` is violated:

- STOP
- candidate `stop_reason`: `scope_violation`
- do not continue implementation

Forbidden behavior:

- touch files outside scope because it seems useful
- refactor unrelated code
- fix nearby issues
- change CI/deployment unless explicitly in scope
- change `approvals/`
- change `tasks/active-task.md`
- change `source_contract`
- move queue items

## 8. File Mutation Rules

Agent may modify only files explicitly allowed by `source_contract`.

Agent must not modify:

- `tasks/active-task.md`
- `source_contract`
- `source_task` (unless explicitly in scope)
- `approvals/`
- `reports/execution/.gitkeep`
- queue files
- done/failed/dropped task state files

Execution session file may be updated only by later M13 tooling/protocol.
Task 13.5.1 does not implement automatic session updates.

## 9. Changed Files Recording

After edits, agent must record changed files evidence.

MVP behavior:

- agent lists changed files in response / execution log
- future tooling writes `changed_files` into session file

Changed files format:

- repository-relative paths only
- no absolute paths
- no parent traversal

If changed file is outside scope:

- STOP
- candidate `stop_reason`: `scope_violation`

## 10. Verification Preparation

Agent must prepare verification commands from `source_contract`.

Task 13.5.1 does not run verification runner.

Rules:

- verification commands come from `source_contract`
- agent must not invent weaker verification
- agent must not remove failing verification
- agent must not claim PASS unless command actually ran

If verification plan is missing:

- record verification gap
- do not claim completion

## 11. Stop Conditions

Agent must stop if:

- `session.status != in_progress`
- `readiness_result != PASS`
- `source_contract` missing
- `source_contract` unclear
- `in_scope` / `out_of_scope` conflict
- plan violates scope
- attempted change touches forbidden area
- verification requirements cannot be identified
- user manually aborts

Allowed candidate stop reasons:

- `scope_violation` — attempted change violates `in_scope` or touches `out_of_scope`
- `manual_abort` — user or operator explicitly stopped execution
- `watchdog_abort` — reserved for future watchdog mechanism; agent may record it if an external abort signal is received

`readiness_fail` must not be used as stop reason inside execution steps.
Readiness is already PASS for `in_progress` sessions.
If readiness re-check is needed, that is outside this protocol.

## 12. Completion Boundary

Agent may implement.
Agent may prepare verification.
Agent may report evidence.
Agent may not mark task completed.
Agent may not move task to done.
Agent may not mark task failed.
Agent may not drop task.

Completion remains a separate lifecycle transition outside 13.5.1.

## 13. Human Checkpoint

After implementation and evidence collection, agent must stop and output this checkpoint in response:

Implementation changes are prepared.
Verification evidence is pending / available.
Completion decision is out of scope for this protocol.

If human review is required:

- request human review before any completion/failure transition

This checkpoint message must be output in agent response before stopping.
This message must not be written into session file by this protocol. That behavior is reserved for future tooling.

## 14. Non-goals

This protocol does not implement:

- session creation
- dry-run
- readiness check
- scope checker script
- verification runner script
- automatic `changed_files` writing
- automatic `verification_evidence` writing
- task completion
- task failure
- queue movement
- approval generation
- rollback automation
- deployment

## 15. Required Future Artifacts

Planned M13 follow-up artifacts:

- `scripts/check-execution-scope.py`
- `tools/execution/CHECK-EXECUTION-SCOPE.md`
- `scripts/run-execution-verification.py`
- `tools/execution/RUN-EXECUTION-VERIFICATION.md`
- `reports/execution-evidence-report.md`
- `tests/fixtures/negative/execution-runner/`
- `scripts/test-execution-runner-fixtures.py`
- `reports/milestone-13-completion-review.md`
