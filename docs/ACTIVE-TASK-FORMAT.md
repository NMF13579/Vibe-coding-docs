# Active Task Format (Milestone 11)

## 1. Purpose

This document defines the canonical format of `tasks/active-task.md` for Milestone 11.
The file is created or updated only by safe activation logic after explicit human approval.

## 2. Definition

`tasks/active-task.md` is:
- current active task pointer
- activation record
- traceability artifact
- controlled-write output

`tasks/active-task.md` is not:
- approval marker
- verification report
- task completion proof
- agent execution log
- queue processor
- release approval

## 3. Creation Rules

- `tasks/active-task.md` may be created or updated only by approved activation flow.
- The only allowed Milestone 11 transition that writes it is `approved_for_execution -> active`.
- Dry-run must never write it.
- Failed activation must never partially write it.
- Manual edits are discouraged and must be treated as audit-sensitive.

## 4. Canonical Frontmatter Format

```yaml
---
task_id: task-001
state: active
activated_at: 2026-04-28T10:00:00Z
activated_by: human-approved-command
approval_id: approval-task-001-execution
source_task: tasks/task-001
source_contract: tasks/drafts/task-001-contract-draft.md
transition: approved_for_execution:active
---
```

## 5. Field Definitions

`task_id`
- Required. Stable task identifier. Must match the activated task.

`state`
- Required. Must be `active`.

`activated_at`
- Required. UTC timestamp in ISO-8601 format, preferably ending with `Z`.

`activated_by`
- Required. For Milestone 11 must be `human-approved-command`.

`approval_id`
- Required when available. Identifies the approval marker used for activation.
- If approval marker lacks `approval_id`, the field may be empty, but this is reduced traceability.

`source_task`
- Required. Path to the activated task.

`source_contract`
- Optional but recommended. Path to the related contract draft if known.
- Empty string is allowed when unknown.

`transition`
- Required. For Milestone 11 must be `approved_for_execution:active`.

## 6. Body Format

Recommended body:

```md
# Active Task

This task was activated by a human-approved AgentOS command.

Source task: tasks/task-001
Approval marker: approvals/approval-task-001-execution.md
Transition: approved_for_execution:active
```

Body is human-readable.
Canonical data lives in frontmatter.

## 7. Validation Expectations

Future validator expectations (minimum):
- frontmatter exists
- `task_id` exists
- `state == active`
- `activated_at` exists and is parseable
- `activated_by == human-approved-command`
- `source_task` exists
- `transition == approved_for_execution:active`
- `source_contract` exists if non-empty
- `approval_id` exists or warning

Note:
- absence of `approval_id` may be WARN, not necessarily FAIL, if legacy approval marker lacks `approval_id`.

## 8. Overwrite Rules

- If `active-task.md` does not exist, activation may create it.
- If `active-task.md` exists and references same `task_id`, idempotent re-activation may replace it.
- If `active-task.md` exists and references another `task_id`, activation must FAIL.
- If `active-task.md` exists but has no `task_id`, activation must FAIL.

## 9. Auditability Requirements

After reading `active-task.md`, it must be possible to determine:
- which task is active
- when it was activated
- what approval marker authorized it
- which source contract was used
- which transition was performed
- that activation came from explicit human-approved command

## 10. Relationship to Other Files

`approval marker`
- Authorizes scope but is not active state.

`source contract`
- Defines execution contract but is not activation record.

`TASK.md` / `REVIEW.md` / `TRACE.md`
- Provide task lifecycle evidence but are not active pointer.

`reports/verification.md`
- May prove execution verification later but is not activation.

`tasks/queue/`
- Queue stores candidates; `active-task.md` stores one current active pointer.

## 11. Forbidden Uses

`active-task.md` must not be used as:
- proof of completion
- proof of verification
- approval marker
- queue state source of truth
- release approval
- automatic execution trigger
- agent runner log

Critical boundary:
- The presence of `active-task.md` must not automatically execute the task.

## 12. Example

```md
---
task_id: task-001
state: active
activated_at: 2026-04-28T10:00:00Z
activated_by: human-approved-command
approval_id: approval-task-001-execution
source_task: tasks/task-001
source_contract: tasks/drafts/task-001-contract-draft.md
transition: approved_for_execution:active
---

# Active Task

This task was activated by a human-approved AgentOS command.

Source task: tasks/task-001
Approval marker: approvals/approval-task-001-execution.md
Transition: approved_for_execution:active
```

## 13. Non-goals

This document does not define:
- activation CLI implementation
- approval marker schema
- task state machine
- queue processing
- task execution
- task completion
- task failure
- rollback script
- release approval

## Core Principle

`active-task.md` is an activation pointer, not execution proof.
`active-task.md` records which task is currently active.
`active-task.md` preserves traceability to approval marker and source contract.
`active-task.md` does not prove task completion.
`active-task.md` does not replace verification report.
