# Milestone 22 Evidence Report

## Executive Summary
Milestone 22 moved AgentOS toward script-supported guardrails while keeping semantic Markdown as the source of truth. I inspected the M22 document families, validators, config files, schemas, fixtures, and the derived index. I collected validation evidence for the created guardrails and the current index artifacts. The evidence is usable, but it is not complete enough to call M22 finished here. This report does not decide approval, completion, release readiness, correctness, or safety.

## Artifact Inventory
| Artifact | Expected Purpose | Status | Notes |
|---|---|---|---|
| `reports/milestone-22-markdown-to-script-inventory.md` | Inventory of Markdown-to-script candidates | NOT_FOUND | Missing in this checkout |
| `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | Classify Markdown roles | FOUND | Present |
| `docs/SOURCE-OF-TRUTH-MAP.md` | Map concept ownership | FOUND | Present |
| `docs/FRONTMATTER-STANDARD.md` | Define frontmatter contract | FOUND | Present |
| `scripts/validate-frontmatter.py` | Validate frontmatter | FOUND | Present |
| `docs/STATUS-SEMANTICS.md` | Define status marker meaning | FOUND | Present |
| `scripts/validate-status-semantics.py` | Validate status semantics | FOUND | Present |
| `scripts/validate-required-sections.py` | Validate required headings | FOUND | Present |
| `data/required-sections.json` | Required heading profiles | FOUND | Present |
| `docs/BOUNDARY-CLAIMS.md` | Define unsafe boundary claims | FOUND | Present |
| `scripts/validate-boundary-claims.py` | Validate boundary claims | FOUND | Present |
| `docs/INDEX-SCHEMA.md` | Describe derived index shape | FOUND | Present |
| `schemas/index.schema.json` | JSON Schema for index | FOUND | Present |
| `scripts/build-index.py` | Build derived index | FOUND | Present |
| `data/index.json` | Derived navigation index | FOUND | Present |
| `scripts/validate-index.py` | Validate derived index | FOUND | Present |
| `scripts/audit-metadata-consistency.py` | Audit index consistency | FOUND | Present |
| `scripts/test-m22-guardrails.py` | Run M22 guardrail suites | FOUND | Present |

## Documents Created
| Document | Purpose | Key Evidence | Status |
|---|---|---|---|
| `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | Role model for Markdown families | Required headings present; role boundaries defined | FOUND |
| `docs/SOURCE-OF-TRUTH-MAP.md` | Ownership map for major concepts | Ownership statuses and boundaries recorded | FOUND |
| `docs/FRONTMATTER-STANDARD.md` | Frontmatter contract | Required fields, allowed values, and unknown handling defined | FOUND |
| `docs/STATUS-SEMANTICS.md` | Marker semantics | Allowed markers, forbidden claims, and human boundaries defined | FOUND |
| `docs/BOUNDARY-CLAIMS.md` | Unsafe phrasing boundaries | Forbidden and safe claims listed | FOUND |
| `docs/INDEX-SCHEMA.md` | Index boundaries and shape | Derived-navigation-only boundary stated | FOUND |

## Scripts Created
| Script | Purpose | Read-only Expected? | Fixture Coverage | Status |
|---|---|---|---|---|
| `scripts/validate-frontmatter.py` | Check required frontmatter fields and values | Yes | `tests/fixtures/frontmatter/` | FOUND |
| `scripts/validate-status-semantics.py` | Check allowed markers and unsafe claims | Yes | `tests/fixtures/status-semantics/` | FOUND |
| `scripts/validate-required-sections.py` | Check required headings by profile | Yes | `tests/fixtures/required-sections/` | FOUND |
| `scripts/validate-boundary-claims.py` | Detect forbidden boundary claims | Yes | `tests/fixtures/boundary-claims/` | FOUND |
| `scripts/build-index.py` | Build derived `data/index.json` | No, it writes the allowed index file | `tests/fixtures/index/` | FOUND |
| `scripts/validate-index.py` | Validate derived index structure | Yes | `tests/fixtures/index/` | FOUND |
| `scripts/audit-metadata-consistency.py` | Audit index/file consistency | Yes | `tests/fixtures/metadata-consistency/` | FOUND |
| `scripts/test-m22-guardrails.py` | Run M22 validator suites | Yes | All M22 fixture families | FOUND |

