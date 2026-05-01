# Approval Marker Specification

## Purpose

An approval marker is a Markdown evidence file that records explicit human approval for a future controlled transition.
It does not execute the transition.
It does not replace human review.
It does not create `tasks/active-task.md`.
It does not move queue entries.
It does not grant release approval.

## Core Principle

Approval marker is evidence only.
Approval marker must be explicit.
Approval marker must be task-specific.
Approval marker must be scope-specific.
Approval marker must be human-issued.
Approval marker must be validated before use.
Human-readable notes or reason text do not grant approval unless required frontmatter fields are valid.

## Marker Location

Recommended path:

```text
approvals/{approval-id}.md
```

Example:

```text
approvals/approval-task-001-execution.md
```

Milestone 10.14 documents this path only.
Do not create `approvals/`.
Do not create real approval marker files.
If `approvals/` does not exist, that is not an error for this spec-only milestone.

## Marker Format

Approval marker must be a Markdown file with YAML frontmatter.

Example:

```markdown
---
approval_id: approval-task-001-execution
task_id: task-001
approval_type: execution
approved_by: human
approved_at: 2026-04-27T10:00:00Z
expires_at: ""
status: approved
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
reason: "Approved for controlled activation after dry-run checks passed."
---

# Approval Notes

This marker records explicit human approval for the controlled transition
from approved_for_execution to active.
```

Body text is explanatory only.
Body text does not grant approval unless the required YAML frontmatter fields are present and valid.

## Required Fields

| field | required | meaning |
|---|---|---|
| `approval_id` | yes | Unique approval identifier |
| `task_id` | yes | Task this approval applies to |
| `approval_type` | yes | Type of approval |
| `approved_by` | yes | Human approver identifier or human approval source |
| `approved_at` | yes | UTC timestamp |
| `status` | yes | Current approval status |
| `scope` | yes | What this approval permits |
| `related_contract` | yes for execution approval | Contract draft this approval refers to. The file must exist at the specified path at validation time. |

Notes:
- `approved_by` must identify a human approver or human approval source.
- MVP may use `human` if no identity system exists.
- Do not require personal email or sensitive identity data in MVP.

## Optional Fields

| field | meaning |
|---|---|
| `expires_at` | Expiration timestamp. Empty string means no explicit expiration in MVP. |
| `reason` | Human-readable approval reason |
| `conditions` | List of conditions that must remain true |
| `revoked_at` | Timestamp if revoked |
| `revoked_by` | Human who revoked approval |
| `revocation_reason` | Why approval was revoked |
| `superseded_by` | Replacement approval marker id if this marker was superseded |

## Approval Types

Allowed `approval_type` values:

```text
brief
review
trace
contract
execution
drop
restart
```

The most important type for Milestone 11 is `execution`.
Execution approval means a human approved a future controlled state-changing action.
It does not execute that action by itself.

## Approval Scopes

Allowed `scope` values:

```text
approve_brief
approve_contract
activate_task
mark_completed
mark_failed
drop_task
restart_task
```

`scope` must match the requested transition.

| transition | required scope |
|---|---|
| `contract_drafted -> approved_for_execution` | `approve_contract` |
| `approved_for_execution -> active` | `activate_task` |
| `active -> completed` | `mark_completed` |
| `active -> failed` | `mark_failed` |
| `active -> dropped` | `drop_task` |
| `failed -> brief_draft` | `restart_task` |

## Status Values

Allowed `status` values:

```text
approved
revoked
expired
superseded
```

Rules:
- Only `status: approved` may be treated as valid approval evidence.
- `status: revoked` must block transition eligibility.
- `status: expired` must block transition eligibility.
- `status: superseded` must block transition eligibility.
- `expired` may be computed from `expires_at` even if `status` is still `approved`.
- `revoked` may be inferred from `status: revoked` or revocation fields.
- `superseded` may be inferred from `status: superseded` or `superseded_by`.

## Valid Marker Rules

An approval marker is valid only if:
- required fields are present
- `task_id` matches the requested task
- `status` is `approved`
- `approval_type` matches the intended use
- `scope` matches the requested transition
- `related_contract` exists when required
- `related_contract` file exists at the specified path when required
- `approved_at` is present and parseable
- `expires_at` is empty or in the future
- marker is not revoked
- marker is not expired
- marker is not superseded
- marker is not ambiguous
- no conflicting approval markers exist for the same `task_id` and `scope`
- no multiple approved markers exist for the same `task_id` and `scope` unless older markers are explicitly revoked or superseded

Valid approval marker still does not execute the transition.
It only allows future checker or automation to consider the transition eligible.

## Invalid Marker Rules

An approval marker is invalid if:
- required fields are missing
- `task_id` does not match
- `status` is not `approved`
- `approval_type` does not match
- `scope` does not match
- `related_contract` is missing when required
- `related_contract` is present but the file does not exist at the specified path
- `related_contract` points to the wrong task
- `approved_at` is missing
- `approved_at` is malformed
- `expires_at` is malformed
- marker content is ambiguous
- multiple conflicting markers exist for the same `task_id` and `scope`
- multiple approved markers exist for the same `task_id` and `scope` without `superseded` or `revoked` status
- human-readable reason exists but required frontmatter fields are missing or invalid

