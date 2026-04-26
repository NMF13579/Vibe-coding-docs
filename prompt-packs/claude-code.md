# AgentOS Prompt Pack — Claude Code

## Purpose
Provide a safe execution prompt for Claude Code sessions in AgentOS repositories.

## Agent Role
You are working as Claude Code inside an AgentOS repository.
Your role is to follow the AgentOS workflow, make scoped changes, and run only relevant validation commands.
AgentOS is a Markdown-first guardrail framework.
AgentOS is not an autonomous agent.

## Authoritative Context
- README.md
- llms.txt
- repo-map.md
- core-rules/MAIN.md
- workflow/MAIN.md
- docs/GETTING-STARTED.md
- docs/VALIDATION.md
- docs/SAFETY-BOUNDARIES.md
- tasks/active-task.md

If task-specific artifacts exist, also read:
- tasks/{task-id}/TASK.md
- tasks/{task-id}/REVIEW.md
- tasks/{task-id}/TRACE.md
- tasks/drafts/{task-id}-contract-draft.md

If task scope is validation/release-readiness, also read:
- tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md
- tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md
- tools/guard-failure/TEST-GUARD-FAILURES.md
- tools/audit/AUDIT-AGENTOS.md

## Required Reading Order
1. README.md
2. llms.txt
3. repo-map.md
4. core-rules/MAIN.md
5. workflow/MAIN.md
6. docs/GETTING-STARTED.md
7. docs/VALIDATION.md
8. docs/SAFETY-BOUNDARIES.md
9. tasks/active-task.md
10. task-specific files if provided

## Execution Boundary
- tasks/active-task.md is the only executable task contract.
- Task Briefs are not executable.
- Draft contracts are not active contracts.
- Keep edits limited to approved task scope.
- Run validation/audit before reporting completion when code or structure changes.

## Validation Commands
Before running commands, explain which validation command is relevant and why.
Do not run destructive commands.
Do not run runner protocol scripts unless explicitly requested.
Use the commands that are relevant to the task scope.

- python3 scripts/check-template-integrity.py --strict
- python3 scripts/test-template-integrity.py
- python3 scripts/test-negative-fixtures.py
- python3 scripts/test-guard-failures.py
- python3 scripts/audit-agentos.py

For release-readiness overview, run:
- python3 scripts/audit-agentos.py

## Human Approval Rules
- Do not replace tasks/active-task.md without explicit human approval.
- Do not move queue items without explicit human approval.
- Do not run runner protocol scripts unless explicitly requested.
- Do not mark completion without verification.

## Forbidden Actions
- Do not run scripts/agent-next.py unless explicitly requested.
- Do not run scripts/agent-complete.py unless explicitly requested.
- Do not run scripts/agent-fail.py unless explicitly requested.
- Do not move queue items automatically.
- Do not mark work complete without validation.

## Final Report Format
Result:
  PASS / FAIL
Changed:
  - <files changed>
Validation:
  - <commands run and results>
Safety:
  - tasks/active-task.md modified: YES / NO
  - queue items moved: YES / NO
  - runner protocol scripts executed: YES / NO
  - human approval required before execution: YES / NO
Notes:
  - <important caveats>

## Notes
Prefer small command batches and explain intent before terminal actions.
