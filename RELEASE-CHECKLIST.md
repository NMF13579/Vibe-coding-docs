# AgentOS Release Checklist

## Purpose
This checklist is a manual release-readiness checklist for AgentOS MVP.
It helps a human reviewer decide whether the template is ready to publish or use.

The checklist does not approve release automatically.
Release decision requires human approval.

## Release scope
Current release-ready MVP includes:

- Markdown-first AgentOS workflow
- Input / discovery layer
- task brief validation
- review / trace process
- contract draft generation
- queue lifecycle scaffolding
- runner dry-run protocol
- task health metrics
- template integrity checker
- negative fixture runner
- guard failure runner
- audit runner
- docs hardening
- example scenarios
- prompt packs

## Required manual checks
- [ ] README explains what AgentOS is and is not
- [ ] Getting Started docs are present
- [ ] Validation docs are present
- [ ] Safety Boundaries docs are present
- [ ] Example scenarios are present
- [ ] Prompt packs are present
- [ ] Audit runner exists
- [ ] Audit smoke report exists
- [ ] Audit smoke result is PASS
- [ ] Known limitations are acceptable
- [ ] Human reviewer approves release

## Validation commands
Reviewer can run these commands manually:

- `python3 scripts/check-template-integrity.py --strict`
- `python3 scripts/test-template-integrity.py`
- `python3 scripts/test-negative-fixtures.py`
- `python3 scripts/test-guard-failures.py`
- `python3 scripts/audit-agentos.py`

This checklist documents commands but does not run them.

## Documentation readiness
Required files:

- `README.md`
- `docs/GETTING-STARTED.md`
- `docs/VALIDATION.md`
- `docs/SAFETY-BOUNDARIES.md`
- `examples/README.md`
- `prompt-packs/README.md`

## Safety boundaries
- AgentOS is not an autonomous agent.
- AgentOS does not execute tasks automatically.
- tasks/active-task.md is the only executable task contract.
- Task Briefs are not executable.
- Draft contracts are not active contracts.
- Queue items must not move without explicit human approval.
- Runner protocol scripts must not be run unless explicitly requested.
- Audit runner reports readiness signals; it does not approve release.

## Example scenarios
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`

## Prompt packs
- `prompt-packs/cursor.md`
- `prompt-packs/claude-code.md`
- `prompt-packs/codex-cli.md`
- `prompt-packs/chatgpt.md`

## Audit status
Latest expected audit smoke report:
`reports/audit-smoke.md`

Expected:
Actual Result = PASS

## Known limitations
- Release checklist is manual.
- Review / trace / queue / runner guard validators are future coverage.
- Runner protocol remains dry-run oriented.
- AgentOS is not a backend service.
- AgentOS is not a RAG platform.
- AgentOS is not a general orchestration platform.
- Release publication still requires human judgment.

## Release decision
Release decision:
- [ ] APPROVED
- [ ] NOT APPROVED
Reviewer:
Date:
Notes:

Do not mark APPROVED unless a human reviewer explicitly approves release.

## Non-goals
This checklist does not:
- run validation automatically
- approve release automatically
- execute tasks
- modify tasks/active-task.md
- move queue items
- create validators
- create runners
- replace human review