## Configs, Schemas, and Index Artifacts
| Artifact | Purpose | Derived? | Authority Boundary | Status |
|---|---|---|---|---|
| `data/required-sections.json` | Heading profiles for the required-sections validator | Yes | Configuration only; no decision authority | FOUND |
| `schemas/index.schema.json` | Schema for future derived index | Yes | Describes structure only | FOUND |
| `data/index.json` | Derived navigation only | Yes | Markdown remains source of truth; index must not store human decision authority | FOUND |

`data/index.json` is derived navigation only. Markdown remains source of truth. Configs and schemas must not encode human decisions as authority.

## Fixture Coverage
| Fixture Family | Expected Coverage | Status | Notes |
|---|---|---|---|
| `tests/fixtures/frontmatter/` | Valid and invalid frontmatter cases | FOUND | Complete for MVP checks |
| `tests/fixtures/status-semantics/` | Valid markers and invalid/unsafe marker cases | FOUND | Complete for MVP checks |
| `tests/fixtures/required-sections/` | Matching, missing, mismatched, and no-heading cases | FOUND | Complete for MVP checks |
| `tests/fixtures/boundary-claims/` | Safe wording and forbidden claims | FOUND | Complete for MVP checks |
| `tests/fixtures/index/` | Valid, invalid, and file-existence cases | FOUND | Complete for MVP checks |
| `tests/fixtures/metadata-consistency/` | Clean, warning, and failure cases | FOUND | Complete for MVP checks |

