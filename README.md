# AgentOS

AgentOS is a Markdown-first guardrail framework for AI-assisted coding workflows.
It helps structure project context, task briefs, review gates, traces, contract drafts, queues, runner protocols, validation, negative tests, guard failure tests, and audit reports.

AgentOS is governed documentation framework for AI-assisted development.
The current architecture is canonical-module driven: agents and owners navigate through a small set of runtime modules instead of scattered rule files.

## What is AgentOS?

AgentOS is a **Markdown-first guardrail framework** designed for AI-assisted coding workflows. It provides a structured approach to managing project context, task briefs, validation, and execution boundaries.

**Important clarifications:**
- AgentOS is **not** an autonomous agent
- AgentOS is **not** a backend service  
- AgentOS is **not** a RAG platform
- AgentOS is **not** a general orchestration platform

## Core Principles

- **Markdown-first:** All configuration, contracts, and reports are human-readable Markdown files
- **Human-approved execution boundaries:** Execution requires explicit human approval at defined checkpoints
- **Explicit task contracts:** Task contracts are explicit and human-readable
- **Single executable contract:** `tasks/active-task.md` is the only executable task contract
- **Non-executable briefs:** Task Briefs (TASK.md) are not executable; they require validation and approval first
- **Automation follows validation:** Automation only proceeds after manual validation and human approval
- **Read-only checks by default:** Checkers and runners are read-only unless explicitly documented otherwise
- **No autonomous execution:** No part of AgentOS executes tasks without human checkpoints

## Current Capabilities

- Project initialization and discovery layer
- Spec wizard and task brief flow
- Task brief validation
- Review and trace artifacts
- Contract draft generation
- Queue lifecycle scaffolding
- Runner dry-run protocol
- Task health metrics
- **Template integrity checker** – validates required project structure
- **Negative fixture runner** – ensures invalid inputs are rejected
- **Guard failure runner** – aggregates guard and failure checks
- **Audit runner** – aggregates release-readiness validation

## Quick Start

Run validation checks in order:

```bash
# Strict template integrity check
python3 scripts/check-template-integrity.py --strict

# Template integrity self-tests (verify checker is working correctly)
python3 scripts/test-template-integrity.py

# Negative fixture tests (verify invalid inputs are rejected)
python3 scripts/test-negative-fixtures.py

# Guard failure runner (aggregate guard/failure checks)
python3 scripts/test-guard-failures.py

# Audit runner (release-readiness overview)
python3 scripts/audit-agentos.py
```

**For a complete release-readiness overview, run:**
```bash
python3 scripts/audit-agentos.py
```

See [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) for detailed getting started guide.

## Validation and Audit

AgentOS provides validation at multiple layers:

| Level | Tool | Purpose |
|---|---|---|
| **Template Integrity** | `scripts/check-template-integrity.py --strict` | Validates required project structure |
| **Integrity Tests** | `scripts/test-template-integrity.py` | Verifies the checker itself works correctly |
| **Negative Fixtures** | `scripts/test-negative-fixtures.py` | Ensures invalid inputs are rejected |
| **Guard Failures** | `scripts/test-guard-failures.py` | Aggregates guard and failure checks |
| **Audit** | `scripts/audit-agentos.py` | Release-readiness style aggregation |

For detailed information, see [docs/VALIDATION.md](docs/VALIDATION.md).

## Safety Boundaries

AgentOS enforces strict safety boundaries:

- **Does not execute tasks automatically**
- **Does not replace `tasks/active-task.md` without explicit human approval**
- **Does not move queue items autonomously**
- **Does not run runner protocol scripts unless explicitly invoked by user**
- **Does not approve execution**
- **Does not act as a release checklist** (yet)

For detailed information, see [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md).

## Repository Map

Key documentation files:

