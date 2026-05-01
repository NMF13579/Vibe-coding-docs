# Operation Risk Model

## Purpose
This document defines the canonical classification of operation risk classes
used across AgentOS lifecycle scripts and validators.

## Risk Classes

### READ_ONLY
- reads files, metadata, logs
- does not write to any path
- does not mutate lifecycle state

### VALIDATION
- runs validators and reports PASS/WARN/FAIL
- does not mutate lifecycle state
- validation output is not approval

### AUDIT
- reads existing artifacts and reports findings
- does not authorize execution
- audit PASS is not approval

### PLAN
- creates non-authorizing planning artifacts
- does not mutate lifecycle state
- does not authorize execution

### DRY_RUN
- simulation-only actions within temp workspace or stdout
- safe when: no writes to real repository state, no irreversible commands
- unsafe when: writes to real state or invokes irreversible commands

### TEMP_WORKSPACE_MUTATION
- mutates only temp workspace paths
- safe when: temp_workspace_isolated=true AND cleanup_performed=true
- unsafe when: overlaps with real repository paths or missing cleanup

### REAL_LIFECYCLE_MUTATION
- mutates real lifecycle paths (tasks/, reports/, docs/)
- requires explicit valid approval when approval_required=true
- supported operations only

### UNSUPPORTED_MUTATION
- mutation path or operation not supported by AgentOS
- valid approval cannot convert to supported mutation
- always blocked

### FORBIDDEN_MUTATION
- destructive or irreversible forbidden operations
- valid approval cannot authorize
- always blocked

## Classification Rules
- risk class is determined before policy evaluation
- risk class is determined before approval validation
- risk class must be declared explicitly in operation context
- reclassification is allowed only via canonical mapping in APPROVAL-REQUIREMENT-POLICY.md
