# Release Checklist Tooling

## Purpose
Release checklist tooling documents the manual release-readiness process for AgentOS.

## Files
- `RELEASE-CHECKLIST.md`
- `reports/release-checklist.md`
- `reports/audit-smoke.md`
- `reports/audit.md`

## How to use
1. Read `RELEASE-CHECKLIST.md`.
2. Review audit evidence in `reports/audit-smoke.md` and `reports/audit.md`.
3. Optionally run validation commands manually.
4. Record review outcome in `reports/release-checklist.md`.
5. Human reviewer decides APPROVED / NOT APPROVED.

## Required evidence
- audit smoke report exists
- audit smoke Actual Result is PASS
- documentation files exist
- example scenarios exist
- prompt packs exist
- known limitations reviewed

## Human approval
Release requires explicit human approval.
No script or checklist can approve release automatically.

## Non-goals
This tool does not:
- run scripts
- publish release
- approve release automatically
- create validators
- execute tasks
- move queue items