- [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) – Getting started guide and task flow
- [docs/VALIDATION.md](docs/VALIDATION.md) – Validation layers and command reference
- [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md) – Safety boundaries and execution rules
- [tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md](tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md) – Template integrity checker
- [tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md](tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md) – Negative fixture tests
- [tools/guard-failure/TEST-GUARD-FAILURES.md](tools/guard-failure/TEST-GUARD-FAILURES.md) – Guard failure runner
- [tools/audit/AUDIT-AGENTOS.md](tools/audit/AUDIT-AGENTOS.md) – Audit runner
- [repo-map.md](repo-map.md) – Complete repository structure

## Non-Goals

AgentOS does not aim to be:

- An autonomous coding agent
- A backend framework
- A RAG platform
- A general-purpose orchestration platform
- A replacement for human review
- A release checklist (in this milestone)

## Current Status

**Current milestone:** 7.4 Docs Hardening

**Previously completed:**
- Template Integrity – validates required project structure
- Negative Fixtures – ensures invalid inputs are rejected
- Guard Failure Runner – aggregates guard and failure checks
- Audit Runner – release-readiness validation

## Start Here

| Need | Read |
|---|---|
| Quick start with AgentOS | [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) |
| Validation commands | [docs/VALIDATION.md](docs/VALIDATION.md) |
| Safety boundaries | [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md) |
| Agent startup | `llms.txt` |
| Route overview | `ROUTES-REGISTRY.md` |
| Rule priority and authority | `core-rules/MAIN.md` |
| Current state, recovery, transitions | `state/MAIN.md` |
| Planning and execution flow | `workflow/MAIN.md` |
| Verification and release readiness | `quality/MAIN.md` |
| Sensitive data and access boundaries | `security/MAIN.md` |

## Canonical Runtime Modules

| Module | Owns |
|---|---|
| `core-rules/MAIN.md` | Priority, authority, governance, agent boundaries |
| `state/MAIN.md` | State lifecycle, events, recovery, transitions |
| `workflow/MAIN.md` | Plan gate, scope control, execution boundaries, one-task rule |
| `quality/MAIN.md` | Verification, smoke checks, release blockers, audit output |
| `security/MAIN.md` | Sensitive data, least privilege, compliance, security stop conditions |

## Common Situations

| Situation | Route |
|---|---|
| I need to continue work | `state/MAIN.md` |
| I need a plan before changes | `workflow/MAIN.md` |
| The task is expanding | `workflow/MAIN.md` |
| I need to know which instruction wins | `core-rules/MAIN.md` |
| I need proof that the task is done | `quality/MAIN.md` |
| I am preparing for merge or release | `quality/MAIN.md` and `security/MAIN.md` |
| The task touches personal data, auth, access, API, or database | `security/MAIN.md` |
| The agent is unsure what to read | `ROUTES-REGISTRY.md`, then ask the owner if no route fits |

## Working Rule

- Use `llms.txt` as the only agent startup path.
- Use `ROUTES-REGISTRY.md` only to confirm module ownership.
- Keep runtime behavior inside the five canonical modules.
- Do not treat archive, adapter, support, or notes files as runtime authority.
- If the current module does not answer the situation, stop and ask the owner instead of guessing.
## Example scenarios

Practical documentation scenarios are available in:

- `examples/README.md`
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`

These examples are not executable fixtures. They illustrate expected AgentOS workflows and safety boundaries.

## Prompt packs

Ready-to-use prompt packs are available in:

- `prompt-packs/README.md`
- `prompt-packs/cursor.md`
- `prompt-packs/claude-code.md`
- `prompt-packs/codex-cli.md`
- `prompt-packs/chatgpt.md`

Prompt packs help AI coding tools follow AgentOS safety boundaries, read the right context, and run the right validation commands.

## Release checklist

Release readiness checklist:

- `RELEASE-CHECKLIST.md`
- `tools/release/RELEASE-CHECKLIST.md`
- `reports/release-checklist.md`

Release approval is manual. AgentOS does not approve release automatically.
