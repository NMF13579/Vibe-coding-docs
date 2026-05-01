---
policy_case_id: read-only-pass
operation_name: read-task-state
risk_class: READ_ONLY
writes_real_repository_state: false
invokes_irreversible_command: false
temp_workspace_isolated: false
cleanup_performed: false
supported_operation: true
target_state_supported: true
expected_policy_result: APPROVAL_NOT_REQUIRED
expected_policy_decision: PASS
---
# Read-Only Pass

READ_ONLY operations require no approval.
PASS here means: operation is allowed to proceed without approval validation.
