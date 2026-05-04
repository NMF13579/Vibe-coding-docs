# Duplicate File Audit

## Executive Summary

- Найдено подозрительных дублей по шаблону `* 2.md`/`* 2.py`: **890**.
- Файловых имён, повторяющихся в разных каталогах (`*.md`/`*.py`): **195**.
- Наиболее затронутые каталоги: `scripts` (73), `reports` (39), `docs` (32), `tests/fixtures/human-approval` (32), `templates/agentos-full/scripts` (15), `tests/fixtures/contract-validator/invalid` (14), `tests/fixtures/negative/contract-draft` (14), `templates` (10), `tests/fixtures/approval-flow-smoke` (10), `tests/fixtures/negative/queue` (10)
- Общий риск: HIGH (массовые дубли в `docs/`, `scripts/`, `tasks/`, `reports/`).

## Duplicate File Inventory

Команда 1: `find . -type f \( -name "* 2.md" -o -name "* 2.py" \) | sort`

- `./.github/pull_request_template 2.md`
- `./CHANGELOG 2.md`
- `./INIT 2.md`
- `./RELEASE-CHECKLIST 2.md`
- `./ROUTES-REGISTRY 2.md`
- `./approvals/approval-task-20260426-brief-readiness-check-execution 2.md`
- `./architecture/CANON 2.md`
- `./architecture/MAIN 2.md`
- `./architecture/OPERATING-RULES 2.md`
- `./core-rules/MAIN 2.md`
- `./docs/ACTIVATION-RECOVERY 2.md`
- `./docs/ACTIVE-TASK-FORMAT 2.md`
- `./docs/ACTIVE-TASK-VALIDATION 2.md`
- `./docs/APPLIED-TRANSITION-RECORD 2.md`
- `./docs/APPLY-COMMAND-INTEGRATION 2.md`
- `./docs/APPLY-PLAN 2.md`
- `./docs/APPLY-PRECONDITIONS 2.md`
- `./docs/APPROVAL-EVIDENCE-STORAGE 2.md`
- `./docs/APPROVAL-MARKER-SPEC 2.md`
- `./docs/APPROVAL-REQUIREMENT-POLICY 2.md`
- `./docs/APPROVED-MODE-CONTRACT 2.md`
- `./docs/COMPLETION-READINESS 2.md`
- `./docs/COMPLETION-TRANSITION 2.md`
- `./docs/CONTROLLED-COMPLETION 2.md`
- `./docs/CONTROLLED-COMPLETION-WORKFLOW 2.md`
- `./docs/CONTROLLED-EXECUTION-RUNNER 2.md`
- `./docs/CONTROLLED-FAILURE-AND-REVIEW 2.md`
- `./docs/CONTROLLED-LIFECYCLE-MUTATION 2.md`
- `./docs/EXECUTION-READINESS 2.md`
- `./docs/EXECUTION-SESSION 2.md`
- `./docs/GETTING-STARTED 2.md`
- `./docs/HUMAN-APPROVAL-BOUNDARY 2.md`
- `./docs/HUMAN-APPROVAL-EVIDENCE 2.md`
- `./docs/LIFECYCLE-INTEGRATION 2.md`
- `./docs/OPERATION-RISK-MODEL 2.md`
- `./docs/SAFE-TRANSITION-EXECUTION 2.md`
- `./docs/SAFETY-BOUNDARIES 2.md`
- `./docs/TASK-STATE-MACHINE 2.md`
- `./docs/TASK-TRANSITION-RULES 2.md`
- `./docs/VALIDATION 2.md`
- `./docs/quickstart 2.md`
- `./docs/usage 2.md`
- `./examples/README 2.md`
- `./examples/queue-entry-example 2.md`
- `./examples/scenario-01-new-feature 2.md`
- `./examples/scenario-02-bugfix 2.md`
- `./examples/scenario-03-refactor 2.md`
- `./examples/scenario-04-validation-only 2.md`
- `./examples/simple-project/README 2.md`
- `./examples/simple-project/app 2.py`
- `./handoff/HANDOFF 2.md`
- `./handoff/templates/session-summary 2.md`
- `./incidents/templates/incident 2.md`
- `./lessons/lessons 2.md`
- `./lessons/templates/lesson-entry 2.md`
- `./prompt-packs/README 2.md`
- `./prompt-packs/chatgpt 2.md`
- `./prompt-packs/claude-code 2.md`
- `./prompt-packs/codex-cli 2.md`
- `./prompt-packs/cursor 2.md`
- `./quality/MAIN 2.md`
- `./repo-map 2.md`
- `./reports/activation-audit-report 2.md`
- `./reports/activation-positive-smoke 2.md`
- `./reports/active-task-governance-audit-report 2.md`
- `./reports/agentos-validate-cli-hardening 2.md`
- `./reports/agentos-validate-json-smoke 2.md`
- `./reports/agentos-validate-smoke 2.md`
- `./reports/agentos-validate-usage-integration 2.md`
- `./reports/audit 2.md`
- `./reports/audit-smoke 2.md`
- `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z 2.md`
- `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023 2.md`
- `./reports/execution-evidence-report 2.md`
- `./reports/guard-failures-smoke 2.md`
- `./reports/milestone-10-completion-review 2.md`
- `./reports/milestone-10-final-hardening-review 2.md`
- `./reports/milestone-10.11-state-report-hardening 2.md`
- `./reports/milestone-10.11.1-approval-marker-spec 2.md`
- `./reports/milestone-10.11.2-v1.1-hardening 2.md`
- `./reports/milestone-10.12-downstream-v1.1-compatibility 2.md`
- `./reports/milestone-10.13-state-analysis-separation 2.md`
- `./reports/milestone-11-completion-review 2.md`
- `./reports/milestone-12-completion-review 2.md`
- `./reports/milestone-13-completion-review 2.md`
- `./reports/milestone-14-completion-review 2.md`
- `./reports/milestone-14-evidence-report 2.md`
- `./reports/milestone-15-completion-review 2.md`
- `./reports/milestone-15-evidence-report 2.md`
- `./reports/milestone-16-completion-review 2.md`
- `./reports/milestone-16-evidence-report 2.md`
- `./reports/milestone-17-completion-review 2.md`
- `./reports/milestone-17-evidence-report 2.md`
- `./reports/milestone-18-completion-review 2.md`
- `./reports/milestone-18-evidence-report 2.md`
- `./reports/milestone-7.1-handoff 2.md`
- `./reports/negative-fixtures-smoke 2.md`
- `./reports/pre-execution-evidence-report 2.md`
- `./reports/release-checklist 2.md`
- `./reports/session-handoff 2.md`
- `./reports/task-health 2.md`
- `./reports/task-state-machine-smoke 2.md`
- `./reports/templates/verification-report 2.md`
- `./reports/verification 2.md`
- `./scripts/VALIDATORS 2.md`
- `./scripts/activate-task 2.py`
- `./scripts/agent-complete 2.py`
- `./scripts/agent-fail 2.py`
- `./scripts/agent-next 2.py`
- `./scripts/agentos-validate 2.py`
- `./scripts/apply-transition 2.py`
- `./scripts/audit-agentos 2.py`
- `./scripts/audit-approval-boundary 2.py`
- `./scripts/audit-gate-contract 2.py`
- `./scripts/audit-lifecycle-mutation 2.py`
- `./scripts/audit-policy-boundary 2.py`
- `./scripts/audit-release-readiness 2.py`
- `./scripts/check-apply-preconditions 2.py`
- `./scripts/check-completion-readiness 2.py`
- `./scripts/check-dangerous-commands 2.py`
- `./scripts/check-execution-readiness 2.py`
- `./scripts/check-execution-scope 2.py`
- `./scripts/check-links 2.py`
- `./scripts/check-pr-quality 2.py`
- `./scripts/check-risk 2.py`
- `./scripts/check-template-integrity 2.py`
- `./scripts/check-transition 2.py`
- `./scripts/complete-active-task 2.py`
- `./scripts/detect-task-state 2.py`
- `./scripts/generate-repo-map 2.py`
- `./scripts/generate-task-contract 2.py`
- `./scripts/lib/__init__ 2.py`
- `./scripts/lib/path_utils 2.py`
- `./scripts/run-active-task 2.py`
- `./scripts/run-execution-verification 2.py`
- `./scripts/select-context 2.py`
- `./scripts/task-health 2.py`
- `./scripts/test-activation-fixtures 2.py`
- `./scripts/test-active-task-fixtures 2.py`
- `./scripts/test-apply-transition-fixtures 2.py`
- `./scripts/test-approval-fixtures 2.py`
- `./scripts/test-approval-flow-smoke 2.py`
- `./scripts/test-approval-marker-fixtures 2.py`
- `./scripts/test-completion-flow-smoke 2.py`
- `./scripts/test-execution-runner-fixtures 2.py`
- `./scripts/test-gate-regression-fixtures 2.py`
- `./scripts/test-guard-failures 2.py`
- `./scripts/test-human-approval-fixtures 2.py`
- `./scripts/test-negative-fixtures 2.py`
- `./scripts/test-policy-enforcement-fixtures 2.py`
- `./scripts/test-policy-fixtures 2.py`
- `./scripts/test-policy-flow-smoke 2.py`
- `./scripts/test-readiness-fixtures 2.py`
- `./scripts/test-state-fixtures 2.py`
- `./scripts/test-template-integrity 2.py`
- `./scripts/test-template-integrity-fixtures 2.py`
- `./scripts/test-unified-gate-smoke 2.py`
- `./scripts/validate-active-task 2.py`
- `./scripts/validate-approval-marker 2.py`
- `./scripts/validate-commit-msg 2.py`
- `./scripts/validate-contract-draft 2.py`
- `./scripts/validate-docs 2.py`
- `./scripts/validate-gate-contract 2.py`
- `./scripts/validate-handoff 2.py`
- `./scripts/validate-human-approval 2.py`
- `./scripts/validate-incident 2.py`
- `./scripts/validate-lessons 2.py`
- `./scripts/validate-lifecycle-apply 2.py`
- `./scripts/validate-policy 2.py`
- `./scripts/validate-queue 2.py`
- `./scripts/validate-queue-entry 2.py`
- `./scripts/validate-review 2.py`
- `./scripts/validate-route 2.py`
- `./scripts/validate-runner-protocol 2.py`
- `./scripts/validate-task 2.py`
- `./scripts/validate-task-brief 2.py`
- `./scripts/validate-task-state 2.py`
- `./scripts/validate-trace 2.py`
- `./scripts/validate-verification 2.py`
- `./security/MAIN 2.md`
- `./stages/spec-wizard/BOOT 2.md`
- `./state/MAIN 2.md`
- `./tasks/active-task 2.md`
- `./tasks/queue/20260428-queue-schema-check 2.md`
- `./tasks/queue/20260428-runner-human-checkpoints 2.md`
- `./tasks/queue/QUEUE 2.md`
- `./tasks/task-20260426-brief-readiness-check/REVIEW 2.md`
- `./tasks/task-20260426-brief-readiness-check/TASK 2.md`
- `./tasks/task-20260426-brief-readiness-check/TRACE 2.md`
- `./tasks/task-20260426-brief-to-contract-manual-guide/TASK 2.md`
- `./tasks/templates/task-contract 2.md`
- `./templates/agentos-full/.github/copilot-instructions 2.md`
- `./templates/agentos-full/.github/instructions/backend.instructions 2.md`
- `./templates/agentos-full/.github/instructions/frontend.instructions 2.md`
- `./templates/agentos-full/.github/pull_request_template 2.md`
- `./templates/agentos-full/handoff/HANDOFF 2.md`
- `./templates/agentos-full/handoff/templates/session-summary 2.md`
- `./templates/agentos-full/incidents/templates/incident 2.md`
- `./templates/agentos-full/lessons/lessons 2.md`
- `./templates/agentos-full/lessons/templates/lesson-entry 2.md`
- `./templates/agentos-full/repo-map 2.md`
- `./templates/agentos-full/reports/templates/verification-report 2.md`
- `./templates/agentos-full/reports/verification 2.md`
- `./templates/agentos-full/scripts/VALIDATORS 2.md`
- `./templates/agentos-full/scripts/check-dangerous-commands 2.py`
- `./templates/agentos-full/scripts/check-links 2.py`
- `./templates/agentos-full/scripts/check-pr-quality 2.py`
- `./templates/agentos-full/scripts/check-risk 2.py`
- `./templates/agentos-full/scripts/generate-repo-map 2.py`
- `./templates/agentos-full/scripts/select-context 2.py`
- `./templates/agentos-full/scripts/validate-commit-msg 2.py`
- `./templates/agentos-full/scripts/validate-docs 2.py`
- `./templates/agentos-full/scripts/validate-handoff 2.py`
- `./templates/agentos-full/scripts/validate-incident 2.py`
- `./templates/agentos-full/scripts/validate-lessons 2.py`
- `./templates/agentos-full/scripts/validate-route 2.py`
- `./templates/agentos-full/scripts/validate-task 2.py`
- `./templates/agentos-full/scripts/validate-verification 2.py`
- `./templates/agentos-full/tasks/active-task 2.md`
- `./templates/agentos-full/tasks/templates/task-contract 2.md`
- `./templates/agentos-minimal/reports/templates/verification-report 2.md`
- `./templates/agentos-minimal/reports/verification 2.md`
- `./templates/agentos-minimal/scripts/validate-task 2.py`
- `./templates/agentos-minimal/scripts/validate-verification 2.py`
- `./templates/agentos-minimal/tasks/active-task 2.md`
- `./templates/agentos-minimal/tasks/templates/task-contract 2.md`
- `./templates/applied-transition-record 2.md`
- `./templates/apply-plan 2.md`
- `./templates/candidate-tasks 2.md`
- `./templates/commit-message 2.md`
- `./templates/completion-readiness 2.md`
- `./templates/completion-transition 2.md`
- `./templates/execution-session 2.md`
- `./templates/human-approval-record 2.md`
- `./templates/queue-entry 2.md`
- `./templates/task-brief-review 2.md`
- `./tests/fixtures/agent-runner/drafts/high-ready-contract-draft 2.md`
- `./tests/fixtures/agent-runner/queue/high-ready 2.md`
- `./tests/fixtures/agent-runner/queue/normal-blocked 2.md`
- `./tests/fixtures/apply-preconditions-approval/active-task 2.md`
- `./tests/fixtures/apply-preconditions-approval/approval-not-required-transition 2.md`
- `./tests/fixtures/apply-preconditions-approval/approval-required-transition 2.md`
- `./tests/fixtures/apply-preconditions-approval/invalid-vague-approval 2.md`
- `./tests/fixtures/apply-preconditions-approval/readiness-evidence 2.md`
- `./tests/fixtures/apply-preconditions-approval/task-mismatch-approval 2.md`
- `./tests/fixtures/apply-preconditions-approval/valid-approval 2.md`
- `./tests/fixtures/apply-preconditions-approval/verification-evidence 2.md`
- `./tests/fixtures/apply-transition/README 2.md`
- `./tests/fixtures/approval-enforcement/approval-not-required-transition 2.md`
- `./tests/fixtures/approval-enforcement/approval-required-mutation-plan 2.md`
- `./tests/fixtures/approval-enforcement/approval-required-transition 2.md`
- `./tests/fixtures/approval-enforcement/invalid-vague-approval 2.md`
- `./tests/fixtures/approval-enforcement/task-mismatch-approval 2.md`
- `./tests/fixtures/approval-enforcement/transition-mismatch-approval 2.md`
- `./tests/fixtures/approval-enforcement/unsupported-operation-approval 2.md`
- `./tests/fixtures/approval-enforcement/unsupported-target-state-approval 2.md`
- `./tests/fixtures/approval-enforcement/valid-approval 2.md`
- `./tests/fixtures/approval-flow-smoke/README 2.md`
- `./tests/fixtures/approval-flow-smoke/invalid-vague-approval 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-applied-transition-record 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-apply-plan 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-mutation-plan 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-readiness 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-task 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-transition 2.md`
- `./tests/fixtures/approval-flow-smoke/synthetic-verification 2.md`
- `./tests/fixtures/approval-flow-smoke/valid-approval 2.md`
- `./tests/fixtures/completion-flow-smoke/README 2.md`
- `./tests/fixtures/completion-flow-smoke/active-task 2.md`
- `./tests/fixtures/completion-flow-smoke/completion-readiness-evidence 2.md`
- `./tests/fixtures/completion-flow-smoke/prepared-transition 2.md`
- `./tests/fixtures/completion-flow-smoke/reports/execution/session-smoke 2.md`
- `./tests/fixtures/completion-flow-smoke/reports/execution-evidence-report 2.md`
- `./tests/fixtures/completion-flow-smoke/tasks-active-task 2.md`
- `./tests/fixtures/completion-flow-smoke/transition-smoke 2.md`
- `./tests/fixtures/completion-flow-smoke/verification-evidence 2.md`
- `./tests/fixtures/contract-generation/blocked-task/REVIEW 2.md`
- `./tests/fixtures/contract-generation/blocked-task/TASK 2.md`
- `./tests/fixtures/contract-generation/missing-review/TASK 2.md`
- `./tests/fixtures/contract-generation/ready-task/REVIEW 2.md`
- `./tests/fixtures/contract-generation/ready-task/TASK 2.md`
- `./tests/fixtures/contract-validator/invalid/blocked-review-status 2.md`
- `./tests/fixtures/contract-validator/invalid/execution-allowed-false 2.md`
- `./tests/fixtures/contract-validator/invalid/execution-approved 2.md`
- `./tests/fixtures/contract-validator/invalid/invalid-execution-allowed 2.md`
- `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-close 2.md`
- `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-open 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-execution-allowed 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-generated-from-task 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-review-file 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-review-status 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-risk-section 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-task-id 2.md`
- `./tests/fixtures/contract-validator/invalid/missing-verification-section 2.md`
- `./tests/fixtures/contract-validator/invalid/replaces-active-task 2.md`
- `./tests/fixtures/contract-validator/valid/ready-contract-draft 2.md`
- `./tests/fixtures/contract-validator/valid/ready-with-edits-contract-draft 2.md`
- `./tests/fixtures/human-approval/invalid-approval-id-operation-mismatch 2.md`
- `./tests/fixtures/human-approval/invalid-approval-id-task-mismatch 2.md`
- `./tests/fixtures/human-approval/invalid-approval-status-invalid 2.md`
- `./tests/fixtures/human-approval/invalid-approved-at-format 2.md`
- `./tests/fixtures/human-approval/invalid-approved-by-agent 2.md`
- `./tests/fixtures/human-approval/invalid-approved-by-openai-exact 2.md`
- `./tests/fixtures/human-approval/invalid-bypass-preconditions 2.md`
- `./tests/fixtures/human-approval/invalid-expired-status 2.md`
- `./tests/fixtures/human-approval/invalid-expires-at-format 2.md`
- `./tests/fixtures/human-approval/invalid-generic-scope-all 2.md`
- `./tests/fixtures/human-approval/invalid-missing-approval-scope 2.md`
- `./tests/fixtures/human-approval/invalid-missing-related-task-id 2.md`
- `./tests/fixtures/human-approval/invalid-missing-related-transition-id 2.md`
- `./tests/fixtures/human-approval/invalid-missing-required-field 2.md`
- `./tests/fixtures/human-approval/invalid-nested-yaml 2.md`
- `./tests/fixtures/human-approval/invalid-related-task-id-format 2.md`
- `./tests/fixtures/human-approval/invalid-related-transition-id-format 2.md`
- `./tests/fixtures/human-approval/invalid-revoked-status 2.md`
- `./tests/fixtures/human-approval/invalid-statement-missing-operation-reference 2.md`
- `./tests/fixtures/human-approval/invalid-statement-missing-target-state-reference 2.md`
- `./tests/fixtures/human-approval/invalid-statement-missing-task-reference 2.md`
- `./tests/fixtures/human-approval/invalid-statement-missing-transition-reference 2.md`
- `./tests/fixtures/human-approval/invalid-superseded-status 2.md`
- `./tests/fixtures/human-approval/invalid-supersedes-format 2.md`
- `./tests/fixtures/human-approval/invalid-unknown-approval-source 2.md`
- `./tests/fixtures/human-approval/invalid-unknown-status 2.md`
- `./tests/fixtures/human-approval/invalid-unsupported-operation 2.md`
- `./tests/fixtures/human-approval/invalid-unsupported-target-state 2.md`
- `./tests/fixtures/human-approval/invalid-vague-approval 2.md`
- `./tests/fixtures/human-approval/invalid-vague-continue 2.md`
- `./tests/fixtures/human-approval/valid-approved-by-openai-substring 2.md`
- `./tests/fixtures/human-approval/valid-complete-active 2.md`
- `./tests/fixtures/negative/README 2.md`
- `./tests/fixtures/negative/activation/active-task-different-task/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/active-task-different-task/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/active-task-different-task/task/TASK 2.md`
- `./tests/fixtures/negative/activation/active-task-different-task/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/analysis-status-conflict/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/analysis-status-conflict/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/analysis-status-conflict/task/TASK 2.md`
- `./tests/fixtures/negative/activation/analysis-status-conflict/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/analysis-status-invalid/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/analysis-status-invalid/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/analysis-status-invalid/task/TASK 2.md`
- `./tests/fixtures/negative/activation/analysis-status-invalid/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TASK 2.md`
- `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/both-approved-and-dry-run/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TASK 2.md`
- `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/check-transition-fail/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/check-transition-fail/task/TASK 2.md`
- `./tests/fixtures/negative/activation/check-transition-fail/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/contract-missing/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/contract-missing/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/contract-missing/task/TASK 2.md`
- `./tests/fixtures/negative/activation/contract-missing/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/dry-run-does-not-write/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/dry-run-does-not-write/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TASK 2.md`
- `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/expired-approval-marker/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/expired-approval-marker/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/expired-approval-marker/task/TASK 2.md`
- `./tests/fixtures/negative/activation/expired-approval-marker/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/invalid-approval-marker/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/invalid-approval-marker/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/invalid-approval-marker/task/TASK 2.md`
- `./tests/fixtures/negative/activation/invalid-approval-marker/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/missing-approval-marker/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/missing-approval-marker/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/missing-approval-marker/task/TASK 2.md`
- `./tests/fixtures/negative/activation/missing-approval-marker/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/missing-approved-flag/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/missing-approved-flag/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/missing-approved-flag/task/TASK 2.md`
- `./tests/fixtures/negative/activation/missing-approved-flag/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/revoked-approval-marker/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/revoked-approval-marker/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/revoked-approval-marker/task/TASK 2.md`
- `./tests/fixtures/negative/activation/revoked-approval-marker/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/wrong-scope/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/wrong-scope/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/wrong-scope/task/TASK 2.md`
- `./tests/fixtures/negative/activation/wrong-scope/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/wrong-task-id/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/wrong-task-id/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/wrong-task-id/task/TASK 2.md`
- `./tests/fixtures/negative/activation/wrong-task-id/task/TRACE 2.md`
- `./tests/fixtures/negative/activation/wrong-transition/approvals/approval 2.md`
- `./tests/fixtures/negative/activation/wrong-transition/task/REVIEW 2.md`
- `./tests/fixtures/negative/activation/wrong-transition/task/TASK 2.md`
- `./tests/fixtures/negative/activation/wrong-transition/task/TRACE 2.md`
- `./tests/fixtures/negative/active-task/activated-by-unknown-value/README 2.md`
- `./tests/fixtures/negative/active-task/activated-by-unknown-value/active-task 2.md`
- `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-contract 2.md`
- `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-task 2.md`
- `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/README 2.md`
- `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/active-task 2.md`
- `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-contract 2.md`
- `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-task 2.md`
- `./tests/fixtures/negative/active-task/invalid-activated-at/README 2.md`
- `./tests/fixtures/negative/active-task/invalid-activated-at/active-task 2.md`
- `./tests/fixtures/negative/active-task/invalid-activated-at/source-contract 2.md`
- `./tests/fixtures/negative/active-task/invalid-activated-at/source-task 2.md`
- `./tests/fixtures/negative/active-task/malformed-yaml/README 2.md`
- `./tests/fixtures/negative/active-task/malformed-yaml/active-task 2.md`
- `./tests/fixtures/negative/active-task/malformed-yaml/source-contract 2.md`
- `./tests/fixtures/negative/active-task/malformed-yaml/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-at/README 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-at/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-at/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-at/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-by/README 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-by/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-by/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-activated-by/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-active-task/README 2.md`
- `./tests/fixtures/negative/active-task/missing-approval-id/README 2.md`
- `./tests/fixtures/negative/active-task/missing-approval-id/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-approval-id/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-approval-id/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-frontmatter/README 2.md`
- `./tests/fixtures/negative/active-task/missing-frontmatter/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-source-contract/README 2.md`
- `./tests/fixtures/negative/active-task/missing-source-contract/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-source-contract/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-source-contract/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-source-task/README 2.md`
- `./tests/fixtures/negative/active-task/missing-source-task/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-source-task/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-source-task/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-state/README 2.md`
- `./tests/fixtures/negative/active-task/missing-state/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-state/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-state/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-task-id/README 2.md`
- `./tests/fixtures/negative/active-task/missing-task-id/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-task-id/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-task-id/source-task 2.md`
- `./tests/fixtures/negative/active-task/missing-transition/README 2.md`
- `./tests/fixtures/negative/active-task/missing-transition/active-task 2.md`
- `./tests/fixtures/negative/active-task/missing-transition/source-contract 2.md`
- `./tests/fixtures/negative/active-task/missing-transition/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-absolute-path/README 2.md`
- `./tests/fixtures/negative/active-task/source-contract-absolute-path/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-missing/README 2.md`
- `./tests/fixtures/negative/active-task/source-contract-missing/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-missing/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-contract-missing/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-parent-traversal/README 2.md`
- `./tests/fixtures/negative/active-task/source-contract-parent-traversal/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-absolute-path/README 2.md`
- `./tests/fixtures/negative/active-task/source-task-absolute-path/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-absolute-path/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-task-absolute-path/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-missing/README 2.md`
- `./tests/fixtures/negative/active-task/source-task-missing/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-missing/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-task-missing/source-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-parent-traversal/README 2.md`
- `./tests/fixtures/negative/active-task/source-task-parent-traversal/active-task 2.md`
- `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-contract 2.md`
- `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-task 2.md`
- `./tests/fixtures/negative/active-task/state-not-active/README 2.md`
- `./tests/fixtures/negative/active-task/state-not-active/active-task 2.md`
- `./tests/fixtures/negative/active-task/state-not-active/source-contract 2.md`
- `./tests/fixtures/negative/active-task/state-not-active/source-task 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/README 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/active-task 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-contract 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-task 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/README 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/active-task 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-contract 2.md`
- `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-task 2.md`
- `./tests/fixtures/negative/active-task/wrong-transition/README 2.md`
- `./tests/fixtures/negative/active-task/wrong-transition/active-task 2.md`
- `./tests/fixtures/negative/active-task/wrong-transition/source-contract 2.md`
- `./tests/fixtures/negative/active-task/wrong-transition/source-task 2.md`
- `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval 2.md`
- `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval-duplicate 2.md`
- `./tests/fixtures/negative/approval-markers/expired-marker/approval 2.md`
- `./tests/fixtures/negative/approval-markers/invalid-transition-scope/approval 2.md`
- `./tests/fixtures/negative/approval-markers/malformed-approved-at/approval 2.md`
- `./tests/fixtures/negative/approval-markers/missing-related-contract/approval 2.md`
- `./tests/fixtures/negative/approval-markers/missing-required-field/approval 2.md`
- `./tests/fixtures/negative/approval-markers/revoked-marker/approval 2.md`
- `./tests/fixtures/negative/approval-markers/superseded-marker/approval 2.md`
- `./tests/fixtures/negative/approval-markers/wrong-scope/approval 2.md`
- `./tests/fixtures/negative/approval-markers/wrong-task-id/approval 2.md`
- `./tests/fixtures/negative/contract-draft/blocked-review-status 2.md`
- `./tests/fixtures/negative/contract-draft/execution-allowed-false 2.md`
- `./tests/fixtures/negative/contract-draft/execution-approved 2.md`
- `./tests/fixtures/negative/contract-draft/invalid-execution-allowed 2.md`
- `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-close 2.md`
- `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-open 2.md`
- `./tests/fixtures/negative/contract-draft/missing-execution-allowed 2.md`
- `./tests/fixtures/negative/contract-draft/missing-generated-from-task 2.md`
- `./tests/fixtures/negative/contract-draft/missing-review-file 2.md`
- `./tests/fixtures/negative/contract-draft/missing-review-status 2.md`
- `./tests/fixtures/negative/contract-draft/missing-risk-section 2.md`
- `./tests/fixtures/negative/contract-draft/missing-task-id 2.md`
- `./tests/fixtures/negative/contract-draft/missing-verification-section 2.md`
- `./tests/fixtures/negative/contract-draft/replaces-active-task 2.md`
- `./tests/fixtures/negative/contract-generation/draft-already-exists/README 2.md`
- `./tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft 2.md`
- `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW 2.md`
- `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK 2.md`
- `./tests/fixtures/negative/contract-generation/execution-not-allowed/README 2.md`
- `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW 2.md`
- `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK 2.md`
- `./tests/fixtures/negative/contract-generation/missing-review/README 2.md`
- `./tests/fixtures/negative/contract-generation/missing-review/task-example/TASK 2.md`
- `./tests/fixtures/negative/contract-generation/review-not-ready/README 2.md`
- `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW 2.md`
- `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-absolute-path-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/active-task 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/active-task 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/active-task 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run/README 2.md`
- `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-start/README 2.md`
- `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/README 2.md`
- `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/session 2.md`
- `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-scope/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-verification/README 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-verification/session 2.md`
- `./tests/fixtures/negative/execution-runner/blocked-session-verification/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/missing-verification-plan/README 2.md`
- `./tests/fixtures/negative/execution-runner/missing-verification-plan/session 2.md`
- `./tests/fixtures/negative/execution-runner/missing-verification-plan/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/README 2.md`
- `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/session 2.md`
- `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/session-absolute-path-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/session 2.md`
- `./tests/fixtures/negative/execution-runner/session-parent-traversal-scope/README 2.md`
- `./tests/fixtures/negative/execution-runner/session-parent-traversal-verification/README 2.md`
- `./tests/fixtures/negative/execution-runner/shared/source-task 2.md`
- `./tests/fixtures/negative/execution-runner/stopped-session-verification/README 2.md`
- `./tests/fixtures/negative/execution-runner/stopped-session-verification/session 2.md`
- `./tests/fixtures/negative/execution-runner/stopped-session-verification/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/README 2.md`
- `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/session 2.md`
- `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-absolute-executable/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-absolute-executable/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-absolute-executable/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-shell-operator/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-shell-operator/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-shell-operator/source-contract 2.md`
- `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/README 2.md`
- `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/session 2.md`
- `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/source-contract 2.md`
- `./tests/fixtures/negative/queue/blocked-by-not-list 2.md`
- `./tests/fixtures/negative/queue/blocked-with-empty-blocked-by 2.md`
- `./tests/fixtures/negative/queue/empty-task-id 2.md`
- `./tests/fixtures/negative/queue/malformed-frontmatter 2.md`
- `./tests/fixtures/negative/queue/missing-blocked-by 2.md`
- `./tests/fixtures/negative/queue/missing-priority 2.md`
- `./tests/fixtures/negative/queue/missing-status 2.md`
- `./tests/fixtures/negative/queue/missing-task-id 2.md`
- `./tests/fixtures/negative/queue/unknown-priority 2.md`
- `./tests/fixtures/negative/queue/unknown-status 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-fail/README 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-fail/active-task 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-fail/approvals/approval-active-task-validation-fail 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-fail/source-contract 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-fail/source-task 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-partial/README 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-partial/active-task 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-partial/approvals/approval-active-task-validation-partial 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-partial/source-contract 2.md`
- `./tests/fixtures/negative/readiness/active-task-validation-partial/source-task 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-conflict/README 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-conflict/active-task 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-conflict/approvals/approval-analysis-status-conflict 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-conflict/source-contract 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-conflict/source-task 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-invalid/README 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-invalid/active-task 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-invalid/approvals/approval-analysis-status-invalid 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-invalid/source-contract 2.md`
- `./tests/fixtures/negative/readiness/analysis-status-invalid/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/README 2.md`
- `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/README 2.md`
- `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-expired/README 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-expired/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-expired/approvals/approval-approval-marker-expired 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-expired/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-expired/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-invalid/README 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-invalid/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-invalid/approvals/approval-approval-marker-invalid 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-invalid/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-invalid/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-malformed/README 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-malformed/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-malformed/approvals/approval-approval-marker-malformed 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-malformed/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-malformed/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-revoked/README 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-revoked/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-revoked/approvals/approval-approval-marker-revoked 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-revoked/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-revoked/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-unresolved/README 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-unresolved/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-scope-mismatch/README 2.md`
- `./tests/fixtures/negative/readiness/approval-scope-mismatch/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-scope-mismatch/approvals/approval-approval-scope-mismatch 2.md`
- `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-task-id-mismatch/README 2.md`
- `./tests/fixtures/negative/readiness/approval-task-id-mismatch/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals/approval-approval-task-id-mismatch 2.md`
- `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-task 2.md`
- `./tests/fixtures/negative/readiness/approval-transition-mismatch/README 2.md`
- `./tests/fixtures/negative/readiness/approval-transition-mismatch/active-task 2.md`
- `./tests/fixtures/negative/readiness/approval-transition-mismatch/approvals/approval-approval-transition-mismatch 2.md`
- `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-contract 2.md`
- `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-completed/README 2.md`
- `./tests/fixtures/negative/readiness/detected-state-completed/active-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-completed/source-contract 2.md`
- `./tests/fixtures/negative/readiness/detected-state-completed/source-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-conflict/README 2.md`
- `./tests/fixtures/negative/readiness/detected-state-conflict/active-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-conflict/source-contract 2.md`
- `./tests/fixtures/negative/readiness/detected-state-conflict/source-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-dropped/README 2.md`
- `./tests/fixtures/negative/readiness/detected-state-dropped/active-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-dropped/source-contract 2.md`
- `./tests/fixtures/negative/readiness/detected-state-dropped/source-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-failed/README 2.md`
- `./tests/fixtures/negative/readiness/detected-state-failed/active-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-failed/source-contract 2.md`
- `./tests/fixtures/negative/readiness/detected-state-failed/source-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-invalid/README 2.md`
- `./tests/fixtures/negative/readiness/detected-state-invalid/active-task 2.md`
- `./tests/fixtures/negative/readiness/detected-state-invalid/source-contract 2.md`
- `./tests/fixtures/negative/readiness/detected-state-invalid/source-task 2.md`
- `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/README 2.md`
- `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/active-task 2.md`
- `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-contract 2.md`
- `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-task 2.md`
- `./tests/fixtures/negative/readiness/missing-state-validator/README 2.md`
- `./tests/fixtures/negative/readiness/missing-state-validator/active-task 2.md`
- `./tests/fixtures/negative/readiness/missing-state-validator/source-contract 2.md`
- `./tests/fixtures/negative/readiness/missing-state-validator/source-task 2.md`
- `./tests/fixtures/negative/readiness/validate-task-state-fail/README 2.md`
- `./tests/fixtures/negative/readiness/validate-task-state-fail/active-task 2.md`
- `./tests/fixtures/negative/readiness/validate-task-state-fail/source-contract 2.md`
- `./tests/fixtures/negative/readiness/validate-task-state-fail/source-task 2.md`
- `./tests/fixtures/negative/review/blocked-but-execution-true/README 2.md`
- `./tests/fixtures/negative/review/blocked-but-execution-true/REVIEW 2.md`
- `./tests/fixtures/negative/review/blocked-but-execution-true 2.md`
- `./tests/fixtures/negative/review/missing-execution-allowed 2.md`
- `./tests/fixtures/negative/review/missing-review-status/README 2.md`
- `./tests/fixtures/negative/review/missing-review-status/REVIEW 2.md`
- `./tests/fixtures/negative/review/missing-review-status 2.md`
- `./tests/fixtures/negative/review/ready-but-execution-false/README 2.md`
- `./tests/fixtures/negative/review/ready-but-execution-false/REVIEW 2.md`
- `./tests/fixtures/negative/review/ready-but-execution-false 2.md`
- `./tests/fixtures/negative/review/unknown-review-status 2.md`
- `./tests/fixtures/negative/runner/approved-mode-requested/README 2.md`
- `./tests/fixtures/negative/runner/approved-mode-requested/scenario 2.md`
- `./tests/fixtures/negative/runner/attempts-active-task-replace/README 2.md`
- `./tests/fixtures/negative/runner/attempts-active-task-replace/scenario 2.md`
- `./tests/fixtures/negative/runner/missing-human-checkpoint/README 2.md`
- `./tests/fixtures/negative/runner/missing-human-checkpoint/scenario 2.md`
- `./tests/fixtures/negative/state/active-without-approval/README 2.md`
- `./tests/fixtures/negative/state/completed-and-active-conflict/README 2.md`
- `./tests/fixtures/negative/state/contract-without-trace/README 2.md`
- `./tests/fixtures/negative/state/dropped-and-active-conflict/README 2.md`
- `./tests/fixtures/negative/state/invalid-transition-brief-to-active/README 2.md`
- `./tests/fixtures/negative/state/review-ready-without-task/README 2.md`
- `./tests/fixtures/negative/task-brief/executable-true/README 2.md`
- `./tests/fixtures/negative/task-brief/executable-true/TASK 2.md`
- `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/README 2.md`
- `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK 2.md`
- `./tests/fixtures/negative/task-brief/missing-metadata/README 2.md`
- `./tests/fixtures/negative/task-brief/missing-metadata/TASK 2.md`
- `./tests/fixtures/negative/task-brief/status-not-approved/README 2.md`
- `./tests/fixtures/negative/task-brief/status-not-approved/TASK 2.md`
- `./tests/fixtures/negative/template-integrity/README 2.md`
- `./tests/fixtures/negative/trace/active-task-updated 2.md`
- `./tests/fixtures/negative/trace/empty-task-id 2.md`
- `./tests/fixtures/negative/trace/execution-approved 2.md`
- `./tests/fixtures/negative/trace/malformed-frontmatter 2.md`
- `./tests/fixtures/negative/trace/missing-decision-rationale 2.md`
- `./tests/fixtures/negative/trace/missing-source-summary 2.md`
- `./tests/fixtures/negative/trace/missing-task-id 2.md`
- `./tests/fixtures/negative/trace/replaces-review 2.md`
- `./tests/fixtures/negative/trace/replaces-task 2.md`
- `./tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue/task-invalid 2.md`
- `./tests/fixtures/queue-directory-validator/valid/tasks/done/task-done 2.md`
- `./tests/fixtures/queue-directory-validator/valid/tasks/dropped/task-dropped 2.md`
- `./tests/fixtures/queue-directory-validator/valid/tasks/queue/task-queued 2.md`
- `./tests/fixtures/queue-validator/invalid/blocked-by-not-list 2.md`
- `./tests/fixtures/queue-validator/invalid/blocked-with-empty-blocked-by 2.md`
- `./tests/fixtures/queue-validator/invalid/empty-task-id 2.md`
- `./tests/fixtures/queue-validator/invalid/malformed-frontmatter 2.md`
- `./tests/fixtures/queue-validator/invalid/missing-blocked-by 2.md`
- `./tests/fixtures/queue-validator/invalid/missing-priority 2.md`
- `./tests/fixtures/queue-validator/invalid/missing-status 2.md`
- `./tests/fixtures/queue-validator/invalid/missing-task-id 2.md`
- `./tests/fixtures/queue-validator/invalid/unknown-priority 2.md`
- `./tests/fixtures/queue-validator/invalid/unknown-status 2.md`
- `./tests/fixtures/queue-validator/valid/blocked-with-dependency 2.md`
- `./tests/fixtures/queue-validator/valid/done-low 2.md`
- `./tests/fixtures/queue-validator/valid/dropped-normal 2.md`
- `./tests/fixtures/queue-validator/valid/queued-high 2.md`
- `./tests/fixtures/queue-validator/valid/queued-normal 2.md`
- `./tests/fixtures/review-validator/invalid/blocked-but-execution-true 2.md`
- `./tests/fixtures/review-validator/invalid/empty-execution-allowed 2.md`
- `./tests/fixtures/review-validator/invalid/empty-review-status 2.md`
- `./tests/fixtures/review-validator/invalid/invalid-execution-allowed 2.md`
- `./tests/fixtures/review-validator/invalid/malformed-frontmatter 2.md`
- `./tests/fixtures/review-validator/invalid/missing-execution-allowed 2.md`
- `./tests/fixtures/review-validator/invalid/missing-review-status 2.md`
- `./tests/fixtures/review-validator/invalid/ready-but-execution-false 2.md`
- `./tests/fixtures/review-validator/invalid/unknown-review-status 2.md`
- `./tests/fixtures/review-validator/valid/blocked 2.md`
- `./tests/fixtures/review-validator/valid/needs-clarification 2.md`
- `./tests/fixtures/review-validator/valid/ready 2.md`
- `./tests/fixtures/review-validator/valid/ready-with-edits 2.md`
- `./tests/fixtures/runner-validator/invalid/scripts/agent-complete 2.py`
- `./tests/fixtures/runner-validator/invalid/scripts/agent-fail 2.py`
- `./tests/fixtures/runner-validator/invalid/scripts/agent-next 2.py`
- `./tests/fixtures/runner-validator/valid/scripts/agent-complete 2.py`
- `./tests/fixtures/runner-validator/valid/scripts/agent-fail 2.py`
- `./tests/fixtures/runner-validator/valid/scripts/agent-next 2.py`
- `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-fail 2.py`
- `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-next 2.py`
- `./tests/fixtures/task-brief/invalid-task-brief-executable-true 2.md`
- `./tests/fixtures/task-brief/invalid-task-brief-missing-section 2.md`
- `./tests/fixtures/task-brief/valid-task-brief 2.md`
- `./tests/fixtures/task-health/task-health 2.md`
- `./tests/fixtures/task-health/tasks/drafts/task-20260426-ready-contract-draft 2.md`
- `./tests/fixtures/task-health/tasks/queue/blocked-example 2.md`
- `./tests/fixtures/task-health/tasks/queue/queued-example 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/REVIEW 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/TASK 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-no-review/TASK 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-ready/REVIEW 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-ready/TASK 2.md`
- `./tests/fixtures/task-health/tasks/task-20260426-ready/TRACE 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/INIT 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/core-rules/MAIN 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/project/PROJECT 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/repo-map 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/reports/task-health 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-complete 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-fail 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-next 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/auto-runner 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/generate-task-contract 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/task-health 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/validate-task-brief 2.py`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview/BOOT 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard/BOOT 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/queue-entry 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-brief-review 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-contract-from-brief 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-decision-trace 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner/RUNNER-PROTOCOL 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive/WRITE-TRACE 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health/TASK-HEALTH 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue/MANAGE-QUEUE 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review/REVIEW-TASK-BRIEF 2.md`
- `./tests/fixtures/template-integrity/forbidden-auto-runner/workflow/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/INIT 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/project/PROJECT 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/repo-map 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/reports/task-health 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-complete 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-fail 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-next 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/generate-task-contract 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/task-health 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/scripts/validate-task-brief 2.py`
- `./tests/fixtures/template-integrity/missing-core-file/stages/01-interview/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/templates/queue-entry 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/templates/task-brief-review 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/templates/task-contract-from-brief 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/templates/task-decision-trace 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/agent-runner/RUNNER-PROTOCOL 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/interview-archive/WRITE-TRACE 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/task-health/TASK-HEALTH 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/task-queue/MANAGE-QUEUE 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/tools/task-review/REVIEW-TASK-BRIEF 2.md`
- `./tests/fixtures/template-integrity/missing-core-file/workflow/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/INIT 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/core-rules/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/project/PROJECT 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/repo-map 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/reports/task-health 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-complete 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-fail 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-next 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/generate-task-contract 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/task-health 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/validate-task-brief 2.py`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/queue-entry 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-brief-review 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-contract-from-brief 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-decision-trace 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner/RUNNER-PROTOCOL 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive/WRITE-TRACE 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health/TASK-HEALTH 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue/MANAGE-QUEUE 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review/REVIEW-TASK-BRIEF 2.md`
- `./tests/fixtures/template-integrity/missing-fixtures-warning/workflow/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/INIT 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/project/PROJECT 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/repo-map 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/reports/task-health 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-complete 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-fail 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-next 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/generate-task-contract 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/task-health 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/validate-task-brief 2.py`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard/BOOT 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/queue-entry 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-brief-review 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-contract-from-brief 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-decision-trace 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner/RUNNER-PROTOCOL 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive/WRITE-TRACE 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health/TASK-HEALTH 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue/MANAGE-QUEUE 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review/REVIEW-TASK-BRIEF 2.md`
- `./tests/fixtures/template-integrity/missing-gitignore-drafts/workflow/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-optional-report-warning/INIT 2.md`
- `./tests/fixtures/template-integrity/missing-optional-report-warning/core-rules/MAIN 2.md`
- `./tests/fixtures/template-integrity/missing-optional-report-warning/project/PROJECT 2.md`

Команда 2 (повторяющиеся имена): `find . -type f \( -name "*.md" -o -name "*.py" \) -print0 | xargs -0 -I{} basename {} | sort | uniq -d`

- `BOOT 2.md` (9)
- `BOOT.md` (14)
- `BUILD-TASK-CONTRACT 2.md` (4)
- `BUILD-TASK-CONTRACT.md` (7)
- `HANDOFF 2.md` (2)
- `HANDOFF.md` (3)
- `INIT 2.md` (6)
- `INIT.md` (7)
- `MAIN 2.md` (13)
- `MAIN.md` (18)
- `MANAGE-QUEUE 2.md` (4)
- `MANAGE-QUEUE.md` (7)
- `PROJECT 2.md` (5)
- `PROJECT.md` (7)
- `README 2.md` (102)
- `README.md` (114)
- `RELEASE-CHECKLIST.md` (2)
- `REVIEW 2.md` (27)
- `REVIEW-TASK-BRIEF 2.md` (4)
- `REVIEW-TASK-BRIEF.md` (7)
- `REVIEW.md` (27)
- `RUNNER-PROTOCOL 2.md` (4)
- `RUNNER-PROTOCOL.md` (7)
- `TASK 2.md` (32)
- `TASK-HEALTH 2.md` (4)
- `TASK-HEALTH.md` (7)
- `TASK.md` (32)
- `TRACE 2.md` (18)
- `TRACE.md` (18)
- `VALIDATORS 2.md` (2)
- `VALIDATORS.md` (2)
- `WRITE-TRACE 2.md` (4)
- `WRITE-TRACE.md` (7)
- `active-task 2.md` (53)
- `active-task-updated.md` (2)
- `active-task.md` (53)
- `agent-complete 2.py` (7)
- `agent-complete.py` (9)
- `agent-fail 2.py` (8)
- `agent-fail.py` (10)
- `agent-next 2.py` (8)
- `agent-next.py` (10)
- `approval 2.md` (25)
- `approval-not-required-transition 2.md` (2)
- `approval-not-required-transition.md` (2)
- `approval-required-transition 2.md` (2)
- `approval-required-transition.md` (2)
- `approval.md` (25)
- `architecture.md` (3)
- `backend.instructions.md` (2)
- `blocked-but-execution-true 2.md` (2)
- `blocked-but-execution-true.md` (2)
- `blocked-by-not-list 2.md` (2)
- `blocked-by-not-list.md` (2)
- `blocked-review-status 2.md` (2)
- `blocked-review-status.md` (2)
- `blocked-with-empty-blocked-by 2.md` (2)
- `blocked-with-empty-blocked-by.md` (2)
- `check-dangerous-commands 2.py` (2)
- `check-dangerous-commands.py` (2)
- `check-links 2.py` (2)
- `check-links.py` (2)
- `check-pr-quality 2.py` (2)
- `check-pr-quality.py` (2)
- `check-risk 2.py` (2)
- `check-risk.py` (2)
- `claude-code.md` (2)
- `copilot-instructions.md` (2)
- `cursor.md` (2)
- `empty-task-id 2.md` (3)
- `empty-task-id.md` (4)
- `execution-allowed-false 2.md` (2)
- `execution-allowed-false.md` (2)
- `execution-approved 2.md` (3)
- `execution-approved.md` (4)
- `execution-evidence-report 2.md` (2)
- `execution-evidence-report.md` (2)
- `frontend.instructions.md` (2)
- `generate-repo-map 2.py` (2)
- `generate-repo-map.py` (2)
- `generate-task-contract 2.py` (5)
- `generate-task-contract.py` (7)
- `guardrails.md` (3)
- `incident 2.md` (2)
- `incident.md` (2)
- `invalid-execution-allowed 2.md` (3)
- `invalid-execution-allowed.md` (3)
- `invalid-vague-approval 2.md` (4)
- `invalid-vague-approval.md` (4)
- `lesson-entry 2.md` (2)
- `lesson-entry.md` (2)
- `lessons 2.md` (2)
- `lessons.md` (2)
- `limitations.md` (3)
- `malformed-frontmatter 2.md` (4)
- `malformed-frontmatter-no-close 2.md` (2)
- `malformed-frontmatter-no-close.md` (2)
- `malformed-frontmatter-no-open 2.md` (2)
- `malformed-frontmatter-no-open.md` (2)
- `malformed-frontmatter.md` (5)
- `missing-blocked-by 2.md` (2)
- `missing-blocked-by.md` (2)
- `missing-decision-rationale.md` (2)
- `missing-execution-allowed 2.md` (4)
- `missing-execution-allowed.md` (4)
- `missing-generated-from-task 2.md` (2)
- `missing-generated-from-task.md` (2)
- `missing-priority 2.md` (2)
- `missing-priority.md` (2)
- `missing-review-file 2.md` (2)
- `missing-review-file.md` (2)
- `missing-review-status 2.md` (4)
- `missing-review-status.md` (4)
- `missing-risk-section 2.md` (2)
- `missing-risk-section.md` (2)
- `missing-source-summary.md` (2)
- `missing-status 2.md` (2)
- `missing-status.md` (2)
- `missing-task-id 2.md` (5)
- `missing-task-id.md` (6)
- `missing-verification-section 2.md` (2)
- `missing-verification-section.md` (2)
- `pull_request_template 2.md` (2)
- `pull_request_template.md` (2)
- `queue-entry 2.md` (5)
- `queue-entry.md` (7)
- `ready-but-execution-false 2.md` (2)
- `ready-but-execution-false.md` (2)
- `release-checklist.md` (2)
- `replaces-active-task 2.md` (2)
- `replaces-active-task.md` (2)
- `replaces-review.md` (2)
- `replaces-task.md` (2)
- `repo-map 2.md` (6)
- `repo-map.md` (8)
- `scenario 2.md` (3)
- `scenario.md` (3)
- `select-context 2.py` (2)
- `select-context.py` (2)
- `session 2.md` (18)
- `session-summary 2.md` (2)
- `session-summary.md` (2)
- `session.md` (18)
- `source-contract 2.md` (61)
- `source-contract.md` (61)
- `source-task 2.md` (45)
- `source-task.md` (45)
- `task-brief-review 2.md` (5)
- `task-brief-review.md` (7)
- `task-contract 2.md` (3)
- `task-contract-from-brief 2.md` (4)
- `task-contract-from-brief.md` (7)
- `task-contract.md` (3)
- `task-decision-trace 2.md` (4)
- `task-decision-trace.md` (7)
- `task-health 2.md` (6)
- `task-health 2.py` (5)
- `task-health.md` (7)
- `task-health.py` (7)
- `task-mismatch-approval 2.md` (2)
- `task-mismatch-approval.md` (2)
- `task.md` (4)
- `troubleshooting.md` (3)
- `unknown-priority 2.md` (2)
- `unknown-priority.md` (2)
- `unknown-review-status 2.md` (2)
- `unknown-review-status.md` (2)
- `unknown-status 2.md` (2)
- `unknown-status.md` (2)
- `valid-approval 2.md` (3)
- `valid-approval.md` (3)
- `validate-commit-msg 2.py` (2)
- `validate-commit-msg.py` (2)
- `validate-docs 2.py` (2)
- `validate-docs.py` (2)
- `validate-handoff 2.py` (2)
- `validate-handoff.py` (2)
- `validate-incident 2.py` (2)
- `validate-incident.py` (2)
- `validate-lessons 2.py` (2)
- `validate-lessons.py` (2)
- `validate-route 2.py` (2)
- `validate-route.py` (2)
- `validate-task 2.py` (3)
- `validate-task-brief 2.py` (5)
- `validate-task-brief.py` (7)
- `validate-task.py` (3)
- `validate-verification 2.py` (3)
- `validate-verification.py` (3)
- `verification 2.md` (3)
- `verification-evidence 2.md` (2)
- `verification-evidence.md` (2)
- `verification-report 2.md` (3)
- `verification-report.md` (3)
- `verification.md` (7)

| File A | File B | Classification | Size diff | Last commit A | Last commit B | Risk | Recommendation |
|---|---|---|---|---|---|---|---|
| `./.github/pull_request_template.md` | `./.github/pull_request_template 2.md` | EXACT_COPY | 352 vs 352 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./CHANGELOG.md` | `./CHANGELOG 2.md` | EXACT_COPY | 547 vs 547 | 57c03d7 docs(m20): refresh evidence and completion review | NOT_COMMITTED | LOW | likely safe to remove B |
| `./INIT.md` | `./INIT 2.md` | EXACT_COPY | 971 vs 971 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./RELEASE-CHECKLIST.md` | `./RELEASE-CHECKLIST 2.md` | EXACT_COPY | 3288 vs 3288 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./ROUTES-REGISTRY.md` | `./ROUTES-REGISTRY 2.md` | EXACT_COPY | 963 vs 963 | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules | NOT_COMMITTED | LOW | likely safe to remove B |
| `./approvals/approval-task-20260426-brief-readiness-check-execution.md` | `./approvals/approval-task-20260426-brief-readiness-check-execution 2.md` | EXACT_COPY | 502 vs 502 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./architecture/CANON.md` | `./architecture/CANON 2.md` | EXACT_COPY | 1290 vs 1290 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | LOW | likely safe to remove B |
| `./architecture/MAIN.md` | `./architecture/MAIN 2.md` | EXACT_COPY | 1616 vs 1616 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | LOW | likely safe to remove B |
| `./architecture/OPERATING-RULES.md` | `./architecture/OPERATING-RULES 2.md` | EXACT_COPY | 1307 vs 1307 | dbed59d Cleanup repo: remove legacy/LAYER docs and keep canonical architecture only | NOT_COMMITTED | LOW | likely safe to remove B |
| `./core-rules/MAIN.md` | `./core-rules/MAIN 2.md` | EXACT_COPY | 2439 vs 2439 | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules | NOT_COMMITTED | HIGH | human review needed |
| `./docs/ACTIVATION-RECOVERY.md` | `./docs/ACTIVATION-RECOVERY 2.md` | EXACT_COPY | 5953 vs 5953 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./docs/ACTIVE-TASK-FORMAT.md` | `./docs/ACTIVE-TASK-FORMAT 2.md` | EXACT_COPY | 5301 vs 5301 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./docs/ACTIVE-TASK-VALIDATION.md` | `./docs/ACTIVE-TASK-VALIDATION 2.md` | EXACT_COPY | 6268 vs 6268 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPLIED-TRANSITION-RECORD.md` | `./docs/APPLIED-TRANSITION-RECORD 2.md` | EXACT_COPY | 3212 vs 3212 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPLY-COMMAND-INTEGRATION.md` | `./docs/APPLY-COMMAND-INTEGRATION 2.md` | EXACT_COPY | 11118 vs 11118 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPLY-PLAN.md` | `./docs/APPLY-PLAN 2.md` | EXACT_COPY | 2924 vs 2924 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPLY-PRECONDITIONS.md` | `./docs/APPLY-PRECONDITIONS 2.md` | EXACT_COPY | 5964 vs 5964 | 8eb08d1 feat(check-apply-preconditions): add policy gate before approval check | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPROVAL-EVIDENCE-STORAGE.md` | `./docs/APPROVAL-EVIDENCE-STORAGE 2.md` | EXACT_COPY | 7540 vs 7540 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPROVAL-MARKER-SPEC.md` | `./docs/APPROVAL-MARKER-SPEC 2.md` | EXACT_COPY | 11860 vs 11860 | a678121 feat(m10.14.1): approval marker spec | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPROVAL-REQUIREMENT-POLICY.md` | `./docs/APPROVAL-REQUIREMENT-POLICY 2.md` | EXACT_COPY | 6729 vs 6729 | 0f23129 docs(operation-risk-model): create canonical risk class definitions | NOT_COMMITTED | HIGH | human review needed |
| `./docs/APPROVED-MODE-CONTRACT.md` | `./docs/APPROVED-MODE-CONTRACT 2.md` | EXACT_COPY | 4513 vs 4513 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./docs/COMPLETION-READINESS.md` | `./docs/COMPLETION-READINESS 2.md` | EXACT_COPY | 8010 vs 8010 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/COMPLETION-TRANSITION.md` | `./docs/COMPLETION-TRANSITION 2.md` | EXACT_COPY | 6035 vs 6035 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/CONTROLLED-COMPLETION.md` | `./docs/CONTROLLED-COMPLETION 2.md` | EXACT_COPY | 6191 vs 6191 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/CONTROLLED-COMPLETION-WORKFLOW.md` | `./docs/CONTROLLED-COMPLETION-WORKFLOW 2.md` | EXACT_COPY | 2398 vs 2398 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./docs/CONTROLLED-EXECUTION-RUNNER.md` | `./docs/CONTROLLED-EXECUTION-RUNNER 2.md` | EXACT_COPY | 8633 vs 8633 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./docs/CONTROLLED-FAILURE-AND-REVIEW.md` | `./docs/CONTROLLED-FAILURE-AND-REVIEW 2.md` | EXACT_COPY | 3516 vs 3516 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/CONTROLLED-LIFECYCLE-MUTATION.md` | `./docs/CONTROLLED-LIFECYCLE-MUTATION 2.md` | EXACT_COPY | 3901 vs 3901 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/EXECUTION-READINESS.md` | `./docs/EXECUTION-READINESS 2.md` | EXACT_COPY | 7587 vs 7587 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./docs/EXECUTION-SESSION.md` | `./docs/EXECUTION-SESSION 2.md` | EXACT_COPY | 7615 vs 7615 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./docs/GETTING-STARTED.md` | `./docs/GETTING-STARTED 2.md` | EXACT_COPY | 4041 vs 4041 | e4c81fc docs(core): update agentos entrypoints and boundaries | NOT_COMMITTED | HIGH | human review needed |
| `./docs/HUMAN-APPROVAL-BOUNDARY.md` | `./docs/HUMAN-APPROVAL-BOUNDARY 2.md` | EXACT_COPY | 6701 vs 6701 | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | NOT_COMMITTED | HIGH | human review needed |
| `./docs/HUMAN-APPROVAL-EVIDENCE.md` | `./docs/HUMAN-APPROVAL-EVIDENCE 2.md` | EXACT_COPY | 7933 vs 7933 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./docs/LIFECYCLE-INTEGRATION.md` | `./docs/LIFECYCLE-INTEGRATION 2.md` | EXACT_COPY | 7090 vs 7090 | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | NOT_COMMITTED | HIGH | human review needed |
| `./docs/OPERATION-RISK-MODEL.md` | `./docs/OPERATION-RISK-MODEL 2.md` | EXACT_COPY | 1817 vs 1817 | 0f23129 docs(operation-risk-model): create canonical risk class definitions | NOT_COMMITTED | HIGH | human review needed |
| `./docs/SAFE-TRANSITION-EXECUTION.md` | `./docs/SAFE-TRANSITION-EXECUTION 2.md` | EXACT_COPY | 4340 vs 4340 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./docs/SAFETY-BOUNDARIES.md` | `./docs/SAFETY-BOUNDARIES 2.md` | EXACT_COPY | 6115 vs 6115 | e4c81fc docs(core): update agentos entrypoints and boundaries | NOT_COMMITTED | HIGH | human review needed |
| `./docs/TASK-STATE-MACHINE.md` | `./docs/TASK-STATE-MACHINE 2.md` | EXACT_COPY | 11923 vs 11923 | 11cb1b4 feat(m10.13.1): state/analysis separation | NOT_COMMITTED | HIGH | human review needed |
| `./docs/TASK-TRANSITION-RULES.md` | `./docs/TASK-TRANSITION-RULES 2.md` | EXACT_COPY | 9897 vs 9897 | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | NOT_COMMITTED | HIGH | human review needed |
| `./docs/VALIDATION.md` | `./docs/VALIDATION 2.md` | EXACT_COPY | 6645 vs 6645 | e4c81fc docs(core): update agentos entrypoints and boundaries | NOT_COMMITTED | HIGH | human review needed |
| `./docs/quickstart.md` | `./docs/quickstart 2.md` | NEAR_COPY | 1783 vs 1410 | 04988ce chore(m21): finalize packaging audit and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./docs/usage.md` | `./docs/usage 2.md` | NEAR_COPY | 2854 vs 2312 | 04988ce chore(m21): finalize packaging audit and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./examples/README.md` | `./examples/README 2.md` | EXACT_COPY | 897 vs 897 | d1c8246 docs(7.5.1): add example scenarios index | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/queue-entry-example.md` | `./examples/queue-entry-example 2.md` | EXACT_COPY | 930 vs 930 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/scenario-01-new-feature.md` | `./examples/scenario-01-new-feature 2.md` | EXACT_COPY | 1698 vs 1698 | c3f9586 docs(7.5.1): add new feature scenario | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/scenario-02-bugfix.md` | `./examples/scenario-02-bugfix 2.md` | EXACT_COPY | 1556 vs 1556 | 3cbcf8d docs(7.5.1): add bugfix scenario | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/scenario-03-refactor.md` | `./examples/scenario-03-refactor 2.md` | EXACT_COPY | 1471 vs 1471 | 2582d2c docs(7.5.1): add refactor scenario | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/scenario-04-validation-only.md` | `./examples/scenario-04-validation-only 2.md` | EXACT_COPY | 1386 vs 1386 | 517ed04 docs(examples-reports): add usage scenarios and validation reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/simple-project/README.md` | `./examples/simple-project/README 2.md` | EXACT_COPY | 481 vs 481 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./examples/simple-project/app.py` | `./examples/simple-project/app 2.py` | EXACT_COPY | 100 vs 100 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./handoff/HANDOFF.md` | `./handoff/HANDOFF 2.md` | EXACT_COPY | 830 vs 830 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./handoff/templates/session-summary.md` | `./handoff/templates/session-summary 2.md` | EXACT_COPY | 420 vs 420 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./incidents/templates/incident.md` | `./incidents/templates/incident 2.md` | EXACT_COPY | 420 vs 420 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./lessons/lessons.md` | `./lessons/lessons 2.md` | EXACT_COPY | 1309 vs 1309 | c729552 docs(lessons): add lesson-002 approval-gate-not-implemented | NOT_COMMITTED | LOW | likely safe to remove B |
| `./lessons/templates/lesson-entry.md` | `./lessons/templates/lesson-entry 2.md` | EXACT_COPY | 281 vs 281 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./prompt-packs/README.md` | `./prompt-packs/README 2.md` | EXACT_COPY | 1245 vs 1245 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./prompt-packs/chatgpt.md` | `./prompt-packs/chatgpt 2.md` | EXACT_COPY | 3183 vs 3183 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./prompt-packs/claude-code.md` | `./prompt-packs/claude-code 2.md` | EXACT_COPY | 3093 vs 3093 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./prompt-packs/codex-cli.md` | `./prompt-packs/codex-cli 2.md` | EXACT_COPY | 3059 vs 3059 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./prompt-packs/cursor.md` | `./prompt-packs/cursor 2.md` | EXACT_COPY | 2825 vs 2825 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./quality/MAIN.md` | `./quality/MAIN 2.md` | EXACT_COPY | 2908 vs 2908 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | HIGH | human review needed |
| `./repo-map.md` | `./repo-map 2.md` | EXACT_COPY | 14768 vs 14768 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./reports/activation-audit-report.md` | `./reports/activation-audit-report 2.md` | EXACT_COPY | 6946 vs 6946 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./reports/activation-positive-smoke.md` | `./reports/activation-positive-smoke 2.md` | EXACT_COPY | 4378 vs 4378 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./reports/active-task-governance-audit-report.md` | `./reports/active-task-governance-audit-report 2.md` | EXACT_COPY | 9966 vs 9966 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/agentos-validate-cli-hardening.md` | `./reports/agentos-validate-cli-hardening 2.md` | EXACT_COPY | 2745 vs 2745 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | HIGH | human review needed |
| `./reports/agentos-validate-json-smoke.md` | `./reports/agentos-validate-json-smoke 2.md` | EXACT_COPY | 2660 vs 2660 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | HIGH | human review needed |
| `./reports/agentos-validate-smoke.md` | `./reports/agentos-validate-smoke 2.md` | EXACT_COPY | 1751 vs 1751 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | HIGH | human review needed |
| `./reports/agentos-validate-usage-integration.md` | `./reports/agentos-validate-usage-integration 2.md` | EXACT_COPY | 2117 vs 2117 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | HIGH | human review needed |
| `./reports/audit.md` | `./reports/audit 2.md` | EXACT_COPY | 1126 vs 1126 | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report | NOT_COMMITTED | HIGH | human review needed |
| `./reports/audit-smoke.md` | `./reports/audit-smoke 2.md` | EXACT_COPY | 1535 vs 1535 | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report | NOT_COMMITTED | HIGH | human review needed |
| `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z.md` | `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z 2.md` | EXACT_COPY | 377 vs 377 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023.md` | `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023 2.md` | EXACT_COPY | 2856 vs 2856 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./reports/execution-evidence-report.md` | `./reports/execution-evidence-report 2.md` | EXACT_COPY | 5618 vs 5618 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./reports/guard-failures-smoke.md` | `./reports/guard-failures-smoke 2.md` | EXACT_COPY | 1107 vs 1107 | 517ed04 docs(examples-reports): add usage scenarios and validation reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10-completion-review.md` | `./reports/milestone-10-completion-review 2.md` | EXACT_COPY | 10397 vs 10397 | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10-final-hardening-review.md` | `./reports/milestone-10-final-hardening-review 2.md` | EXACT_COPY | 9588 vs 9588 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10.11-state-report-hardening.md` | `./reports/milestone-10.11-state-report-hardening 2.md` | EXACT_COPY | 2725 vs 2725 | da5300b chore(reports): add milestone-10.11 report alias for 10.12.1 preflight | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10.11.1-approval-marker-spec.md` | `./reports/milestone-10.11.1-approval-marker-spec 2.md` | EXACT_COPY | 868 vs 868 | ef3e281 feat(m10.11.1): add approval marker spec | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10.11.2-v1.1-hardening.md` | `./reports/milestone-10.11.2-v1.1-hardening 2.md` | EXACT_COPY | 2725 vs 2725 | edffb6d feat(m10.11.2): task state report v1.1 hardening | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10.12-downstream-v1.1-compatibility.md` | `./reports/milestone-10.12-downstream-v1.1-compatibility 2.md` | EXACT_COPY | 4460 vs 4460 | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-10.13-state-analysis-separation.md` | `./reports/milestone-10.13-state-analysis-separation 2.md` | NEAR_COPY | 3472 vs 3665 | cdbf1bc fix(doc-tests): replace absolute local paths with relative in reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-11-completion-review.md` | `./reports/milestone-11-completion-review 2.md` | EXACT_COPY | 4211 vs 4211 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-12-completion-review.md` | `./reports/milestone-12-completion-review 2.md` | EXACT_COPY | 9401 vs 9401 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-13-completion-review.md` | `./reports/milestone-13-completion-review 2.md` | EXACT_COPY | 9085 vs 9085 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-14-completion-review.md` | `./reports/milestone-14-completion-review 2.md` | EXACT_COPY | 2084 vs 2084 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-14-evidence-report.md` | `./reports/milestone-14-evidence-report 2.md` | EXACT_COPY | 3510 vs 3510 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-15-completion-review.md` | `./reports/milestone-15-completion-review 2.md` | EXACT_COPY | 4246 vs 4246 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-15-evidence-report.md` | `./reports/milestone-15-evidence-report 2.md` | EXACT_COPY | 3904 vs 3904 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-16-completion-review.md` | `./reports/milestone-16-completion-review 2.md` | EXACT_COPY | 10228 vs 10228 | c504080 docs(m16): finalize milestone 16 status reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-16-evidence-report.md` | `./reports/milestone-16-evidence-report 2.md` | EXACT_COPY | 11157 vs 11157 | c504080 docs(m16): finalize milestone 16 status reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-17-completion-review.md` | `./reports/milestone-17-completion-review 2.md` | EXACT_COPY | 4706 vs 4706 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-17-evidence-report.md` | `./reports/milestone-17-evidence-report 2.md` | EXACT_COPY | 7088 vs 7088 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-18-completion-review.md` | `./reports/milestone-18-completion-review 2.md` | EXACT_COPY | 3363 vs 3363 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-18-evidence-report.md` | `./reports/milestone-18-evidence-report 2.md` | EXACT_COPY | 3764 vs 3764 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./reports/milestone-7.1-handoff.md` | `./reports/milestone-7.1-handoff 2.md` | EXACT_COPY | 4949 vs 4949 | 517ed04 docs(examples-reports): add usage scenarios and validation reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/negative-fixtures-smoke.md` | `./reports/negative-fixtures-smoke 2.md` | EXACT_COPY | 1206 vs 1206 | 32306aa test(7.1.6): add negative fixture runner smoke report | NOT_COMMITTED | HIGH | human review needed |
| `./reports/pre-execution-evidence-report.md` | `./reports/pre-execution-evidence-report 2.md` | EXACT_COPY | 5098 vs 5098 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/release-checklist.md` | `./reports/release-checklist 2.md` | EXACT_COPY | 2165 vs 2165 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | HIGH | human review needed |
| `./reports/session-handoff.md` | `./reports/session-handoff 2.md` | EXACT_COPY | 4669 vs 4669 | dae7288 chore(hand-off): record milestone 12 closure and hardening | NOT_COMMITTED | HIGH | human review needed |
| `./reports/task-health.md` | `./reports/task-health 2.md` | NEAR_COPY | 872 vs 920 | cdbf1bc fix(doc-tests): replace absolute local paths with relative in reports | NOT_COMMITTED | HIGH | human review needed |
| `./reports/task-state-machine-smoke.md` | `./reports/task-state-machine-smoke 2.md` | EXACT_COPY | 3278 vs 3278 | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | NOT_COMMITTED | HIGH | human review needed |
| `./reports/templates/verification-report.md` | `./reports/templates/verification-report 2.md` | EXACT_COPY | 554 vs 554 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./reports/verification.md` | `./reports/verification 2.md` | EXACT_COPY | 544 vs 544 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/VALIDATORS.md` | `./scripts/VALIDATORS 2.md` | EXACT_COPY | 524 vs 524 | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/activate-task.py` | `./scripts/activate-task 2.py` | EXACT_COPY | 10898 vs 10898 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/agent-complete.py` | `./scripts/agent-complete 2.py` | EXACT_COPY | 3784 vs 3784 | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/agent-fail.py` | `./scripts/agent-fail 2.py` | EXACT_COPY | 3752 vs 3752 | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/agent-next.py` | `./scripts/agent-next 2.py` | EXACT_COPY | 4740 vs 4740 | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/agentos-validate.py` | `./scripts/agentos-validate 2.py` | EXACT_COPY | 6460 vs 6460 | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/apply-transition.py` | `./scripts/apply-transition 2.py` | EXACT_COPY | 39562 vs 39562 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/audit-agentos.py` | `./scripts/audit-agentos 2.py` | EXACT_COPY | 7449 vs 7449 | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/audit-approval-boundary.py` | `./scripts/audit-approval-boundary 2.py` | EXACT_COPY | 17486 vs 17486 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/audit-gate-contract.py` | `./scripts/audit-gate-contract 2.py` | DIVERGED | 1837 vs 8909 | 7360621 feat(audit): add gate contract docs and checks for release-readiness | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/audit-lifecycle-mutation.py` | `./scripts/audit-lifecycle-mutation 2.py` | EXACT_COPY | 8405 vs 8405 | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/audit-policy-boundary.py` | `./scripts/audit-policy-boundary 2.py` | EXACT_COPY | 9339 vs 9339 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/audit-release-readiness.py` | `./scripts/audit-release-readiness 2.py` | EXACT_COPY | 10124 vs 10124 | 57c03d7 docs(m20): refresh evidence and completion review | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-apply-preconditions.py` | `./scripts/check-apply-preconditions 2.py` | EXACT_COPY | 14077 vs 14077 | 8eb08d1 feat(check-apply-preconditions): add policy gate before approval check | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-completion-readiness.py` | `./scripts/check-completion-readiness 2.py` | EXACT_COPY | 17148 vs 17148 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-dangerous-commands.py` | `./scripts/check-dangerous-commands 2.py` | EXACT_COPY | 1250 vs 1250 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-execution-readiness.py` | `./scripts/check-execution-readiness 2.py` | EXACT_COPY | 17199 vs 17199 | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-execution-scope.py` | `./scripts/check-execution-scope 2.py` | EXACT_COPY | 18576 vs 18576 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-links.py` | `./scripts/check-links 2.py` | EXACT_COPY | 1787 vs 1787 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-pr-quality.py` | `./scripts/check-pr-quality 2.py` | EXACT_COPY | 5203 vs 5203 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-risk.py` | `./scripts/check-risk 2.py` | EXACT_COPY | 5438 vs 5438 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/check-template-integrity.py` | `./scripts/check-template-integrity 2.py` | DIVERGED | 9141 vs 5818 | 04988ce chore(m21): finalize packaging audit and milestone reviews | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/check-transition.py` | `./scripts/check-transition 2.py` | EXACT_COPY | 12552 vs 12552 | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/complete-active-task.py` | `./scripts/complete-active-task 2.py` | EXACT_COPY | 13973 vs 13973 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/detect-task-state.py` | `./scripts/detect-task-state 2.py` | EXACT_COPY | 15781 vs 15781 | 11cb1b4 feat(m10.13.1): state/analysis separation | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/generate-repo-map.py` | `./scripts/generate-repo-map 2.py` | EXACT_COPY | 4082 vs 4082 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/generate-task-contract.py` | `./scripts/generate-task-contract 2.py` | EXACT_COPY | 8985 vs 8985 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/lib/__init__.py` | `./scripts/lib/__init__ 2.py` | EXACT_COPY | 0 vs 0 | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/lib/path_utils.py` | `./scripts/lib/path_utils 2.py` | EXACT_COPY | 402 vs 402 | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/run-active-task.py` | `./scripts/run-active-task 2.py` | EXACT_COPY | 21176 vs 21176 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/run-execution-verification.py` | `./scripts/run-execution-verification 2.py` | EXACT_COPY | 17054 vs 17054 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/select-context.py` | `./scripts/select-context 2.py` | EXACT_COPY | 4512 vs 4512 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/task-health.py` | `./scripts/task-health 2.py` | EXACT_COPY | 11263 vs 11263 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-activation-fixtures.py` | `./scripts/test-activation-fixtures 2.py` | EXACT_COPY | 9399 vs 9399 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-active-task-fixtures.py` | `./scripts/test-active-task-fixtures 2.py` | EXACT_COPY | 3311 vs 3311 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-apply-transition-fixtures.py` | `./scripts/test-apply-transition-fixtures 2.py` | EXACT_COPY | 18660 vs 18660 | 39b732b fix(m16): fix two gaps in apply-transition and fixture runner | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-approval-fixtures.py` | `./scripts/test-approval-fixtures 2.py` | EXACT_COPY | 11740 vs 11740 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-approval-flow-smoke.py` | `./scripts/test-approval-flow-smoke 2.py` | EXACT_COPY | 10275 vs 10275 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-approval-marker-fixtures.py` | `./scripts/test-approval-marker-fixtures 2.py` | EXACT_COPY | 5536 vs 5536 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-completion-flow-smoke.py` | `./scripts/test-completion-flow-smoke 2.py` | EXACT_COPY | 17048 vs 17048 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-execution-runner-fixtures.py` | `./scripts/test-execution-runner-fixtures 2.py` | EXACT_COPY | 8402 vs 8402 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-gate-regression-fixtures.py` | `./scripts/test-gate-regression-fixtures 2.py` | DIVERGED | 836 vs 1767 | 7360621 feat(audit): add gate contract docs and checks for release-readiness | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/test-guard-failures.py` | `./scripts/test-guard-failures 2.py` | EXACT_COPY | 5945 vs 5945 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-human-approval-fixtures.py` | `./scripts/test-human-approval-fixtures 2.py` | EXACT_COPY | 5480 vs 5480 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-negative-fixtures.py` | `./scripts/test-negative-fixtures 2.py` | NEAR_COPY | 20071 vs 20035 | 57c03d7 docs(m20): refresh evidence and completion review | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-policy-enforcement-fixtures.py` | `./scripts/test-policy-enforcement-fixtures 2.py` | EXACT_COPY | 5067 vs 5067 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-policy-fixtures.py` | `./scripts/test-policy-fixtures 2.py` | EXACT_COPY | 3536 vs 3536 | 0f23129 docs(operation-risk-model): create canonical risk class definitions | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-policy-flow-smoke.py` | `./scripts/test-policy-flow-smoke 2.py` | EXACT_COPY | 4065 vs 4065 | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-readiness-fixtures.py` | `./scripts/test-readiness-fixtures 2.py` | EXACT_COPY | 5125 vs 5125 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-state-fixtures.py` | `./scripts/test-state-fixtures 2.py` | EXACT_COPY | 11176 vs 11176 | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-template-integrity.py` | `./scripts/test-template-integrity 2.py` | DIVERGED | 1181 vs 3688 | 57c03d7 docs(m20): refresh evidence and completion review | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/test-template-integrity-fixtures.py` | `./scripts/test-template-integrity-fixtures 2.py` | EXACT_COPY | 1773 vs 1773 | 57c03d7 docs(m20): refresh evidence and completion review | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/test-unified-gate-smoke.py` | `./scripts/test-unified-gate-smoke 2.py` | DIVERGED | 711 vs 4250 | 7360621 feat(audit): add gate contract docs and checks for release-readiness | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/validate-active-task.py` | `./scripts/validate-active-task 2.py` | EXACT_COPY | 9421 vs 9421 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-approval-marker.py` | `./scripts/validate-approval-marker 2.py` | EXACT_COPY | 10926 vs 10926 | 9241afd feat(m10.15.1): approval marker validator | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-commit-msg.py` | `./scripts/validate-commit-msg 2.py` | EXACT_COPY | 3676 vs 3676 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-contract-draft.py` | `./scripts/validate-contract-draft 2.py` | EXACT_COPY | 4931 vs 4931 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-docs.py` | `./scripts/validate-docs 2.py` | EXACT_COPY | 2513 vs 2513 | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-gate-contract.py` | `./scripts/validate-gate-contract 2.py` | DIVERGED | 987 vs 6404 | 7360621 feat(audit): add gate contract docs and checks for release-readiness | NOT_COMMITTED | MEDIUM | human review needed |
| `./scripts/validate-handoff.py` | `./scripts/validate-handoff 2.py` | EXACT_COPY | 2089 vs 2089 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-human-approval.py` | `./scripts/validate-human-approval 2.py` | EXACT_COPY | 10122 vs 10122 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-incident.py` | `./scripts/validate-incident 2.py` | EXACT_COPY | 2200 vs 2200 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-lessons.py` | `./scripts/validate-lessons 2.py` | EXACT_COPY | 2163 vs 2163 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-lifecycle-apply.py` | `./scripts/validate-lifecycle-apply 2.py` | EXACT_COPY | 6926 vs 6926 | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-policy.py` | `./scripts/validate-policy 2.py` | EXACT_COPY | 6354 vs 6354 | 0f23129 docs(operation-risk-model): create canonical risk class definitions | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-queue.py` | `./scripts/validate-queue 2.py` | EXACT_COPY | 2644 vs 2644 | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-queue-entry.py` | `./scripts/validate-queue-entry 2.py` | EXACT_COPY | 3467 vs 3467 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-review.py` | `./scripts/validate-review 2.py` | EXACT_COPY | 3647 vs 3647 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-route.py` | `./scripts/validate-route 2.py` | EXACT_COPY | 1685 vs 1685 | dbed59d Cleanup repo: remove legacy/LAYER docs and keep canonical architecture only | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-runner-protocol.py` | `./scripts/validate-runner-protocol 2.py` | EXACT_COPY | 3720 vs 3720 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-task.py` | `./scripts/validate-task 2.py` | EXACT_COPY | 1604 vs 1604 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-task-brief.py` | `./scripts/validate-task-brief 2.py` | EXACT_COPY | 2945 vs 2945 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-task-state.py` | `./scripts/validate-task-state 2.py` | EXACT_COPY | 13567 vs 13567 | 11cb1b4 feat(m10.13.1): state/analysis separation | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-trace.py` | `./scripts/validate-trace 2.py` | EXACT_COPY | 2941 vs 2941 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | HIGH | human review needed |
| `./scripts/validate-verification.py` | `./scripts/validate-verification 2.py` | EXACT_COPY | 1631 vs 1631 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./security/MAIN.md` | `./security/MAIN 2.md` | EXACT_COPY | 2715 vs 2715 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | HIGH | human review needed |
| `./stages/spec-wizard/BOOT.md` | `./stages/spec-wizard/BOOT 2.md` | EXACT_COPY | 8984 vs 8984 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./state/MAIN.md` | `./state/MAIN 2.md` | EXACT_COPY | 3477 vs 3477 | 1e053f3 Stabilize canonical module architecture and validators | NOT_COMMITTED | HIGH | human review needed |
| `./tasks/active-task.md` | `./tasks/active-task 2.md` | EXACT_COPY | 531 vs 531 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./tasks/queue/20260428-queue-schema-check.md` | `./tasks/queue/20260428-queue-schema-check 2.md` | EXACT_COPY | 221 vs 221 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/queue/20260428-runner-human-checkpoints.md` | `./tasks/queue/20260428-runner-human-checkpoints 2.md` | EXACT_COPY | 245 vs 245 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/queue/QUEUE.md` | `./tasks/queue/QUEUE 2.md` | EXACT_COPY | 520 vs 520 | 1f467cf chore(worktree): pre-existing unrelated changes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/task-20260426-brief-readiness-check/REVIEW.md` | `./tasks/task-20260426-brief-readiness-check/REVIEW 2.md` | EXACT_COPY | 1768 vs 1768 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/task-20260426-brief-readiness-check/TASK.md` | `./tasks/task-20260426-brief-readiness-check/TASK 2.md` | EXACT_COPY | 2046 vs 2046 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/task-20260426-brief-readiness-check/TRACE.md` | `./tasks/task-20260426-brief-readiness-check/TRACE 2.md` | EXACT_COPY | 2642 vs 2642 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/task-20260426-brief-to-contract-manual-guide/TASK.md` | `./tasks/task-20260426-brief-to-contract-manual-guide/TASK 2.md` | EXACT_COPY | 2500 vs 2500 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tasks/templates/task-contract.md` | `./tasks/templates/task-contract 2.md` | EXACT_COPY | 285 vs 285 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/.github/copilot-instructions.md` | `./templates/agentos-full/.github/copilot-instructions 2.md` | EXACT_COPY | 603 vs 603 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/.github/instructions/backend.instructions.md` | `./templates/agentos-full/.github/instructions/backend.instructions 2.md` | EXACT_COPY | 484 vs 484 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/.github/instructions/frontend.instructions.md` | `./templates/agentos-full/.github/instructions/frontend.instructions 2.md` | EXACT_COPY | 429 vs 429 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/.github/pull_request_template.md` | `./templates/agentos-full/.github/pull_request_template 2.md` | EXACT_COPY | 352 vs 352 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/handoff/HANDOFF.md` | `./templates/agentos-full/handoff/HANDOFF 2.md` | EXACT_COPY | 830 vs 830 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/handoff/templates/session-summary.md` | `./templates/agentos-full/handoff/templates/session-summary 2.md` | EXACT_COPY | 420 vs 420 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/incidents/templates/incident.md` | `./templates/agentos-full/incidents/templates/incident 2.md` | EXACT_COPY | 420 vs 420 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/lessons/lessons.md` | `./templates/agentos-full/lessons/lessons 2.md` | EXACT_COPY | 324 vs 324 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/lessons/templates/lesson-entry.md` | `./templates/agentos-full/lessons/templates/lesson-entry 2.md` | EXACT_COPY | 281 vs 281 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/repo-map.md` | `./templates/agentos-full/repo-map 2.md` | EXACT_COPY | 9031 vs 9031 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/agentos-full/reports/templates/verification-report.md` | `./templates/agentos-full/reports/templates/verification-report 2.md` | EXACT_COPY | 554 vs 554 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/reports/verification.md` | `./templates/agentos-full/reports/verification 2.md` | EXACT_COPY | 544 vs 544 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/VALIDATORS.md` | `./templates/agentos-full/scripts/VALIDATORS 2.md` | EXACT_COPY | 524 vs 524 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/check-dangerous-commands.py` | `./templates/agentos-full/scripts/check-dangerous-commands 2.py` | EXACT_COPY | 1250 vs 1250 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/check-links.py` | `./templates/agentos-full/scripts/check-links 2.py` | EXACT_COPY | 1787 vs 1787 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/check-pr-quality.py` | `./templates/agentos-full/scripts/check-pr-quality 2.py` | EXACT_COPY | 5203 vs 5203 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/check-risk.py` | `./templates/agentos-full/scripts/check-risk 2.py` | EXACT_COPY | 5438 vs 5438 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/generate-repo-map.py` | `./templates/agentos-full/scripts/generate-repo-map 2.py` | EXACT_COPY | 4082 vs 4082 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/select-context.py` | `./templates/agentos-full/scripts/select-context 2.py` | EXACT_COPY | 4512 vs 4512 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-commit-msg.py` | `./templates/agentos-full/scripts/validate-commit-msg 2.py` | EXACT_COPY | 3676 vs 3676 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-docs.py` | `./templates/agentos-full/scripts/validate-docs 2.py` | EXACT_COPY | 2513 vs 2513 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-handoff.py` | `./templates/agentos-full/scripts/validate-handoff 2.py` | EXACT_COPY | 2089 vs 2089 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-incident.py` | `./templates/agentos-full/scripts/validate-incident 2.py` | EXACT_COPY | 2200 vs 2200 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-lessons.py` | `./templates/agentos-full/scripts/validate-lessons 2.py` | EXACT_COPY | 2163 vs 2163 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-route.py` | `./templates/agentos-full/scripts/validate-route 2.py` | EXACT_COPY | 1685 vs 1685 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-task.py` | `./templates/agentos-full/scripts/validate-task 2.py` | EXACT_COPY | 1604 vs 1604 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/scripts/validate-verification.py` | `./templates/agentos-full/scripts/validate-verification 2.py` | EXACT_COPY | 1631 vs 1631 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/tasks/active-task.md` | `./templates/agentos-full/tasks/active-task 2.md` | EXACT_COPY | 3019 vs 3019 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-full/tasks/templates/task-contract.md` | `./templates/agentos-full/tasks/templates/task-contract 2.md` | EXACT_COPY | 285 vs 285 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/reports/templates/verification-report.md` | `./templates/agentos-minimal/reports/templates/verification-report 2.md` | EXACT_COPY | 554 vs 554 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/reports/verification.md` | `./templates/agentos-minimal/reports/verification 2.md` | EXACT_COPY | 544 vs 544 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/scripts/validate-task.py` | `./templates/agentos-minimal/scripts/validate-task 2.py` | EXACT_COPY | 1604 vs 1604 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/scripts/validate-verification.py` | `./templates/agentos-minimal/scripts/validate-verification 2.py` | EXACT_COPY | 1631 vs 1631 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/tasks/active-task.md` | `./templates/agentos-minimal/tasks/active-task 2.md` | EXACT_COPY | 3019 vs 3019 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/agentos-minimal/tasks/templates/task-contract.md` | `./templates/agentos-minimal/tasks/templates/task-contract 2.md` | EXACT_COPY | 285 vs 285 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | HIGH | human review needed |
| `./templates/applied-transition-record.md` | `./templates/applied-transition-record 2.md` | EXACT_COPY | 432 vs 432 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/apply-plan.md` | `./templates/apply-plan 2.md` | EXACT_COPY | 308 vs 308 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/candidate-tasks.md` | `./templates/candidate-tasks 2.md` | EXACT_COPY | 670 vs 670 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/commit-message.md` | `./templates/commit-message 2.md` | EXACT_COPY | 172 vs 172 | c8117c1 feat(example-project): add example validation flow | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/completion-readiness.md` | `./templates/completion-readiness 2.md` | EXACT_COPY | 1638 vs 1638 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/completion-transition.md` | `./templates/completion-transition 2.md` | EXACT_COPY | 1652 vs 1652 | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/execution-session.md` | `./templates/execution-session 2.md` | EXACT_COPY | 978 vs 978 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/human-approval-record.md` | `./templates/human-approval-record 2.md` | EXACT_COPY | 277 vs 277 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/queue-entry.md` | `./templates/queue-entry 2.md` | EXACT_COPY | 379 vs 379 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./templates/task-brief-review.md` | `./templates/task-brief-review 2.md` | EXACT_COPY | 1147 vs 1147 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/agent-runner/drafts/high-ready-contract-draft.md` | `./tests/fixtures/agent-runner/drafts/high-ready-contract-draft 2.md` | EXACT_COPY | 126 vs 126 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/agent-runner/queue/high-ready.md` | `./tests/fixtures/agent-runner/queue/high-ready 2.md` | EXACT_COPY | 196 vs 196 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/agent-runner/queue/normal-blocked.md` | `./tests/fixtures/agent-runner/queue/normal-blocked 2.md` | EXACT_COPY | 142 vs 142 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/active-task.md` | `./tests/fixtures/apply-preconditions-approval/active-task 2.md` | EXACT_COPY | 73 vs 73 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/approval-not-required-transition.md` | `./tests/fixtures/apply-preconditions-approval/approval-not-required-transition 2.md` | EXACT_COPY | 341 vs 341 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/approval-required-transition.md` | `./tests/fixtures/apply-preconditions-approval/approval-required-transition 2.md` | EXACT_COPY | 365 vs 365 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/invalid-vague-approval.md` | `./tests/fixtures/apply-preconditions-approval/invalid-vague-approval 2.md` | EXACT_COPY | 595 vs 595 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/readiness-evidence.md` | `./tests/fixtures/apply-preconditions-approval/readiness-evidence 2.md` | EXACT_COPY | 64 vs 64 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/task-mismatch-approval.md` | `./tests/fixtures/apply-preconditions-approval/task-mismatch-approval 2.md` | EXACT_COPY | 782 vs 782 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/valid-approval.md` | `./tests/fixtures/apply-preconditions-approval/valid-approval 2.md` | EXACT_COPY | 791 vs 791 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-preconditions-approval/verification-evidence.md` | `./tests/fixtures/apply-preconditions-approval/verification-evidence 2.md` | EXACT_COPY | 64 vs 64 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/apply-transition/README.md` | `./tests/fixtures/apply-transition/README 2.md` | EXACT_COPY | 391 vs 391 | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/approval-not-required-transition.md` | `./tests/fixtures/approval-enforcement/approval-not-required-transition 2.md` | EXACT_COPY | 272 vs 272 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/approval-required-mutation-plan.md` | `./tests/fixtures/approval-enforcement/approval-required-mutation-plan 2.md` | EXACT_COPY | 514 vs 514 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/approval-required-transition.md` | `./tests/fixtures/approval-enforcement/approval-required-transition 2.md` | EXACT_COPY | 296 vs 296 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/invalid-vague-approval.md` | `./tests/fixtures/approval-enforcement/invalid-vague-approval 2.md` | EXACT_COPY | 593 vs 593 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/task-mismatch-approval.md` | `./tests/fixtures/approval-enforcement/task-mismatch-approval 2.md` | EXACT_COPY | 791 vs 791 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/transition-mismatch-approval.md` | `./tests/fixtures/approval-enforcement/transition-mismatch-approval 2.md` | EXACT_COPY | 785 vs 785 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/unsupported-operation-approval.md` | `./tests/fixtures/approval-enforcement/unsupported-operation-approval 2.md` | EXACT_COPY | 684 vs 684 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/unsupported-target-state-approval.md` | `./tests/fixtures/approval-enforcement/unsupported-target-state-approval 2.md` | EXACT_COPY | 747 vs 747 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-enforcement/valid-approval.md` | `./tests/fixtures/approval-enforcement/valid-approval 2.md` | EXACT_COPY | 773 vs 773 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/README.md` | `./tests/fixtures/approval-flow-smoke/README 2.md` | EXACT_COPY | 719 vs 719 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/invalid-vague-approval.md` | `./tests/fixtures/approval-flow-smoke/invalid-vague-approval 2.md` | EXACT_COPY | 575 vs 575 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-applied-transition-record.md` | `./tests/fixtures/approval-flow-smoke/synthetic-applied-transition-record 2.md` | EXACT_COPY | 195 vs 195 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-apply-plan.md` | `./tests/fixtures/approval-flow-smoke/synthetic-apply-plan 2.md` | EXACT_COPY | 129 vs 129 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-mutation-plan.md` | `./tests/fixtures/approval-flow-smoke/synthetic-mutation-plan 2.md` | EXACT_COPY | 405 vs 405 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-readiness.md` | `./tests/fixtures/approval-flow-smoke/synthetic-readiness 2.md` | EXACT_COPY | 29 vs 29 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-task.md` | `./tests/fixtures/approval-flow-smoke/synthetic-task 2.md` | EXACT_COPY | 184 vs 184 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-transition.md` | `./tests/fixtures/approval-flow-smoke/synthetic-transition 2.md` | EXACT_COPY | 284 vs 284 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/synthetic-verification.md` | `./tests/fixtures/approval-flow-smoke/synthetic-verification 2.md` | EXACT_COPY | 49 vs 49 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/approval-flow-smoke/valid-approval.md` | `./tests/fixtures/approval-flow-smoke/valid-approval 2.md` | EXACT_COPY | 743 vs 743 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/README.md` | `./tests/fixtures/completion-flow-smoke/README 2.md` | EXACT_COPY | 168 vs 168 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/active-task.md` | `./tests/fixtures/completion-flow-smoke/active-task 2.md` | EXACT_COPY | 145 vs 145 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/completion-readiness-evidence.md` | `./tests/fixtures/completion-flow-smoke/completion-readiness-evidence 2.md` | EXACT_COPY | 47 vs 47 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/prepared-transition.md` | `./tests/fixtures/completion-flow-smoke/prepared-transition 2.md` | EXACT_COPY | 184 vs 184 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/reports/execution/session-smoke.md` | `./tests/fixtures/completion-flow-smoke/reports/execution/session-smoke 2.md` | EXACT_COPY | 92 vs 92 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/completion-flow-smoke/reports/execution-evidence-report.md` | `./tests/fixtures/completion-flow-smoke/reports/execution-evidence-report 2.md` | EXACT_COPY | 53 vs 53 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/completion-flow-smoke/tasks-active-task.md` | `./tests/fixtures/completion-flow-smoke/tasks-active-task 2.md` | EXACT_COPY | 145 vs 145 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/transition-smoke.md` | `./tests/fixtures/completion-flow-smoke/transition-smoke 2.md` | EXACT_COPY | 184 vs 184 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/completion-flow-smoke/verification-evidence.md` | `./tests/fixtures/completion-flow-smoke/verification-evidence 2.md` | EXACT_COPY | 50 vs 50 | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-generation/blocked-task/REVIEW.md` | `./tests/fixtures/contract-generation/blocked-task/REVIEW 2.md` | EXACT_COPY | 1033 vs 1033 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-generation/blocked-task/TASK.md` | `./tests/fixtures/contract-generation/blocked-task/TASK 2.md` | EXACT_COPY | 627 vs 627 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-generation/missing-review/TASK.md` | `./tests/fixtures/contract-generation/missing-review/TASK 2.md` | EXACT_COPY | 659 vs 659 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-generation/ready-task/REVIEW.md` | `./tests/fixtures/contract-generation/ready-task/REVIEW 2.md` | EXACT_COPY | 1107 vs 1107 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-generation/ready-task/TASK.md` | `./tests/fixtures/contract-generation/ready-task/TASK 2.md` | EXACT_COPY | 888 vs 888 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/blocked-review-status.md` | `./tests/fixtures/contract-validator/invalid/blocked-review-status 2.md` | EXACT_COPY | 263 vs 263 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/execution-allowed-false.md` | `./tests/fixtures/contract-validator/invalid/execution-allowed-false 2.md` | EXACT_COPY | 285 vs 285 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/execution-approved.md` | `./tests/fixtures/contract-validator/invalid/execution-approved 2.md` | EXACT_COPY | 312 vs 312 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/invalid-execution-allowed.md` | `./tests/fixtures/contract-validator/invalid/invalid-execution-allowed 2.md` | EXACT_COPY | 289 vs 289 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-close.md` | `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-close 2.md` | EXACT_COPY | 286 vs 286 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-open.md` | `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-open 2.md` | EXACT_COPY | 258 vs 258 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-execution-allowed.md` | `./tests/fixtures/contract-validator/invalid/missing-execution-allowed 2.md` | EXACT_COPY | 266 vs 266 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-generated-from-task.md` | `./tests/fixtures/contract-validator/invalid/missing-generated-from-task 2.md` | EXACT_COPY | 226 vs 226 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-review-file.md` | `./tests/fixtures/contract-validator/invalid/missing-review-file 2.md` | EXACT_COPY | 232 vs 232 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-review-status.md` | `./tests/fixtures/contract-validator/invalid/missing-review-status 2.md` | EXACT_COPY | 281 vs 281 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-risk-section.md` | `./tests/fixtures/contract-validator/invalid/missing-risk-section 2.md` | EXACT_COPY | 231 vs 231 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-task-id.md` | `./tests/fixtures/contract-validator/invalid/missing-task-id 2.md` | EXACT_COPY | 238 vs 238 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/missing-verification-section.md` | `./tests/fixtures/contract-validator/invalid/missing-verification-section 2.md` | EXACT_COPY | 265 vs 265 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/invalid/replaces-active-task.md` | `./tests/fixtures/contract-validator/invalid/replaces-active-task 2.md` | EXACT_COPY | 307 vs 307 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/valid/ready-contract-draft.md` | `./tests/fixtures/contract-validator/valid/ready-contract-draft 2.md` | EXACT_COPY | 414 vs 414 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/contract-validator/valid/ready-with-edits-contract-draft.md` | `./tests/fixtures/contract-validator/valid/ready-with-edits-contract-draft 2.md` | EXACT_COPY | 490 vs 490 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approval-id-operation-mismatch.md` | `./tests/fixtures/human-approval/invalid-approval-id-operation-mismatch 2.md` | EXACT_COPY | 664 vs 664 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approval-id-task-mismatch.md` | `./tests/fixtures/human-approval/invalid-approval-id-task-mismatch 2.md` | EXACT_COPY | 665 vs 665 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approval-status-invalid.md` | `./tests/fixtures/human-approval/invalid-approval-status-invalid 2.md` | EXACT_COPY | 666 vs 666 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approved-at-format.md` | `./tests/fixtures/human-approval/invalid-approved-at-format 2.md` | EXACT_COPY | 658 vs 658 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approved-by-agent.md` | `./tests/fixtures/human-approval/invalid-approved-by-agent 2.md` | EXACT_COPY | 656 vs 656 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-approved-by-openai-exact.md` | `./tests/fixtures/human-approval/invalid-approved-by-openai-exact 2.md` | EXACT_COPY | 657 vs 657 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-bypass-preconditions.md` | `./tests/fixtures/human-approval/invalid-bypass-preconditions 2.md` | EXACT_COPY | 690 vs 690 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-expired-status.md` | `./tests/fixtures/human-approval/invalid-expired-status 2.md` | EXACT_COPY | 666 vs 666 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-expires-at-format.md` | `./tests/fixtures/human-approval/invalid-expires-at-format 2.md` | EXACT_COPY | 670 vs 670 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-generic-scope-all.md` | `./tests/fixtures/human-approval/invalid-generic-scope-all 2.md` | EXACT_COPY | 591 vs 591 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-missing-approval-scope.md` | `./tests/fixtures/human-approval/invalid-missing-approval-scope 2.md` | EXACT_COPY | 588 vs 588 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-missing-related-task-id.md` | `./tests/fixtures/human-approval/invalid-missing-related-task-id 2.md` | EXACT_COPY | 634 vs 634 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-missing-related-transition-id.md` | `./tests/fixtures/human-approval/invalid-missing-related-transition-id 2.md` | EXACT_COPY | 633 vs 633 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-missing-required-field.md` | `./tests/fixtures/human-approval/invalid-missing-required-field 2.md` | EXACT_COPY | 635 vs 635 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-nested-yaml.md` | `./tests/fixtures/human-approval/invalid-nested-yaml 2.md` | EXACT_COPY | 659 vs 659 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-related-task-id-format.md` | `./tests/fixtures/human-approval/invalid-related-task-id-format 2.md` | EXACT_COPY | 660 vs 660 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-related-transition-id-format.md` | `./tests/fixtures/human-approval/invalid-related-transition-id-format 2.md` | EXACT_COPY | 660 vs 660 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-revoked-status.md` | `./tests/fixtures/human-approval/invalid-revoked-status 2.md` | EXACT_COPY | 666 vs 666 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-statement-missing-operation-reference.md` | `./tests/fixtures/human-approval/invalid-statement-missing-operation-reference 2.md` | EXACT_COPY | 638 vs 638 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-statement-missing-target-state-reference.md` | `./tests/fixtures/human-approval/invalid-statement-missing-target-state-reference 2.md` | EXACT_COPY | 629 vs 629 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-statement-missing-task-reference.md` | `./tests/fixtures/human-approval/invalid-statement-missing-task-reference 2.md` | EXACT_COPY | 620 vs 620 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-statement-missing-transition-reference.md` | `./tests/fixtures/human-approval/invalid-statement-missing-transition-reference 2.md` | EXACT_COPY | 615 vs 615 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-superseded-status.md` | `./tests/fixtures/human-approval/invalid-superseded-status 2.md` | EXACT_COPY | 669 vs 669 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-supersedes-format.md` | `./tests/fixtures/human-approval/invalid-supersedes-format 2.md` | EXACT_COPY | 679 vs 679 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-unknown-approval-source.md` | `./tests/fixtures/human-approval/invalid-unknown-approval-source 2.md` | EXACT_COPY | 666 vs 666 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-unknown-status.md` | `./tests/fixtures/human-approval/invalid-unknown-status 2.md` | EXACT_COPY | 666 vs 666 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-unsupported-operation.md` | `./tests/fixtures/human-approval/invalid-unsupported-operation 2.md` | EXACT_COPY | 601 vs 601 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-unsupported-target-state.md` | `./tests/fixtures/human-approval/invalid-unsupported-target-state 2.md` | EXACT_COPY | 661 vs 661 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-vague-approval.md` | `./tests/fixtures/human-approval/invalid-vague-approval 2.md` | EXACT_COPY | 514 vs 514 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/invalid-vague-continue.md` | `./tests/fixtures/human-approval/invalid-vague-continue 2.md` | EXACT_COPY | 520 vs 520 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/valid-approved-by-openai-substring.md` | `./tests/fixtures/human-approval/valid-approved-by-openai-substring 2.md` | EXACT_COPY | 691 vs 691 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/human-approval/valid-complete-active.md` | `./tests/fixtures/human-approval/valid-complete-active 2.md` | EXACT_COPY | 665 vs 665 | e6c9069 feat(m17): approval evidence and authorization hardening layer | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/README.md` | `./tests/fixtures/negative/README 2.md` | EXACT_COPY | 2818 vs 2818 | 5fb5f70 docs(7.1.5): document negative fixture test runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/active-task-different-task/approvals/approval.md` | `./tests/fixtures/negative/activation/active-task-different-task/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/active-task-different-task/task/REVIEW.md` | `./tests/fixtures/negative/activation/active-task-different-task/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/active-task-different-task/task/TASK.md` | `./tests/fixtures/negative/activation/active-task-different-task/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/active-task-different-task/task/TRACE.md` | `./tests/fixtures/negative/activation/active-task-different-task/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-conflict/approvals/approval.md` | `./tests/fixtures/negative/activation/analysis-status-conflict/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/REVIEW.md` | `./tests/fixtures/negative/activation/analysis-status-conflict/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/TASK.md` | `./tests/fixtures/negative/activation/analysis-status-conflict/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/TRACE.md` | `./tests/fixtures/negative/activation/analysis-status-conflict/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-invalid/approvals/approval.md` | `./tests/fixtures/negative/activation/analysis-status-invalid/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/REVIEW.md` | `./tests/fixtures/negative/activation/analysis-status-invalid/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/TASK.md` | `./tests/fixtures/negative/activation/analysis-status-invalid/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/TRACE.md` | `./tests/fixtures/negative/activation/analysis-status-invalid/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals/approval.md` | `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/REVIEW.md` | `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TASK.md` | `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TRACE.md` | `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/approvals/approval.md` | `./tests/fixtures/negative/activation/both-approved-and-dry-run/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/REVIEW.md` | `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TASK.md` | `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TRACE.md` | `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/check-transition-fail/task/REVIEW.md` | `./tests/fixtures/negative/activation/check-transition-fail/task/REVIEW 2.md` | EXACT_COPY | 15 vs 15 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/check-transition-fail/task/TASK.md` | `./tests/fixtures/negative/activation/check-transition-fail/task/TASK 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/check-transition-fail/task/TRACE.md` | `./tests/fixtures/negative/activation/check-transition-fail/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/contract-missing/approvals/approval.md` | `./tests/fixtures/negative/activation/contract-missing/approvals/approval 2.md` | EXACT_COPY | 276 vs 276 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/contract-missing/task/REVIEW.md` | `./tests/fixtures/negative/activation/contract-missing/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/contract-missing/task/TASK.md` | `./tests/fixtures/negative/activation/contract-missing/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/contract-missing/task/TRACE.md` | `./tests/fixtures/negative/activation/contract-missing/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/approvals/approval.md` | `./tests/fixtures/negative/activation/dry-run-does-not-write/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/REVIEW.md` | `./tests/fixtures/negative/activation/dry-run-does-not-write/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TASK.md` | `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TRACE.md` | `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/expired-approval-marker/approvals/approval.md` | `./tests/fixtures/negative/activation/expired-approval-marker/approvals/approval 2.md` | EXACT_COPY | 316 vs 316 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/REVIEW.md` | `./tests/fixtures/negative/activation/expired-approval-marker/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/TASK.md` | `./tests/fixtures/negative/activation/expired-approval-marker/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/TRACE.md` | `./tests/fixtures/negative/activation/expired-approval-marker/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/invalid-approval-marker/approvals/approval.md` | `./tests/fixtures/negative/activation/invalid-approval-marker/approvals/approval 2.md` | EXACT_COPY | 16 vs 16 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/REVIEW.md` | `./tests/fixtures/negative/activation/invalid-approval-marker/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/TASK.md` | `./tests/fixtures/negative/activation/invalid-approval-marker/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/TRACE.md` | `./tests/fixtures/negative/activation/invalid-approval-marker/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approval-marker/approvals/approval.md` | `./tests/fixtures/negative/activation/missing-approval-marker/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/REVIEW.md` | `./tests/fixtures/negative/activation/missing-approval-marker/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/TASK.md` | `./tests/fixtures/negative/activation/missing-approval-marker/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/TRACE.md` | `./tests/fixtures/negative/activation/missing-approval-marker/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approved-flag/approvals/approval.md` | `./tests/fixtures/negative/activation/missing-approved-flag/approvals/approval 2.md` | EXACT_COPY | 294 vs 294 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/REVIEW.md` | `./tests/fixtures/negative/activation/missing-approved-flag/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/TASK.md` | `./tests/fixtures/negative/activation/missing-approved-flag/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/TRACE.md` | `./tests/fixtures/negative/activation/missing-approved-flag/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/revoked-approval-marker/approvals/approval.md` | `./tests/fixtures/negative/activation/revoked-approval-marker/approvals/approval 2.md` | EXACT_COPY | 316 vs 316 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/REVIEW.md` | `./tests/fixtures/negative/activation/revoked-approval-marker/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/TASK.md` | `./tests/fixtures/negative/activation/revoked-approval-marker/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/TRACE.md` | `./tests/fixtures/negative/activation/revoked-approval-marker/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-scope/approvals/approval.md` | `./tests/fixtures/negative/activation/wrong-scope/approvals/approval 2.md` | EXACT_COPY | 289 vs 289 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-scope/task/REVIEW.md` | `./tests/fixtures/negative/activation/wrong-scope/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-scope/task/TASK.md` | `./tests/fixtures/negative/activation/wrong-scope/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-scope/task/TRACE.md` | `./tests/fixtures/negative/activation/wrong-scope/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-task-id/approvals/approval.md` | `./tests/fixtures/negative/activation/wrong-task-id/approvals/approval 2.md` | EXACT_COPY | 283 vs 283 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-task-id/task/REVIEW.md` | `./tests/fixtures/negative/activation/wrong-task-id/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-task-id/task/TASK.md` | `./tests/fixtures/negative/activation/wrong-task-id/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-task-id/task/TRACE.md` | `./tests/fixtures/negative/activation/wrong-task-id/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-transition/approvals/approval.md` | `./tests/fixtures/negative/activation/wrong-transition/approvals/approval 2.md` | EXACT_COPY | 270 vs 270 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-transition/task/REVIEW.md` | `./tests/fixtures/negative/activation/wrong-transition/task/REVIEW 2.md` | EXACT_COPY | 62 vs 62 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-transition/task/TASK.md` | `./tests/fixtures/negative/activation/wrong-transition/task/TASK 2.md` | EXACT_COPY | 32 vs 32 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/activation/wrong-transition/task/TRACE.md` | `./tests/fixtures/negative/activation/wrong-transition/task/TRACE 2.md` | EXACT_COPY | 14 vs 14 | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/README.md` | `./tests/fixtures/negative/active-task/activated-by-unknown-value/README 2.md` | EXACT_COPY | 155 vs 155 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/active-task.md` | `./tests/fixtures/negative/active-task/activated-by-unknown-value/active-task 2.md` | EXACT_COPY | 393 vs 393 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-contract.md` | `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-task.md` | `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/README.md` | `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/README 2.md` | EXACT_COPY | 246 vs 246 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/active-task.md` | `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/active-task 2.md` | EXACT_COPY | 397 vs 397 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-contract.md` | `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-task.md` | `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/invalid-activated-at/README.md` | `./tests/fixtures/negative/active-task/invalid-activated-at/README 2.md` | EXACT_COPY | 149 vs 149 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/invalid-activated-at/active-task.md` | `./tests/fixtures/negative/active-task/invalid-activated-at/active-task 2.md` | EXACT_COPY | 372 vs 372 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/invalid-activated-at/source-contract.md` | `./tests/fixtures/negative/active-task/invalid-activated-at/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/invalid-activated-at/source-task.md` | `./tests/fixtures/negative/active-task/invalid-activated-at/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/malformed-yaml/README.md` | `./tests/fixtures/negative/active-task/malformed-yaml/README 2.md` | EXACT_COPY | 143 vs 143 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/malformed-yaml/active-task.md` | `./tests/fixtures/negative/active-task/malformed-yaml/active-task 2.md` | EXACT_COPY | 360 vs 360 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/malformed-yaml/source-contract.md` | `./tests/fixtures/negative/active-task/malformed-yaml/source-contract 2.md` | EXACT_COPY | 26 vs 26 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/malformed-yaml/source-task.md` | `./tests/fixtures/negative/active-task/malformed-yaml/source-task 2.md` | EXACT_COPY | 26 vs 26 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-at/README.md` | `./tests/fixtures/negative/active-task/missing-activated-at/README 2.md` | EXACT_COPY | 149 vs 149 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-at/active-task.md` | `./tests/fixtures/negative/active-task/missing-activated-at/active-task 2.md` | EXACT_COPY | 352 vs 352 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-at/source-contract.md` | `./tests/fixtures/negative/active-task/missing-activated-at/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-at/source-task.md` | `./tests/fixtures/negative/active-task/missing-activated-at/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-by/README.md` | `./tests/fixtures/negative/active-task/missing-activated-by/README 2.md` | EXACT_COPY | 149 vs 149 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-by/active-task.md` | `./tests/fixtures/negative/active-task/missing-activated-by/active-task 2.md` | EXACT_COPY | 350 vs 350 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-by/source-contract.md` | `./tests/fixtures/negative/active-task/missing-activated-by/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-activated-by/source-task.md` | `./tests/fixtures/negative/active-task/missing-activated-by/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-active-task/README.md` | `./tests/fixtures/negative/active-task/missing-active-task/README 2.md` | EXACT_COPY | 176 vs 176 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-approval-id/README.md` | `./tests/fixtures/negative/active-task/missing-approval-id/README 2.md` | EXACT_COPY | 148 vs 148 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-approval-id/active-task.md` | `./tests/fixtures/negative/active-task/missing-approval-id/active-task 2.md` | EXACT_COPY | 344 vs 344 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-approval-id/source-contract.md` | `./tests/fixtures/negative/active-task/missing-approval-id/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-approval-id/source-task.md` | `./tests/fixtures/negative/active-task/missing-approval-id/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-frontmatter/README.md` | `./tests/fixtures/negative/active-task/missing-frontmatter/README 2.md` | EXACT_COPY | 148 vs 148 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-frontmatter/active-task.md` | `./tests/fixtures/negative/active-task/missing-frontmatter/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-contract/README.md` | `./tests/fixtures/negative/active-task/missing-source-contract/README 2.md` | EXACT_COPY | 209 vs 209 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-contract/active-task.md` | `./tests/fixtures/negative/active-task/missing-source-contract/active-task 2.md` | EXACT_COPY | 297 vs 297 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-contract/source-contract.md` | `./tests/fixtures/negative/active-task/missing-source-contract/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-contract/source-task.md` | `./tests/fixtures/negative/active-task/missing-source-contract/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-task/README.md` | `./tests/fixtures/negative/active-task/missing-source-task/README 2.md` | EXACT_COPY | 201 vs 201 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-task/active-task.md` | `./tests/fixtures/negative/active-task/missing-source-task/active-task 2.md` | EXACT_COPY | 301 vs 301 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-task/source-contract.md` | `./tests/fixtures/negative/active-task/missing-source-task/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-source-task/source-task.md` | `./tests/fixtures/negative/active-task/missing-source-task/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-state/README.md` | `./tests/fixtures/negative/active-task/missing-state/README 2.md` | EXACT_COPY | 142 vs 142 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/active-task/missing-state/active-task.md` | `./tests/fixtures/negative/active-task/missing-state/active-task 2.md` | EXACT_COPY | 359 vs 359 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/active-task/missing-state/source-contract.md` | `./tests/fixtures/negative/active-task/missing-state/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/active-task/missing-state/source-task.md` | `./tests/fixtures/negative/active-task/missing-state/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/active-task/missing-task-id/README.md` | `./tests/fixtures/negative/active-task/missing-task-id/README 2.md` | EXACT_COPY | 144 vs 144 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-task-id/active-task.md` | `./tests/fixtures/negative/active-task/missing-task-id/active-task 2.md` | EXACT_COPY | 359 vs 359 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-task-id/source-contract.md` | `./tests/fixtures/negative/active-task/missing-task-id/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-task-id/source-task.md` | `./tests/fixtures/negative/active-task/missing-task-id/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-transition/README.md` | `./tests/fixtures/negative/active-task/missing-transition/README 2.md` | EXACT_COPY | 147 vs 147 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-transition/active-task.md` | `./tests/fixtures/negative/active-task/missing-transition/active-task 2.md` | EXACT_COPY | 341 vs 341 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-transition/source-contract.md` | `./tests/fixtures/negative/active-task/missing-transition/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/missing-transition/source-task.md` | `./tests/fixtures/negative/active-task/missing-transition/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/README.md` | `./tests/fixtures/negative/active-task/source-contract-absolute-path/README 2.md` | EXACT_COPY | 158 vs 158 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/active-task.md` | `./tests/fixtures/negative/active-task/source-contract-absolute-path/active-task 2.md` | EXACT_COPY | 339 vs 339 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-contract.md` | `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-task.md` | `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-missing/README.md` | `./tests/fixtures/negative/active-task/source-contract-missing/README 2.md` | EXACT_COPY | 210 vs 210 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-missing/active-task.md` | `./tests/fixtures/negative/active-task/source-contract-missing/active-task 2.md` | EXACT_COPY | 394 vs 394 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-missing/source-contract.md` | `./tests/fixtures/negative/active-task/source-contract-missing/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-missing/source-task.md` | `./tests/fixtures/negative/active-task/source-contract-missing/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/README.md` | `./tests/fixtures/negative/active-task/source-contract-parent-traversal/README 2.md` | EXACT_COPY | 161 vs 161 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/active-task.md` | `./tests/fixtures/negative/active-task/source-contract-parent-traversal/active-task 2.md` | EXACT_COPY | 347 vs 347 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-contract.md` | `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-task.md` | `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/README.md` | `./tests/fixtures/negative/active-task/source-task-absolute-path/README 2.md` | EXACT_COPY | 154 vs 154 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/active-task.md` | `./tests/fixtures/negative/active-task/source-task-absolute-path/active-task 2.md` | EXACT_COPY | 332 vs 332 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/source-contract.md` | `./tests/fixtures/negative/active-task/source-task-absolute-path/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/source-task.md` | `./tests/fixtures/negative/active-task/source-task-absolute-path/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-missing/README.md` | `./tests/fixtures/negative/active-task/source-task-missing/README 2.md` | EXACT_COPY | 202 vs 202 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-missing/active-task.md` | `./tests/fixtures/negative/active-task/source-task-missing/active-task 2.md` | EXACT_COPY | 386 vs 386 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-missing/source-contract.md` | `./tests/fixtures/negative/active-task/source-task-missing/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-missing/source-task.md` | `./tests/fixtures/negative/active-task/source-task-missing/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/README.md` | `./tests/fixtures/negative/active-task/source-task-parent-traversal/README 2.md` | EXACT_COPY | 157 vs 157 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/active-task.md` | `./tests/fixtures/negative/active-task/source-task-parent-traversal/active-task 2.md` | EXACT_COPY | 341 vs 341 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-contract.md` | `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-task.md` | `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/state-not-active/README.md` | `./tests/fixtures/negative/active-task/state-not-active/README 2.md` | EXACT_COPY | 145 vs 145 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/state-not-active/active-task.md` | `./tests/fixtures/negative/active-task/state-not-active/active-task 2.md` | EXACT_COPY | 379 vs 379 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/state-not-active/source-contract.md` | `./tests/fixtures/negative/active-task/state-not-active/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/state-not-active/source-task.md` | `./tests/fixtures/negative/active-task/state-not-active/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/README.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/README 2.md` | EXACT_COPY | 161 vs 161 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/active-task.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/active-task 2.md` | EXACT_COPY | 411 vs 411 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-contract.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-contract 2.md` | EXACT_COPY | 26 vs 26 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-task.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/README.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/README 2.md` | EXACT_COPY | 157 vs 157 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/active-task.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/active-task 2.md` | EXACT_COPY | 403 vs 403 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-contract.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-task.md` | `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-task 2.md` | EXACT_COPY | 26 vs 26 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/wrong-transition/README.md` | `./tests/fixtures/negative/active-task/wrong-transition/README 2.md` | EXACT_COPY | 145 vs 145 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/wrong-transition/active-task.md` | `./tests/fixtures/negative/active-task/wrong-transition/active-task 2.md` | EXACT_COPY | 366 vs 366 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/wrong-transition/source-contract.md` | `./tests/fixtures/negative/active-task/wrong-transition/source-contract 2.md` | EXACT_COPY | 37 vs 37 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/active-task/wrong-transition/source-task.md` | `./tests/fixtures/negative/active-task/wrong-transition/source-task 2.md` | EXACT_COPY | 43 vs 43 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval.md` | `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval 2.md` | EXACT_COPY | 252 vs 252 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval-duplicate.md` | `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval-duplicate 2.md` | EXACT_COPY | 252 vs 252 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/expired-marker/approval.md` | `./tests/fixtures/negative/approval-markers/expired-marker/approval 2.md` | EXACT_COPY | 276 vs 276 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/invalid-transition-scope/approval.md` | `./tests/fixtures/negative/approval-markers/invalid-transition-scope/approval 2.md` | EXACT_COPY | 262 vs 262 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/malformed-approved-at/approval.md` | `./tests/fixtures/negative/approval-markers/malformed-approved-at/approval 2.md` | EXACT_COPY | 255 vs 255 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/missing-related-contract/approval.md` | `./tests/fixtures/negative/approval-markers/missing-related-contract/approval 2.md` | EXACT_COPY | 267 vs 267 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/missing-required-field/approval.md` | `./tests/fixtures/negative/approval-markers/missing-required-field/approval 2.md` | EXACT_COPY | 269 vs 269 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/revoked-marker/approval.md` | `./tests/fixtures/negative/approval-markers/revoked-marker/approval 2.md` | EXACT_COPY | 308 vs 308 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/superseded-marker/approval.md` | `./tests/fixtures/negative/approval-markers/superseded-marker/approval 2.md` | EXACT_COPY | 293 vs 293 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/wrong-scope/approval.md` | `./tests/fixtures/negative/approval-markers/wrong-scope/approval 2.md` | EXACT_COPY | 256 vs 256 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/approval-markers/wrong-task-id/approval.md` | `./tests/fixtures/negative/approval-markers/wrong-task-id/approval 2.md` | EXACT_COPY | 260 vs 260 | 6157be6 feat(m10.16.1): approval marker negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/blocked-review-status.md` | `./tests/fixtures/negative/contract-draft/blocked-review-status 2.md` | EXACT_COPY | 263 vs 263 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/execution-allowed-false.md` | `./tests/fixtures/negative/contract-draft/execution-allowed-false 2.md` | EXACT_COPY | 285 vs 285 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/execution-approved.md` | `./tests/fixtures/negative/contract-draft/execution-approved 2.md` | EXACT_COPY | 312 vs 312 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/invalid-execution-allowed.md` | `./tests/fixtures/negative/contract-draft/invalid-execution-allowed 2.md` | EXACT_COPY | 289 vs 289 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-close.md` | `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-close 2.md` | EXACT_COPY | 286 vs 286 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-open.md` | `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-open 2.md` | EXACT_COPY | 258 vs 258 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-execution-allowed.md` | `./tests/fixtures/negative/contract-draft/missing-execution-allowed 2.md` | EXACT_COPY | 266 vs 266 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-generated-from-task.md` | `./tests/fixtures/negative/contract-draft/missing-generated-from-task 2.md` | EXACT_COPY | 226 vs 226 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-review-file.md` | `./tests/fixtures/negative/contract-draft/missing-review-file 2.md` | EXACT_COPY | 232 vs 232 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-review-status.md` | `./tests/fixtures/negative/contract-draft/missing-review-status 2.md` | EXACT_COPY | 281 vs 281 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-risk-section.md` | `./tests/fixtures/negative/contract-draft/missing-risk-section 2.md` | EXACT_COPY | 231 vs 231 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-task-id.md` | `./tests/fixtures/negative/contract-draft/missing-task-id 2.md` | EXACT_COPY | 238 vs 238 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/missing-verification-section.md` | `./tests/fixtures/negative/contract-draft/missing-verification-section 2.md` | EXACT_COPY | 265 vs 265 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-draft/replaces-active-task.md` | `./tests/fixtures/negative/contract-draft/replaces-active-task 2.md` | EXACT_COPY | 307 vs 307 | 9edebde feat(8.4.2): wire contract draft negative fixtures | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/README.md` | `./tests/fixtures/negative/contract-generation/draft-already-exists/README 2.md` | EXACT_COPY | 645 vs 645 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft.md` | `./tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft 2.md` | EXACT_COPY | 74 vs 74 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW.md` | `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW 2.md` | EXACT_COPY | 335 vs 335 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK.md` | `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK 2.md` | EXACT_COPY | 758 vs 758 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/README.md` | `./tests/fixtures/negative/contract-generation/execution-not-allowed/README 2.md` | EXACT_COPY | 615 vs 615 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW.md` | `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW 2.md` | EXACT_COPY | 343 vs 343 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK.md` | `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK 2.md` | EXACT_COPY | 759 vs 759 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/missing-review/README.md` | `./tests/fixtures/negative/contract-generation/missing-review/README 2.md` | EXACT_COPY | 598 vs 598 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/missing-review/task-example/TASK.md` | `./tests/fixtures/negative/contract-generation/missing-review/task-example/TASK 2.md` | EXACT_COPY | 632 vs 632 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/review-not-ready/README.md` | `./tests/fixtures/negative/contract-generation/review-not-ready/README 2.md` | EXACT_COPY | 630 vs 630 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW.md` | `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW 2.md` | EXACT_COPY | 316 vs 316 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK.md` | `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK 2.md` | EXACT_COPY | 754 vs 754 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-absolute-path-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-absolute-path-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/active-task.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/active-task 2.md` | EXACT_COPY | 41 vs 41 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/active-task.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/active-task 2.md` | EXACT_COPY | 210 vs 210 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/active-task.md` | `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/active-task 2.md` | EXACT_COPY | 243 vs 243 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run/README.md` | `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-start/README.md` | `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-start/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/README.md` | `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/session.md` | `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/session 2.md` | EXACT_COPY | 951 vs 951 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/source-contract.md` | `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/source-contract 2.md` | EXACT_COPY | 84 vs 84 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/README.md` | `./tests/fixtures/negative/execution-runner/blocked-session-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/session.md` | `./tests/fixtures/negative/execution-runner/blocked-session-scope/session 2.md` | EXACT_COPY | 928 vs 928 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/source-contract.md` | `./tests/fixtures/negative/execution-runner/blocked-session-scope/source-contract 2.md` | EXACT_COPY | 60 vs 60 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/README.md` | `./tests/fixtures/negative/execution-runner/blocked-session-verification/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/session.md` | `./tests/fixtures/negative/execution-runner/blocked-session-verification/session 2.md` | EXACT_COPY | 942 vs 942 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/source-contract.md` | `./tests/fixtures/negative/execution-runner/blocked-session-verification/source-contract 2.md` | EXACT_COPY | 79 vs 79 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/README.md` | `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/session.md` | `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/session 2.md` | EXACT_COPY | 954 vs 954 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/source-contract.md` | `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/source-contract 2.md` | EXACT_COPY | 60 vs 60 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/README.md` | `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/session.md` | `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/session 2.md` | EXACT_COPY | 948 vs 948 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/source-contract.md` | `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/source-contract 2.md` | EXACT_COPY | 60 vs 60 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/README.md` | `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/session.md` | `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/session 2.md` | EXACT_COPY | 948 vs 948 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/source-contract.md` | `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/source-contract 2.md` | EXACT_COPY | 31 vs 31 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/README.md` | `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/session.md` | `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/session 2.md` | EXACT_COPY | 958 vs 958 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/source-contract.md` | `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/source-contract 2.md` | EXACT_COPY | 60 vs 60 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/README.md` | `./tests/fixtures/negative/execution-runner/missing-verification-plan/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/session.md` | `./tests/fixtures/negative/execution-runner/missing-verification-plan/session 2.md` | EXACT_COPY | 923 vs 923 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/source-contract.md` | `./tests/fixtures/negative/execution-runner/missing-verification-plan/source-contract 2.md` | EXACT_COPY | 53 vs 53 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/README.md` | `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/session.md` | `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/session 2.md` | EXACT_COPY | 944 vs 944 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/source-contract.md` | `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/source-contract 2.md` | EXACT_COPY | 31 vs 31 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/session-absolute-path-scope/README.md` | `./tests/fixtures/negative/execution-runner/session-absolute-path-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/README.md` | `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/session.md` | `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/session 2.md` | EXACT_COPY | 963 vs 963 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/session-parent-traversal-scope/README.md` | `./tests/fixtures/negative/execution-runner/session-parent-traversal-scope/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/session-parent-traversal-verification/README.md` | `./tests/fixtures/negative/execution-runner/session-parent-traversal-verification/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/shared/source-task.md` | `./tests/fixtures/negative/execution-runner/shared/source-task 2.md` | EXACT_COPY | 21 vs 21 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/README.md` | `./tests/fixtures/negative/execution-runner/stopped-session-verification/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/session.md` | `./tests/fixtures/negative/execution-runner/stopped-session-verification/session 2.md` | EXACT_COPY | 937 vs 937 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/source-contract.md` | `./tests/fixtures/negative/execution-runner/stopped-session-verification/source-contract 2.md` | EXACT_COPY | 79 vs 79 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/README.md` | `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/session.md` | `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/session 2.md` | EXACT_COPY | 943 vs 943 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/source-contract.md` | `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/README.md` | `./tests/fixtures/negative/execution-runner/verification-absolute-executable/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/session.md` | `./tests/fixtures/negative/execution-runner/verification-absolute-executable/session 2.md` | EXACT_COPY | 937 vs 937 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-absolute-executable/source-contract 2.md` | EXACT_COPY | 67 vs 67 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/README.md` | `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/session.md` | `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/session 2.md` | EXACT_COPY | 951 vs 951 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/source-contract 2.md` | EXACT_COPY | 77 vs 77 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/README.md` | `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/session.md` | `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/session 2.md` | EXACT_COPY | 939 vs 939 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/source-contract 2.md` | EXACT_COPY | 48 vs 48 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/README.md` | `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/session.md` | `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/session 2.md` | EXACT_COPY | 949 vs 949 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/source-contract 2.md` | EXACT_COPY | 53 vs 53 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/README.md` | `./tests/fixtures/negative/execution-runner/verification-shell-operator/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/session.md` | `./tests/fixtures/negative/execution-runner/verification-shell-operator/session 2.md` | EXACT_COPY | 927 vs 927 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-shell-operator/source-contract 2.md` | EXACT_COPY | 72 vs 72 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/README.md` | `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/README 2.md` | EXACT_COPY | 99 vs 99 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/session.md` | `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/session 2.md` | EXACT_COPY | 943 vs 943 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/source-contract.md` | `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/source-contract 2.md` | EXACT_COPY | 56 vs 56 | 17b9664 feat(m13): save controlled execution runner milestone artifacts | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/blocked-by-not-list.md` | `./tests/fixtures/negative/queue/blocked-by-not-list 2.md` | EXACT_COPY | 138 vs 138 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/blocked-with-empty-blocked-by.md` | `./tests/fixtures/negative/queue/blocked-with-empty-blocked-by 2.md` | EXACT_COPY | 144 vs 144 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/empty-task-id.md` | `./tests/fixtures/negative/queue/empty-task-id 2.md` | EXACT_COPY | 117 vs 117 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/malformed-frontmatter.md` | `./tests/fixtures/negative/queue/malformed-frontmatter 2.md` | EXACT_COPY | 128 vs 128 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/missing-blocked-by.md` | `./tests/fixtures/negative/queue/missing-blocked-by 2.md` | EXACT_COPY | 114 vs 114 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/missing-priority.md` | `./tests/fixtures/negative/queue/missing-priority 2.md` | EXACT_COPY | 110 vs 110 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/missing-status.md` | `./tests/fixtures/negative/queue/missing-status 2.md` | EXACT_COPY | 110 vs 110 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/missing-task-id.md` | `./tests/fixtures/negative/queue/missing-task-id 2.md` | EXACT_COPY | 104 vs 104 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/unknown-priority.md` | `./tests/fixtures/negative/queue/unknown-priority 2.md` | EXACT_COPY | 140 vs 140 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/queue/unknown-status.md` | `./tests/fixtures/negative/queue/unknown-status 2.md` | EXACT_COPY | 140 vs 140 | 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/README.md` | `./tests/fixtures/negative/readiness/active-task-validation-fail/README 2.md` | EXACT_COPY | 221 vs 221 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/active-task.md` | `./tests/fixtures/negative/readiness/active-task-validation-fail/active-task 2.md` | EXACT_COPY | 412 vs 412 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/approvals/approval-active-task-validation-fail.md` | `./tests/fixtures/negative/readiness/active-task-validation-fail/approvals/approval-active-task-validation-fail 2.md` | EXACT_COPY | 357 vs 357 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/source-contract.md` | `./tests/fixtures/negative/readiness/active-task-validation-fail/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/source-task.md` | `./tests/fixtures/negative/readiness/active-task-validation-fail/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/README.md` | `./tests/fixtures/negative/readiness/active-task-validation-partial/README 2.md` | EXACT_COPY | 248 vs 248 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/active-task.md` | `./tests/fixtures/negative/readiness/active-task-validation-partial/active-task 2.md` | EXACT_COPY | 421 vs 421 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/approvals/approval-active-task-validation-partial.md` | `./tests/fixtures/negative/readiness/active-task-validation-partial/approvals/approval-active-task-validation-partial 2.md` | EXACT_COPY | 363 vs 363 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/source-contract.md` | `./tests/fixtures/negative/readiness/active-task-validation-partial/source-contract 2.md` | EXACT_COPY | 30 vs 30 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/source-task.md` | `./tests/fixtures/negative/readiness/active-task-validation-partial/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/README.md` | `./tests/fixtures/negative/readiness/analysis-status-conflict/README 2.md` | EXACT_COPY | 205 vs 205 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/active-task.md` | `./tests/fixtures/negative/readiness/analysis-status-conflict/active-task 2.md` | EXACT_COPY | 403 vs 403 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/approvals/approval-analysis-status-conflict.md` | `./tests/fixtures/negative/readiness/analysis-status-conflict/approvals/approval-analysis-status-conflict 2.md` | EXACT_COPY | 351 vs 351 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/source-contract.md` | `./tests/fixtures/negative/readiness/analysis-status-conflict/source-contract 2.md` | EXACT_COPY | 69 vs 69 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/source-task.md` | `./tests/fixtures/negative/readiness/analysis-status-conflict/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/README.md` | `./tests/fixtures/negative/readiness/analysis-status-invalid/README 2.md` | EXACT_COPY | 203 vs 203 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/active-task.md` | `./tests/fixtures/negative/readiness/analysis-status-invalid/active-task 2.md` | EXACT_COPY | 400 vs 400 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/approvals/approval-analysis-status-invalid.md` | `./tests/fixtures/negative/readiness/analysis-status-invalid/approvals/approval-analysis-status-invalid 2.md` | EXACT_COPY | 349 vs 349 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/source-contract.md` | `./tests/fixtures/negative/readiness/analysis-status-invalid/source-contract 2.md` | EXACT_COPY | 68 vs 68 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/source-task.md` | `./tests/fixtures/negative/readiness/analysis-status-invalid/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/README.md` | `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/README 2.md` | EXACT_COPY | 381 vs 381 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/active-task.md` | `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-contract.md` | `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-task.md` | `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/README.md` | `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/README 2.md` | EXACT_COPY | 350 vs 350 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/active-task.md` | `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-contract.md` | `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-task.md` | `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-expired/README.md` | `./tests/fixtures/negative/readiness/approval-marker-expired/README 2.md` | EXACT_COPY | 206 vs 206 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-expired/active-task.md` | `./tests/fixtures/negative/readiness/approval-marker-expired/active-task 2.md` | EXACT_COPY | 400 vs 400 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-expired/approvals/approval-approval-marker-expired.md` | `./tests/fixtures/negative/readiness/approval-marker-expired/approvals/approval-approval-marker-expired 2.md` | EXACT_COPY | 382 vs 382 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-expired/source-contract.md` | `./tests/fixtures/negative/readiness/approval-marker-expired/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-expired/source-task.md` | `./tests/fixtures/negative/readiness/approval-marker-expired/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/README.md` | `./tests/fixtures/negative/readiness/approval-marker-invalid/README 2.md` | EXACT_COPY | 196 vs 196 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/active-task.md` | `./tests/fixtures/negative/readiness/approval-marker-invalid/active-task 2.md` | EXACT_COPY | 400 vs 400 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/approvals/approval-approval-marker-invalid.md` | `./tests/fixtures/negative/readiness/approval-marker-invalid/approvals/approval-approval-marker-invalid 2.md` | EXACT_COPY | 351 vs 351 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/source-contract.md` | `./tests/fixtures/negative/readiness/approval-marker-invalid/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/source-task.md` | `./tests/fixtures/negative/readiness/approval-marker-invalid/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/README.md` | `./tests/fixtures/negative/readiness/approval-marker-malformed/README 2.md` | EXACT_COPY | 200 vs 200 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/active-task.md` | `./tests/fixtures/negative/readiness/approval-marker-malformed/active-task 2.md` | EXACT_COPY | 406 vs 406 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/approvals/approval-approval-marker-malformed.md` | `./tests/fixtures/negative/readiness/approval-marker-malformed/approvals/approval-approval-marker-malformed 2.md` | EXACT_COPY | 79 vs 79 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/source-contract.md` | `./tests/fixtures/negative/readiness/approval-marker-malformed/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/source-task.md` | `./tests/fixtures/negative/readiness/approval-marker-malformed/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/README.md` | `./tests/fixtures/negative/readiness/approval-marker-revoked/README 2.md` | EXACT_COPY | 184 vs 184 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/active-task.md` | `./tests/fixtures/negative/readiness/approval-marker-revoked/active-task 2.md` | EXACT_COPY | 400 vs 400 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/approvals/approval-approval-marker-revoked.md` | `./tests/fixtures/negative/readiness/approval-marker-revoked/approvals/approval-approval-marker-revoked 2.md` | EXACT_COPY | 348 vs 348 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/source-contract.md` | `./tests/fixtures/negative/readiness/approval-marker-revoked/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/source-task.md` | `./tests/fixtures/negative/readiness/approval-marker-revoked/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/README.md` | `./tests/fixtures/negative/readiness/approval-marker-unresolved/README 2.md` | EXACT_COPY | 231 vs 231 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/active-task.md` | `./tests/fixtures/negative/readiness/approval-marker-unresolved/active-task 2.md` | EXACT_COPY | 409 vs 409 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-contract.md` | `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-task.md` | `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/README.md` | `./tests/fixtures/negative/readiness/approval-scope-mismatch/README 2.md` | EXACT_COPY | 204 vs 204 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/active-task.md` | `./tests/fixtures/negative/readiness/approval-scope-mismatch/active-task 2.md` | EXACT_COPY | 400 vs 400 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/approvals/approval-approval-scope-mismatch.md` | `./tests/fixtures/negative/readiness/approval-scope-mismatch/approvals/approval-approval-scope-mismatch 2.md` | EXACT_COPY | 347 vs 347 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-contract.md` | `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-task.md` | `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/README.md` | `./tests/fixtures/negative/readiness/approval-task-id-mismatch/README 2.md` | EXACT_COPY | 209 vs 209 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/active-task.md` | `./tests/fixtures/negative/readiness/approval-task-id-mismatch/active-task 2.md` | EXACT_COPY | 406 vs 406 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals/approval-approval-task-id-mismatch.md` | `./tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals/approval-approval-task-id-mismatch 2.md` | EXACT_COPY | 349 vs 349 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-contract.md` | `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-task.md` | `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/README.md` | `./tests/fixtures/negative/readiness/approval-transition-mismatch/README 2.md` | EXACT_COPY | 230 vs 230 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/active-task.md` | `./tests/fixtures/negative/readiness/approval-transition-mismatch/active-task 2.md` | EXACT_COPY | 415 vs 415 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/approvals/approval-approval-transition-mismatch.md` | `./tests/fixtures/negative/readiness/approval-transition-mismatch/approvals/approval-approval-transition-mismatch 2.md` | EXACT_COPY | 346 vs 346 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-contract.md` | `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-contract 2.md` | EXACT_COPY | 63 vs 63 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-task.md` | `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-task 2.md` | EXACT_COPY | 49 vs 49 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-completed/README.md` | `./tests/fixtures/negative/readiness/detected-state-completed/README 2.md` | EXACT_COPY | 359 vs 359 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-completed/active-task.md` | `./tests/fixtures/negative/readiness/detected-state-completed/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-completed/source-contract.md` | `./tests/fixtures/negative/readiness/detected-state-completed/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-completed/source-task.md` | `./tests/fixtures/negative/readiness/detected-state-completed/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-conflict/README.md` | `./tests/fixtures/negative/readiness/detected-state-conflict/README 2.md` | EXACT_COPY | 358 vs 358 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-conflict/active-task.md` | `./tests/fixtures/negative/readiness/detected-state-conflict/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-conflict/source-contract.md` | `./tests/fixtures/negative/readiness/detected-state-conflict/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-conflict/source-task.md` | `./tests/fixtures/negative/readiness/detected-state-conflict/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-dropped/README.md` | `./tests/fixtures/negative/readiness/detected-state-dropped/README 2.md` | EXACT_COPY | 357 vs 357 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-dropped/active-task.md` | `./tests/fixtures/negative/readiness/detected-state-dropped/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-dropped/source-contract.md` | `./tests/fixtures/negative/readiness/detected-state-dropped/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-dropped/source-task.md` | `./tests/fixtures/negative/readiness/detected-state-dropped/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-failed/README.md` | `./tests/fixtures/negative/readiness/detected-state-failed/README 2.md` | EXACT_COPY | 356 vs 356 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-failed/active-task.md` | `./tests/fixtures/negative/readiness/detected-state-failed/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-failed/source-contract.md` | `./tests/fixtures/negative/readiness/detected-state-failed/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-failed/source-task.md` | `./tests/fixtures/negative/readiness/detected-state-failed/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-invalid/README.md` | `./tests/fixtures/negative/readiness/detected-state-invalid/README 2.md` | EXACT_COPY | 357 vs 357 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-invalid/active-task.md` | `./tests/fixtures/negative/readiness/detected-state-invalid/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-invalid/source-contract.md` | `./tests/fixtures/negative/readiness/detected-state-invalid/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/detected-state-invalid/source-task.md` | `./tests/fixtures/negative/readiness/detected-state-invalid/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/README.md` | `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/README 2.md` | EXACT_COPY | 368 vs 368 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/active-task.md` | `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-contract.md` | `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-task.md` | `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-state-validator/README.md` | `./tests/fixtures/negative/readiness/missing-state-validator/README 2.md` | EXACT_COPY | 331 vs 331 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-state-validator/active-task.md` | `./tests/fixtures/negative/readiness/missing-state-validator/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-state-validator/source-contract.md` | `./tests/fixtures/negative/readiness/missing-state-validator/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/missing-state-validator/source-task.md` | `./tests/fixtures/negative/readiness/missing-state-validator/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/README.md` | `./tests/fixtures/negative/readiness/validate-task-state-fail/README 2.md` | EXACT_COPY | 340 vs 340 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/active-task.md` | `./tests/fixtures/negative/readiness/validate-task-state-fail/active-task 2.md` | EXACT_COPY | 27 vs 27 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/source-contract.md` | `./tests/fixtures/negative/readiness/validate-task-state-fail/source-contract 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/source-task.md` | `./tests/fixtures/negative/readiness/validate-task-state-fail/source-task 2.md` | EXACT_COPY | 10 vs 10 | 04184f7 feat(m12): finalize active task governance and readiness reports | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/blocked-but-execution-true/README.md` | `./tests/fixtures/negative/review/blocked-but-execution-true/README 2.md` | EXACT_COPY | 536 vs 536 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/blocked-but-execution-true/REVIEW.md` | `./tests/fixtures/negative/review/blocked-but-execution-true/REVIEW 2.md` | EXACT_COPY | 315 vs 315 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/blocked-but-execution-true.md` | `./tests/fixtures/negative/review/blocked-but-execution-true 2.md` | EXACT_COPY | 122 vs 122 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/missing-execution-allowed.md` | `./tests/fixtures/negative/review/missing-execution-allowed 2.md` | EXACT_COPY | 38 vs 38 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/missing-review-status/README.md` | `./tests/fixtures/negative/review/missing-review-status/README 2.md` | EXACT_COPY | 453 vs 453 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/missing-review-status/REVIEW.md` | `./tests/fixtures/negative/review/missing-review-status/REVIEW 2.md` | EXACT_COPY | 268 vs 268 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/missing-review-status.md` | `./tests/fixtures/negative/review/missing-review-status 2.md` | EXACT_COPY | 41 vs 41 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/ready-but-execution-false/README.md` | `./tests/fixtures/negative/review/ready-but-execution-false/README 2.md` | EXACT_COPY | 530 vs 530 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/ready-but-execution-false/REVIEW.md` | `./tests/fixtures/negative/review/ready-but-execution-false/REVIEW 2.md` | EXACT_COPY | 309 vs 309 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/ready-but-execution-false.md` | `./tests/fixtures/negative/review/ready-but-execution-false 2.md` | EXACT_COPY | 118 vs 118 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/review/unknown-review-status.md` | `./tests/fixtures/negative/review/unknown-review-status 2.md` | EXACT_COPY | 71 vs 71 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/approved-mode-requested/README.md` | `./tests/fixtures/negative/runner/approved-mode-requested/README 2.md` | EXACT_COPY | 471 vs 471 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/approved-mode-requested/scenario.md` | `./tests/fixtures/negative/runner/approved-mode-requested/scenario 2.md` | EXACT_COPY | 302 vs 302 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/attempts-active-task-replace/README.md` | `./tests/fixtures/negative/runner/attempts-active-task-replace/README 2.md` | EXACT_COPY | 509 vs 509 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/attempts-active-task-replace/scenario.md` | `./tests/fixtures/negative/runner/attempts-active-task-replace/scenario 2.md` | EXACT_COPY | 297 vs 297 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/missing-human-checkpoint/README.md` | `./tests/fixtures/negative/runner/missing-human-checkpoint/README 2.md` | EXACT_COPY | 475 vs 475 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/runner/missing-human-checkpoint/scenario.md` | `./tests/fixtures/negative/runner/missing-human-checkpoint/scenario 2.md` | EXACT_COPY | 310 vs 310 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/state/active-without-approval/README.md` | `./tests/fixtures/negative/state/active-without-approval/README 2.md` | EXACT_COPY | 92 vs 92 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/state/completed-and-active-conflict/README.md` | `./tests/fixtures/negative/state/completed-and-active-conflict/README 2.md` | EXACT_COPY | 77 vs 77 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/state/contract-without-trace/README.md` | `./tests/fixtures/negative/state/contract-without-trace/README 2.md` | EXACT_COPY | 76 vs 76 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/state/dropped-and-active-conflict/README.md` | `./tests/fixtures/negative/state/dropped-and-active-conflict/README 2.md` | EXACT_COPY | 73 vs 73 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/state/invalid-transition-brief-to-active/README.md` | `./tests/fixtures/negative/state/invalid-transition-brief-to-active/README 2.md` | EXACT_COPY | 127 vs 127 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/state/review-ready-without-task/README.md` | `./tests/fixtures/negative/state/review-ready-without-task/README 2.md` | EXACT_COPY | 74 vs 74 | add019e feat(m10.7.1): add negative state fixtures | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/negative/task-brief/executable-true/README.md` | `./tests/fixtures/negative/task-brief/executable-true/README 2.md` | EXACT_COPY | 498 vs 498 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/executable-true/TASK.md` | `./tests/fixtures/negative/task-brief/executable-true/TASK 2.md` | EXACT_COPY | 615 vs 615 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/README.md` | `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/README 2.md` | EXACT_COPY | 548 vs 548 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK.md` | `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK 2.md` | EXACT_COPY | 610 vs 610 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/missing-metadata/README.md` | `./tests/fixtures/negative/task-brief/missing-metadata/README 2.md` | EXACT_COPY | 493 vs 493 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/missing-metadata/TASK.md` | `./tests/fixtures/negative/task-brief/missing-metadata/TASK 2.md` | EXACT_COPY | 430 vs 430 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/status-not-approved/README.md` | `./tests/fixtures/negative/task-brief/status-not-approved/README 2.md` | EXACT_COPY | 505 vs 505 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/task-brief/status-not-approved/TASK.md` | `./tests/fixtures/negative/task-brief/status-not-approved/TASK 2.md` | EXACT_COPY | 629 vs 629 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/template-integrity/README.md` | `./tests/fixtures/negative/template-integrity/README 2.md` | EXACT_COPY | 1205 vs 1205 | 85b75f6 test(7.1): add negative fixture inventory and manual notes | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/active-task-updated.md` | `./tests/fixtures/negative/trace/active-task-updated 2.md` | EXACT_COPY | 145 vs 145 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/empty-task-id.md` | `./tests/fixtures/negative/trace/empty-task-id 2.md` | EXACT_COPY | 104 vs 104 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/execution-approved.md` | `./tests/fixtures/negative/trace/execution-approved 2.md` | EXACT_COPY | 147 vs 147 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/malformed-frontmatter.md` | `./tests/fixtures/negative/trace/malformed-frontmatter 2.md` | EXACT_COPY | 179 vs 179 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/missing-decision-rationale.md` | `./tests/fixtures/negative/trace/missing-decision-rationale 2.md` | EXACT_COPY | 84 vs 84 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/missing-source-summary.md` | `./tests/fixtures/negative/trace/missing-source-summary 2.md` | EXACT_COPY | 85 vs 85 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/missing-task-id.md` | `./tests/fixtures/negative/trace/missing-task-id 2.md` | EXACT_COPY | 92 vs 92 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/replaces-review.md` | `./tests/fixtures/negative/trace/replaces-review 2.md` | EXACT_COPY | 148 vs 148 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/negative/trace/replaces-task.md` | `./tests/fixtures/negative/trace/replaces-task 2.md` | EXACT_COPY | 144 vs 144 | 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue/task-invalid.md` | `./tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue/task-invalid 2.md` | EXACT_COPY | 166 vs 166 | 0451da8 feat(8.3.2): add queue directory validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-directory-validator/valid/tasks/done/task-done.md` | `./tests/fixtures/queue-directory-validator/valid/tasks/done/task-done 2.md` | EXACT_COPY | 83 vs 83 | 0451da8 feat(8.3.2): add queue directory validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-directory-validator/valid/tasks/dropped/task-dropped.md` | `./tests/fixtures/queue-directory-validator/valid/tasks/dropped/task-dropped 2.md` | EXACT_COPY | 92 vs 92 | 0451da8 feat(8.3.2): add queue directory validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-directory-validator/valid/tasks/queue/task-queued.md` | `./tests/fixtures/queue-directory-validator/valid/tasks/queue/task-queued 2.md` | EXACT_COPY | 90 vs 90 | 0451da8 feat(8.3.2): add queue directory validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/blocked-by-not-list.md` | `./tests/fixtures/queue-validator/invalid/blocked-by-not-list 2.md` | EXACT_COPY | 107 vs 107 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/blocked-with-empty-blocked-by.md` | `./tests/fixtures/queue-validator/invalid/blocked-with-empty-blocked-by 2.md` | EXACT_COPY | 98 vs 98 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/empty-task-id.md` | `./tests/fixtures/queue-validator/invalid/empty-task-id 2.md` | EXACT_COPY | 81 vs 81 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/malformed-frontmatter.md` | `./tests/fixtures/queue-validator/invalid/malformed-frontmatter 2.md` | EXACT_COPY | 126 vs 126 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/missing-blocked-by.md` | `./tests/fixtures/queue-validator/invalid/missing-blocked-by 2.md` | EXACT_COPY | 87 vs 87 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/missing-priority.md` | `./tests/fixtures/queue-validator/invalid/missing-priority 2.md` | EXACT_COPY | 83 vs 83 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/missing-status.md` | `./tests/fixtures/queue-validator/invalid/missing-status 2.md` | EXACT_COPY | 83 vs 83 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/missing-task-id.md` | `./tests/fixtures/queue-validator/invalid/missing-task-id 2.md` | EXACT_COPY | 69 vs 69 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/unknown-priority.md` | `./tests/fixtures/queue-validator/invalid/unknown-priority 2.md` | EXACT_COPY | 100 vs 100 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/invalid/unknown-status.md` | `./tests/fixtures/queue-validator/invalid/unknown-status 2.md` | EXACT_COPY | 99 vs 99 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/valid/blocked-with-dependency.md` | `./tests/fixtures/queue-validator/valid/blocked-with-dependency 2.md` | EXACT_COPY | 107 vs 107 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/valid/done-low.md` | `./tests/fixtures/queue-validator/valid/done-low 2.md` | EXACT_COPY | 87 vs 87 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/valid/dropped-normal.md` | `./tests/fixtures/queue-validator/valid/dropped-normal 2.md` | EXACT_COPY | 99 vs 99 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/valid/queued-high.md` | `./tests/fixtures/queue-validator/valid/queued-high 2.md` | EXACT_COPY | 93 vs 93 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/queue-validator/valid/queued-normal.md` | `./tests/fixtures/queue-validator/valid/queued-normal 2.md` | EXACT_COPY | 97 vs 97 | 6496270 feat(8.3.1): add queue entry validator | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/blocked-but-execution-true.md` | `./tests/fixtures/review-validator/invalid/blocked-but-execution-true 2.md` | EXACT_COPY | 122 vs 122 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/empty-execution-allowed.md` | `./tests/fixtures/review-validator/invalid/empty-execution-allowed 2.md` | EXACT_COPY | 60 vs 60 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/empty-review-status.md` | `./tests/fixtures/review-validator/invalid/empty-review-status 2.md` | EXACT_COPY | 59 vs 59 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/invalid-execution-allowed.md` | `./tests/fixtures/review-validator/invalid/invalid-execution-allowed 2.md` | EXACT_COPY | 61 vs 61 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/malformed-frontmatter.md` | `./tests/fixtures/review-validator/invalid/malformed-frontmatter 2.md` | EXACT_COPY | 95 vs 95 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/missing-execution-allowed.md` | `./tests/fixtures/review-validator/invalid/missing-execution-allowed 2.md` | EXACT_COPY | 38 vs 38 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/missing-review-status.md` | `./tests/fixtures/review-validator/invalid/missing-review-status 2.md` | EXACT_COPY | 41 vs 41 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/ready-but-execution-false.md` | `./tests/fixtures/review-validator/invalid/ready-but-execution-false 2.md` | EXACT_COPY | 118 vs 118 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/invalid/unknown-review-status.md` | `./tests/fixtures/review-validator/invalid/unknown-review-status 2.md` | EXACT_COPY | 71 vs 71 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/valid/blocked.md` | `./tests/fixtures/review-validator/valid/blocked 2.md` | EXACT_COPY | 74 vs 74 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/valid/needs-clarification.md` | `./tests/fixtures/review-validator/valid/needs-clarification 2.md` | EXACT_COPY | 98 vs 98 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/valid/ready.md` | `./tests/fixtures/review-validator/valid/ready 2.md` | EXACT_COPY | 104 vs 104 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/review-validator/valid/ready-with-edits.md` | `./tests/fixtures/review-validator/valid/ready-with-edits 2.md` | EXACT_COPY | 97 vs 97 | 452b49f feat(8.2.2): wire trace negative fixtures into runner | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-complete.py` | `./tests/fixtures/runner-validator/invalid/scripts/agent-complete 2.py` | EXACT_COPY | 189 vs 189 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-fail.py` | `./tests/fixtures/runner-validator/invalid/scripts/agent-fail 2.py` | EXACT_COPY | 181 vs 181 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-next.py` | `./tests/fixtures/runner-validator/invalid/scripts/agent-next 2.py` | EXACT_COPY | 203 vs 203 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/valid/scripts/agent-complete.py` | `./tests/fixtures/runner-validator/valid/scripts/agent-complete 2.py` | EXACT_COPY | 266 vs 266 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/valid/scripts/agent-fail.py` | `./tests/fixtures/runner-validator/valid/scripts/agent-fail 2.py` | EXACT_COPY | 267 vs 267 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/valid/scripts/agent-next.py` | `./tests/fixtures/runner-validator/valid/scripts/agent-next 2.py` | EXACT_COPY | 244 vs 244 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-fail.py` | `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-fail 2.py` | EXACT_COPY | 198 vs 198 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-next.py` | `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-next 2.py` | EXACT_COPY | 283 vs 283 | 218521d feat(8.5.1): add runner protocol static validator | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/task-brief/invalid-task-brief-executable-true.md` | `./tests/fixtures/task-brief/invalid-task-brief-executable-true 2.md` | EXACT_COPY | 574 vs 574 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-brief/invalid-task-brief-missing-section.md` | `./tests/fixtures/task-brief/invalid-task-brief-missing-section 2.md` | EXACT_COPY | 499 vs 499 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-brief/valid-task-brief.md` | `./tests/fixtures/task-brief/valid-task-brief 2.md` | EXACT_COPY | 514 vs 514 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/task-health.md` | `./tests/fixtures/task-health/task-health 2.md` | EXACT_COPY | 1050 vs 1050 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/drafts/task-20260426-ready-contract-draft.md` | `./tests/fixtures/task-health/tasks/drafts/task-20260426-ready-contract-draft 2.md` | EXACT_COPY | 126 vs 126 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/queue/blocked-example.md` | `./tests/fixtures/task-health/tasks/queue/blocked-example 2.md` | EXACT_COPY | 105 vs 105 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/queue/queued-example.md` | `./tests/fixtures/task-health/tasks/queue/queued-example 2.md` | EXACT_COPY | 50 vs 50 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/REVIEW.md` | `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/REVIEW 2.md` | EXACT_COPY | 60 vs 60 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/TASK.md` | `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/TASK 2.md` | EXACT_COPY | 43 vs 43 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-no-review/TASK.md` | `./tests/fixtures/task-health/tasks/task-20260426-no-review/TASK 2.md` | EXACT_COPY | 33 vs 33 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/REVIEW.md` | `./tests/fixtures/task-health/tasks/task-20260426-ready/REVIEW 2.md` | EXACT_COPY | 45 vs 45 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/TASK.md` | `./tests/fixtures/task-health/tasks/task-20260426-ready/TASK 2.md` | EXACT_COPY | 29 vs 29 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/TRACE.md` | `./tests/fixtures/task-health/tasks/task-20260426-ready/TRACE 2.md` | EXACT_COPY | 23 vs 23 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/INIT.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/INIT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/core-rules/MAIN.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/core-rules/MAIN 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/project/PROJECT.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/project/PROJECT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/repo-map.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/repo-map 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/reports/task-health.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/reports/task-health 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-complete.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-complete 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-fail.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-fail 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-next.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-next 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/auto-runner.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/auto-runner 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/generate-task-contract.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/generate-task-contract 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/task-health.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/task-health 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/validate-task-brief.py` | `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/validate-task-brief 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview/BOOT.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard/BOOT.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/queue-entry.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/queue-entry 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-brief-review.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-brief-review 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-contract-from-brief.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-contract-from-brief 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-decision-trace.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-decision-trace 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner/RUNNER-PROTOCOL.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner/RUNNER-PROTOCOL 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive/WRITE-TRACE.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive/WRITE-TRACE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder/BUILD-TASK-CONTRACT.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health/TASK-HEALTH.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health/TASK-HEALTH 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue/MANAGE-QUEUE.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue/MANAGE-QUEUE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review/REVIEW-TASK-BRIEF.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review/REVIEW-TASK-BRIEF 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/workflow/MAIN.md` | `./tests/fixtures/template-integrity/forbidden-auto-runner/workflow/MAIN 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/INIT.md` | `./tests/fixtures/template-integrity/missing-core-file/INIT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/project/PROJECT.md` | `./tests/fixtures/template-integrity/missing-core-file/project/PROJECT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/repo-map.md` | `./tests/fixtures/template-integrity/missing-core-file/repo-map 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/reports/task-health.md` | `./tests/fixtures/template-integrity/missing-core-file/reports/task-health 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-complete.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-complete 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-fail.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-fail 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-next.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-next 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/generate-task-contract.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/generate-task-contract 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/task-health.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/task-health 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/validate-task-brief.py` | `./tests/fixtures/template-integrity/missing-core-file/scripts/validate-task-brief 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-core-file/stages/01-interview/BOOT.md` | `./tests/fixtures/template-integrity/missing-core-file/stages/01-interview/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard/BOOT.md` | `./tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/templates/queue-entry.md` | `./tests/fixtures/template-integrity/missing-core-file/templates/queue-entry 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-brief-review.md` | `./tests/fixtures/template-integrity/missing-core-file/templates/task-brief-review 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-contract-from-brief.md` | `./tests/fixtures/template-integrity/missing-core-file/templates/task-contract-from-brief 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-decision-trace.md` | `./tests/fixtures/template-integrity/missing-core-file/templates/task-decision-trace 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/agent-runner/RUNNER-PROTOCOL.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/agent-runner/RUNNER-PROTOCOL 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/interview-archive/WRITE-TRACE.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/interview-archive/WRITE-TRACE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder/BUILD-TASK-CONTRACT.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-health/TASK-HEALTH.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/task-health/TASK-HEALTH 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-queue/MANAGE-QUEUE.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/task-queue/MANAGE-QUEUE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-review/REVIEW-TASK-BRIEF.md` | `./tests/fixtures/template-integrity/missing-core-file/tools/task-review/REVIEW-TASK-BRIEF 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-core-file/workflow/MAIN.md` | `./tests/fixtures/template-integrity/missing-core-file/workflow/MAIN 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/INIT.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/INIT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/core-rules/MAIN.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/core-rules/MAIN 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/project/PROJECT.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/project/PROJECT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/repo-map.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/repo-map 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/reports/task-health.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/reports/task-health 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-complete.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-complete 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-fail.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-fail 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-next.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-next 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/generate-task-contract.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/generate-task-contract 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/task-health.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/task-health 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/validate-task-brief.py` | `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/validate-task-brief 2.py` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview/BOOT.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview/BOOT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard/BOOT.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard/BOOT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/queue-entry.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/queue-entry 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-brief-review.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-brief-review 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-contract-from-brief.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-contract-from-brief 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-decision-trace.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-decision-trace 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner/RUNNER-PROTOCOL.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner/RUNNER-PROTOCOL 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive/WRITE-TRACE.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive/WRITE-TRACE 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder/BUILD-TASK-CONTRACT.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health/TASK-HEALTH.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health/TASK-HEALTH 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue/MANAGE-QUEUE.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue/MANAGE-QUEUE 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review/REVIEW-TASK-BRIEF.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review/REVIEW-TASK-BRIEF 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/workflow/MAIN.md` | `./tests/fixtures/template-integrity/missing-fixtures-warning/workflow/MAIN 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/INIT.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/INIT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules/MAIN.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules/MAIN 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/project/PROJECT.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/project/PROJECT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/repo-map.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/repo-map 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/reports/task-health.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/reports/task-health 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-complete.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-complete 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-fail.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-fail 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-next.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-next 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/generate-task-contract.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/generate-task-contract 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/task-health.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/task-health 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/validate-task-brief.py` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/validate-task-brief 2.py` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview/BOOT.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard/BOOT.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard/BOOT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/queue-entry.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/queue-entry 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-brief-review.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-brief-review 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-contract-from-brief.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-contract-from-brief 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-decision-trace.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-decision-trace 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner/RUNNER-PROTOCOL.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner/RUNNER-PROTOCOL 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive/WRITE-TRACE.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive/WRITE-TRACE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder/BUILD-TASK-CONTRACT.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health/TASK-HEALTH.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health/TASK-HEALTH 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue/MANAGE-QUEUE.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue/MANAGE-QUEUE 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review/REVIEW-TASK-BRIEF.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review/REVIEW-TASK-BRIEF 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/workflow/MAIN.md` | `./tests/fixtures/template-integrity/missing-gitignore-drafts/workflow/MAIN 2.md` | EXACT_COPY | 8 vs 8 | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/INIT.md` | `./tests/fixtures/template-integrity/missing-optional-report-warning/INIT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/core-rules/MAIN.md` | `./tests/fixtures/template-integrity/missing-optional-report-warning/core-rules/MAIN 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | HIGH | human review needed |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/project/PROJECT.md` | `./tests/fixtures/template-integrity/missing-optional-report-warning/project/PROJECT 2.md` | EXACT_COPY | 8 vs 8 | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | NOT_COMMITTED | LOW | likely safe to remove B |

