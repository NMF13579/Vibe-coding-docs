# AgentOS Prompt Packs

## Purpose
Prompt packs provide ready-to-use instructions for AI coding tools working inside AgentOS repositories.
They help agents follow AgentOS boundaries, read the right context, run the right validation commands, and avoid unsafe automation.

## Available prompt packs
| Prompt pack | Tool |
|---|---|
| cursor.md | Cursor |
| claude-code.md | Claude Code |
| codex-cli.md | Codex / CLI agent |
| chatgpt.md | Generic ChatGPT |

## Core safety rule
AgentOS is not an autonomous agent.
The agent must not:
- execute Task Briefs directly
- replace tasks/active-task.md without explicit human approval
- move queue items without explicit human approval
- run runner protocol scripts unless explicitly requested
- mark completion without verification

## Recommended validation
For release-readiness overview:
    python3 scripts/audit-agentos.py
For full validation sequence:
    python3 scripts/check-template-integrity.py --strict
    python3 scripts/test-template-integrity.py
    python3 scripts/test-negative-fixtures.py
    python3 scripts/test-guard-failures.py
    python3 scripts/audit-agentos.py

## Related docs
- docs/GETTING-STARTED.md
- docs/VALIDATION.md
- docs/SAFETY-BOUNDARIES.md
- examples/README.md
