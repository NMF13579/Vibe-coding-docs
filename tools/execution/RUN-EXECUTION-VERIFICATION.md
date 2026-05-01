# Run Execution Verification

## Purpose

`scripts/run-execution-verification.py` runs verification commands from `source_contract` and reports evidence.
It does not prove completion.
It does not move queue state.
It does not change session status in M13.7.1.

## Command

```bash
python3 scripts/run-execution-verification.py --session reports/execution/<session-id>.md
python3 scripts/run-execution-verification.py --session reports/execution/<session-id>.md --dry-run
```

## Dry Run

Dry run parses session and source contract, extracts verification plan, and prints commands that would run.
Dry run does not execute commands and does not modify files.
Dry run always returns `NOT RUN` by design, because commands were not executed.

## Session Preconditions

Required session fields:

- `session_id`
- `task_id`
- `source_contract`
- `status`
- `readiness_result`
- `changed_files`
- `verification_evidence`

Session status rules:

- allowed: `in_progress`, `evidence_ready`
- `blocked` -> `NOT RUN`
- `stopped` -> `NOT RUN` (requires separate review before verification)

## Verification Plan Source

Verification plan is extracted from `source_contract`:

1. frontmatter `verification_plan` list
2. markdown fallback sections:
   - `## Verification Plan`
   - `## Verification`

If verification_plan is missing, result is `NOT RUN`.

## Command Safety

Safety checks per command:

1. parse with `shlex.split`
2. allow only executables: `python3`, `python`, `bash`, `git`
3. reject absolute/traversal executable paths
4. reject shell operators (`|`, `&&`, `||`, `;`, `>`, `>>`, `<`, `` ` ``, `$(`)
5. validate path-like arguments (no absolute path, no parent traversal)
6. detect lifecycle mutation commands and reject as unsupported

Any failed safety check is command-level `PARTIAL` and command is not run.

## Git Command Safety

`git` is allowed only with read-only subcommands:

- `diff`
- `status`
- `log`
- `show`
- `ls-files`

Missing or unsupported git subcommand is command-level `PARTIAL`.
Mutating git commands are not run in this MVP.

## Command Timeout

Each command runs with `timeout=30` seconds.
If timeout is exceeded, command status is `PARTIAL` with timeout reason.
Runner continues with next command and does not hang indefinitely.

## Verification Command Side Effects

Runner is read-only with respect to AgentOS lifecycle state.
Verification commands may produce normal project-level artifacts (for example caches), but runner must not intentionally perform lifecycle mutation.
Lifecycle mutation commands are treated as unsupported (`PARTIAL`) when detectable.

## Command Results

Per-command mapping:

- exit code `0` -> command `PASS`
- non-zero exit code -> command `FAIL`
- parse/safety/timeout/start errors -> command `PARTIAL`

Evidence includes:

- command
- status
- exit_code
- ran_at
- short stdout summary
- short stderr summary

## Result Statuses

- `PASS`: all commands ran and all returned exit code `0`
- `FAIL`: at least one command ran and returned non-zero exit code
- `PARTIAL`: plan exists but some commands were not runnable / timed out / unsupported / incomplete evidence
- `NOT RUN`: session/contract/plan not executable context, or dry-run mode, or no commands ran

`PASS` is impossible without actual command execution.
`PARTIAL` and `NOT RUN` are not success.

## Exit Codes

- `0` = `VERIFICATION_PASS`
- `1` = `VERIFICATION_FAIL`
- `2` = `VERIFICATION_PARTIAL_OR_NOT_RUN`

Mapping:

- `PASS` -> `0`
- `FAIL` -> `1`
- `PARTIAL` -> `2`
- `NOT RUN` -> `2`

## Safety Boundaries

Runner must not modify:

- `tasks/active-task.md`
- execution session file
- `source_contract`
- `source_task`
- `reports/execution/.gitkeep`
- queue files
- `approvals/`

Runner must not create:

- `reports/execution-evidence-report.md`

Runner must not execute:

- task implementation protocol
- completion protocol
- rollback protocol
- approval generation
- queue transition

## Limitations

MVP supports only simple shell-free command format parsed by `shlex.split`.
It does not update `verification_evidence` in session file.
It does not set `evidence_ready`.
It does not make completion decisions.

## Future Work

- automatic writing of verification evidence into session files
- tighter command allowlist per task domain
- integration with completion review tooling
- fixture-based negative tests for verification runner behavior
