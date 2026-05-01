# Approved Mode Contract (Milestone 11 MVP)

## 1. Purpose

This document defines the explicit approved mode required for safe transition execution in AgentOS.
It prevents approval from being inferred from files, dry-run results, environment state, or previous commands.

## 2. Definition: Approved Mode

Approved mode is:
- an explicit, human-requested execution mode
- for one requested transition
- in one command invocation
- after all validations pass

Approved mode is not:
- a stored state
- a global flag
- a reusable permission
- a replacement for approval marker validation
- a replacement for dry-run checks

## 3. Required Flag

Recommended flag:
- `--approved`

Contract rule:
- `--approved` must be passed explicitly in the command invocation that performs the write.

Future command example:

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md \
  --approved
```

## 4. Approved Mode Scope

Approved mode applies only to:
- one requested transition
- one requested task
- one approval marker
- one command invocation

Approved mode must not extend to:
- another task
- another transition
- another approval marker
- future command invocation
- queue processing
- task completion
- task failure marking
- release approval

## 5. Relationship to Approval Marker

Approval marker proves that a human approved a specific scope.
But it does not itself execute or authorize command mode.

Approval marker alone is insufficient because:
- marker may be stale
- marker may be copied
- marker may be valid for a different transition
- marker may be valid for a different task
- marker does not prove the current command was intentionally approved

## 6. Relationship to Dry Run

Dry-run PASS proves that the requested transition appears safe.
But it does not authorize the write.

Dry-run PASS alone is insufficient because:
- dry-run is diagnostic
- dry-run may be run by automation
- dry-run may be run before final human review
- dry-run does not express intent to modify files

## 7. Relationship to Validation

`--approved` does not bypass validation.

Approved mode unlocks write only after:
- task state validation passes
- transition validation passes
- approval marker validation passes
- semantic approval checks pass
- write safety checks pass

If any check fails:
- approved mode must not write anything

## 8. Forbidden Approval Sources

Forbidden:
- implicit approval
- approval by file presence only
- approval by dry-run PASS only
- approval by environment variable only
- approval by previous command
- approval by cached state
- approval by config default
- approval by branch name
- approval by commit message
- approval by agent assumption

## 9. Failure Behavior

If `--approved` is missing during write attempt:
- fail closed
- do not write
- explain that explicit approved mode is required

If `--approved` is present but checks fail:
- fail closed
- do not write
- explain failed check

## 10. Audit Requirements

Future implementation of approved mode must make it possible to determine:
- which command was run
- which task was requested
- which approval marker was used
- which transition was requested
- whether approved mode was explicit
- whether dry-run or write mode was used

## 11. Examples

Valid:

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md \
  --approved
```

Why valid:
- explicit approved mode
- specific task
- specific approval marker
- specific transition inferred from activate-task target

Invalid: marker only

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md
```

Reason:
- approval marker present, but approved mode absent

Invalid: dry-run only

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md \
  --dry-run
```

Reason:
- dry-run checks safety but does not write

Invalid: remembered approval

A previous command used `--approved`, so the next command writes without it.

Reason:
- approved mode must not persist across invocations

## 12. Non-goals

This document does not define:
- activation implementation
- approval marker schema
- task state machine
- queue automation
- task completion
- rollback script
- agent runner execution
- release approval

## Core Principle

Approval marker is evidence.
Approved mode is intent.
Execution requires both.

Dry-run PASS is verification, not permission.
