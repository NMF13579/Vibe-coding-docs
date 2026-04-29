# Execution Session Model (Milestone 13)

## 1. Purpose

Execution session is an evidence artifact for a controlled execution attempt.

Execution session records an attempt to start or run controlled execution.
It does not prove task completion.
It does not move queue state.
It does not modify `tasks/active-task.md`.

## 2. Relationship to Controlled Runner

This model is the runtime/evidence model for `docs/CONTROLLED-EXECUTION-RUNNER.md`.

Flow:

`active task validation PASS`
↓
`execution readiness PASS`
↓
`execution session may enter in_progress`
↓
`execution evidence may be recorded`
↓
`completion remains out of scope for M13`

Directory purpose:

- `reports/execution/` — directory for future execution evidence reports.
- `reports/execution/.gitkeep` is only a git-tracked placeholder.
- Concrete execution report files are created in later M13 tasks.
- No execution report files are created in Task 13.2.1.

## 3. Session vs Attempt

Blocked attempt:

- readiness checked
- readiness is not PASS
- status: `blocked`
- stop_reason: `readiness_fail`
- no execution steps allowed

Execution session:

- readiness checked
- readiness is PASS
- status: `in_progress`
- execution steps may run under protocol

Both blocked attempts and execution sessions use the same artifact format.

## 4. Required Frontmatter Fields

Execution session file must include YAML frontmatter with the required structure:

```yaml
---
session_id: exec-task-001-20260429-001
task_id: task-001
active_task: tasks/active-task.md
active_task_snapshot:
  task_id: task-001
  state: active
  activated_at: 2026-04-29T10:00:00Z
  activated_by: human-approved-command
  approval_id: approval-task-001-execution
  source_task: tasks/task-001
  source_contract: tasks/drafts/task-001-contract-draft.md
  transition: approved_for_execution:active
source_task: tasks/task-001
source_contract: tasks/drafts/task-001-contract-draft.md
readiness_result: PASS
readiness_checked_at: 2026-04-29T10:01:00Z
status: in_progress
stop_reason:
started_at: 2026-04-29T10:01:30Z
started_by: controlled-execution-runner
changed_files: []
verification_evidence: []
---
```

## 5. Required Fields

Required fields:

- `session_id`
- `task_id`
- `active_task`
- `active_task_snapshot`
- `source_task`
- `source_contract`
- `readiness_result`
- `readiness_checked_at`
- `status`
- `started_at`
- `started_by`
- `changed_files`
- `verification_evidence`

`stop_reason` is required only when:

- `status == blocked`
- `status == stopped`

`started_at` means time when the session / attempt record was created.
It does not prove that execution steps started.
For blocked attempts, `started_at` records when the blocked attempt was created.

Allowed values for `started_by` in M13:

- `controlled-execution-runner` — standard start through controlled runner
- `agent-requested-controlled-runner` — agent requested the controlled runner entrypoint
- `human-direct-command` — human invoked the controlled runner directly

Other values are not allowed in M13.

`started_by` must not represent bypassing the controlled runner.
Even `agent-requested-controlled-runner` means the agent requested the controlled runner entrypoint, not direct execution outside runner control.

## 6. Status Values

Exactly four status values are allowed in M13:

- `blocked`
- `in_progress`
- `stopped`
- `evidence_ready`

Rules:

`blocked`:

- readiness is not PASS
- execution steps are not allowed
- `stop_reason` MUST be `readiness_fail`

`in_progress`:

- readiness is PASS
- controlled execution is allowed
- `stop_reason` MUST be empty

`stopped`:

- session ended early
- `stop_reason` MUST be non-empty
- valid `stop_reason` values: `scope_violation | watchdog_abort | manual_abort`
- verification may be incomplete

`evidence_ready`:

- verification evidence is recorded
- session stops before task completion
- `stop_reason` MUST be empty
- If `stop_reason` is non-empty, status MUST be `stopped`, not `evidence_ready`

No other status values may be added in M13.

`status: evidence_ready` and `stop_reason: non-empty` are mutually exclusive.
A session that ends with a stop_reason MUST use `status: stopped`.

## 7. stop_reason Values

Exactly four stop_reason values are allowed:

- `readiness_fail`
- `scope_violation`
- `watchdog_abort`
- `manual_abort`

Rules per value:

`readiness_fail`:

- readiness was FAIL, PARTIAL, or NOT RUN
- only valid when `status` is `blocked`

`scope_violation`:

- execution touched or attempted to touch out-of-scope area

`watchdog_abort`:

- session was stopped due to timeout, hung state, or technical watchdog

`manual_abort`:

- user or agent explicitly stopped the session

Different stop reasons MUST NOT be collapsed into a generic STOP record.
`readiness_fail` MUST NOT be used when `status` is `stopped`.
`scope_violation`, `watchdog_abort`, `manual_abort` MUST NOT be used when `status` is `blocked`.

## 8. Readiness Rules

- `readiness_result: PASS` -> `status` may become `in_progress`
- `readiness_result: FAIL` -> `status` must be `blocked`
- `readiness_result: PARTIAL` -> `status` must be `blocked`
- `readiness_result: NOT RUN` -> `status` must be `blocked`

If readiness is not PASS:

- `status: blocked`
- `stop_reason: readiness_fail`
- `changed_files: []`
- `verification_evidence: []`

## 9. active_task_snapshot Rules

`active_task_snapshot` captures metadata from `tasks/active-task.md` at session start.
It is evidence, not a mutable copy.

Rules:

- `tasks/active-task.md` remains read-only
- `active_task_snapshot` must not be used to mutate active task
- `source_task` and `source_contract` in snapshot must match top-level session fields
- snapshot exists to support audit/debug

## 10. source_contract Rules

`source_contract` is the authoritative task contract for execution verification.

Runner may read:

- acceptance criteria
- verification plan
- in_scope
- out_of_scope
- rollback notes, if present

Runner must not:

- modify `source_contract`
- rewrite acceptance criteria
- add new scope
- remove verification requirements

## 11. changed_files Rules

`changed_files` must be a list of repository-relative paths.

Example:

```yaml
changed_files:
  - scripts/example.py
  - docs/example.md
```

Not allowed:

- absolute paths
- parent traversal
- external filesystem paths

If there are no changes:

```yaml
changed_files: []
```

## 12. verification_evidence Rules

`verification_evidence` must be a list of records.

Example:

```yaml
verification_evidence:
  - command: python3 scripts/validate-active-task.py
    status: PASS
    exit_code: 0
    ran_at: 2026-04-29T10:05:00Z
    notes: active task validation passed
```

Allowed `status` values:

- PASS
- FAIL
- PARTIAL
- NOT RUN

Main rule:

PASS must not be recorded unless the command actually ran.

## 13. Human-readable Body

After YAML frontmatter, file must have markdown body with these sections:

- `# Execution Session`
- `## Purpose`
- `## Active Task Snapshot`
- `## Readiness Evidence`
- `## Execution Log`
- `## Changed Files`
- `## Verification Evidence`
- `## Stop Reason`
- `## Completion Boundary`
- `## Notes`

## 14. Completion Boundary

`evidence_ready` does not mean completed.
Completion remains a separate lifecycle transition.
M13 does not mark tasks done, failed, dropped, or moved.

## 15. Non-goals

Execution session is not:

- completion record
- approval record
- rollback record
- queue transition record
- replacement for `active-task.md`
- replacement for `source_contract`
- autonomous execution permission
- record that allows `evidence_ready` to coexist with a non-empty `stop_reason`