## Directory Risk Map

| Directory | Duplicate Count | Risk Level | Notes |
|---|---|---|---|
| `scripts` | 73 | HIGH | Критичный каталог |
| `reports` | 39 | HIGH | Критичный каталог |
| `docs` | 32 | HIGH | Критичный каталог |
| `tests/fixtures/human-approval` | 32 | HIGH | Рабочий/тестовый каталог |
| `templates/agentos-full/scripts` | 15 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/contract-validator/invalid` | 14 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-draft` | 14 | MEDIUM | Рабочий/тестовый каталог |
| `templates` | 10 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/approval-flow-smoke` | 10 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/negative/queue` | 10 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/queue-validator/invalid` | 10 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/approval-enforcement` | 9 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/negative/trace` | 9 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/review-validator/invalid` | 9 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/apply-preconditions-approval` | 8 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/completion-flow-smoke` | 7 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/scripts` | 7 | MEDIUM | Рабочий/тестовый каталог |
| `examples` | 6 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/scripts` | 6 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/scripts` | 6 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/scripts` | 6 | MEDIUM | Рабочий/тестовый каталог |
| `.` | 5 | MEDIUM | Рабочий/тестовый каталог |
| `prompt-packs` | 5 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/negative/review` | 5 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/queue-validator/valid` | 5 | MEDIUM | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/activated-by-unknown-value` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/extra-dangerous-execution-claim` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/invalid-activated-at` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/malformed-yaml` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-activated-at` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-activated-by` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-approval-id` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-source-contract` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-source-task` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-state` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-task-id` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-transition` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-contract-absolute-path` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-contract-missing` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-contract-parent-traversal` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-task-absolute-path` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-task-missing` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/source-task-parent-traversal` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/state-not-active` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/task-id-mismatch-source-contract` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/task-id-mismatch-source-task` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/wrong-transition` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/active-task-validation-fail` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/active-task-validation-partial` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/analysis-status-conflict` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/analysis-status-invalid` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-id-mismatch-if-present` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-expired` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-invalid` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-malformed` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-revoked` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-unresolved` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-scope-mismatch` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-task-id-mismatch` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-transition-mismatch` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/detected-state-completed` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/detected-state-conflict` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/detected-state-dropped` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/detected-state-failed` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/detected-state-invalid` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/missing-state-validator` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/validate-task-state-fail` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/review-validator/valid` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/templates` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/templates` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/templates` | 4 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/templates` | 4 | LOW | Рабочий/тестовый каталог |
| `architecture` | 3 | LOW | Рабочий/тестовый каталог |
| `tasks/queue` | 3 | LOW | Критичный каталог |
| `tasks/task-20260426-brief-readiness-check` | 3 | LOW | Критичный каталог |
| `tests/fixtures/negative/activation/active-task-different-task/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/analysis-status-conflict/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/analysis-status-invalid/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/both-approved-and-dry-run/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/check-transition-fail/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/contract-missing/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/dry-run-does-not-write/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/expired-approval-marker/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/invalid-approval-marker/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/missing-approval-marker/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/missing-approved-flag/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/revoked-approval-marker/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-scope/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-task-id/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-transition/task` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/blocked-session-scope` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/blocked-session-verification` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/changed-file-out-of-scope` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/changed-file-outside-in-scope` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/missing-verification-plan` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/path-boundary-scripts-old` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/stopped-session-verification` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/unsafe-scope-entry` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-absolute-executable` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-mutating-git-command` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-parent-traversal-argument` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-shell-operator` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/verification-unsupported-executable` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/runner-validator/invalid/scripts` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/runner-validator/valid/scripts` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-brief` | 3 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health/tasks/task-20260426-ready` | 3 | LOW | Рабочий/тестовый каталог |
| `examples/simple-project` | 2 | LOW | Рабочий/тестовый каталог |
| `scripts/lib` | 2 | LOW | Критичный каталог |
| `templates/agentos-full/.github` | 2 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/.github/instructions` | 2 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-minimal/scripts` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/agent-runner/queue` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/contract-generation/blocked-task` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/contract-generation/ready-task` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/contract-validator/valid` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-frontmatter` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/duplicate-approved-markers` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/draft-already-exists/task-example` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/execution-not-allowed/task-example` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/review-not-ready/task-example` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-missing-task-id-start` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/session-missing-source-contract-scope` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/review/blocked-but-execution-true` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/review/missing-review-status` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/review/ready-but-execution-false` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/runner/approved-mode-requested` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/runner/attempts-active-task-replace` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/runner/missing-human-checkpoint` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/task-brief/executable-true` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/task-brief/missing-acceptance-criteria` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/task-brief/missing-metadata` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/task-brief/status-not-approved` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/runner-validator/valid-with-warnings/scripts` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health/tasks/queue` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health/tasks/task-20260426-needs-clarification` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning` | 2 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts` | 2 | LOW | Рабочий/тестовый каталог |
| `.github` | 1 | LOW | Рабочий/тестовый каталог |
| `approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `core-rules` | 1 | LOW | Критичный каталог |
| `handoff` | 1 | LOW | Рабочий/тестовый каталог |
| `handoff/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `incidents/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `lessons` | 1 | LOW | Рабочий/тестовый каталог |
| `lessons/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `quality` | 1 | LOW | Критичный каталог |
| `reports/completion` | 1 | LOW | Критичный каталог |
| `reports/execution` | 1 | LOW | Критичный каталог |
| `reports/templates` | 1 | LOW | Критичный каталог |
| `security` | 1 | LOW | Критичный каталог |
| `stages/spec-wizard` | 1 | LOW | Рабочий/тестовый каталог |
| `state` | 1 | LOW | Критичный каталог |
| `tasks` | 1 | LOW | Критичный каталог |
| `tasks/task-20260426-brief-to-contract-manual-guide` | 1 | LOW | Критичный каталог |
| `tasks/templates` | 1 | LOW | Критичный каталог |
| `templates/agentos-full` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/handoff` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/handoff/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/incidents/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/lessons` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/lessons/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/reports/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/tasks` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-full/tasks/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-minimal/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-minimal/reports/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-minimal/tasks` | 1 | LOW | Рабочий/тестовый каталог |
| `templates/agentos-minimal/tasks/templates` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/agent-runner/drafts` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/apply-transition` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/completion-flow-smoke/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/completion-flow-smoke/reports/execution` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/contract-generation/missing-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/active-task-different-task/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/analysis-status-conflict/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/analysis-status-invalid/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/both-approved-and-dry-run/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/contract-missing/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/dry-run-does-not-write/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/expired-approval-marker/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/invalid-approval-marker/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/missing-approval-marker/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/missing-approved-flag/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/revoked-approval-marker/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-scope/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-task-id/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/activation/wrong-transition/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/active-task/missing-active-task` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/expired-marker` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/invalid-transition-scope` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/malformed-approved-at` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/missing-related-contract` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/missing-required-field` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/revoked-marker` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/superseded-marker` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/wrong-scope` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/approval-markers/wrong-task-id` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/draft-already-exists` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/draft-already-exists/drafts` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/execution-not-allowed` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/missing-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/missing-review/task-example` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/contract-generation/review-not-ready` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-absolute-path-start` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-missing-start` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/active-task-parent-traversal-start` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/session-absolute-path-scope` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/session-parent-traversal-scope` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/session-parent-traversal-verification` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/execution-runner/shared` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/active-task-validation-fail/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/active-task-validation-partial/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/analysis-status-conflict/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/analysis-status-invalid/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-expired/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-invalid/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-malformed/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-marker-revoked/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-scope-mismatch/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/readiness/approval-transition-mismatch/approvals` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/active-without-approval` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/completed-and-active-conflict` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/contract-without-trace` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/dropped-and-active-conflict` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/invalid-transition-brief-to-active` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/state/review-ready-without-task` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/negative/template-integrity` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/queue-directory-validator/valid/tasks/done` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/queue-directory-validator/valid/tasks/dropped` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/queue-directory-validator/valid/tasks/queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health/tasks/drafts` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/task-health/tasks/task-20260426-no-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/core-rules` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/project` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/forbidden-auto-runner/workflow` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/project` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/stages/01-interview` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/agent-runner` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/interview-archive` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/task-health` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/task-queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/tools/task-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-core-file/workflow` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/core-rules` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/project` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-fixtures-warning/workflow` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/project` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/reports` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-gitignore-drafts/workflow` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-optional-report-warning` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-optional-report-warning/core-rules` | 1 | LOW | Рабочий/тестовый каталог |
| `tests/fixtures/template-integrity/missing-optional-report-warning/project` | 1 | LOW | Рабочий/тестовый каталог |

## Human Decision Required

| File | Why Human Decision Needed | Blocking Task |
|---|---|---|
| `./core-rules/MAIN 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/ACTIVATION-RECOVERY 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/ACTIVE-TASK-FORMAT 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/ACTIVE-TASK-VALIDATION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPLIED-TRANSITION-RECORD 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPLY-COMMAND-INTEGRATION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPLY-PLAN 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPLY-PRECONDITIONS 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPROVAL-EVIDENCE-STORAGE 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPROVAL-MARKER-SPEC 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPROVAL-REQUIREMENT-POLICY 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/APPROVED-MODE-CONTRACT 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/COMPLETION-READINESS 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/COMPLETION-TRANSITION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/CONTROLLED-COMPLETION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/CONTROLLED-COMPLETION-WORKFLOW 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/CONTROLLED-EXECUTION-RUNNER 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/CONTROLLED-FAILURE-AND-REVIEW 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/CONTROLLED-LIFECYCLE-MUTATION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/EXECUTION-READINESS 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/EXECUTION-SESSION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/GETTING-STARTED 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/HUMAN-APPROVAL-BOUNDARY 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/HUMAN-APPROVAL-EVIDENCE 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/LIFECYCLE-INTEGRATION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/OPERATION-RISK-MODEL 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/SAFE-TRANSITION-EXECUTION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/SAFETY-BOUNDARIES 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/TASK-STATE-MACHINE 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/TASK-TRANSITION-RULES 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/VALIDATION 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/quickstart 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./docs/usage 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./quality/MAIN 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/activation-audit-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/activation-positive-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/active-task-governance-audit-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/agentos-validate-cli-hardening 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/agentos-validate-json-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/agentos-validate-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/agentos-validate-usage-integration 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/audit 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/audit-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/execution-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/guard-failures-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10-final-hardening-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10.11-state-report-hardening 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10.11.1-approval-marker-spec 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10.11.2-v1.1-hardening 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10.12-downstream-v1.1-compatibility 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-10.13-state-analysis-separation 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-11-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-12-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-13-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-14-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-14-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-15-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-15-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-16-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-16-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-17-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-17-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-18-completion-review 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-18-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/milestone-7.1-handoff 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/negative-fixtures-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/pre-execution-evidence-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/release-checklist 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/session-handoff 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/task-health 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/task-state-machine-smoke 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/templates/verification-report 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./reports/verification 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/VALIDATORS 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/activate-task 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/agent-complete 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/agent-fail 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/agent-next 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/agentos-validate 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/apply-transition 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/audit-agentos 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/audit-approval-boundary 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/audit-lifecycle-mutation 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/audit-policy-boundary 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/audit-release-readiness 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-apply-preconditions 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-completion-readiness 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-dangerous-commands 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-execution-readiness 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-execution-scope 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-links 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-pr-quality 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-risk 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/check-transition 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/complete-active-task 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/detect-task-state 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/generate-repo-map 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/generate-task-contract 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/lib/__init__ 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/lib/path_utils 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/run-active-task 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/run-execution-verification 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/select-context 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/task-health 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-activation-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-active-task-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-apply-transition-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-approval-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-approval-flow-smoke 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-approval-marker-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-completion-flow-smoke 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-execution-runner-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-guard-failures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-human-approval-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-negative-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-policy-enforcement-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-policy-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-policy-flow-smoke 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-readiness-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-state-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/test-template-integrity-fixtures 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-active-task 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-approval-marker 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-commit-msg 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-contract-draft 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-docs 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-handoff 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-human-approval 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-incident 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-lessons 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-lifecycle-apply 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-policy 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-queue 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-queue-entry 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-review 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-route 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-runner-protocol 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-task 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-task-brief 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-task-state 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-trace 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./scripts/validate-verification 2.py` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./security/MAIN 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./state/MAIN 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./tasks/active-task 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |
| `./tasks/templates/task-contract 2.md` | Файл влияет на источник правил/проверок | 22.3.1 Source-of-Truth Map |

## Safe to Proceed Without Resolving

| File Pair | Why Not Blocking | Notes |
|---|---|---|
| `./.github/pull_request_template.md <> ./.github/pull_request_template 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./CHANGELOG.md <> ./CHANGELOG 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./INIT.md <> ./INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./RELEASE-CHECKLIST.md <> ./RELEASE-CHECKLIST 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./ROUTES-REGISTRY.md <> ./ROUTES-REGISTRY 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./approvals/approval-task-20260426-brief-readiness-check-execution.md <> ./approvals/approval-task-20260426-brief-readiness-check-execution 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./architecture/CANON.md <> ./architecture/CANON 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./architecture/MAIN.md <> ./architecture/MAIN 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./architecture/OPERATING-RULES.md <> ./architecture/OPERATING-RULES 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/README.md <> ./examples/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/queue-entry-example.md <> ./examples/queue-entry-example 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/scenario-01-new-feature.md <> ./examples/scenario-01-new-feature 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/scenario-02-bugfix.md <> ./examples/scenario-02-bugfix 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/scenario-03-refactor.md <> ./examples/scenario-03-refactor 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/scenario-04-validation-only.md <> ./examples/scenario-04-validation-only 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/simple-project/README.md <> ./examples/simple-project/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./examples/simple-project/app.py <> ./examples/simple-project/app 2.py` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./handoff/HANDOFF.md <> ./handoff/HANDOFF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./handoff/templates/session-summary.md <> ./handoff/templates/session-summary 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./incidents/templates/incident.md <> ./incidents/templates/incident 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./lessons/lessons.md <> ./lessons/lessons 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./lessons/templates/lesson-entry.md <> ./lessons/templates/lesson-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./prompt-packs/README.md <> ./prompt-packs/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./prompt-packs/chatgpt.md <> ./prompt-packs/chatgpt 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./prompt-packs/claude-code.md <> ./prompt-packs/claude-code 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./prompt-packs/codex-cli.md <> ./prompt-packs/codex-cli 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./prompt-packs/cursor.md <> ./prompt-packs/cursor 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./repo-map.md <> ./repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./scripts/audit-gate-contract.py <> ./scripts/audit-gate-contract 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./scripts/check-template-integrity.py <> ./scripts/check-template-integrity 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./scripts/test-gate-regression-fixtures.py <> ./scripts/test-gate-regression-fixtures 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./scripts/test-template-integrity.py <> ./scripts/test-template-integrity 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./scripts/test-unified-gate-smoke.py <> ./scripts/test-unified-gate-smoke 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./scripts/validate-gate-contract.py <> ./scripts/validate-gate-contract 2.py` | Вне критичных зон или низкий риск | DIVERGED |
| `./stages/spec-wizard/BOOT.md <> ./stages/spec-wizard/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/queue/20260428-queue-schema-check.md <> ./tasks/queue/20260428-queue-schema-check 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/queue/20260428-runner-human-checkpoints.md <> ./tasks/queue/20260428-runner-human-checkpoints 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/queue/QUEUE.md <> ./tasks/queue/QUEUE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/task-20260426-brief-readiness-check/REVIEW.md <> ./tasks/task-20260426-brief-readiness-check/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/task-20260426-brief-readiness-check/TASK.md <> ./tasks/task-20260426-brief-readiness-check/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/task-20260426-brief-readiness-check/TRACE.md <> ./tasks/task-20260426-brief-readiness-check/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tasks/task-20260426-brief-to-contract-manual-guide/TASK.md <> ./tasks/task-20260426-brief-to-contract-manual-guide/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/.github/copilot-instructions.md <> ./templates/agentos-full/.github/copilot-instructions 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/.github/instructions/backend.instructions.md <> ./templates/agentos-full/.github/instructions/backend.instructions 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/.github/instructions/frontend.instructions.md <> ./templates/agentos-full/.github/instructions/frontend.instructions 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/.github/pull_request_template.md <> ./templates/agentos-full/.github/pull_request_template 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/handoff/HANDOFF.md <> ./templates/agentos-full/handoff/HANDOFF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/handoff/templates/session-summary.md <> ./templates/agentos-full/handoff/templates/session-summary 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/incidents/templates/incident.md <> ./templates/agentos-full/incidents/templates/incident 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/lessons/lessons.md <> ./templates/agentos-full/lessons/lessons 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/lessons/templates/lesson-entry.md <> ./templates/agentos-full/lessons/templates/lesson-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/agentos-full/repo-map.md <> ./templates/agentos-full/repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/applied-transition-record.md <> ./templates/applied-transition-record 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/apply-plan.md <> ./templates/apply-plan 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/candidate-tasks.md <> ./templates/candidate-tasks 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/commit-message.md <> ./templates/commit-message 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/completion-readiness.md <> ./templates/completion-readiness 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/completion-transition.md <> ./templates/completion-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/execution-session.md <> ./templates/execution-session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/human-approval-record.md <> ./templates/human-approval-record 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/queue-entry.md <> ./templates/queue-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./templates/task-brief-review.md <> ./templates/task-brief-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/agent-runner/drafts/high-ready-contract-draft.md <> ./tests/fixtures/agent-runner/drafts/high-ready-contract-draft 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/agent-runner/queue/high-ready.md <> ./tests/fixtures/agent-runner/queue/high-ready 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/agent-runner/queue/normal-blocked.md <> ./tests/fixtures/agent-runner/queue/normal-blocked 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/active-task.md <> ./tests/fixtures/apply-preconditions-approval/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/approval-not-required-transition.md <> ./tests/fixtures/apply-preconditions-approval/approval-not-required-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/approval-required-transition.md <> ./tests/fixtures/apply-preconditions-approval/approval-required-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/invalid-vague-approval.md <> ./tests/fixtures/apply-preconditions-approval/invalid-vague-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/readiness-evidence.md <> ./tests/fixtures/apply-preconditions-approval/readiness-evidence 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/task-mismatch-approval.md <> ./tests/fixtures/apply-preconditions-approval/task-mismatch-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/valid-approval.md <> ./tests/fixtures/apply-preconditions-approval/valid-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-preconditions-approval/verification-evidence.md <> ./tests/fixtures/apply-preconditions-approval/verification-evidence 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/apply-transition/README.md <> ./tests/fixtures/apply-transition/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/approval-not-required-transition.md <> ./tests/fixtures/approval-enforcement/approval-not-required-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/approval-required-mutation-plan.md <> ./tests/fixtures/approval-enforcement/approval-required-mutation-plan 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/approval-required-transition.md <> ./tests/fixtures/approval-enforcement/approval-required-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/invalid-vague-approval.md <> ./tests/fixtures/approval-enforcement/invalid-vague-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/task-mismatch-approval.md <> ./tests/fixtures/approval-enforcement/task-mismatch-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/transition-mismatch-approval.md <> ./tests/fixtures/approval-enforcement/transition-mismatch-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/unsupported-operation-approval.md <> ./tests/fixtures/approval-enforcement/unsupported-operation-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/unsupported-target-state-approval.md <> ./tests/fixtures/approval-enforcement/unsupported-target-state-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-enforcement/valid-approval.md <> ./tests/fixtures/approval-enforcement/valid-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/README.md <> ./tests/fixtures/approval-flow-smoke/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/invalid-vague-approval.md <> ./tests/fixtures/approval-flow-smoke/invalid-vague-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-applied-transition-record.md <> ./tests/fixtures/approval-flow-smoke/synthetic-applied-transition-record 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-apply-plan.md <> ./tests/fixtures/approval-flow-smoke/synthetic-apply-plan 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-mutation-plan.md <> ./tests/fixtures/approval-flow-smoke/synthetic-mutation-plan 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-readiness.md <> ./tests/fixtures/approval-flow-smoke/synthetic-readiness 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-task.md <> ./tests/fixtures/approval-flow-smoke/synthetic-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-transition.md <> ./tests/fixtures/approval-flow-smoke/synthetic-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/synthetic-verification.md <> ./tests/fixtures/approval-flow-smoke/synthetic-verification 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/approval-flow-smoke/valid-approval.md <> ./tests/fixtures/approval-flow-smoke/valid-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/README.md <> ./tests/fixtures/completion-flow-smoke/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/active-task.md <> ./tests/fixtures/completion-flow-smoke/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/completion-readiness-evidence.md <> ./tests/fixtures/completion-flow-smoke/completion-readiness-evidence 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/prepared-transition.md <> ./tests/fixtures/completion-flow-smoke/prepared-transition 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/tasks-active-task.md <> ./tests/fixtures/completion-flow-smoke/tasks-active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/transition-smoke.md <> ./tests/fixtures/completion-flow-smoke/transition-smoke 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/completion-flow-smoke/verification-evidence.md <> ./tests/fixtures/completion-flow-smoke/verification-evidence 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-generation/blocked-task/REVIEW.md <> ./tests/fixtures/contract-generation/blocked-task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-generation/blocked-task/TASK.md <> ./tests/fixtures/contract-generation/blocked-task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-generation/missing-review/TASK.md <> ./tests/fixtures/contract-generation/missing-review/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-generation/ready-task/REVIEW.md <> ./tests/fixtures/contract-generation/ready-task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-generation/ready-task/TASK.md <> ./tests/fixtures/contract-generation/ready-task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/blocked-review-status.md <> ./tests/fixtures/contract-validator/invalid/blocked-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/execution-allowed-false.md <> ./tests/fixtures/contract-validator/invalid/execution-allowed-false 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/execution-approved.md <> ./tests/fixtures/contract-validator/invalid/execution-approved 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/invalid-execution-allowed.md <> ./tests/fixtures/contract-validator/invalid/invalid-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-close.md <> ./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-close 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-open.md <> ./tests/fixtures/contract-validator/invalid/malformed-frontmatter-no-open 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-execution-allowed.md <> ./tests/fixtures/contract-validator/invalid/missing-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-generated-from-task.md <> ./tests/fixtures/contract-validator/invalid/missing-generated-from-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-review-file.md <> ./tests/fixtures/contract-validator/invalid/missing-review-file 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-review-status.md <> ./tests/fixtures/contract-validator/invalid/missing-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-risk-section.md <> ./tests/fixtures/contract-validator/invalid/missing-risk-section 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-task-id.md <> ./tests/fixtures/contract-validator/invalid/missing-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/missing-verification-section.md <> ./tests/fixtures/contract-validator/invalid/missing-verification-section 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/invalid/replaces-active-task.md <> ./tests/fixtures/contract-validator/invalid/replaces-active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/valid/ready-contract-draft.md <> ./tests/fixtures/contract-validator/valid/ready-contract-draft 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/contract-validator/valid/ready-with-edits-contract-draft.md <> ./tests/fixtures/contract-validator/valid/ready-with-edits-contract-draft 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approval-id-operation-mismatch.md <> ./tests/fixtures/human-approval/invalid-approval-id-operation-mismatch 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approval-id-task-mismatch.md <> ./tests/fixtures/human-approval/invalid-approval-id-task-mismatch 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approval-status-invalid.md <> ./tests/fixtures/human-approval/invalid-approval-status-invalid 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approved-at-format.md <> ./tests/fixtures/human-approval/invalid-approved-at-format 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approved-by-agent.md <> ./tests/fixtures/human-approval/invalid-approved-by-agent 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-approved-by-openai-exact.md <> ./tests/fixtures/human-approval/invalid-approved-by-openai-exact 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-bypass-preconditions.md <> ./tests/fixtures/human-approval/invalid-bypass-preconditions 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-expired-status.md <> ./tests/fixtures/human-approval/invalid-expired-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-expires-at-format.md <> ./tests/fixtures/human-approval/invalid-expires-at-format 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-generic-scope-all.md <> ./tests/fixtures/human-approval/invalid-generic-scope-all 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-missing-approval-scope.md <> ./tests/fixtures/human-approval/invalid-missing-approval-scope 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-missing-related-task-id.md <> ./tests/fixtures/human-approval/invalid-missing-related-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-missing-related-transition-id.md <> ./tests/fixtures/human-approval/invalid-missing-related-transition-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-missing-required-field.md <> ./tests/fixtures/human-approval/invalid-missing-required-field 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-nested-yaml.md <> ./tests/fixtures/human-approval/invalid-nested-yaml 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-related-task-id-format.md <> ./tests/fixtures/human-approval/invalid-related-task-id-format 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-related-transition-id-format.md <> ./tests/fixtures/human-approval/invalid-related-transition-id-format 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-revoked-status.md <> ./tests/fixtures/human-approval/invalid-revoked-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-statement-missing-operation-reference.md <> ./tests/fixtures/human-approval/invalid-statement-missing-operation-reference 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-statement-missing-target-state-reference.md <> ./tests/fixtures/human-approval/invalid-statement-missing-target-state-reference 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-statement-missing-task-reference.md <> ./tests/fixtures/human-approval/invalid-statement-missing-task-reference 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-statement-missing-transition-reference.md <> ./tests/fixtures/human-approval/invalid-statement-missing-transition-reference 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-superseded-status.md <> ./tests/fixtures/human-approval/invalid-superseded-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-supersedes-format.md <> ./tests/fixtures/human-approval/invalid-supersedes-format 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-unknown-approval-source.md <> ./tests/fixtures/human-approval/invalid-unknown-approval-source 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-unknown-status.md <> ./tests/fixtures/human-approval/invalid-unknown-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-unsupported-operation.md <> ./tests/fixtures/human-approval/invalid-unsupported-operation 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-unsupported-target-state.md <> ./tests/fixtures/human-approval/invalid-unsupported-target-state 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-vague-approval.md <> ./tests/fixtures/human-approval/invalid-vague-approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/invalid-vague-continue.md <> ./tests/fixtures/human-approval/invalid-vague-continue 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/valid-approved-by-openai-substring.md <> ./tests/fixtures/human-approval/valid-approved-by-openai-substring 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/human-approval/valid-complete-active.md <> ./tests/fixtures/human-approval/valid-complete-active 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/README.md <> ./tests/fixtures/negative/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/active-task-different-task/approvals/approval.md <> ./tests/fixtures/negative/activation/active-task-different-task/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/active-task-different-task/task/REVIEW.md <> ./tests/fixtures/negative/activation/active-task-different-task/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/active-task-different-task/task/TASK.md <> ./tests/fixtures/negative/activation/active-task-different-task/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/active-task-different-task/task/TRACE.md <> ./tests/fixtures/negative/activation/active-task-different-task/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-conflict/approvals/approval.md <> ./tests/fixtures/negative/activation/analysis-status-conflict/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/REVIEW.md <> ./tests/fixtures/negative/activation/analysis-status-conflict/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/TASK.md <> ./tests/fixtures/negative/activation/analysis-status-conflict/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-conflict/task/TRACE.md <> ./tests/fixtures/negative/activation/analysis-status-conflict/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-invalid/approvals/approval.md <> ./tests/fixtures/negative/activation/analysis-status-invalid/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/REVIEW.md <> ./tests/fixtures/negative/activation/analysis-status-invalid/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/TASK.md <> ./tests/fixtures/negative/activation/analysis-status-invalid/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/analysis-status-invalid/task/TRACE.md <> ./tests/fixtures/negative/activation/analysis-status-invalid/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals/approval.md <> ./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/REVIEW.md <> ./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TASK.md <> ./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TRACE.md <> ./tests/fixtures/negative/activation/approval-marker-valid-but-no-approved/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/approvals/approval.md <> ./tests/fixtures/negative/activation/both-approved-and-dry-run/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/REVIEW.md <> ./tests/fixtures/negative/activation/both-approved-and-dry-run/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TASK.md <> ./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TRACE.md <> ./tests/fixtures/negative/activation/both-approved-and-dry-run/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/check-transition-fail/task/REVIEW.md <> ./tests/fixtures/negative/activation/check-transition-fail/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/check-transition-fail/task/TASK.md <> ./tests/fixtures/negative/activation/check-transition-fail/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/check-transition-fail/task/TRACE.md <> ./tests/fixtures/negative/activation/check-transition-fail/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/contract-missing/approvals/approval.md <> ./tests/fixtures/negative/activation/contract-missing/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/contract-missing/task/REVIEW.md <> ./tests/fixtures/negative/activation/contract-missing/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/contract-missing/task/TASK.md <> ./tests/fixtures/negative/activation/contract-missing/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/contract-missing/task/TRACE.md <> ./tests/fixtures/negative/activation/contract-missing/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/approvals/approval.md <> ./tests/fixtures/negative/activation/dry-run-does-not-write/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/REVIEW.md <> ./tests/fixtures/negative/activation/dry-run-does-not-write/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TASK.md <> ./tests/fixtures/negative/activation/dry-run-does-not-write/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/dry-run-does-not-write/task/TRACE.md <> ./tests/fixtures/negative/activation/dry-run-does-not-write/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/expired-approval-marker/approvals/approval.md <> ./tests/fixtures/negative/activation/expired-approval-marker/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/REVIEW.md <> ./tests/fixtures/negative/activation/expired-approval-marker/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/TASK.md <> ./tests/fixtures/negative/activation/expired-approval-marker/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/expired-approval-marker/task/TRACE.md <> ./tests/fixtures/negative/activation/expired-approval-marker/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/invalid-approval-marker/approvals/approval.md <> ./tests/fixtures/negative/activation/invalid-approval-marker/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/REVIEW.md <> ./tests/fixtures/negative/activation/invalid-approval-marker/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/TASK.md <> ./tests/fixtures/negative/activation/invalid-approval-marker/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/invalid-approval-marker/task/TRACE.md <> ./tests/fixtures/negative/activation/invalid-approval-marker/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approval-marker/approvals/approval.md <> ./tests/fixtures/negative/activation/missing-approval-marker/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/REVIEW.md <> ./tests/fixtures/negative/activation/missing-approval-marker/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/TASK.md <> ./tests/fixtures/negative/activation/missing-approval-marker/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approval-marker/task/TRACE.md <> ./tests/fixtures/negative/activation/missing-approval-marker/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approved-flag/approvals/approval.md <> ./tests/fixtures/negative/activation/missing-approved-flag/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/REVIEW.md <> ./tests/fixtures/negative/activation/missing-approved-flag/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/TASK.md <> ./tests/fixtures/negative/activation/missing-approved-flag/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/missing-approved-flag/task/TRACE.md <> ./tests/fixtures/negative/activation/missing-approved-flag/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/revoked-approval-marker/approvals/approval.md <> ./tests/fixtures/negative/activation/revoked-approval-marker/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/REVIEW.md <> ./tests/fixtures/negative/activation/revoked-approval-marker/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/TASK.md <> ./tests/fixtures/negative/activation/revoked-approval-marker/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/revoked-approval-marker/task/TRACE.md <> ./tests/fixtures/negative/activation/revoked-approval-marker/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-scope/approvals/approval.md <> ./tests/fixtures/negative/activation/wrong-scope/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-scope/task/REVIEW.md <> ./tests/fixtures/negative/activation/wrong-scope/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-scope/task/TASK.md <> ./tests/fixtures/negative/activation/wrong-scope/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-scope/task/TRACE.md <> ./tests/fixtures/negative/activation/wrong-scope/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-task-id/approvals/approval.md <> ./tests/fixtures/negative/activation/wrong-task-id/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-task-id/task/REVIEW.md <> ./tests/fixtures/negative/activation/wrong-task-id/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-task-id/task/TASK.md <> ./tests/fixtures/negative/activation/wrong-task-id/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-task-id/task/TRACE.md <> ./tests/fixtures/negative/activation/wrong-task-id/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-transition/approvals/approval.md <> ./tests/fixtures/negative/activation/wrong-transition/approvals/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-transition/task/REVIEW.md <> ./tests/fixtures/negative/activation/wrong-transition/task/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-transition/task/TASK.md <> ./tests/fixtures/negative/activation/wrong-transition/task/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/activation/wrong-transition/task/TRACE.md <> ./tests/fixtures/negative/activation/wrong-transition/task/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/README.md <> ./tests/fixtures/negative/active-task/activated-by-unknown-value/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/active-task.md <> ./tests/fixtures/negative/active-task/activated-by-unknown-value/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-contract.md <> ./tests/fixtures/negative/active-task/activated-by-unknown-value/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/activated-by-unknown-value/source-task.md <> ./tests/fixtures/negative/active-task/activated-by-unknown-value/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/README.md <> ./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/active-task.md <> ./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-contract.md <> ./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-task.md <> ./tests/fixtures/negative/active-task/extra-dangerous-execution-claim/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/invalid-activated-at/README.md <> ./tests/fixtures/negative/active-task/invalid-activated-at/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/invalid-activated-at/active-task.md <> ./tests/fixtures/negative/active-task/invalid-activated-at/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/invalid-activated-at/source-contract.md <> ./tests/fixtures/negative/active-task/invalid-activated-at/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/invalid-activated-at/source-task.md <> ./tests/fixtures/negative/active-task/invalid-activated-at/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/malformed-yaml/README.md <> ./tests/fixtures/negative/active-task/malformed-yaml/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/malformed-yaml/active-task.md <> ./tests/fixtures/negative/active-task/malformed-yaml/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/malformed-yaml/source-contract.md <> ./tests/fixtures/negative/active-task/malformed-yaml/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/malformed-yaml/source-task.md <> ./tests/fixtures/negative/active-task/malformed-yaml/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-at/README.md <> ./tests/fixtures/negative/active-task/missing-activated-at/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-at/active-task.md <> ./tests/fixtures/negative/active-task/missing-activated-at/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-at/source-contract.md <> ./tests/fixtures/negative/active-task/missing-activated-at/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-at/source-task.md <> ./tests/fixtures/negative/active-task/missing-activated-at/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-by/README.md <> ./tests/fixtures/negative/active-task/missing-activated-by/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-by/active-task.md <> ./tests/fixtures/negative/active-task/missing-activated-by/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-by/source-contract.md <> ./tests/fixtures/negative/active-task/missing-activated-by/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-activated-by/source-task.md <> ./tests/fixtures/negative/active-task/missing-activated-by/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-active-task/README.md <> ./tests/fixtures/negative/active-task/missing-active-task/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-approval-id/README.md <> ./tests/fixtures/negative/active-task/missing-approval-id/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-approval-id/active-task.md <> ./tests/fixtures/negative/active-task/missing-approval-id/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-approval-id/source-contract.md <> ./tests/fixtures/negative/active-task/missing-approval-id/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-approval-id/source-task.md <> ./tests/fixtures/negative/active-task/missing-approval-id/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-frontmatter/README.md <> ./tests/fixtures/negative/active-task/missing-frontmatter/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-frontmatter/active-task.md <> ./tests/fixtures/negative/active-task/missing-frontmatter/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-contract/README.md <> ./tests/fixtures/negative/active-task/missing-source-contract/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-contract/active-task.md <> ./tests/fixtures/negative/active-task/missing-source-contract/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-contract/source-contract.md <> ./tests/fixtures/negative/active-task/missing-source-contract/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-contract/source-task.md <> ./tests/fixtures/negative/active-task/missing-source-contract/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-task/README.md <> ./tests/fixtures/negative/active-task/missing-source-task/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-task/active-task.md <> ./tests/fixtures/negative/active-task/missing-source-task/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-task/source-contract.md <> ./tests/fixtures/negative/active-task/missing-source-task/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-source-task/source-task.md <> ./tests/fixtures/negative/active-task/missing-source-task/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-task-id/README.md <> ./tests/fixtures/negative/active-task/missing-task-id/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-task-id/active-task.md <> ./tests/fixtures/negative/active-task/missing-task-id/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-task-id/source-contract.md <> ./tests/fixtures/negative/active-task/missing-task-id/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-task-id/source-task.md <> ./tests/fixtures/negative/active-task/missing-task-id/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-transition/README.md <> ./tests/fixtures/negative/active-task/missing-transition/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-transition/active-task.md <> ./tests/fixtures/negative/active-task/missing-transition/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-transition/source-contract.md <> ./tests/fixtures/negative/active-task/missing-transition/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/missing-transition/source-task.md <> ./tests/fixtures/negative/active-task/missing-transition/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/README.md <> ./tests/fixtures/negative/active-task/source-contract-absolute-path/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/active-task.md <> ./tests/fixtures/negative/active-task/source-contract-absolute-path/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-contract.md <> ./tests/fixtures/negative/active-task/source-contract-absolute-path/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-absolute-path/source-task.md <> ./tests/fixtures/negative/active-task/source-contract-absolute-path/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-missing/README.md <> ./tests/fixtures/negative/active-task/source-contract-missing/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-missing/active-task.md <> ./tests/fixtures/negative/active-task/source-contract-missing/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-missing/source-contract.md <> ./tests/fixtures/negative/active-task/source-contract-missing/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-missing/source-task.md <> ./tests/fixtures/negative/active-task/source-contract-missing/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/README.md <> ./tests/fixtures/negative/active-task/source-contract-parent-traversal/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/active-task.md <> ./tests/fixtures/negative/active-task/source-contract-parent-traversal/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-contract.md <> ./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-task.md <> ./tests/fixtures/negative/active-task/source-contract-parent-traversal/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/README.md <> ./tests/fixtures/negative/active-task/source-task-absolute-path/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/active-task.md <> ./tests/fixtures/negative/active-task/source-task-absolute-path/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/source-contract.md <> ./tests/fixtures/negative/active-task/source-task-absolute-path/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-absolute-path/source-task.md <> ./tests/fixtures/negative/active-task/source-task-absolute-path/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-missing/README.md <> ./tests/fixtures/negative/active-task/source-task-missing/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-missing/active-task.md <> ./tests/fixtures/negative/active-task/source-task-missing/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-missing/source-contract.md <> ./tests/fixtures/negative/active-task/source-task-missing/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-missing/source-task.md <> ./tests/fixtures/negative/active-task/source-task-missing/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/README.md <> ./tests/fixtures/negative/active-task/source-task-parent-traversal/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/active-task.md <> ./tests/fixtures/negative/active-task/source-task-parent-traversal/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-contract.md <> ./tests/fixtures/negative/active-task/source-task-parent-traversal/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/source-task-parent-traversal/source-task.md <> ./tests/fixtures/negative/active-task/source-task-parent-traversal/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/state-not-active/README.md <> ./tests/fixtures/negative/active-task/state-not-active/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/state-not-active/active-task.md <> ./tests/fixtures/negative/active-task/state-not-active/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/state-not-active/source-contract.md <> ./tests/fixtures/negative/active-task/state-not-active/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/state-not-active/source-task.md <> ./tests/fixtures/negative/active-task/state-not-active/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/README.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/active-task.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-contract.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-task.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-contract/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/README.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-task/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/active-task.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-task/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-contract.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-task.md <> ./tests/fixtures/negative/active-task/task-id-mismatch-source-task/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/wrong-transition/README.md <> ./tests/fixtures/negative/active-task/wrong-transition/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/wrong-transition/active-task.md <> ./tests/fixtures/negative/active-task/wrong-transition/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/wrong-transition/source-contract.md <> ./tests/fixtures/negative/active-task/wrong-transition/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/active-task/wrong-transition/source-task.md <> ./tests/fixtures/negative/active-task/wrong-transition/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval.md <> ./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval-duplicate.md <> ./tests/fixtures/negative/approval-markers/duplicate-approved-markers/approval-duplicate 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/expired-marker/approval.md <> ./tests/fixtures/negative/approval-markers/expired-marker/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/invalid-transition-scope/approval.md <> ./tests/fixtures/negative/approval-markers/invalid-transition-scope/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/malformed-approved-at/approval.md <> ./tests/fixtures/negative/approval-markers/malformed-approved-at/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/missing-related-contract/approval.md <> ./tests/fixtures/negative/approval-markers/missing-related-contract/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/missing-required-field/approval.md <> ./tests/fixtures/negative/approval-markers/missing-required-field/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/revoked-marker/approval.md <> ./tests/fixtures/negative/approval-markers/revoked-marker/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/superseded-marker/approval.md <> ./tests/fixtures/negative/approval-markers/superseded-marker/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/wrong-scope/approval.md <> ./tests/fixtures/negative/approval-markers/wrong-scope/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/approval-markers/wrong-task-id/approval.md <> ./tests/fixtures/negative/approval-markers/wrong-task-id/approval 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/blocked-review-status.md <> ./tests/fixtures/negative/contract-draft/blocked-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/execution-allowed-false.md <> ./tests/fixtures/negative/contract-draft/execution-allowed-false 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/execution-approved.md <> ./tests/fixtures/negative/contract-draft/execution-approved 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/invalid-execution-allowed.md <> ./tests/fixtures/negative/contract-draft/invalid-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-close.md <> ./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-close 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-open.md <> ./tests/fixtures/negative/contract-draft/malformed-frontmatter-no-open 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-execution-allowed.md <> ./tests/fixtures/negative/contract-draft/missing-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-generated-from-task.md <> ./tests/fixtures/negative/contract-draft/missing-generated-from-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-review-file.md <> ./tests/fixtures/negative/contract-draft/missing-review-file 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-review-status.md <> ./tests/fixtures/negative/contract-draft/missing-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-risk-section.md <> ./tests/fixtures/negative/contract-draft/missing-risk-section 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-task-id.md <> ./tests/fixtures/negative/contract-draft/missing-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/missing-verification-section.md <> ./tests/fixtures/negative/contract-draft/missing-verification-section 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-draft/replaces-active-task.md <> ./tests/fixtures/negative/contract-draft/replaces-active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/README.md <> ./tests/fixtures/negative/contract-generation/draft-already-exists/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft.md <> ./tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW.md <> ./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK.md <> ./tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/README.md <> ./tests/fixtures/negative/contract-generation/execution-not-allowed/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW.md <> ./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK.md <> ./tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/missing-review/README.md <> ./tests/fixtures/negative/contract-generation/missing-review/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/missing-review/task-example/TASK.md <> ./tests/fixtures/negative/contract-generation/missing-review/task-example/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/review-not-ready/README.md <> ./tests/fixtures/negative/contract-generation/review-not-ready/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW.md <> ./tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK.md <> ./tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-absolute-path-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-absolute-path-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/active-task.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-frontmatter-start/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/active-task.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-source-contract-start/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/active-task.md <> ./tests/fixtures/negative/execution-runner/active-task-missing-task-id-start/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run/README.md <> ./tests/fixtures/negative/execution-runner/active-task-parent-traversal-dry-run/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/active-task-parent-traversal-start/README.md <> ./tests/fixtures/negative/execution-runner/active-task-parent-traversal-start/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/README.md <> ./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/session.md <> ./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/source-contract.md <> ./tests/fixtures/negative/execution-runner/behavior-verification-safe-help-command/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/README.md <> ./tests/fixtures/negative/execution-runner/blocked-session-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/session.md <> ./tests/fixtures/negative/execution-runner/blocked-session-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-scope/source-contract.md <> ./tests/fixtures/negative/execution-runner/blocked-session-scope/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/README.md <> ./tests/fixtures/negative/execution-runner/blocked-session-verification/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/session.md <> ./tests/fixtures/negative/execution-runner/blocked-session-verification/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/blocked-session-verification/source-contract.md <> ./tests/fixtures/negative/execution-runner/blocked-session-verification/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/README.md <> ./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/session.md <> ./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/source-contract.md <> ./tests/fixtures/negative/execution-runner/changed-file-absolute-path-scope/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/README.md <> ./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/session.md <> ./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/source-contract.md <> ./tests/fixtures/negative/execution-runner/changed-file-out-of-scope/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/README.md <> ./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/session.md <> ./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/source-contract.md <> ./tests/fixtures/negative/execution-runner/changed-file-outside-in-scope/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/README.md <> ./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/session.md <> ./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/source-contract.md <> ./tests/fixtures/negative/execution-runner/changed-file-parent-traversal-scope/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/README.md <> ./tests/fixtures/negative/execution-runner/missing-verification-plan/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/session.md <> ./tests/fixtures/negative/execution-runner/missing-verification-plan/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/missing-verification-plan/source-contract.md <> ./tests/fixtures/negative/execution-runner/missing-verification-plan/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/README.md <> ./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/session.md <> ./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/source-contract.md <> ./tests/fixtures/negative/execution-runner/path-boundary-scripts-old/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/session-absolute-path-scope/README.md <> ./tests/fixtures/negative/execution-runner/session-absolute-path-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/README.md <> ./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/session.md <> ./tests/fixtures/negative/execution-runner/session-missing-source-contract-scope/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/session-parent-traversal-scope/README.md <> ./tests/fixtures/negative/execution-runner/session-parent-traversal-scope/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/session-parent-traversal-verification/README.md <> ./tests/fixtures/negative/execution-runner/session-parent-traversal-verification/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/shared/source-task.md <> ./tests/fixtures/negative/execution-runner/shared/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/README.md <> ./tests/fixtures/negative/execution-runner/stopped-session-verification/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/session.md <> ./tests/fixtures/negative/execution-runner/stopped-session-verification/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/stopped-session-verification/source-contract.md <> ./tests/fixtures/negative/execution-runner/stopped-session-verification/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/README.md <> ./tests/fixtures/negative/execution-runner/unsafe-scope-entry/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/session.md <> ./tests/fixtures/negative/execution-runner/unsafe-scope-entry/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/unsafe-scope-entry/source-contract.md <> ./tests/fixtures/negative/execution-runner/unsafe-scope-entry/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/README.md <> ./tests/fixtures/negative/execution-runner/verification-absolute-executable/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/session.md <> ./tests/fixtures/negative/execution-runner/verification-absolute-executable/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-absolute-executable/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-absolute-executable/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/README.md <> ./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/session.md <> ./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-lifecycle-mutation-command/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/README.md <> ./tests/fixtures/negative/execution-runner/verification-mutating-git-command/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/session.md <> ./tests/fixtures/negative/execution-runner/verification-mutating-git-command/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-mutating-git-command/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-mutating-git-command/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/README.md <> ./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/session.md <> ./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-parent-traversal-argument/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/README.md <> ./tests/fixtures/negative/execution-runner/verification-shell-operator/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/session.md <> ./tests/fixtures/negative/execution-runner/verification-shell-operator/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-shell-operator/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-shell-operator/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/README.md <> ./tests/fixtures/negative/execution-runner/verification-unsupported-executable/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/session.md <> ./tests/fixtures/negative/execution-runner/verification-unsupported-executable/session 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/execution-runner/verification-unsupported-executable/source-contract.md <> ./tests/fixtures/negative/execution-runner/verification-unsupported-executable/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/blocked-by-not-list.md <> ./tests/fixtures/negative/queue/blocked-by-not-list 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/blocked-with-empty-blocked-by.md <> ./tests/fixtures/negative/queue/blocked-with-empty-blocked-by 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/empty-task-id.md <> ./tests/fixtures/negative/queue/empty-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/malformed-frontmatter.md <> ./tests/fixtures/negative/queue/malformed-frontmatter 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/missing-blocked-by.md <> ./tests/fixtures/negative/queue/missing-blocked-by 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/missing-priority.md <> ./tests/fixtures/negative/queue/missing-priority 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/missing-status.md <> ./tests/fixtures/negative/queue/missing-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/missing-task-id.md <> ./tests/fixtures/negative/queue/missing-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/unknown-priority.md <> ./tests/fixtures/negative/queue/unknown-priority 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/queue/unknown-status.md <> ./tests/fixtures/negative/queue/unknown-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/README.md <> ./tests/fixtures/negative/readiness/active-task-validation-fail/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/active-task.md <> ./tests/fixtures/negative/readiness/active-task-validation-fail/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/approvals/approval-active-task-validation-fail.md <> ./tests/fixtures/negative/readiness/active-task-validation-fail/approvals/approval-active-task-validation-fail 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/source-contract.md <> ./tests/fixtures/negative/readiness/active-task-validation-fail/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-fail/source-task.md <> ./tests/fixtures/negative/readiness/active-task-validation-fail/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/README.md <> ./tests/fixtures/negative/readiness/active-task-validation-partial/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/active-task.md <> ./tests/fixtures/negative/readiness/active-task-validation-partial/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/approvals/approval-active-task-validation-partial.md <> ./tests/fixtures/negative/readiness/active-task-validation-partial/approvals/approval-active-task-validation-partial 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/source-contract.md <> ./tests/fixtures/negative/readiness/active-task-validation-partial/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/active-task-validation-partial/source-task.md <> ./tests/fixtures/negative/readiness/active-task-validation-partial/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/README.md <> ./tests/fixtures/negative/readiness/analysis-status-conflict/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/active-task.md <> ./tests/fixtures/negative/readiness/analysis-status-conflict/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/approvals/approval-analysis-status-conflict.md <> ./tests/fixtures/negative/readiness/analysis-status-conflict/approvals/approval-analysis-status-conflict 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/source-contract.md <> ./tests/fixtures/negative/readiness/analysis-status-conflict/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-conflict/source-task.md <> ./tests/fixtures/negative/readiness/analysis-status-conflict/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/README.md <> ./tests/fixtures/negative/readiness/analysis-status-invalid/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/active-task.md <> ./tests/fixtures/negative/readiness/analysis-status-invalid/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/approvals/approval-analysis-status-invalid.md <> ./tests/fixtures/negative/readiness/analysis-status-invalid/approvals/approval-analysis-status-invalid 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/source-contract.md <> ./tests/fixtures/negative/readiness/analysis-status-invalid/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/analysis-status-invalid/source-task.md <> ./tests/fixtures/negative/readiness/analysis-status-invalid/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/README.md <> ./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/active-task.md <> ./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-contract.md <> ./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-task.md <> ./tests/fixtures/negative/readiness/approval-direct-checks-pass-with-limitations/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/README.md <> ./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/active-task.md <> ./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-contract.md <> ./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-task.md <> ./tests/fixtures/negative/readiness/approval-id-mismatch-if-present/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-expired/README.md <> ./tests/fixtures/negative/readiness/approval-marker-expired/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-expired/active-task.md <> ./tests/fixtures/negative/readiness/approval-marker-expired/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-expired/approvals/approval-approval-marker-expired.md <> ./tests/fixtures/negative/readiness/approval-marker-expired/approvals/approval-approval-marker-expired 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-expired/source-contract.md <> ./tests/fixtures/negative/readiness/approval-marker-expired/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-expired/source-task.md <> ./tests/fixtures/negative/readiness/approval-marker-expired/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/README.md <> ./tests/fixtures/negative/readiness/approval-marker-invalid/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/active-task.md <> ./tests/fixtures/negative/readiness/approval-marker-invalid/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/approvals/approval-approval-marker-invalid.md <> ./tests/fixtures/negative/readiness/approval-marker-invalid/approvals/approval-approval-marker-invalid 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/source-contract.md <> ./tests/fixtures/negative/readiness/approval-marker-invalid/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-invalid/source-task.md <> ./tests/fixtures/negative/readiness/approval-marker-invalid/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/README.md <> ./tests/fixtures/negative/readiness/approval-marker-malformed/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/active-task.md <> ./tests/fixtures/negative/readiness/approval-marker-malformed/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/approvals/approval-approval-marker-malformed.md <> ./tests/fixtures/negative/readiness/approval-marker-malformed/approvals/approval-approval-marker-malformed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/source-contract.md <> ./tests/fixtures/negative/readiness/approval-marker-malformed/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-malformed/source-task.md <> ./tests/fixtures/negative/readiness/approval-marker-malformed/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/README.md <> ./tests/fixtures/negative/readiness/approval-marker-revoked/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/active-task.md <> ./tests/fixtures/negative/readiness/approval-marker-revoked/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/approvals/approval-approval-marker-revoked.md <> ./tests/fixtures/negative/readiness/approval-marker-revoked/approvals/approval-approval-marker-revoked 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/source-contract.md <> ./tests/fixtures/negative/readiness/approval-marker-revoked/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-revoked/source-task.md <> ./tests/fixtures/negative/readiness/approval-marker-revoked/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/README.md <> ./tests/fixtures/negative/readiness/approval-marker-unresolved/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/active-task.md <> ./tests/fixtures/negative/readiness/approval-marker-unresolved/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-contract.md <> ./tests/fixtures/negative/readiness/approval-marker-unresolved/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-marker-unresolved/source-task.md <> ./tests/fixtures/negative/readiness/approval-marker-unresolved/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/README.md <> ./tests/fixtures/negative/readiness/approval-scope-mismatch/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/active-task.md <> ./tests/fixtures/negative/readiness/approval-scope-mismatch/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/approvals/approval-approval-scope-mismatch.md <> ./tests/fixtures/negative/readiness/approval-scope-mismatch/approvals/approval-approval-scope-mismatch 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-contract.md <> ./tests/fixtures/negative/readiness/approval-scope-mismatch/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-scope-mismatch/source-task.md <> ./tests/fixtures/negative/readiness/approval-scope-mismatch/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/README.md <> ./tests/fixtures/negative/readiness/approval-task-id-mismatch/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/active-task.md <> ./tests/fixtures/negative/readiness/approval-task-id-mismatch/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals/approval-approval-task-id-mismatch.md <> ./tests/fixtures/negative/readiness/approval-task-id-mismatch/approvals/approval-approval-task-id-mismatch 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-contract.md <> ./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-task.md <> ./tests/fixtures/negative/readiness/approval-task-id-mismatch/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/README.md <> ./tests/fixtures/negative/readiness/approval-transition-mismatch/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/active-task.md <> ./tests/fixtures/negative/readiness/approval-transition-mismatch/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/approvals/approval-approval-transition-mismatch.md <> ./tests/fixtures/negative/readiness/approval-transition-mismatch/approvals/approval-approval-transition-mismatch 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-contract.md <> ./tests/fixtures/negative/readiness/approval-transition-mismatch/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/approval-transition-mismatch/source-task.md <> ./tests/fixtures/negative/readiness/approval-transition-mismatch/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-completed/README.md <> ./tests/fixtures/negative/readiness/detected-state-completed/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-completed/active-task.md <> ./tests/fixtures/negative/readiness/detected-state-completed/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-completed/source-contract.md <> ./tests/fixtures/negative/readiness/detected-state-completed/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-completed/source-task.md <> ./tests/fixtures/negative/readiness/detected-state-completed/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-conflict/README.md <> ./tests/fixtures/negative/readiness/detected-state-conflict/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-conflict/active-task.md <> ./tests/fixtures/negative/readiness/detected-state-conflict/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-conflict/source-contract.md <> ./tests/fixtures/negative/readiness/detected-state-conflict/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-conflict/source-task.md <> ./tests/fixtures/negative/readiness/detected-state-conflict/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-dropped/README.md <> ./tests/fixtures/negative/readiness/detected-state-dropped/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-dropped/active-task.md <> ./tests/fixtures/negative/readiness/detected-state-dropped/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-dropped/source-contract.md <> ./tests/fixtures/negative/readiness/detected-state-dropped/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-dropped/source-task.md <> ./tests/fixtures/negative/readiness/detected-state-dropped/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-failed/README.md <> ./tests/fixtures/negative/readiness/detected-state-failed/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-failed/active-task.md <> ./tests/fixtures/negative/readiness/detected-state-failed/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-failed/source-contract.md <> ./tests/fixtures/negative/readiness/detected-state-failed/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-failed/source-task.md <> ./tests/fixtures/negative/readiness/detected-state-failed/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-invalid/README.md <> ./tests/fixtures/negative/readiness/detected-state-invalid/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-invalid/active-task.md <> ./tests/fixtures/negative/readiness/detected-state-invalid/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-invalid/source-contract.md <> ./tests/fixtures/negative/readiness/detected-state-invalid/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/detected-state-invalid/source-task.md <> ./tests/fixtures/negative/readiness/detected-state-invalid/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/README.md <> ./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/active-task.md <> ./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-contract.md <> ./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-task.md <> ./tests/fixtures/negative/readiness/missing-approval-validator-unreliable-direct-checks/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-state-validator/README.md <> ./tests/fixtures/negative/readiness/missing-state-validator/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-state-validator/active-task.md <> ./tests/fixtures/negative/readiness/missing-state-validator/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-state-validator/source-contract.md <> ./tests/fixtures/negative/readiness/missing-state-validator/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/missing-state-validator/source-task.md <> ./tests/fixtures/negative/readiness/missing-state-validator/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/README.md <> ./tests/fixtures/negative/readiness/validate-task-state-fail/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/active-task.md <> ./tests/fixtures/negative/readiness/validate-task-state-fail/active-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/source-contract.md <> ./tests/fixtures/negative/readiness/validate-task-state-fail/source-contract 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/readiness/validate-task-state-fail/source-task.md <> ./tests/fixtures/negative/readiness/validate-task-state-fail/source-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/blocked-but-execution-true/README.md <> ./tests/fixtures/negative/review/blocked-but-execution-true/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/blocked-but-execution-true/REVIEW.md <> ./tests/fixtures/negative/review/blocked-but-execution-true/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/blocked-but-execution-true.md <> ./tests/fixtures/negative/review/blocked-but-execution-true 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/missing-execution-allowed.md <> ./tests/fixtures/negative/review/missing-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/missing-review-status/README.md <> ./tests/fixtures/negative/review/missing-review-status/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/missing-review-status/REVIEW.md <> ./tests/fixtures/negative/review/missing-review-status/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/missing-review-status.md <> ./tests/fixtures/negative/review/missing-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/ready-but-execution-false/README.md <> ./tests/fixtures/negative/review/ready-but-execution-false/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/ready-but-execution-false/REVIEW.md <> ./tests/fixtures/negative/review/ready-but-execution-false/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/ready-but-execution-false.md <> ./tests/fixtures/negative/review/ready-but-execution-false 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/review/unknown-review-status.md <> ./tests/fixtures/negative/review/unknown-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/approved-mode-requested/README.md <> ./tests/fixtures/negative/runner/approved-mode-requested/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/approved-mode-requested/scenario.md <> ./tests/fixtures/negative/runner/approved-mode-requested/scenario 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/attempts-active-task-replace/README.md <> ./tests/fixtures/negative/runner/attempts-active-task-replace/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/attempts-active-task-replace/scenario.md <> ./tests/fixtures/negative/runner/attempts-active-task-replace/scenario 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/missing-human-checkpoint/README.md <> ./tests/fixtures/negative/runner/missing-human-checkpoint/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/runner/missing-human-checkpoint/scenario.md <> ./tests/fixtures/negative/runner/missing-human-checkpoint/scenario 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/executable-true/README.md <> ./tests/fixtures/negative/task-brief/executable-true/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/executable-true/TASK.md <> ./tests/fixtures/negative/task-brief/executable-true/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/README.md <> ./tests/fixtures/negative/task-brief/missing-acceptance-criteria/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK.md <> ./tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/missing-metadata/README.md <> ./tests/fixtures/negative/task-brief/missing-metadata/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/missing-metadata/TASK.md <> ./tests/fixtures/negative/task-brief/missing-metadata/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/status-not-approved/README.md <> ./tests/fixtures/negative/task-brief/status-not-approved/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/task-brief/status-not-approved/TASK.md <> ./tests/fixtures/negative/task-brief/status-not-approved/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/template-integrity/README.md <> ./tests/fixtures/negative/template-integrity/README 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/active-task-updated.md <> ./tests/fixtures/negative/trace/active-task-updated 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/empty-task-id.md <> ./tests/fixtures/negative/trace/empty-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/execution-approved.md <> ./tests/fixtures/negative/trace/execution-approved 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/malformed-frontmatter.md <> ./tests/fixtures/negative/trace/malformed-frontmatter 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/missing-decision-rationale.md <> ./tests/fixtures/negative/trace/missing-decision-rationale 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/missing-source-summary.md <> ./tests/fixtures/negative/trace/missing-source-summary 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/missing-task-id.md <> ./tests/fixtures/negative/trace/missing-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/replaces-review.md <> ./tests/fixtures/negative/trace/replaces-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/negative/trace/replaces-task.md <> ./tests/fixtures/negative/trace/replaces-task 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue/task-invalid.md <> ./tests/fixtures/queue-directory-validator/invalid/invalid-entry/tasks/queue/task-invalid 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-directory-validator/valid/tasks/done/task-done.md <> ./tests/fixtures/queue-directory-validator/valid/tasks/done/task-done 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-directory-validator/valid/tasks/dropped/task-dropped.md <> ./tests/fixtures/queue-directory-validator/valid/tasks/dropped/task-dropped 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-directory-validator/valid/tasks/queue/task-queued.md <> ./tests/fixtures/queue-directory-validator/valid/tasks/queue/task-queued 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/blocked-by-not-list.md <> ./tests/fixtures/queue-validator/invalid/blocked-by-not-list 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/blocked-with-empty-blocked-by.md <> ./tests/fixtures/queue-validator/invalid/blocked-with-empty-blocked-by 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/empty-task-id.md <> ./tests/fixtures/queue-validator/invalid/empty-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/malformed-frontmatter.md <> ./tests/fixtures/queue-validator/invalid/malformed-frontmatter 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/missing-blocked-by.md <> ./tests/fixtures/queue-validator/invalid/missing-blocked-by 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/missing-priority.md <> ./tests/fixtures/queue-validator/invalid/missing-priority 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/missing-status.md <> ./tests/fixtures/queue-validator/invalid/missing-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/missing-task-id.md <> ./tests/fixtures/queue-validator/invalid/missing-task-id 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/unknown-priority.md <> ./tests/fixtures/queue-validator/invalid/unknown-priority 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/invalid/unknown-status.md <> ./tests/fixtures/queue-validator/invalid/unknown-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/valid/blocked-with-dependency.md <> ./tests/fixtures/queue-validator/valid/blocked-with-dependency 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/valid/done-low.md <> ./tests/fixtures/queue-validator/valid/done-low 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/valid/dropped-normal.md <> ./tests/fixtures/queue-validator/valid/dropped-normal 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/valid/queued-high.md <> ./tests/fixtures/queue-validator/valid/queued-high 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/queue-validator/valid/queued-normal.md <> ./tests/fixtures/queue-validator/valid/queued-normal 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/blocked-but-execution-true.md <> ./tests/fixtures/review-validator/invalid/blocked-but-execution-true 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/empty-execution-allowed.md <> ./tests/fixtures/review-validator/invalid/empty-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/empty-review-status.md <> ./tests/fixtures/review-validator/invalid/empty-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/invalid-execution-allowed.md <> ./tests/fixtures/review-validator/invalid/invalid-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/malformed-frontmatter.md <> ./tests/fixtures/review-validator/invalid/malformed-frontmatter 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/missing-execution-allowed.md <> ./tests/fixtures/review-validator/invalid/missing-execution-allowed 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/missing-review-status.md <> ./tests/fixtures/review-validator/invalid/missing-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/ready-but-execution-false.md <> ./tests/fixtures/review-validator/invalid/ready-but-execution-false 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/invalid/unknown-review-status.md <> ./tests/fixtures/review-validator/invalid/unknown-review-status 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/valid/blocked.md <> ./tests/fixtures/review-validator/valid/blocked 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/valid/needs-clarification.md <> ./tests/fixtures/review-validator/valid/needs-clarification 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/valid/ready.md <> ./tests/fixtures/review-validator/valid/ready 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/review-validator/valid/ready-with-edits.md <> ./tests/fixtures/review-validator/valid/ready-with-edits 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-brief/invalid-task-brief-executable-true.md <> ./tests/fixtures/task-brief/invalid-task-brief-executable-true 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-brief/invalid-task-brief-missing-section.md <> ./tests/fixtures/task-brief/invalid-task-brief-missing-section 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-brief/valid-task-brief.md <> ./tests/fixtures/task-brief/valid-task-brief 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/task-health.md <> ./tests/fixtures/task-health/task-health 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/drafts/task-20260426-ready-contract-draft.md <> ./tests/fixtures/task-health/tasks/drafts/task-20260426-ready-contract-draft 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/queue/blocked-example.md <> ./tests/fixtures/task-health/tasks/queue/blocked-example 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/queue/queued-example.md <> ./tests/fixtures/task-health/tasks/queue/queued-example 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/REVIEW.md <> ./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/TASK.md <> ./tests/fixtures/task-health/tasks/task-20260426-needs-clarification/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-no-review/TASK.md <> ./tests/fixtures/task-health/tasks/task-20260426-no-review/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/REVIEW.md <> ./tests/fixtures/task-health/tasks/task-20260426-ready/REVIEW 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/TASK.md <> ./tests/fixtures/task-health/tasks/task-20260426-ready/TASK 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/task-health/tasks/task-20260426-ready/TRACE.md <> ./tests/fixtures/task-health/tasks/task-20260426-ready/TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/INIT.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/project/PROJECT.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/project/PROJECT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/repo-map.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview/BOOT.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/stages/01-interview/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard/BOOT.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/stages/spec-wizard/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/queue-entry.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/templates/queue-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-brief-review.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-brief-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-contract-from-brief.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-contract-from-brief 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-decision-trace.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/templates/task-decision-trace 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner/RUNNER-PROTOCOL.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/agent-runner/RUNNER-PROTOCOL 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive/WRITE-TRACE.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/interview-archive/WRITE-TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder/BUILD-TASK-CONTRACT.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health/TASK-HEALTH.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-health/TASK-HEALTH 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue/MANAGE-QUEUE.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-queue/MANAGE-QUEUE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review/REVIEW-TASK-BRIEF.md <> ./tests/fixtures/template-integrity/forbidden-auto-runner/tools/task-review/REVIEW-TASK-BRIEF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/INIT.md <> ./tests/fixtures/template-integrity/missing-core-file/INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/project/PROJECT.md <> ./tests/fixtures/template-integrity/missing-core-file/project/PROJECT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/repo-map.md <> ./tests/fixtures/template-integrity/missing-core-file/repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/stages/01-interview/BOOT.md <> ./tests/fixtures/template-integrity/missing-core-file/stages/01-interview/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard/BOOT.md <> ./tests/fixtures/template-integrity/missing-core-file/stages/spec-wizard/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/templates/queue-entry.md <> ./tests/fixtures/template-integrity/missing-core-file/templates/queue-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-brief-review.md <> ./tests/fixtures/template-integrity/missing-core-file/templates/task-brief-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-contract-from-brief.md <> ./tests/fixtures/template-integrity/missing-core-file/templates/task-contract-from-brief 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/templates/task-decision-trace.md <> ./tests/fixtures/template-integrity/missing-core-file/templates/task-decision-trace 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/agent-runner/RUNNER-PROTOCOL.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/agent-runner/RUNNER-PROTOCOL 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/interview-archive/WRITE-TRACE.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/interview-archive/WRITE-TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder/BUILD-TASK-CONTRACT.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-health/TASK-HEALTH.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/task-health/TASK-HEALTH 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-queue/MANAGE-QUEUE.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/task-queue/MANAGE-QUEUE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-core-file/tools/task-review/REVIEW-TASK-BRIEF.md <> ./tests/fixtures/template-integrity/missing-core-file/tools/task-review/REVIEW-TASK-BRIEF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/INIT.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/project/PROJECT.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/project/PROJECT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/repo-map.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview/BOOT.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/stages/01-interview/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard/BOOT.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/stages/spec-wizard/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/queue-entry.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/templates/queue-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-brief-review.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-brief-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-contract-from-brief.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-contract-from-brief 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-decision-trace.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/templates/task-decision-trace 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner/RUNNER-PROTOCOL.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/agent-runner/RUNNER-PROTOCOL 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive/WRITE-TRACE.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/interview-archive/WRITE-TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder/BUILD-TASK-CONTRACT.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health/TASK-HEALTH.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-health/TASK-HEALTH 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue/MANAGE-QUEUE.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-queue/MANAGE-QUEUE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review/REVIEW-TASK-BRIEF.md <> ./tests/fixtures/template-integrity/missing-fixtures-warning/tools/task-review/REVIEW-TASK-BRIEF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/INIT.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/project/PROJECT.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/project/PROJECT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/repo-map.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/repo-map 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview/BOOT.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/01-interview/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard/BOOT.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/stages/spec-wizard/BOOT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/queue-entry.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/queue-entry 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-brief-review.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-brief-review 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-contract-from-brief.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-contract-from-brief 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-decision-trace.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/templates/task-decision-trace 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner/RUNNER-PROTOCOL.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/agent-runner/RUNNER-PROTOCOL 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive/WRITE-TRACE.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/interview-archive/WRITE-TRACE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder/BUILD-TASK-CONTRACT.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-contract-builder/BUILD-TASK-CONTRACT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health/TASK-HEALTH.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-health/TASK-HEALTH 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue/MANAGE-QUEUE.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-queue/MANAGE-QUEUE 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review/REVIEW-TASK-BRIEF.md <> ./tests/fixtures/template-integrity/missing-gitignore-drafts/tools/task-review/REVIEW-TASK-BRIEF 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/INIT.md <> ./tests/fixtures/template-integrity/missing-optional-report-warning/INIT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/project/PROJECT.md <> ./tests/fixtures/template-integrity/missing-optional-report-warning/project/PROJECT 2.md` | Вне критичных зон или низкий риск | EXACT_COPY |

