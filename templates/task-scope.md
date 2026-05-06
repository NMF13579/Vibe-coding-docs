---
type: template
module: m23
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Task Scope Template

## Purpose
This template defines a reusable machine-readable `scope_control` block for task contracts. It helps describe where changes are allowed and where changes are forbidden.

## Usage
Use this template in tasks that modify files and need explicit scope boundaries. Fill paths and booleans for the specific task before execution.

## Scope Control Block
```yaml
scope_control:
  allowed_paths:
    - docs/example.md
  forbidden_paths:
    - scripts/run-all.sh
    - .github/
  allow_new_files: true
  allowed_new_files:
    - docs/
  forbidden_new_files:
    - scripts/
    - .github/
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/
    - .github/
    - templates/
    - data/
    - schemas/
```

## Field Definitions
- `allowed_paths`: allowed file or directory patterns for changes.
- `forbidden_paths`: forbidden file or directory patterns for any change.
- `allow_new_files`: boolean permission to create new files.
- `allowed_new_files`: allowed path patterns for new files.
- `forbidden_new_files`: forbidden path patterns for new files.
- `allow_modify_existing`: boolean permission to modify existing files.
- `allow_deletes`: boolean permission to delete files.
- `allow_renames`: boolean permission to rename files.
- `sensitive_paths`: paths that require extra human review when changed.

Distinction rules:
- `allow_new_files` = boolean permission to create new files.
- `allowed_new_files` = allowed path patterns for new files.
- `forbidden_new_files` = forbidden path patterns for new files.

## Default Safety Rules
- Empty `allowed_paths` is invalid unless the task explicitly documents why no file changes are expected.
- Missing scope_control is invalid for tasks that modify files.
- Forbidden paths override allowed paths.
- Sensitive paths require human review when changed.
- Deletes are forbidden unless `allow_deletes` is true.
- Renames are forbidden unless `allow_renames` is true.
- New files are forbidden unless `allow_new_files` is true.
- NOT_RUN is not PASS.

## Valid Example
```yaml
scope_control:
  allowed_paths:
    - templates/task-scope.md
  forbidden_paths:
    - scripts/
  allow_new_files: true
  allowed_new_files:
    - templates/
  forbidden_new_files:
    - scripts/
  allow_modify_existing: false
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/
    - .github/
```

## Invalid Example
```yaml
scope_control:
  allowed_paths: []
  forbidden_paths:
    - templates/
  allow_new_files: false
  allowed_new_files:
    - templates/
  forbidden_new_files: []
  allow_modify_existing: true
  allow_deletes: true
  allow_renames: true
  sensitive_paths: []
```

Invalid reasons in this example:
- `allowed_paths` is empty without documented exception.
- `allow_new_files` is false while `allowed_new_files` is provided as if new files are allowed.
- delete and rename permissions are enabled without explicit scope justification.

## Human Review Rules
- A scope violation requires human review.
- Changes to `sensitive_paths` require human review.
- FAIL blocks acceptance unless a human explicitly overrides.
- PASS does not prove implementation correctness.

## Non-Authority Boundaries
Unsafe claims that are rejected:
- scope_control approves task completion
- scope_control proves correctness
- scope_control replaces human review
- scope_control authorizes sensitive changes automatically
- PASS means the implementation is correct

This template does not approve completion and does not replace human review.
