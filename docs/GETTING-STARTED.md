# Getting Started with AgentOS

## What AgentOS Is

AgentOS is a **Markdown-first guardrail framework** for AI-assisted coding workflows. It provides structured validation, task management, and safety boundaries to ensure human oversight in automated workflows.

**Key points:**
- AgentOS is **not** an autonomous agent
- All configuration is human-readable Markdown
- Execution requires explicit human approval
- `tasks/active-task.md` is the only executable task contract

## Recommended First Commands

Start with template validation and then audit:

```bash
# Strict template integrity check (validates required structure)
python3 scripts/check-template-integrity.py --strict

# Audit runner (release-readiness overview)
python3 scripts/audit-agentos.py
```

Both commands should return `Result: PASS` if everything is ready.

## Understanding the Task Flow

AgentOS structures task management through several stages:

1. **Initialization** (`/init`)
   - Creates `project/PROJECT.md`

2. **Specification** (`/spec`)
   - Creates task brief at `tasks/{task-id}/TASK.md`
   - Task Brief is **not executable** yet

3. **Validation** (`validate-task-brief.py`)
   - Validates task brief structure and content

4. **Review & Trace** 
   - Creates `REVIEW.md` (review artifacts)
   - Creates `TRACE.md` (execution trace)

5. **Contract Generation** (`generate-task-contract.py`)
   - Generates draft contract at `tasks/drafts/{task-id}-contract-draft.md`
   - Draft contract is **not the active contract** yet

6. **Human Approval**
   - Human reviews draft contract
   - Human explicitly approves or requests changes

7. **Activation**
   - Approved draft is promoted to `tasks/active-task.md`
   - **Only `tasks/active-task.md` is executable**

## Key Boundaries

**Tasks are not executable until approved:**
- Task Briefs (TASK.md) are descriptive documents, not executable
- Draft contracts (tasks/drafts/) are proposals, not active
- Only `tasks/active-task.md` is the active executable contract

**Human approval is required:**
- Before replacing `tasks/active-task.md`
- Before marking task completion
- Before autonomous execution (not yet implemented in this milestone)

## Understanding Validation

Validation happens at multiple layers. Run commands in this order:

1. **Template Integrity** – validates project structure exists
   ```bash
   python3 scripts/check-template-integrity.py --strict
   ```

2. **Template Tests** – verify the checker itself works
   ```bash
   python3 scripts/test-template-integrity.py
   ```

3. **Negative Fixtures** – ensure invalid inputs are rejected
   ```bash
   python3 scripts/test-negative-fixtures.py
   ```

4. **Guard Failures** – aggregate guard and failure checks
   ```bash
   python3 scripts/test-guard-failures.py
   ```

5. **Audit** – overall release-readiness
   ```bash
   python3 scripts/audit-agentos.py
   ```

For detailed information about each validation layer, see [VALIDATION.md](VALIDATION.md).

## Human Approval Boundaries

AgentOS enforces these safety boundaries:

| Boundary | What it protects |
|---|---|
| **Task execution boundary** | Only `tasks/active-task.md` is executable; TASK.md is not |
| **Contract boundary** | Draft contracts require human review before activation |
| **Queue boundary** | Queue items are not moved autonomously by validation tools |
| **Approval checkpoint** | Human must approve before replacing active task |
| **Runner boundary** | Runner protocol remains dry-run; no autonomous execution yet |

## Where to Go Next

**To run validation:**
- See [VALIDATION.md](VALIDATION.md) for complete validation reference

**To understand safety:**
- See [SAFETY-BOUNDARIES.md](SAFETY-BOUNDARIES.md) for detailed boundaries

**To understand the framework:**
- Read `llms.txt` for agent bootstrap order
- Read `workflow/MAIN.md` for execution flow
- Read `quality/MAIN.md` for verification strategy

**To check project status:**
- Run `python3 scripts/check-template-integrity.py --strict`
- Run `python3 scripts/audit-agentos.py`
