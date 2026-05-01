# AgentOS Validate CLI Hardening Report

## Date

2026-04-28

## Branch

dev

## Commands Tested

- `python3 scripts/agentos-validate.py unknown`
- `python3 scripts/agentos-validate.py`
- `python3 scripts/agentos-validate.py all --bad-flag`
- `python3 scripts/agentos-validate.py --help`
- `python3 scripts/agentos-validate.py unknown --json`
- `python3 scripts/agentos-validate.py all --bad-flag --json`
- `python3 scripts/agentos-validate.py all --json`

## Results

PASS_WITH_LIMITATIONS

## Unknown Command

Exit code: `2`

Behavior:

- clear argparse error message shown
- no Python traceback
- validators were not executed

## Missing Command Argument

Exit code: `2`

Behavior:

- usage output shown
- clear missing-command error shown
- no Python traceback
- validators were not executed

## Invalid Flag

Exit code: `2`

Behavior:

- clear argparse-style error shown
- no Python traceback
- validators were not executed

## Help Output

Exit code: `0`

Behavior:

- available commands are listed
- `--json` is documented
- no validators are executed

## JSON Failure Behavior

Exit code: `1`

Behavior:

- `python3 scripts/agentos-validate.py all --json` produced valid JSON on stdout
- top-level result was `FAIL`
- top-level exit code was non-zero
- failed suites were marked `FAIL`

## Missing Mapped Script Behavior

Not safely simulated in this run.

The wrapper code path is documented and returns `FAIL` with an `error` field when a mapped script is missing.

## Stdout/Stderr Discipline

- Text mode prints human-readable suite lines.
- Parser errors are human-readable stderr errors.
- JSON mode keeps stdout as JSON only for executed validation commands.
- Unexpected runtime errors may appear on stderr.

## Documentation Updates

`tools/validation/AGENTOS-VALIDATE.md` now documents usage, JSON mode, parser-level behavior, missing command handling, and safety boundaries.

## Known Limitations

- Parser-level argparse errors remain human-readable rather than JSON.
- Missing mapped script behavior was documented but not forced by mutating real files.
- JSON suite failure behavior was verified with existing failing suites rather than by forcing new failures.
- This milestone does not add new validation logic.

## Safety Confirmation

agentos-validate.py was used only as a validation wrapper.

No task files were intentionally modified.
No queue entries were moved.
No approval markers were created.
No state transitions were executed.
No release approval was granted.
No active-task.md replacement was performed.
No validator scripts were renamed, deleted, moved, or corrupted to force failures.
No audit policy was changed.
WARN_THRESHOLD was not re-implemented.
Warning counts were not recalculated by the wrapper.
