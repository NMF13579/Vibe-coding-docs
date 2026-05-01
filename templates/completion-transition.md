---
transition_id: completion-<task-id>-<timestamp>
task_id: <task-id>
session_id: <execution-session-id>
transition_type: complete
status: blocked
source_task: tasks/active-task.md
source_contract: <path-or-missing>
execution_session: <path-or-missing>
completion_readiness: <path-or-stdout-reference>
evidence_report: <path-or-missing>
completion_readiness_result: NOT RUN
stop_reason: ""
scope_result: NOT RUN
verification_result: NOT RUN
evidence_report_result: NOT RUN
changed_files: []
required_gates:
  active_task_exists: NOT RUN
  execution_session_exists: NOT RUN
  session_status_not_failed: NOT RUN
  session_status_evidence_ready: NOT RUN
  session_status_not_in_progress: NOT RUN
  session_status_not_blocked: NOT RUN
  scope_check_pass: NOT RUN
  verification_runner_pass: NOT RUN
  execution_evidence_report_pass: NOT RUN
  source_contract_exists: NOT RUN
  acceptance_criteria_present: NOT RUN
  changed_files_known: NOT RUN
  human_review_satisfied_if_required: NOT RUN
safety_checks:
  active_task_mutated: NO
  queue_mutated: NO
  task_moved_to_done: NO
  completion_applied: NO
  approval_created: NO
  transition_status_applied: NO
created_at: ""
created_by: controlled-completion-gate
---

## Notes

- This record is evidence only.
- This record does not complete the task.
- This record does not apply lifecycle transition.
- status: applied is forbidden in M14 and reserved for M15 only.
- status: prepared means future M15 application may be considered.
- status: blocked means completion must not proceed.
- Template defaults are intentionally in the safest blocked/NOT RUN state. Never create a template with PASS defaults.
