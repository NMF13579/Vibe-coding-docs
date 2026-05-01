---
task_id: task-fixture-approval-enforcement
transition_id: transition-fixture-approval-enforcement
target_state: completed
operation: complete-active
allowed_operation: complete-active
allowed_target_state: completed
approval_required: true
result: COMPLETE_ACTIVE_PLAN_READY
completion_destination: __TO_BE_REPLACED__
completion_operation: copy_active_task_to_completion_destination_and_mark_active_task_completed
allowed_task_paths:
  - tasks/active-task.md
  - __TO_BE_REPLACED_DONE__
would_mutate: true
---