## Expired Marker Rules

An approval marker is expired if:
- `expires_at` is present
- `expires_at` is not empty
- `expires_at` is earlier than the current UTC time
- or `status: expired`

An expired marker:
- must not be treated as valid approval evidence
- must not allow transition eligibility
- must be reported as expired evidence

## Revoked Marker Rules

An approval marker is revoked if:
- `status: revoked`
- or `revoked_at` is present
- or `revoked_by` is present

A revoked marker:
- must not be treated as valid approval evidence
- must block transition eligibility
- must be reported as revoked evidence

## Superseded Marker Rules

An approval marker is superseded if:
- `status: superseded`
- or `superseded_by` is present

A superseded marker:
- must not be treated as valid approval evidence
- must not allow transition eligibility
- must point to the replacement marker if `superseded_by` is present
- must be reported as superseded evidence

## Relationship to State Machine

Approval marker may support `approved_for_execution` state.
Approval marker may support a future transition check.
Approval marker does not replace `TASK.md`, `REVIEW.md`, `TRACE.md`, or a contract draft.
Approval marker does not bypass required evidence.
Approval marker does not override `state_conflict` or `analysis_status: conflict`.
Approval marker does not override `analysis_status: invalid`.

If the later state model uses separation between state and analysis:
Approval marker does not override `analysis_status: conflict` or `analysis_status: invalid`.

## Relationship to Transition Checker

`check-transition.py` may treat a valid approval marker as required evidence.
`check-transition.py` must still verify the current state.
`check-transition.py` must still verify the transition rule.
`check-transition.py` must still verify required evidence.
`check-transition.py` must still return dry-run only.

Even if the marker is valid:

```text
Transition executed: no
```

must remain true for Milestone 10.

## Relationship to Milestone 11

Milestone 11 may use approval markers only if:
- current state is valid
- `analysis_status` is `ok`
- requested transition is allowed
- required evidence exists
- dry-run check passes
- approval marker is valid
- human explicitly requested approved mode

Milestone 10.14 does not add approved mode.

## Safety Boundaries

Approval marker does not execute transitions.
Approval marker does not create approval automatically.
Approval marker does not replace human review.
Approval marker does not replace `tasks/active-task.md`.
Approval marker does not move queue entries.
Approval marker does not mark tasks completed.
Approval marker does not mark tasks failed.
Approval marker does not drop tasks.
Approval marker does not grant release approval.
Approval marker does not bypass validators.
Human-readable approval notes do not bypass required marker fields.

## Out of Scope

Milestone 10.14 does not add:
- approval marker validator
- approval marker schema
- approval marker fixtures
- approval marker generation
- automatic approval
- automatic transition execution
- approved mode
- `tasks/active-task.md` replacement
- queue movement
- completion automation
- failure automation
- drop automation
- release approval
- backend
- RAG
- vector DB
- web UI

## Examples

### Valid execution approval

```markdown
---
approval_id: approval-task-001-execution
task_id: task-001
approval_type: execution
approved_by: human
approved_at: 2026-04-27T10:00:00Z
expires_at: ""
status: approved
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
reason: "Approved for controlled activation after dry-run checks passed."
---
```

### Invalid marker: task mismatch + file path mismatch

```markdown
---
approval_id: approval-task-999-execution
task_id: task-999
approval_type: execution
approved_by: human
approved_at: 2026-04-27T10:00:00Z
status: approved
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
---
```

Invalid reason 1: `task_id task-999` does not match `related_contract` task `task-001`.
Invalid reason 2: `related_contract` points to the wrong task.

### Expired marker

```markdown
---
approval_id: approval-task-001-expired
task_id: task-001
approval_type: execution
approved_by: human
approved_at: 2026-04-20T10:00:00Z
expires_at: 2026-04-21T10:00:00Z
status: approved
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
---
```

### Revoked marker

```markdown
---
approval_id: approval-task-001-revoked
task_id: task-001
approval_type: execution
approved_by: human
approved_at: 2026-04-27T10:00:00Z
status: revoked
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
revoked_at: 2026-04-27T11:00:00Z
revoked_by: human
revocation_reason: "Scope changed before execution."
---
```

### Superseded marker

```markdown
---
approval_id: approval-task-001-old
task_id: task-001
approval_type: execution
approved_by: human
approved_at: 2026-04-27T10:00:00Z
status: superseded
scope: activate_task
related_contract: tasks/drafts/task-001-contract-draft.md
superseded_by: approval-task-001-new
reason: "Superseded after contract draft update."
---
```

## Future Validator Requirements

The next stage may be `10.15.1 — Approval Marker Validator MVP`.

That validator should check:
- required fields
- `task_id` match
- `status`
- `approval_type`
- `scope`
- `related_contract` field present when required
- `related_contract` file exists at the specified path
- `approved_at` format
- `expires_at` logic
- revoked status
- superseded status
- duplicate or conflicting markers for the same `task_id` and `scope`
- multiple approved markers for the same `task_id` and `scope`
- read-only guarantee

Milestone 10.14 does not create that validator.
