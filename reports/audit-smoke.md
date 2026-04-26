# AgentOS Audit Smoke Report

## Metadata
- milestone: 8.6.3
- command: python3 scripts/audit-agentos.py
- date: 2026-04-27
- branch: dev

## Result
- overall_result: PASS_WITH_WARNINGS
- exit_code: 0

## Section Summary
- template-integrity: PASS (template-integrity-strict: PASS, template-integrity-self-test: PASS)
- negative-fixtures: PASS
- runner-protocol: WARN (optional suite failed inside guard-failures; expected for smoke evidence with warnings)
- guard-failures: PASS_WITH_WARNINGS
- other audit sections, if present:
  - release checklist: SKIPPED (future milestone)
  - full docs hardening: SKIPPED (future milestone)
  - example scenarios: SKIPPED (future milestone)
  - prompt packs: SKIPPED (future milestone)

## Output Summary
Audit smoke run completed successfully with warnings. Core suites template-integrity and negative-fixtures passed. Guard-failures returned PASS_WITH_WARNINGS because runner-protocol reported WARN (optional suite failed).

## Warnings
- guard-failures: PASS_WITH_WARNINGS
- runner-protocol: WARN - optional suite failed

## Failures
None

## Known Limitations
- Audit smoke report records one run only.
- PASS_WITH_WARNINGS is acceptable for smoke evidence if warnings are documented.
- This report does not approve release.
- This report does not approve execution.

## Safety Confirmation
- Audit smoke did not approve execution.
- Audit smoke did not move queue items.
- Audit smoke did not update tasks/active-task.md.
- Human approval remains required for execution/state transitions.
