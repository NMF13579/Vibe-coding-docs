# Completion Readiness

```yaml
readiness_id: completion-readiness-<task-id>-<timestamp>
task_id: <task-id>
session_id: <execution-session-id>

source_task: tasks/active-task.md
source_contract: <path-or-missing>
execution_evidence_report: <path-or-missing>

readiness_result: NOT RUN
stop_reason: ""

session_status: ""
scope_result: ""
verification_result: ""
evidence_report_result: ""

acceptance_criteria_status: ""
changed_files_status: ""

human_review_required: false
human_review_status: ""

critical_evidence_gaps: []

notes: ""

created_at: ""
created_by: completion-readiness-gate
```

## Required Gates

```yaml
required_gates:
  active_task_exists: NOT RUN
  execution_session_exists: NOT RUN
  session_status_evidence_ready: NOT RUN
  session_status_not_in_progress: NOT RUN
  session_status_not_blocked: NOT RUN
  session_status_not_failed: NOT RUN
  scope_check_pass: NOT RUN
  verification_runner_pass: NOT RUN
  execution_evidence_report_pass: NOT RUN
  source_contract_exists: NOT RUN
  acceptance_criteria_present: NOT RUN
  changed_files_known: NOT RUN
  human_review_satisfied_if_required: NOT RUN
```

## Evidence Inputs

```yaml
evidence_inputs:
  active_task: ""
  execution_session: ""
  scope_check: ""
  verification_runner: ""
  execution_evidence_report: ""
  source_contract: ""
  changed_files: []
```

## Critical Evidence Gaps

- NONE

## Notes

- Completion readiness does not complete the task.
- Completion readiness does not apply lifecycle transition.
- Completion readiness PASS only allows future completion transition preparation.
- blocked and failed session statuses both produce FAIL in M14.
