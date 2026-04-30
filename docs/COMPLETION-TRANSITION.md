# Completion Transition Record

## 1. Purpose

A completion transition record is an evidence artifact for a future
controlled completion attempt.

It records:

- which task is being considered for completion
- which execution session was used
- which completion readiness result was obtained
- which gates passed
- whether transition preparation was allowed or blocked

Important:

- completion transition record is not task completion
- completion transition record is not lifecycle mutation
- completion transition record is not approval
- prepared transition is not applied transition
- blocked transition is evidence only

## 2. Relationship to M14 and M15

Boundary:

M14:

- may define transition record model
- may later prepare transition record
- may later create blocked transition record
- must not apply transition

M15:

- may safely apply lifecycle transition
- may move task to done/
- may mutate active-task.md
- may advance queue
- must use M14 evidence as input

Main rule:

M14 can prepare or block a completion transition record, but M14 MUST NOT
apply it.

## 3. Allowed Transition Types

In M14, only one transition type is allowed:

```yaml
transition_type: complete
```

With M14-safe statuses only:

```yaml
status: prepared
status: blocked
```

`applied` is reserved for M15 and forbidden in M14.

status: applied is forbidden in M14 and reserved for M15 only.

Rules:

- prepared means readiness passed and future lifecycle transition may be considered by M15
- blocked means readiness did not pass and completion must not proceed
- applied MUST NOT be created in M14

## 4. Transition Record Statuses

prepared:

Completion readiness PASS.
Transition may be considered for future application in M15.
No lifecycle state is changed.

blocked:

Completion readiness is FAIL / PARTIAL / NOT RUN.
Completion must not proceed.
No lifecycle state is changed.

applied:

Reserved for M15 only.
status: applied is forbidden in M14 and reserved for M15 only.
M14 MUST NOT create records with status: applied.

Required rule:

Any transition record with status: applied created during M14 is a safety
violation.

## 5. Required Fields

Transition record must contain:

- transition_id
- task_id
- session_id
- source_task
- source_contract
- completion_readiness_result
- stop_reason
- scope_result
- verification_result
- evidence_report_result
- evidence_report
- transition_type
- status
- created_at
- created_by
- changed_files
- required_gates
- safety_checks
- notes

Recommended IDs:

- transition_id: completion-<task-id>-<YYYYMMDD-HHMMSS>
- created_by: controlled-completion-gate

## 6. Required Source Links

Transition record must reference existing artifacts where possible:

- source_task: tasks/active-task.md
- source_contract: <path-or-missing>
- session_id: <execution-session-id>
- execution_session: reports/execution/<session-id>.md
- completion_readiness: <path-or-stdout-reference>
- evidence_report: reports/execution-evidence-report.md

If an artifact is missing, the transition record must not claim PASS.

Missing required artifacts should produce:

- status: blocked
- stop_reason: evidence_missing

or a more specific reason if available.

## 7. Prepared Transition Rule

A transition record may be prepared only if:

- completion_readiness_result: PASS
- scope_result: PASS
- verification_result: PASS
- evidence_report_result: PASS
- all required evidence exists

Prepared transition record MUST NOT:

- move task to done/
- mutate tasks/active-task.md
- advance queue
- create approval
- apply lifecycle transition

Prepared means:

future completion application may be considered by M15.

## 8. Blocked Transition Rule

A transition record must be blocked if completion readiness result is:

- FAIL
- PARTIAL
- NOT RUN

Blocked transition record must include:

- stop_reason
- failing gate if known
- missing evidence if known
- notes explaining why completion is blocked

Blocked transition record MUST NOT:

- move task to failed/
- move task to done/
- mutate active-task.md
- advance queue
- apply failure transition
- apply needs-review transition

Blocked record is evidence only.

## 9. Stop Reason Model

Allowed stop_reason values:

- active_task_missing
- session_missing
- evidence_missing
- scope_violation
- verification_fail
- evidence_report_fail
- human_review_pending
- human_review_missing
- changed_files_unknown
- changed_files_incomplete
- source_contract_missing
- acceptance_criteria_missing
- watchdog_abort
- manual_abort
- readiness_fail

Rule:

Specific stop_reason values take priority over readiness_fail.
readiness_fail is fallback only.

## 10. Safety Checks

Transition record must include safety checks:

```yaml
safety_checks:
  active_task_mutated: NO
  queue_mutated: NO
  task_moved_to_done: NO
  completion_applied: NO
  approval_created: NO
  transition_status_applied: NO
```

Important:

These fields are claims inside the transition record.
Actual safety must still be validated externally through git diff and
validation commands.

## 11. Notes Field

The notes field satisfies the notes requirement from §5.
In the template it is implemented as a Markdown section below the YAML front
matter block. This section is the canonical notes field for the transition
record.

Rule:

The Notes section MUST be present in every transition record.
It must include at minimum:

- why the record is prepared or blocked
- explicit statement that status: applied is forbidden in M14 and reserved for M15

Template defaults must be in the safest blocked/NOT RUN state.

## 12. Forbidden M14 Behavior

M14 MUST NOT:

- create transition record with status: applied
- mutate tasks/active-task.md
- move task to done/
- move task to failed/
- advance queue
- generate approval
- apply transition
- deploy
- merge
- rollback

Completion transition record is evidence only.

## 13. Expected Result

Completion transition record means:

AgentOS can record whether completion transition preparation is allowed or
blocked, but cannot apply the transition in M14.