## Validation Evidence
| Command | Expected | Status | Output Summary | Notes |
|---|---|---|---|---|
| `python3 scripts/validate-frontmatter.py tests/fixtures/frontmatter/valid` | exit 0 | PASS | 1 file passed | Valid frontmatter fixture passed |
| `python3 scripts/validate-frontmatter.py tests/fixtures/frontmatter/invalid` | exit 1 | PASS | 2 files failed as expected | Invalid frontmatter fixtures failed as expected |
| `python3 scripts/validate-status-semantics.py tests/fixtures/status-semantics/valid` | exit 0 | PASS | 3 files passed | Valid marker fixtures passed |
| `python3 scripts/validate-status-semantics.py tests/fixtures/status-semantics/invalid` | exit 1 | PASS | 6 files failed as expected | Invalid marker and unsafe-claim fixtures failed as expected |
| `python3 scripts/validate-required-sections.py --profile frontmatter_standard tests/fixtures/required-sections/valid/frontmatter-standard.md` | exit 0 | PASS | Required headings present | Valid profile fixture passed |
| `python3 scripts/validate-boundary-claims.py tests/fixtures/boundary-claims/valid` | exit 0 | PASS | 3 files passed | Safe boundary-language fixtures passed |
| `python3 scripts/validate-boundary-claims.py tests/fixtures/boundary-claims/invalid` | exit 1 | PASS | 7 files failed as expected | Forbidden-claim fixtures failed as expected |
| `python3 -m json.tool schemas/index.schema.json` | exit 0 | PASS | JSON schema is valid JSON | Schema parse check passed |
| `python3 -m json.tool data/index.json` | exit 0 | PASS | Derived index is valid JSON | Current index parses correctly |
| `python3 scripts/validate-index.py tests/fixtures/index/valid/minimal-index.json --root tests/fixtures/index/files` | exit 0 | PASS | Minimal index passed | Valid index fixture passed |
| `python3 scripts/validate-index.py tests/fixtures/index/valid/index-with-unknowns.json --root tests/fixtures/index/files` | exit 0 | PASS | Unknowns warned but did not fail | Warning-only fixture passed |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/missing-top-level-field.json --root tests/fixtures/index/files` | exit 1 | PASS | Missing top-level field failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/missing-entry-field.json --root tests/fixtures/index/files` | exit 1 | PASS | Missing entry field failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/invalid-type.json --root tests/fixtures/index/files` | exit 1 | PASS | Invalid type failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/invalid-date.json --root tests/fixtures/index/files` | exit 1 | PASS | Invalid date failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/missing-path.json --root tests/fixtures/index/files` | exit 1 | PASS | Missing path failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/duplicate-path.json --root tests/fixtures/index/files` | exit 1 | PASS | Duplicate path failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py tests/fixtures/index/invalid/unsafe-authority-field.json --root tests/fixtures/index/files` | exit 1 | PASS | Unsafe authority field failed | Invalid index fixture failed as expected |
| `python3 scripts/validate-index.py` | exit 0/1 | FAIL | Real index reports many warnings and 141 failures | Existing source Markdown still contains invalid status values |
| `python3 scripts/audit-metadata-consistency.py` | exit 0/1/NOT_FOUND | WARN | Real index loads; warnings only, no failures | Many `unknown` fields and warnings fields remain |
| `python3 scripts/test-m22-guardrails.py` | exit 0 or 1 | PASS | All suites PASS | Unified M22 guardrail runner passed |
| `python3 -m json.tool data/index.json` | exit 0 | PASS | JSON parses correctly | Already covered above; included for completeness |
| `python3 scripts/build-index.py` | not required for this report | NOT_RUN | Not run to avoid rewriting `data/index.json` | Skipped because this task is evidence-only |
| `git status --short` | read-only observation | WARN | Unrelated `project/` changes remain; report file is untracked | Workspace contains pre-existing residue outside this report |

## Markdown-to-Script Progress
| Rule / Pattern | Script Support | Evidence | Remaining Gap |
|---|---|---|---|
| frontmatter required fields | `scripts/validate-frontmatter.py` | Frontmatter fixtures pass/fail as expected | Existing docs without frontmatter still produce warnings in the index |
| status markers | `scripts/validate-status-semantics.py` | Valid/invalid marker fixtures behave as expected | Real repository Markdown still contains many non-M22 status values |
| required sections | `scripts/validate-required-sections.py` | Profile-based heading checks pass | Some other document families are not yet mapped here |
| boundary claims | `scripts/validate-boundary-claims.py` | Forbidden claim fixtures fail as expected | Wording control remains manual for documents not in fixtures |
| index structure | `scripts/build-index.py` and `scripts/validate-index.py` | Derived index builds and validates as JSON | Real index still reflects legacy content issues |
| metadata consistency | `scripts/audit-metadata-consistency.py` | Audit runs and warns on unknown metadata | Legacy Markdown still has many unknown fields |
| negative fixture runner | `scripts/test-m22-guardrails.py` | All suites PASS | Missing upstream artifacts are not all present in this checkout |

## Semantic Markdown Preserved
| Area | Preserved As Markdown? | Reason | Script Boundary |
|---|---|---|---|
| architecture | Yes | Meaning and rationale live in prose | Scripts may check headings only |
| risk rationale | Yes | Human judgment remains necessary | Scripts must not auto-classify risk |
| approval rationale | Yes | Approval stays human-controlled | Boundary checks only |
| completion rationale | Yes | Completion is a decision, not data | Evidence only |
| release rationale | Yes | Release decisions remain human-controlled | Boundary checks only |
| limitations | Yes | Useful context for readers | Scriptable presence checks only |
| human decision boundaries | Yes | Protects the human role | Forbidden-claim checks only |
| lessons | Yes | Stores learning and context | Format checks only |

## Known Gaps and Warnings
| Gap / Warning | Impact | Recommended Follow-Up | Severity |
|---|---|---|---|
| `reports/milestone-22-markdown-to-script-inventory.md` is missing | One expected upstream artifact is absent | Recreate or locate the inventory report if needed for audit continuity | MEDIUM |
| `python3 scripts/validate-index.py` fails on the current repository index | Existing Markdown still has many invalid status values | Review legacy status values before treating the index as clean | HIGH |
| `python3 scripts/audit-metadata-consistency.py` reports many `unknown` fields and warnings fields | Derived index still carries a lot of uncertainty | Reduce legacy metadata gaps in source Markdown | MEDIUM |
| Workspace contains unrelated `project/` changes and untracked files | This report is not the only worktree residue | Leave unrelated files untouched | LOW |
| `python3 scripts/build-index.py` was not run during this report | Avoided rewriting `data/index.json` in an evidence-only task | Use it only when a rebuild is intentionally required | LOW |

## Do Not Treat as Completion Decision
This evidence report does not complete M22. This evidence report does not approve release. This evidence report does not prove correctness. This evidence report does not replace human review. Completion decision belongs to `22.15.1 — Milestone 22 Completion Review`.

## Recommended Next Task
`22.15.1 — Milestone 22 Completion Review`

Completion review should come after evidence collection because it needs the factual record first. Evidence shows what exists and what failed; completion review makes the final human decision using that record.

## Final Evidence Result
`READY_WITH_WARNINGS`

Major M22 artifacts are present and the guardrail runner passes, so the evidence is usable. The report still records one missing upstream inventory report and the real index validator still fails against legacy repository content, so completion review should proceed with caution. The next step is `22.15.1 — Milestone 22 Completion Review`.

