#!/usr/bin/env python3
"""Execution scope check MVP (file-level, read-only)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCOPE_PASS = 0
SCOPE_FAIL = 1
SCOPE_PARTIAL_OR_NOT_RUN = 2


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check changed files against source_contract scope.")
    parser.add_argument("--session", required=True, help="Execution session file path (repository-relative).")
    parser.add_argument(
        "--changed-files-from-git",
        action="store_true",
        help="Ignore session.changed_files and use git diff --name-only.",
    )
    return parser.parse_args(argv)


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    data: dict[str, object] = {}
    current_key: str | None = None
    idx = 1
    while idx < len(lines):
        line = lines[idx]
        if line.strip() == "---":
            return data, None

        if not line.strip() or line.strip().startswith("#"):
            idx += 1
            continue

        if line.startswith((" ", "\t")):
            stripped = line.strip()
            if current_key and stripped.startswith("- "):
                current_val = data.get(current_key)
                if not isinstance(current_val, list):
                    current_val = []
                    data[current_key] = current_val
                current_val.append(strip_quotes(stripped[2:].strip()))
            idx += 1
            continue

        if ":" not in line:
            return None, f"malformed frontmatter line: {line}"

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        current_key = key

        if value == "":
            data[key] = []
        elif value == "[]":
            data[key] = []
        else:
            data[key] = strip_quotes(value)
        idx += 1

    return None, "missing YAML frontmatter terminator"


def path_is_safe_rel(path_text: str) -> bool:
    if not path_text.strip():
        return False
    p = Path(path_text)
    if p.is_absolute():
        return False
    if ".." in p.parts:
        return False
    return True


def validate_repo_file_path(repo_root: Path, path_text: str) -> tuple[bool, Path | None, str | None]:
    if not path_is_safe_rel(path_text):
        return False, None, "invalid path: must be repository-relative and without parent traversal"
    p = repo_root / Path(path_text)
    if not p.exists():
        return False, None, "path does not exist"
    if not p.is_file():
        return False, None, "path is not a file"
    return True, p, None


def git_changed_files(repo_root: Path) -> tuple[list[str] | None, str | None]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return None, f"git diff failed to start: {exc}"
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        return None, f"git diff returned exit code {result.returncode}: {stderr or 'no stderr'}"
    files = [line.strip() for line in (result.stdout or "").splitlines() if line.strip()]
    return files, None


def parse_scope_from_markdown(text: str) -> tuple[list[str], list[str]]:
    in_scope: list[str] = []
    out_of_scope: list[str] = []
    mode: str | None = None

    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        if lower in {"## in scope", "### in scope"}:
            mode = "in"
            continue
        if lower in {"## out of scope", "### out of scope"}:
            mode = "out"
            continue
        if stripped.startswith("#"):
            mode = None
            continue
        if mode and stripped.startswith("- "):
            item = strip_quotes(stripped[2:].strip())
            if mode == "in":
                in_scope.append(item)
            else:
                out_of_scope.append(item)

    return in_scope, out_of_scope


def extract_scope(contract_text: str) -> tuple[list[str], list[str], list[str]]:
    warnings: list[str] = []
    fm, fm_err = parse_frontmatter(contract_text)
    in_scope: list[str] = []
    out_of_scope: list[str] = []

    if fm_err is None and fm is not None:
        in_val = fm.get("in_scope")
        out_val = fm.get("out_of_scope")
        if isinstance(in_val, list):
            in_scope.extend([str(x).strip() for x in in_val if str(x).strip()])
        elif isinstance(in_val, str) and in_val.strip():
            in_scope.append(in_val.strip())
        if isinstance(out_val, list):
            out_of_scope.extend([str(x).strip() for x in out_val if str(x).strip()])
        elif isinstance(out_val, str) and out_val.strip():
            out_of_scope.append(out_val.strip())
    else:
        warnings.append("source_contract frontmatter not parseable; using markdown heading fallback")

    if not in_scope and not out_of_scope:
        md_in, md_out = parse_scope_from_markdown(contract_text)
        in_scope = md_in
        out_of_scope = md_out

    return in_scope, out_of_scope, warnings


def normalize_scope_entry(entry: str) -> str:
    e = entry.strip()
    while e.startswith("./"):
        e = e[2:]
    if e.endswith("/"):
        e = e[:-1]
    return e


def scope_match(entry: str, changed_file: str) -> bool:
    e = normalize_scope_entry(entry)
    c = changed_file.strip().lstrip("./")
    if not e or not c:
        return False
    return c == e or c.startswith(e + "/")


def print_result(
    *,
    session: str,
    source_contract: str,
    changed_source: str,
    changed_files: list[str],
    in_scope: list[str],
    out_of_scope: list[str],
    violations: list[str],
    warnings: list[str],
    result: str,
) -> None:
    print("AgentOS Execution Scope Check")
    print("Session:")
    print(f"- {session}")
    print("Source contract:")
    print(f"- {source_contract}")
    print("Changed files source:")
    print(f"- {changed_source}")
    print("Changed files:")
    if changed_files:
        for f in changed_files:
            print(f"- {f}")
    else:
        print("- none")
    print("In scope:")
    if in_scope:
        for s in in_scope:
            print(f"- {s}")
    else:
        print("- none")
    print("Out of scope:")
    if out_of_scope:
        for s in out_of_scope:
            print(f"- {s}")
    else:
        print("- none")
    print("Violations:")
    if violations:
        for v in violations:
            print(f"- {v}")
    else:
        print("- none")
    print("Warnings:")
    if warnings:
        for w in warnings:
            print(f"- {w}")
    else:
        print("- none")
    print("Result:")
    print(f"- {result}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    ok, session_path, err = validate_repo_file_path(repo_root, args.session)
    if not ok or session_path is None:
        print_result(
            session=args.session,
            source_contract="unknown",
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"invalid session path: {err}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    try:
        session_text = session_path.read_text(encoding="utf-8")
    except OSError as exc:
        print_result(
            session=args.session,
            source_contract="unknown",
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"cannot read session file: {exc}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    session_fm, fm_err = parse_frontmatter(session_text)
    if fm_err or session_fm is None:
        print_result(
            session=args.session,
            source_contract="unknown",
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"unreadable session frontmatter: {fm_err}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    required = ["session_id", "task_id", "source_contract", "status", "readiness_result", "changed_files"]
    missing = [k for k in required if k not in session_fm]
    if missing:
        print_result(
            session=args.session,
            source_contract=str(session_fm.get("source_contract", "unknown")),
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"missing required session fields: {', '.join(missing)}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    status = str(session_fm.get("status", "")).strip().strip('"')
    source_contract_rel = str(session_fm.get("source_contract", "")).strip().strip('"')

    if status == "blocked":
        print_result(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            changed_source="not evaluated",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=["blocked session has no execution changes to scope-check"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    if status not in {"in_progress", "evidence_ready", "stopped"}:
        print_result(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"unsupported session status for scope check: {status or 'empty'}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    ok_sc, source_contract_path, sc_err = validate_repo_file_path(repo_root, source_contract_rel)
    if not ok_sc or source_contract_path is None:
        print_result(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"invalid or missing source_contract: {sc_err}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    try:
        contract_text = source_contract_path.read_text(encoding="utf-8")
    except OSError as exc:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source="unknown",
            changed_files=[],
            in_scope=[],
            out_of_scope=[],
            violations=[],
            warnings=[f"cannot read source_contract: {exc}"],
            result="NOT RUN",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    in_scope, out_of_scope, warnings = extract_scope(contract_text)

    session_changed_raw = session_fm.get("changed_files")
    session_changed: list[str] = []
    if isinstance(session_changed_raw, list):
        session_changed = [str(x).strip() for x in session_changed_raw if str(x).strip()]

    changed_source = "session.changed_files"
    changed_files: list[str] = []
    git_files: list[str] | None = None
    git_err: str | None = None

    if args.changed_files_from_git:
        changed_source = "git diff"
        git_files, git_err = git_changed_files(repo_root)
        if git_files is None:
            print_result(
                session=args.session,
                source_contract=source_contract_rel,
                changed_source=changed_source,
                changed_files=[],
                in_scope=in_scope,
                out_of_scope=out_of_scope,
                violations=[],
                warnings=warnings + [f"changed files unavailable: {git_err}"],
                result="NOT RUN",
            )
            return SCOPE_PARTIAL_OR_NOT_RUN
        changed_files = git_files
    else:
        if session_changed:
            changed_source = "session.changed_files"
            changed_files = session_changed
        else:
            changed_source = "git diff"
            git_files, git_err = git_changed_files(repo_root)
            if git_files is None:
                if status == "stopped":
                    print_result(
                        session=args.session,
                        source_contract=source_contract_rel,
                        changed_source=changed_source,
                        changed_files=[],
                        in_scope=in_scope,
                        out_of_scope=out_of_scope,
                        violations=[],
                        warnings=warnings + [
                            "status=stopped: scope check allowed, but changed files unavailable",
                            f"changed files unavailable: {git_err}",
                        ],
                        result="NOT RUN",
                    )
                    return SCOPE_PARTIAL_OR_NOT_RUN
                print_result(
                    session=args.session,
                    source_contract=source_contract_rel,
                    changed_source=changed_source,
                    changed_files=[],
                    in_scope=in_scope,
                    out_of_scope=out_of_scope,
                    violations=[],
                    warnings=warnings + [f"changed files unavailable: {git_err}"],
                    result="NOT RUN",
                )
                return SCOPE_PARTIAL_OR_NOT_RUN
            changed_files = git_files

    if not changed_files:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source=changed_source,
            changed_files=[],
            in_scope=in_scope,
            out_of_scope=out_of_scope,
            violations=[],
            warnings=warnings,
            result="PASS",
        )
        return SCOPE_PASS

    violations: list[str] = []
    for cf in changed_files:
        if not path_is_safe_rel(cf):
            violations.append(f"unsafe changed file path: {cf}")
    if violations:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source=changed_source,
            changed_files=changed_files,
            in_scope=in_scope,
            out_of_scope=out_of_scope,
            violations=violations,
            warnings=warnings,
            result="FAIL",
        )
        return SCOPE_FAIL

    for entry in in_scope + out_of_scope:
        if not path_is_safe_rel(entry):
            print_result(
                session=args.session,
                source_contract=source_contract_rel,
                changed_source=changed_source,
                changed_files=changed_files,
                in_scope=in_scope,
                out_of_scope=out_of_scope,
                violations=[],
                warnings=warnings + [f"unsafe scope entry in source_contract: {entry}"],
                result="PARTIAL",
            )
            return SCOPE_PARTIAL_OR_NOT_RUN

    out_violations: list[str] = []
    for cf in changed_files:
        for out in out_of_scope:
            if scope_match(out, cf):
                out_violations.append(f"out_of_scope violation: {cf} matches {out}")
                break
    if out_violations:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source=changed_source,
            changed_files=changed_files,
            in_scope=in_scope,
            out_of_scope=out_of_scope,
            violations=out_violations,
            warnings=warnings,
            result="FAIL",
        )
        return SCOPE_FAIL

    if in_scope:
        matched = [cf for cf in changed_files if any(scope_match(i, cf) for i in in_scope)]
        if len(matched) == len(changed_files):
            print_result(
                session=args.session,
                source_contract=source_contract_rel,
                changed_source=changed_source,
                changed_files=changed_files,
                in_scope=in_scope,
                out_of_scope=out_of_scope,
                violations=[],
                warnings=warnings,
                result="PASS",
            )
            return SCOPE_PASS

        unmatched = [cf for cf in changed_files if cf not in matched]
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source=changed_source,
            changed_files=changed_files,
            in_scope=in_scope,
            out_of_scope=out_of_scope,
            violations=[],
            warnings=warnings + [f"files outside known in_scope: {', '.join(unmatched)}"],
            result="PARTIAL",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    if out_of_scope:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            changed_source=changed_source,
            changed_files=changed_files,
            in_scope=in_scope,
            out_of_scope=out_of_scope,
            violations=[],
            warnings=warnings + ["in_scope missing; cannot confirm full scope coverage"],
            result="PARTIAL",
        )
        return SCOPE_PARTIAL_OR_NOT_RUN

    print_result(
        session=args.session,
        source_contract=source_contract_rel,
        changed_source=changed_source,
        changed_files=changed_files,
        in_scope=[],
        out_of_scope=[],
        violations=[],
        warnings=warnings + ["no scope fields found in source_contract"],
        result="PARTIAL",
    )
    return SCOPE_PARTIAL_OR_NOT_RUN


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
