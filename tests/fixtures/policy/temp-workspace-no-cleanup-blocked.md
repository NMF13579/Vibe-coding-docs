---
policy_case_id: temp-workspace-no-cleanup-blocked
operation_name: temp-workspace-write-no-cleanup
risk_class: TEMP_WORKSPACE_MUTATION
writes_real_repository_state: false
invokes_irreversible_command: false
temp_workspace_isolated: true
cleanup_performed: false
supported_operation: true
target_state_supported: true
expected_policy_result: BLOCKED_UNSUPPORTED
expected_policy_decision: BLOCKED
---
# Temp Workspace No Cleanup Blocked