## Git Evidence

Для HIGH-риска показаны `git log --oneline -5 <filename>`.

| File | Git History Summary | Notes |
|---|---|---|
| `./core-rules/MAIN.md` | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> 21a1643 extract: instruction-priority + owner + system-constraints → core-rules/MAIN.md <br> 8150031 extract: document-governance → core-rules/MAIN.md <br> 90baede extract: decision-guide → core-rules/MAIN.md <br> 58c9afe extract: anti-patterns → core-rules/MAIN.md | HIGH pair (EXACT_COPY) A |
| `./core-rules/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/ACTIVATION-RECOVERY.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./docs/ACTIVATION-RECOVERY 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/ACTIVE-TASK-FORMAT.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./docs/ACTIVE-TASK-FORMAT 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/ACTIVE-TASK-VALIDATION.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./docs/ACTIVE-TASK-VALIDATION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPLIED-TRANSITION-RECORD.md` | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/APPLIED-TRANSITION-RECORD 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPLY-COMMAND-INTEGRATION.md` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline <br> e6c9069 feat(m17): approval evidence and authorization hardening layer <br> 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | HIGH pair (EXACT_COPY) A |
| `./docs/APPLY-COMMAND-INTEGRATION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPLY-PLAN.md` | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/APPLY-PLAN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPLY-PRECONDITIONS.md` | 8eb08d1 feat(check-apply-preconditions): add policy gate before approval check <br> e6c9069 feat(m17): approval evidence and authorization hardening layer <br> e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/APPLY-PRECONDITIONS 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPROVAL-EVIDENCE-STORAGE.md` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./docs/APPROVAL-EVIDENCE-STORAGE 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPROVAL-MARKER-SPEC.md` | a678121 feat(m10.14.1): approval marker spec <br> ef3e281 feat(m10.11.1): add approval marker spec | HIGH pair (EXACT_COPY) A |
| `./docs/APPROVAL-MARKER-SPEC 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPROVAL-REQUIREMENT-POLICY.md` | 0f23129 docs(operation-risk-model): create canonical risk class definitions | HIGH pair (EXACT_COPY) A |
| `./docs/APPROVAL-REQUIREMENT-POLICY 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/APPROVED-MODE-CONTRACT.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./docs/APPROVED-MODE-CONTRACT 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/COMPLETION-READINESS.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/COMPLETION-READINESS 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/COMPLETION-TRANSITION.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/COMPLETION-TRANSITION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/CONTROLLED-COMPLETION.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/CONTROLLED-COMPLETION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/CONTROLLED-COMPLETION-WORKFLOW.md` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline <br> e6c9069 feat(m17): approval evidence and authorization hardening layer <br> 8063fa0 docs(m16): add CONTROLLED-COMPLETION-WORKFLOW.md | HIGH pair (EXACT_COPY) A |
| `./docs/CONTROLLED-COMPLETION-WORKFLOW 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/CONTROLLED-EXECUTION-RUNNER.md` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./docs/CONTROLLED-EXECUTION-RUNNER 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/CONTROLLED-FAILURE-AND-REVIEW.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/CONTROLLED-FAILURE-AND-REVIEW 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/CONTROLLED-LIFECYCLE-MUTATION.md` | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./docs/CONTROLLED-LIFECYCLE-MUTATION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/EXECUTION-READINESS.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./docs/EXECUTION-READINESS 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/EXECUTION-SESSION.md` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./docs/EXECUTION-SESSION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/GETTING-STARTED.md` | e4c81fc docs(core): update agentos entrypoints and boundaries | HIGH pair (EXACT_COPY) A |
| `./docs/GETTING-STARTED 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/HUMAN-APPROVAL-BOUNDARY.md` | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | HIGH pair (EXACT_COPY) A |
| `./docs/HUMAN-APPROVAL-BOUNDARY 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/HUMAN-APPROVAL-EVIDENCE.md` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./docs/HUMAN-APPROVAL-EVIDENCE 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/LIFECYCLE-INTEGRATION.md` | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | HIGH pair (EXACT_COPY) A |
| `./docs/LIFECYCLE-INTEGRATION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/OPERATION-RISK-MODEL.md` | 0f23129 docs(operation-risk-model): create canonical risk class definitions | HIGH pair (EXACT_COPY) A |
| `./docs/OPERATION-RISK-MODEL 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/SAFE-TRANSITION-EXECUTION.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./docs/SAFE-TRANSITION-EXECUTION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/SAFETY-BOUNDARIES.md` | e4c81fc docs(core): update agentos entrypoints and boundaries | HIGH pair (EXACT_COPY) A |
| `./docs/SAFETY-BOUNDARIES 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/TASK-STATE-MACHINE.md` | 11cb1b4 feat(m10.13.1): state/analysis separation <br> 27e1557 docs(m10): clarify state vs analysis_status, mark failed as reserved <br> 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./docs/TASK-STATE-MACHINE 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/TASK-TRANSITION-RULES.md` | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./docs/TASK-TRANSITION-RULES 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/VALIDATION.md` | e4c81fc docs(core): update agentos entrypoints and boundaries <br> 47a7e8d 2 <br> d63ca9a fix: устранить критичные и средние ошибки аудита <br> 2940402 feat: добавить PROJECT-MEMORY, VALIDATION и ERROR-TYPES документы | HIGH pair (EXACT_COPY) A |
| `./docs/VALIDATION 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./docs/quickstart.md` | 04988ce chore(m21): finalize packaging audit and milestone reviews <br> 1f467cf chore(worktree): pre-existing unrelated changes <br> c8117c1 feat(example-project): add example validation flow | HIGH pair (NEAR_COPY) A |
| `./docs/quickstart 2.md` | NOT_COMMITTED | HIGH pair (NEAR_COPY) B |
| `./docs/usage.md` | 04988ce chore(m21): finalize packaging audit and milestone reviews <br> 1f467cf chore(worktree): pre-existing unrelated changes <br> c8117c1 feat(example-project): add example validation flow | HIGH pair (NEAR_COPY) A |
| `./docs/usage 2.md` | NOT_COMMITTED | HIGH pair (NEAR_COPY) B |
| `./quality/MAIN.md` | 1e053f3 Stabilize canonical module architecture and validators <br> eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> 0e7a68a extract: release-blockers + post-launch → quality/MAIN.md <br> 3a4c517 extract: testing + verification + scenarios → quality/MAIN.md <br> db43ac0 extract: audit → quality/MAIN.md | HIGH pair (EXACT_COPY) A |
| `./quality/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/activation-audit-report.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./reports/activation-audit-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/activation-positive-smoke.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./reports/activation-positive-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/active-task-governance-audit-report.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./reports/active-task-governance-audit-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/agentos-validate-cli-hardening.md` | 1f467cf chore(worktree): pre-existing unrelated changes | HIGH pair (EXACT_COPY) A |
| `./reports/agentos-validate-cli-hardening 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/agentos-validate-json-smoke.md` | 1f467cf chore(worktree): pre-existing unrelated changes | HIGH pair (EXACT_COPY) A |
| `./reports/agentos-validate-json-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/agentos-validate-smoke.md` | 1f467cf chore(worktree): pre-existing unrelated changes | HIGH pair (EXACT_COPY) A |
| `./reports/agentos-validate-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/agentos-validate-usage-integration.md` | 1f467cf chore(worktree): pre-existing unrelated changes | HIGH pair (EXACT_COPY) A |
| `./reports/agentos-validate-usage-integration 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/audit.md` | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report <br> 517ed04 docs(examples-reports): add usage scenarios and validation reports | HIGH pair (EXACT_COPY) A |
| `./reports/audit 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/audit-smoke.md` | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report <br> 517ed04 docs(examples-reports): add usage scenarios and validation reports | HIGH pair (EXACT_COPY) A |
| `./reports/audit-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023.md` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/execution-evidence-report.md` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./reports/execution-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/guard-failures-smoke.md` | 517ed04 docs(examples-reports): add usage scenarios and validation reports | HIGH pair (EXACT_COPY) A |
| `./reports/guard-failures-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10-completion-review.md` | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10-final-hardening-review.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs <br> b8da991 feat(m10.18.1): milestone 10 final hardening review | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10-final-hardening-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10.11-state-report-hardening.md` | da5300b chore(reports): add milestone-10.11 report alias for 10.12.1 preflight | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10.11-state-report-hardening 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10.11.1-approval-marker-spec.md` | ef3e281 feat(m10.11.1): add approval marker spec | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10.11.1-approval-marker-spec 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10.11.2-v1.1-hardening.md` | edffb6d feat(m10.11.2): task state report v1.1 hardening | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10.11.2-v1.1-hardening 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10.12-downstream-v1.1-compatibility.md` | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-10.12-downstream-v1.1-compatibility 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-10.13-state-analysis-separation.md` | cdbf1bc fix(doc-tests): replace absolute local paths with relative in reports <br> 11cb1b4 feat(m10.13.1): state/analysis separation | HIGH pair (NEAR_COPY) A |
| `./reports/milestone-10.13-state-analysis-separation 2.md` | NOT_COMMITTED | HIGH pair (NEAR_COPY) B |
| `./reports/milestone-11-completion-review.md` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-11-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-12-completion-review.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-12-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-13-completion-review.md` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-13-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-14-completion-review.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-14-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-14-evidence-report.md` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-14-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-15-completion-review.md` | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-15-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-15-evidence-report.md` | e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-15-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-16-completion-review.md` | c504080 docs(m16): finalize milestone 16 status reports <br> e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-16-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-16-evidence-report.md` | c504080 docs(m16): finalize milestone 16 status reports <br> e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-16-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-17-completion-review.md` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-17-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-17-evidence-report.md` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-17-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-18-completion-review.md` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-18-completion-review 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-18-evidence-report.md` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-18-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/milestone-7.1-handoff.md` | 517ed04 docs(examples-reports): add usage scenarios and validation reports | HIGH pair (EXACT_COPY) A |
| `./reports/milestone-7.1-handoff 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/negative-fixtures-smoke.md` | 32306aa test(7.1.6): add negative fixture runner smoke report | HIGH pair (EXACT_COPY) A |
| `./reports/negative-fixtures-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/pre-execution-evidence-report.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./reports/pre-execution-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/release-checklist.md` | 452b49f feat(8.2.2): wire trace negative fixtures into runner | HIGH pair (EXACT_COPY) A |
| `./reports/release-checklist 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/session-handoff.md` | dae7288 chore(hand-off): record milestone 12 closure and hardening <br> 445c018 chore(hand-off): record milestone 11 completion <br> 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs <br> 4a4260d docs: save current session context | HIGH pair (EXACT_COPY) A |
| `./reports/session-handoff 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/task-health.md` | cdbf1bc fix(doc-tests): replace absolute local paths with relative in reports <br> d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (NEAR_COPY) A |
| `./reports/task-health 2.md` | NOT_COMMITTED | HIGH pair (NEAR_COPY) B |
| `./reports/task-state-machine-smoke.md` | 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./reports/task-state-machine-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/templates/verification-report.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./reports/templates/verification-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./reports/verification.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./reports/verification 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/VALIDATORS.md` | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> ed209b8 fix(stage-2): classify validators as canonical vs legacy in VALIDATORS.md <br> e078571 fix: reduce route ambiguity in README and llms | HIGH pair (EXACT_COPY) A |
| `./scripts/VALIDATORS 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/activate-task.py` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./scripts/activate-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/agent-complete.py` | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing <br> d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/agent-fail.py` | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing <br> d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/agent-next.py` | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing <br> d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/agentos-validate.py` | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit <br> 04184f7 feat(m12): finalize active task governance and readiness reports <br> 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs <br> 63dd2c4 feat(m10.17.1): approval-fixtures CLI command <br> bcfdc5e feat(m9.1.1): add unified validation wrapper | HIGH pair (EXACT_COPY) A |
| `./scripts/agentos-validate 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/apply-transition.py` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline <br> f839d76 fix(apply-transition): implement approval gate for complete-active mode <br> e6c9069 feat(m17): approval evidence and authorization hardening layer <br> e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps <br> e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./scripts/apply-transition 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/audit-agentos.py` | 97aab4b feat(8.6.2-8.6.3): update audit runner and add smoke report <br> 033e264 feat(validation): add guard-failure and audit runners | HIGH pair (EXACT_COPY) A |
| `./scripts/audit-agentos 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/audit-approval-boundary.py` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./scripts/audit-approval-boundary 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/audit-lifecycle-mutation.py` | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | HIGH pair (EXACT_COPY) A |
| `./scripts/audit-lifecycle-mutation 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/audit-policy-boundary.py` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | HIGH pair (EXACT_COPY) A |
| `./scripts/audit-policy-boundary 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/audit-release-readiness.py` | 57c03d7 docs(m20): refresh evidence and completion review | HIGH pair (EXACT_COPY) A |
| `./scripts/audit-release-readiness 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-apply-preconditions.py` | 8eb08d1 feat(check-apply-preconditions): add policy gate before approval check <br> e6c9069 feat(m17): approval evidence and authorization hardening layer <br> e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./scripts/check-apply-preconditions 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-completion-readiness.py` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./scripts/check-completion-readiness 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-dangerous-commands.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/check-dangerous-commands 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-execution-readiness.py` | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit <br> 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./scripts/check-execution-readiness 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-execution-scope.py` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./scripts/check-execution-scope 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-links.py` | 1e053f3 Stabilize canonical module architecture and validators <br> dbed59d Cleanup repo: remove legacy/LAYER docs and keep canonical architecture only <br> e078571 fix: reduce route ambiguity in README and llms | HIGH pair (EXACT_COPY) A |
| `./scripts/check-links 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-pr-quality.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/check-pr-quality 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-risk.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/check-risk 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/check-transition.py` | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility <br> 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./scripts/check-transition 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/complete-active-task.py` | e64f9d8 docs(m14): add controlled completion gate artifacts and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./scripts/complete-active-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/detect-task-state.py` | 11cb1b4 feat(m10.13.1): state/analysis separation <br> edffb6d feat(m10.11.2): task state report v1.1 hardening <br> 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./scripts/detect-task-state 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/generate-repo-map.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/generate-repo-map 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/generate-task-contract.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/generate-task-contract 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/lib/__init__.py` | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | HIGH pair (EXACT_COPY) A |
| `./scripts/lib/__init__ 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/lib/path_utils.py` | 173ff2a fix(m12): harden path resolution and pointer-aware pre-commit | HIGH pair (EXACT_COPY) A |
| `./scripts/lib/path_utils 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/run-active-task.py` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./scripts/run-active-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/run-execution-verification.py` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./scripts/run-execution-verification 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/select-context.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/select-context 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/task-health.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/task-health 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-activation-fixtures.py` | 1cb95ce feat(m11): add safe activation layer, fixtures, and recovery docs | HIGH pair (EXACT_COPY) A |
| `./scripts/test-activation-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-active-task-fixtures.py` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./scripts/test-active-task-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-apply-transition-fixtures.py` | 39b732b fix(m16): fix two gaps in apply-transition and fixture runner <br> 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) <br> e0d4892 feat(m15): add lifecycle mutation controls and milestone reviews | HIGH pair (EXACT_COPY) A |
| `./scripts/test-apply-transition-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-approval-fixtures.py` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./scripts/test-approval-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-approval-flow-smoke.py` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./scripts/test-approval-flow-smoke 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-approval-marker-fixtures.py` | 6157be6 feat(m10.16.1): approval marker negative fixtures | HIGH pair (EXACT_COPY) A |
| `./scripts/test-approval-marker-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-completion-flow-smoke.py` | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | HIGH pair (EXACT_COPY) A |
| `./scripts/test-completion-flow-smoke 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-execution-runner-fixtures.py` | 17b9664 feat(m13): save controlled execution runner milestone artifacts | HIGH pair (EXACT_COPY) A |
| `./scripts/test-execution-runner-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-guard-failures.py` | 218521d feat(8.5.1): add runner protocol static validator <br> 033e264 feat(validation): add guard-failure and audit runners | HIGH pair (EXACT_COPY) A |
| `./scripts/test-guard-failures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-human-approval-fixtures.py` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./scripts/test-human-approval-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-negative-fixtures.py` | 57c03d7 docs(m20): refresh evidence and completion review <br> 9edebde feat(8.4.2): wire contract draft negative fixtures <br> 3e0b0b6 feat(8.3.3): wire queue negative fixtures into runner <br> 5cf2a97 feat(8.2.2): wire trace negative fixtures into runner <br> a115af2 test(7.1.4): add negative fixture test runner MVP | HIGH pair (NEAR_COPY) A |
| `./scripts/test-negative-fixtures 2.py` | NOT_COMMITTED | HIGH pair (NEAR_COPY) B |
| `./scripts/test-policy-enforcement-fixtures.py` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | HIGH pair (EXACT_COPY) A |
| `./scripts/test-policy-enforcement-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-policy-fixtures.py` | 0f23129 docs(operation-risk-model): create canonical risk class definitions | HIGH pair (EXACT_COPY) A |
| `./scripts/test-policy-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-policy-flow-smoke.py` | 570e27a feat(milestone-18): complete policy gate and enforcement pipeline | HIGH pair (EXACT_COPY) A |
| `./scripts/test-policy-flow-smoke 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-readiness-fixtures.py` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./scripts/test-readiness-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-state-fixtures.py` | fecfcb1 feat(m10.12.1): downstream v1.1 compatibility <br> add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./scripts/test-state-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/test-template-integrity-fixtures.py` | 57c03d7 docs(m20): refresh evidence and completion review | HIGH pair (EXACT_COPY) A |
| `./scripts/test-template-integrity-fixtures 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-active-task.py` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-active-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-approval-marker.py` | 9241afd feat(m10.15.1): approval marker validator | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-approval-marker 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-commit-msg.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-commit-msg 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-contract-draft.py` | 9edebde feat(8.4.2): wire contract draft negative fixtures | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-contract-draft 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-docs.py` | eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> af31e09 fix(quality-2): consolidate legacy quality content into canonical quality/MAIN.md <br> e078571 fix: reduce route ambiguity in README and llms | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-docs 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-handoff.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-handoff 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-human-approval.py` | e6c9069 feat(m17): approval evidence and authorization hardening layer | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-human-approval 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-incident.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-incident 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-lessons.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-lessons 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-lifecycle-apply.py` | 3878dad feat(m16): push M16 integration artifacts (16.1.1-16.6.1) | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-lifecycle-apply 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-policy.py` | 0f23129 docs(operation-risk-model): create canonical risk class definitions | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-policy 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-queue.py` | 84558a7 fix(m10.19): pre-m11 script fixes for queue/status parsing <br> 0451da8 feat(8.3.2): add queue directory validator | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-queue 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-queue-entry.py` | 6496270 feat(8.3.1): add queue entry validator | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-queue-entry 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-review.py` | 452b49f feat(8.2.2): wire trace negative fixtures into runner | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-review 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-route.py` | dbed59d Cleanup repo: remove legacy/LAYER docs and keep canonical architecture only <br> eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> e078571 fix: reduce route ambiguity in README and llms | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-route 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-runner-protocol.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-runner-protocol 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-task.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-task-brief.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-task-brief 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-task-state.py` | 11cb1b4 feat(m10.13.1): state/analysis separation <br> edffb6d feat(m10.11.2): task state report v1.1 hardening <br> 10f324b feat(m10): add state awareness layer (10.1.1-10.10.1) | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-task-state 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-trace.py` | 452b49f feat(8.2.2): wire trace negative fixtures into runner | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-trace 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./scripts/validate-verification.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./scripts/validate-verification 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./security/MAIN.md` | 1e053f3 Stabilize canonical module architecture and validators <br> eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> 46d80cf extract: security → security/MAIN.md <br> 911f87c feat: deprecate legacy routes and stabilize new primary architecture | HIGH pair (EXACT_COPY) A |
| `./security/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./state/MAIN.md` | 1e053f3 Stabilize canonical module architecture and validators <br> eb1e383 Finalize canonical conversion: llms, routes, MAIN.md modules <br> 77138fa extract: state-transitions → state/MAIN.md <br> 375ba55 extract: session-lifecycle → state/MAIN.md <br> 24cc911 extract: event-dictionary → state/MAIN.md | HIGH pair (EXACT_COPY) A |
| `./state/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tasks/active-task.md` | 04184f7 feat(m12): finalize active task governance and readiness reports <br> c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./tasks/active-task 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tasks/templates/task-contract.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./tasks/templates/task-contract 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/reports/templates/verification-report.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/reports/templates/verification-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/reports/verification.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/reports/verification 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/VALIDATORS.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/VALIDATORS 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/check-dangerous-commands.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/check-dangerous-commands 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/check-links.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/check-links 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/check-pr-quality.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/check-pr-quality 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/check-risk.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/check-risk 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/generate-repo-map.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/generate-repo-map 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/select-context.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/select-context 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-commit-msg.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-commit-msg 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-docs.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-docs 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-handoff.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-handoff 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-incident.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-incident 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-lessons.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-lessons 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-route.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-route 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-task.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/scripts/validate-verification.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/scripts/validate-verification 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/tasks/active-task.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/tasks/active-task 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-full/tasks/templates/task-contract.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-full/tasks/templates/task-contract 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/reports/templates/verification-report.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/reports/templates/verification-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/reports/verification.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/reports/verification 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/scripts/validate-task.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/scripts/validate-task 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/scripts/validate-verification.py` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/scripts/validate-verification 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/tasks/active-task.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/tasks/active-task 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./templates/agentos-minimal/tasks/templates/task-contract.md` | c8117c1 feat(example-project): add example validation flow | HIGH pair (EXACT_COPY) A |
| `./templates/agentos-minimal/tasks/templates/task-contract 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/completion-flow-smoke/reports/execution/session-smoke.md` | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/completion-flow-smoke/reports/execution/session-smoke 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/completion-flow-smoke/reports/execution-evidence-report.md` | e81f8f6 feat(m16): complete stage artifacts and hotfix apply-transition gaps | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/completion-flow-smoke/reports/execution-evidence-report 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/active-task/missing-state/README.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/active-task/missing-state/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/active-task/missing-state/active-task.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/active-task/missing-state/active-task 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/active-task/missing-state/source-contract.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/active-task/missing-state/source-contract 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/active-task/missing-state/source-task.md` | 04184f7 feat(m12): finalize active task governance and readiness reports | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/active-task/missing-state/source-task 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/active-without-approval/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/active-without-approval/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/completed-and-active-conflict/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/completed-and-active-conflict/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/contract-without-trace/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/contract-without-trace/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/dropped-and-active-conflict/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/dropped-and-active-conflict/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/invalid-transition-brief-to-active/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/invalid-transition-brief-to-active/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/negative/state/review-ready-without-task/README.md` | add019e feat(m10.7.1): add negative state fixtures | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/negative/state/review-ready-without-task/README 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-complete.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-fail.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-next.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/invalid/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/valid/scripts/agent-complete.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/valid/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/valid/scripts/agent-fail.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/valid/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/valid/scripts/agent-next.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/valid/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-fail.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-next.py` | 218521d feat(8.5.1): add runner protocol static validator | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/runner-validator/valid-with-warnings/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/core-rules/MAIN.md` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/core-rules/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/reports/task-health.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/reports/task-health 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-complete.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-fail.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-next.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/auto-runner.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/auto-runner 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/generate-task-contract.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/generate-task-contract 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/task-health.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/task-health 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/validate-task-brief.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/scripts/validate-task-brief 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/workflow/MAIN.md` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/forbidden-auto-runner/workflow/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/reports/task-health.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/reports/task-health 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-complete.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-fail.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-next.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/generate-task-contract.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/generate-task-contract 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/task-health.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/task-health 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/validate-task-brief.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/scripts/validate-task-brief 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-core-file/workflow/MAIN.md` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-core-file/workflow/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/core-rules/MAIN.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/core-rules/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/reports/task-health.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/reports/task-health 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-complete.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-fail.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-next.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/generate-task-contract.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/generate-task-contract 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/task-health.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/task-health 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/validate-task-brief.py` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/scripts/validate-task-brief 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/workflow/MAIN.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-fixtures-warning/workflow/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules/MAIN.md` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/core-rules/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/reports/task-health.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/reports/task-health 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-complete.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-complete 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-fail.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-fail 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-next.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/agent-next 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/generate-task-contract.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/generate-task-contract 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/task-health.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/task-health 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/validate-task-brief.py` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/scripts/validate-task-brief 2.py` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/workflow/MAIN.md` | d796ea7 feat(7.0.1): add Template Integrity Checker MVP | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-gitignore-drafts/workflow/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/core-rules/MAIN.md` | 5530ff9 feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks | HIGH pair (EXACT_COPY) A |
| `./tests/fixtures/template-integrity/missing-optional-report-warning/core-rules/MAIN 2.md` | NOT_COMMITTED | HIGH pair (EXACT_COPY) B |

