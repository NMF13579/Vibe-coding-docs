# AgentOS Validation

Validation in AgentOS happens at multiple layers. Each layer checks different aspects of project readiness.

## Validation Layers

| Layer | Purpose | Tool | Status |
|---|---|---|---|
| **Template Integrity** | Validates required project structure | `scripts/check-template-integrity.py --strict` | ✓ Current |
| **Template Tests** | Verifies the checker works correctly | `scripts/test-template-integrity.py` | ✓ Current |
| **Negative Fixtures** | Ensures invalid inputs are rejected | `scripts/test-negative-fixtures.py` | ✓ Current |
| **Guard Failures** | Aggregates guard/failure checks | `scripts/test-guard-failures.py` | ✓ Current |
| **Audit** | Release-readiness overview | `scripts/audit-agentos.py` | ✓ Current |
| **Release Checklist** | Final release approval | Not yet implemented | 🔜 Future |

## Template Integrity

**Purpose:** Validates that the project has all required files and structure.

**Command:**
```bash
python3 scripts/check-template-integrity.py --strict
```

**Expected result:** `exit 0`

**What it checks:**
- Required core files exist (README.md, repo-map.md, etc.)
- Required directories exist (tasks/, docs/, etc.)
- Forbidden files do not exist (auto-runners that should not be present)
- .gitignore rules are in place

**Documentation:** See [tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md](../tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md)

## Template Integrity Self-Tests

**Purpose:** Verifies that the template integrity checker itself works correctly.

**Command:**
```bash
python3 scripts/test-template-integrity.py
```

**Expected result:** `exit 0`

**What it does:**
- Runs the checker against a set of test fixtures
- Verifies the checker correctly identifies valid and invalid projects
- Tests both positive (should pass) and negative (should fail) cases

**Documentation:** See [tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md](../tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md)

## Negative Fixtures

**Purpose:** Ensures that invalid inputs are correctly rejected by validation tools.

**Command:**
```bash
python3 scripts/test-negative-fixtures.py
```

**Expected result:** `exit 0`

**What it does:**
- Tests invalid/malformed payloads
- Verifies that bad inputs are rejected as expected
- Ensures validators don't pass when they shouldn't

**Interpreting negative fixture results:**
- `PASS` means the invalid input was **correctly rejected** (this is the desired outcome)
- `FAIL` means an invalid input was not properly rejected (this is a problem)

**Documentation:** See [tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md](../tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md)

## Guard Failure Runner

**Purpose:** Aggregates guard and failure checks into one command.

**Command:**
```bash
python3 scripts/test-guard-failures.py
```

**Expected result:** `exit 0`

**What it does:**
- Runs template integrity tests
- Runs negative fixture tests
- Combines results into a unified report

**Runnable suites:**
- template-integrity: validates checker fixtures
- negative-fixtures: validates invalid inputs are rejected

**Documentation:** See [tools/guard-failure/TEST-GUARD-FAILURES.md](../tools/guard-failure/TEST-GUARD-FAILURES.md)

## Audit Runner

**Purpose:** Provides a release-readiness style aggregation of all validation checks.

**Command:**
```bash
python3 scripts/audit-agentos.py
```

**Expected result:** `exit 0` with `Result: PASS`

**What it does:**
- Runs template integrity strict check
- Runs template integrity self-tests
- Runs negative fixture tests
- Runs guard failure runner
- Produces a comprehensive audit report

**Audit report location:** `reports/audit.md`

**Documentation:** See [tools/audit/AUDIT-AGENTOS.md](../tools/audit/AUDIT-AGENTOS.md)

## Expected Command Order

Run validation commands in this sequence for best results:

```bash
# 1. Strict template check (validates required structure)
python3 scripts/check-template-integrity.py --strict

# 2. Template self-tests (verify checker is working)
python3 scripts/test-template-integrity.py

# 3. Negative fixtures (verify invalid inputs rejected)
python3 scripts/test-negative-fixtures.py

# 4. Guard failures (aggregate all above)
python3 scripts/test-guard-failures.py

# 5. Audit (release-readiness overview)
python3 scripts/audit-agentos.py
```

Or, for a quick overview, run just:
```bash
python3 scripts/audit-agentos.py
```

This will run all checks and produce `reports/audit.md`.

## Interpreting Results

### PASS

`PASS` means the check behaved as expected:

- **For positive checks (like template-integrity):** Required structure was found, no issues detected
- **For negative checks (like negative-fixtures):** Invalid input was correctly rejected
- **For runners:** All runnable suites passed

Exit code: `0`

### FAIL

`FAIL` means at least one required check failed or a prerequisite was missing:

- Required file or structure not found
- Invalid input was not properly rejected
- Prerequisite for a runner was not satisfied

Exit code: `1`

### SKIPPED

`SKIPPED` means the suite is intentionally not automated yet (deferred to future milestone):

- Release checklist (future milestone)
- Full docs hardening (future milestone)
- Example scenarios (future milestone)
- Prompt packs (future milestone)

`SKIPPED` suites do **not** affect the pass/fail result.

## Interpreting Negative Fixtures

**Important:** For negative fixture tests, the semantics are inverted:

- `PASS` = **invalid input was correctly rejected** (desired outcome)
- `FAIL` = **invalid input was NOT rejected** (unexpected, indicates problem)

This is different from positive tests where PASS means "good data was accepted."

## Running All Validation

To validate the entire project at once:

```bash
python3 scripts/audit-agentos.py
```

This produces:
- Console output showing each suite result
- Markdown report at `reports/audit.md`

Exit code is `0` if all suites pass, `1` if any fail.

## Validation Reports

Each validation tool generates reports:

| Tool | Report |
|---|---|
| Audit runner | `reports/audit.md` |
| Guard failure runner | `reports/guard-failures-smoke.md` |
| Template integrity | Part of audit and guard-failure reports |
| Negative fixtures | Part of audit and guard-failure reports |

For detailed reports after running validation, see the generated files in `reports/`.

## Next Steps

- **To understand safety boundaries**, see [SAFETY-BOUNDARIES.md](SAFETY-BOUNDARIES.md)
- **For getting started guide**, see [GETTING-STARTED.md](GETTING-STARTED.md)
- **For project overview**, see [../README.md](../README.md)
