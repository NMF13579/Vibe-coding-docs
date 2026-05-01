---
policy_case_id: real-lifecycle-approval-required-pass
operation_name: apply-lifecycle-transition
risk_class: REAL_LIFECYCLE_MUTATION
writes_real_repository_state: true
invokes_irreversible_command: false
temp_workspace_isolated: false
cleanup_performed: false
supported_operation: true
target_state_supported: true
expected_policy_result: APPROVAL_REQUIRED
expected_policy_decision: PASS
---
# Real Lifecycle Mutation - Approval Required

REAL_LIFECYCLE_MUTATION with supported operation and supported target state requires approval.
PASS here means: operation may proceed to the approval validation step.
PASS does NOT mean approval evidence exists or has been validated.
This validator does not check whether approval evidence exists.
