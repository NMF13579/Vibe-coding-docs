# Approval Requirement Policy

## Purpose
This document defines the canonical policy that decides whether approval is required, not required, not applicable, unsupported, or forbidden for each operation risk class.

Core rule:

policy decides whether an operation is approvable before approval evidence is checked

## Policy Evaluation Order
- approval policy is evaluated after operation risk classification
- approval policy is evaluated before approval record validation
- approval policy does not create approval evidence
- approval policy does not mutate lifecycle state
- approval policy does not replace preconditions
- approval policy does not replace validation
- approval policy does not replace audit

## Policy Results
Allowed policy results:
- APPROVAL_NOT_REQUIRED
- APPROVAL_REQUIRED
- APPROVAL_NOT_APPLICABLE
- BLOCKED_UNSUPPORTED
- BLOCKED_FORBIDDEN

Optional approval result is not used in this policy.

## Canonical Mapping
- READ_ONLY → APPROVAL_NOT_REQUIRED
- VALIDATION → APPROVAL_NOT_REQUIRED
- AUDIT → APPROVAL_NOT_APPLICABLE
- PLAN → APPROVAL_NOT_REQUIRED
- safe DRY_RUN → APPROVAL_NOT_REQUIRED
- claimed DRY_RUN that writes to real repository state → reclassify as REAL_LIFECYCLE_MUTATION if supported, otherwise BLOCKED_UNSUPPORTED
- claimed DRY_RUN that invokes irreversible commands → BLOCKED_FORBIDDEN or BLOCKED_UNSUPPORTED
- TEMP_WORKSPACE_MUTATION when isolated and protected → APPROVAL_NOT_REQUIRED
- TEMP_WORKSPACE_MUTATION when isolation is not guaranteed → BLOCKED_UNSUPPORTED
- REAL_LIFECYCLE_MUTATION → APPROVAL_REQUIRED
- UNSUPPORTED_MUTATION → BLOCKED_UNSUPPORTED
- FORBIDDEN_MUTATION → BLOCKED_FORBIDDEN

## Definitions
- a DRY_RUN is safe when it does not write to real repository state, does not invoke irreversible commands, and operates only within temp workspace or stdout
- a claimed DRY_RUN that writes to real repository state is not treated as safe DRY_RUN
- a claimed DRY_RUN that invokes irreversible commands is not treated as safe DRY_RUN
- isolation is not guaranteed when the temp workspace path overlaps with a real repository path, or when cleanup is not performed after the operation
- PLAN may create non-authorizing planning artifacts, but it does not mutate lifecycle state and does not authorize execution
- AUDIT reads existing evidence and reports findings; it does not authorize execution

## Risk Class Policies

### READ_ONLY
- approval requirement: not required
- policy result: APPROVAL_NOT_REQUIRED
- allowed behavior: read files, inspect metadata, collect context
- blocked behavior: none from approval policy alone
- examples: reading docs, reading logs, listing files
- notes: no lifecycle mutation

### VALIDATION
- approval requirement: not required
- policy result: APPROVAL_NOT_REQUIRED
- allowed behavior: run validators, report PASS/WARN/FAIL
- blocked behavior: validation must not mutate lifecycle state
- examples: schema checks, frontmatter checks, consistency checks
- notes: validation output is not approval

### AUDIT
- approval requirement: not applicable
- policy result: APPROVAL_NOT_APPLICABLE
- allowed behavior: read existing artifacts and report findings
- blocked behavior: audit must not authorize execution
- examples: boundary audits, evidence audits
- notes: audit PASS is not approval

### PLAN
- approval requirement: not required
- policy result: APPROVAL_NOT_REQUIRED
- allowed behavior: create non-authorizing planning artifacts
- blocked behavior: no lifecycle mutation and no execution authorization
- examples: plan drafts, operation planning notes
- notes: planning output is not approval

### DRY_RUN
- approval requirement: depends on safe classification
- policy result: APPROVAL_NOT_REQUIRED for safe DRY_RUN
- allowed behavior: simulation-only actions within temp workspace or stdout
- blocked behavior: writes to real repository state or irreversible execution under claimed dry-run
- examples: read-only simulation, dry-run reporting
- notes: unsafe claimed dry-run must be reclassified or blocked according to canonical mapping

### TEMP_WORKSPACE_MUTATION
- approval requirement: not required only when isolation is guaranteed
- policy result: APPROVAL_NOT_REQUIRED when isolated and protected; BLOCKED_UNSUPPORTED when isolation is not guaranteed
- allowed behavior: mutate only temp workspace paths with cleanup
- blocked behavior: overlap with real repository paths or missing cleanup guarantees
- examples: fixture generation in temp directory, isolated smoke mutation
- notes: isolation failure blocks operation

### REAL_LIFECYCLE_MUTATION
- approval requirement: required
- policy result: APPROVAL_REQUIRED
- allowed behavior: supported lifecycle mutation with explicit valid approval and all required gates
- blocked behavior: missing approval when approval is required
- examples: supported complete-active mutation on real lifecycle paths
- notes: approval check is required by policy before approval validation gate outcome is consumed

### UNSUPPORTED_MUTATION
- approval requirement: ignored
- policy result: BLOCKED_UNSUPPORTED
- allowed behavior: none
- blocked behavior: all unsupported mutation paths
- examples: unsupported lifecycle states or unsupported operations
- notes: valid approval cannot convert UNSUPPORTED_MUTATION into supported mutation

### FORBIDDEN_MUTATION
- approval requirement: ignored
- policy result: BLOCKED_FORBIDDEN
- allowed behavior: none
- blocked behavior: forbidden operations and irreversible forbidden paths
- examples: destructive forbidden operations on protected boundaries
- notes: valid approval cannot authorize FORBIDDEN_MUTATION

## Approval Boundary Rules
- approval is required only when policy says APPROVAL_REQUIRED
- approval is ignored when policy says BLOCKED_UNSUPPORTED
- approval is ignored when policy says BLOCKED_FORBIDDEN
- valid approval cannot convert UNSUPPORTED_MUTATION into supported mutation
- valid approval cannot authorize FORBIDDEN_MUTATION
- valid approval cannot authorize unsupported target states
- valid approval cannot authorize a claimed DRY_RUN that writes to real repository state unless it has been reclassified as a supported REAL_LIFECYCLE_MUTATION
- missing approval blocks REAL_LIFECYCLE_MUTATION when approval is required
- approval is never inferred from conversation text
- approval is never inferred from command success
- approval is never inferred from validation PASS
- approval is never inferred from audit PASS

## Non-Goals
- no policy enforcement in code
- no policy validator
- no fixture creation
- no apply preconditions implementation changes
- no controlled apply behavior changes
- no redefinition of operation risk model
- no redefinition of M17 approval evidence model