## Recommended Next Step

`RESOLVE_DUPLICATES_FIRST`

Найдено много HIGH-риска дублей в каталогах, которые влияют на правила, проверки и отчёты.
Без ручного решения по этим файлам карта source-of-truth может получить неоднозначные связи.
Сначала нужен человеческий выбор, какие копии считать каноническими.

Файлы, требующие решения человека перед следующим шагом:
- `./core-rules/MAIN 2.md`
- `./docs/ACTIVATION-RECOVERY 2.md`
- `./docs/ACTIVE-TASK-FORMAT 2.md`
- `./docs/ACTIVE-TASK-VALIDATION 2.md`
- `./docs/APPLIED-TRANSITION-RECORD 2.md`
- `./docs/APPLY-COMMAND-INTEGRATION 2.md`
- `./docs/APPLY-PLAN 2.md`
- `./docs/APPLY-PRECONDITIONS 2.md`
- `./docs/APPROVAL-EVIDENCE-STORAGE 2.md`
- `./docs/APPROVAL-MARKER-SPEC 2.md`
- `./docs/APPROVAL-REQUIREMENT-POLICY 2.md`
- `./docs/APPROVED-MODE-CONTRACT 2.md`
- `./docs/COMPLETION-READINESS 2.md`
- `./docs/COMPLETION-TRANSITION 2.md`
- `./docs/CONTROLLED-COMPLETION 2.md`
- `./docs/CONTROLLED-COMPLETION-WORKFLOW 2.md`
- `./docs/CONTROLLED-EXECUTION-RUNNER 2.md`
- `./docs/CONTROLLED-FAILURE-AND-REVIEW 2.md`
- `./docs/CONTROLLED-LIFECYCLE-MUTATION 2.md`
- `./docs/EXECUTION-READINESS 2.md`
- `./docs/EXECUTION-SESSION 2.md`
- `./docs/GETTING-STARTED 2.md`
- `./docs/HUMAN-APPROVAL-BOUNDARY 2.md`
- `./docs/HUMAN-APPROVAL-EVIDENCE 2.md`
- `./docs/LIFECYCLE-INTEGRATION 2.md`
- `./docs/OPERATION-RISK-MODEL 2.md`
- `./docs/SAFE-TRANSITION-EXECUTION 2.md`
- `./docs/SAFETY-BOUNDARIES 2.md`
- `./docs/TASK-STATE-MACHINE 2.md`
- `./docs/TASK-TRANSITION-RULES 2.md`
- `./docs/VALIDATION 2.md`
- `./docs/quickstart 2.md`
- `./docs/usage 2.md`
- `./quality/MAIN 2.md`
- `./reports/activation-audit-report 2.md`
- `./reports/activation-positive-smoke 2.md`
- `./reports/active-task-governance-audit-report 2.md`
- `./reports/agentos-validate-cli-hardening 2.md`
- `./reports/agentos-validate-json-smoke 2.md`
- `./reports/agentos-validate-smoke 2.md`
- `./reports/agentos-validate-usage-integration 2.md`
- `./reports/audit 2.md`
- `./reports/audit-smoke 2.md`
- `./reports/completion/completion-task-20260426-brief-readiness-check-20260430T004659Z 2.md`
- `./reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023 2.md`
- `./reports/execution-evidence-report 2.md`
- `./reports/guard-failures-smoke 2.md`
- `./reports/milestone-10-completion-review 2.md`
- `./reports/milestone-10-final-hardening-review 2.md`
- `./reports/milestone-10.11-state-report-hardening 2.md`
- `./reports/milestone-10.11.1-approval-marker-spec 2.md`
- `./reports/milestone-10.11.2-v1.1-hardening 2.md`
- `./reports/milestone-10.12-downstream-v1.1-compatibility 2.md`
- `./reports/milestone-10.13-state-analysis-separation 2.md`
- `./reports/milestone-11-completion-review 2.md`
- `./reports/milestone-12-completion-review 2.md`
- `./reports/milestone-13-completion-review 2.md`
- `./reports/milestone-14-completion-review 2.md`
- `./reports/milestone-14-evidence-report 2.md`
- `./reports/milestone-15-completion-review 2.md`
- `./reports/milestone-15-evidence-report 2.md`
- `./reports/milestone-16-completion-review 2.md`
- `./reports/milestone-16-evidence-report 2.md`
- `./reports/milestone-17-completion-review 2.md`
- `./reports/milestone-17-evidence-report 2.md`
- `./reports/milestone-18-completion-review 2.md`
- `./reports/milestone-18-evidence-report 2.md`
- `./reports/milestone-7.1-handoff 2.md`
- `./reports/negative-fixtures-smoke 2.md`
- `./reports/pre-execution-evidence-report 2.md`
- `./reports/release-checklist 2.md`
- `./reports/session-handoff 2.md`
- `./reports/task-health 2.md`
- `./reports/task-state-machine-smoke 2.md`
- `./reports/templates/verification-report 2.md`
- `./reports/verification 2.md`
- `./scripts/VALIDATORS 2.md`
- `./scripts/activate-task 2.py`
- `./scripts/agent-complete 2.py`
- `./scripts/agent-fail 2.py`
- `./scripts/agent-next 2.py`
- `./scripts/agentos-validate 2.py`
- `./scripts/apply-transition 2.py`
- `./scripts/audit-agentos 2.py`
- `./scripts/audit-approval-boundary 2.py`
- `./scripts/audit-lifecycle-mutation 2.py`
- `./scripts/audit-policy-boundary 2.py`
- `./scripts/audit-release-readiness 2.py`
- `./scripts/check-apply-preconditions 2.py`
- `./scripts/check-completion-readiness 2.py`
- `./scripts/check-dangerous-commands 2.py`
- `./scripts/check-execution-readiness 2.py`
- `./scripts/check-execution-scope 2.py`
- `./scripts/check-links 2.py`
- `./scripts/check-pr-quality 2.py`
- `./scripts/check-risk 2.py`
- `./scripts/check-transition 2.py`
- `./scripts/complete-active-task 2.py`
- `./scripts/detect-task-state 2.py`
- `./scripts/generate-repo-map 2.py`
- `./scripts/generate-task-contract 2.py`
- `./scripts/lib/__init__ 2.py`
- `./scripts/lib/path_utils 2.py`
- `./scripts/run-active-task 2.py`
- `./scripts/run-execution-verification 2.py`
- `./scripts/select-context 2.py`
- `./scripts/task-health 2.py`
- `./scripts/test-activation-fixtures 2.py`
- `./scripts/test-active-task-fixtures 2.py`
- `./scripts/test-apply-transition-fixtures 2.py`
- `./scripts/test-approval-fixtures 2.py`
- `./scripts/test-approval-flow-smoke 2.py`
- `./scripts/test-approval-marker-fixtures 2.py`
- `./scripts/test-completion-flow-smoke 2.py`
- `./scripts/test-execution-runner-fixtures 2.py`
- `./scripts/test-guard-failures 2.py`
- `./scripts/test-human-approval-fixtures 2.py`
- `./scripts/test-negative-fixtures 2.py`
- `./scripts/test-policy-enforcement-fixtures 2.py`
- `./scripts/test-policy-fixtures 2.py`
- `./scripts/test-policy-flow-smoke 2.py`
- `./scripts/test-readiness-fixtures 2.py`
- `./scripts/test-state-fixtures 2.py`
- `./scripts/test-template-integrity-fixtures 2.py`
- `./scripts/validate-active-task 2.py`
- `./scripts/validate-approval-marker 2.py`
- `./scripts/validate-commit-msg 2.py`
- `./scripts/validate-contract-draft 2.py`
- `./scripts/validate-docs 2.py`
- `./scripts/validate-handoff 2.py`
- `./scripts/validate-human-approval 2.py`
- `./scripts/validate-incident 2.py`
- `./scripts/validate-lessons 2.py`
- `./scripts/validate-lifecycle-apply 2.py`
- `./scripts/validate-policy 2.py`
- `./scripts/validate-queue 2.py`
- `./scripts/validate-queue-entry 2.py`
- `./scripts/validate-review 2.py`
- `./scripts/validate-route 2.py`
- `./scripts/validate-runner-protocol 2.py`
- `./scripts/validate-task 2.py`
- `./scripts/validate-task-brief 2.py`
- `./scripts/validate-task-state 2.py`
- `./scripts/validate-trace 2.py`
- `./scripts/validate-verification 2.py`
- `./security/MAIN 2.md`
- `./state/MAIN 2.md`
- `./tasks/active-task 2.md`
- `./tasks/templates/task-contract 2.md`
