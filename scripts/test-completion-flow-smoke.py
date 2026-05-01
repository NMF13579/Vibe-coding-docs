#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

VERSION = "1.0.0"
PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"
SKIP = "SKIP"


@dataclass
class StepResult:
    name: str
    status: str
    detail: str = ""


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_protected_paths(root: Path, rel_paths: list[str]) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for rel in rel_paths:
        target = root / rel
        if target.is_file():
            snapshot[rel] = f"file:{file_hash(target)}"
            continue
        if target.is_dir():
            for p in sorted(target.rglob("*")):
                relp = p.relative_to(root).as_posix()
                if p.is_file():
                    snapshot[relp] = f"file:{file_hash(p)}"
                elif p.is_dir():
                    snapshot[relp] = "dir"
            continue
        snapshot[rel] = "missing"
    return snapshot


def assert_snapshots_equal(before: dict[str, str], after: dict[str, str]) -> tuple[bool, list[str]]:
    changed: list[str] = []
    keys = sorted(set(before.keys()) | set(after.keys()))
    for key in keys:
        if before.get(key) != after.get(key):
            changed.append(key)
    return (len(changed) == 0, changed)


def parse_result_token(stdout: str) -> str | None:
    for line in stdout.splitlines():
        line = line.strip()
        if line.startswith("result:"):
            return line.split(":", 1)[1].strip()
    return None


def parse_json(stdout: str) -> dict[str, object] | None:
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return None


def ensure_contains_task(path: Path, task_id: str) -> bool:
    if not path.is_file():
        return False
    return task_id in read_text(path)


def verify_temp_completed_state(workspace: Path, task_id: str) -> tuple[bool, str]:
    done_file = workspace / "tasks" / "done" / f"{task_id}.md"
    active_file = workspace / "tasks" / "active-task.md"
    if not done_file.is_file():
        return (False, f"completed file missing: {done_file}")
    if not active_file.is_file():
        return (False, "active-task.md missing after mutation")
    active_text = read_text(active_file)
    if "state: completed" not in active_text:
        return (False, "active-task.md does not contain state: completed")
    return (True, "")


def build_mutation_plan_from_json(plan_json: dict[str, object], plan_path: Path) -> None:
    task_id = str(plan_json.get("task_id") or "")
    result = str(plan_json.get("result") or "")
    completion_destination = str(plan_json.get("completion_destination") or "")
    completion_operation = str(plan_json.get("completion_operation") or "")
    allowed = plan_json.get("allowed_task_paths")
    allowed_paths: list[str] = []
    if isinstance(allowed, list):
        for item in allowed:
            if isinstance(item, str):
                allowed_paths.append(item)

    lines = [
        f"task_id: {task_id}",
        f"result: {result}",
        f"completion_destination: {completion_destination}",
        f"completion_operation: {completion_operation}",
        "allowed_task_paths:",
    ]
    for p in allowed_paths:
        lines.append(f"  - {p}")
    lines.append("would_mutate: true")
    write_text(plan_path, "\n".join(lines) + "\n")


def main() -> int:
    root = repo_root()
    fixture_root = root / "tests" / "fixtures" / "completion-flow-smoke"

    results: list[StepResult] = []
    flow_failed = False
    overall_warn = False

    print("Controlled Completion Flow Smoke")
    print(f"version: {VERSION}")
    print()

    if not fixture_root.is_dir():
        print("[FAIL] temp workspace prepared")
        print(f"  missing fixture root: {fixture_root}")
        print()
        print("Result: FAIL")
        return 1

    with tempfile.TemporaryDirectory(prefix="agentos-completion-smoke-") as tmp:
        workspace = Path(tmp)

        # 1. Prepare temp workspace
        try:
            (workspace / "scripts").mkdir(parents=True, exist_ok=True)
            (workspace / "tasks" / "done").mkdir(parents=True, exist_ok=True)
            (workspace / "reports" / "execution").mkdir(parents=True, exist_ok=True)

            shutil.copy2(root / "scripts" / "apply-transition.py", workspace / "scripts" / "apply-transition.py")
            shutil.copy2(root / "scripts" / "check-apply-preconditions.py", workspace / "scripts" / "check-apply-preconditions.py")

            shutil.copy2(fixture_root / "tasks-active-task.md", workspace / "tasks" / "active-task.md")
            shutil.copy2(fixture_root / "reports" / "execution" / "session-smoke.md", workspace / "reports" / "execution" / "session-smoke.md")
            shutil.copy2(fixture_root / "reports" / "execution-evidence-report.md", workspace / "reports" / "execution-evidence-report.md")
            shutil.copy2(fixture_root / "transition-smoke.md", workspace / "transition.md")

            results.append(StepResult("temp workspace prepared", PASS))
        except Exception as exc:  # noqa: BLE001
            results.append(StepResult("temp workspace prepared", FAIL, str(exc)))
            flow_failed = True

        protected = ["tasks/", "reports/", "docs/", "templates/"]
        before_snapshot: dict[str, str] = {}

        # 2. Snapshot before
        if not flow_failed:
            before_snapshot = snapshot_protected_paths(root, protected)
            results.append(StepResult("repository safety snapshot before execution", PASS))

        task_id = "task-smoke-001"
        transition = workspace / "transition.md"
        active_task = workspace / "tasks" / "active-task.md"
        apply_plan = workspace / "tmp" / "apply-plans" / "apply-plan.md"
        applied_record = workspace / "tmp" / "applied-transition" / "applied-transition-record.md"
        mutation_plan = workspace / "tmp" / "apply-plans" / "complete-active-mutation-plan.md"

        # 3. Verification evidence presence
        if not flow_failed:
            evidence = workspace / "reports" / "execution" / "session-smoke.md"
            if ensure_contains_task(evidence, task_id):
                results.append(StepResult("verification evidence present", PASS))
            else:
                results.append(StepResult("verification evidence present", FAIL, "missing file or task_id"))
                flow_failed = True
        else:
            results.append(StepResult("verification evidence present", SKIP))

        # 4. Completion readiness evidence presence
        if not flow_failed:
            readiness = workspace / "reports" / "execution-evidence-report.md"
            if ensure_contains_task(readiness, task_id):
                results.append(StepResult("completion readiness evidence present", PASS))
            else:
                results.append(StepResult("completion readiness evidence present", FAIL, "missing file or task_id"))
                flow_failed = True
        else:
            results.append(StepResult("completion readiness evidence present", SKIP))

        # 5. Prepared transition presence
        if not flow_failed:
            if transition.is_file() and ensure_contains_task(transition, task_id) and "target_state: completed" in read_text(transition):
                results.append(StepResult("prepared transition present", PASS))
            else:
                results.append(StepResult("prepared transition present", FAIL, "transition invalid"))
                flow_failed = True
        else:
            results.append(StepResult("prepared transition present", SKIP))

        # 6. Apply preconditions check
        if not flow_failed:
            pre = run_command([
                "python3", "scripts/check-apply-preconditions.py",
                "--transition", str(transition),
                "--active-task", str(active_task),
            ], cwd=workspace)
            token = parse_result_token(pre.stdout)
            if pre.returncode == 0 and token == "PASS":
                results.append(StepResult("apply preconditions PASS", PASS))
            else:
                detail = f"expected PASS, got rc={pre.returncode}, result={token or 'unknown'}"
                results.append(StepResult("apply preconditions PASS", FAIL, detail))
                flow_failed = True
        else:
            results.append(StepResult("apply preconditions PASS", SKIP))

        # 7. Dry-run
        if not flow_failed:
            before_active_hash = file_hash(active_task)
            dry = run_command([
                "python3", "scripts/apply-transition.py",
                "--transition", str(transition),
                "--dry-run",
            ], cwd=workspace)
            token = parse_result_token(dry.stdout)
            after_active_hash = file_hash(active_task)
            if dry.returncode == 0 and token == "DRY_RUN_PASS" and before_active_hash == after_active_hash:
                results.append(StepResult("apply dry-run", PASS))
            else:
                results.append(StepResult("apply dry-run", FAIL, f"rc={dry.returncode}, result={token or 'unknown'}"))
                flow_failed = True
        else:
            results.append(StepResult("apply dry-run", SKIP))

        # 8. Prepare apply plan
        if not flow_failed:
            prep = run_command([
                "python3", "scripts/apply-transition.py",
                "--transition", str(transition),
                "--prepare",
                "--plan-out", str(apply_plan),
            ], cwd=workspace)
            token = parse_result_token(prep.stdout)
            if prep.returncode == 0 and token == "APPLY_PLAN_PREPARED" and apply_plan.is_file() and ensure_contains_task(apply_plan, task_id):
                results.append(StepResult("apply plan prepared", PASS))
            else:
                results.append(StepResult("apply plan prepared", FAIL, f"rc={prep.returncode}, result={token or 'unknown'}"))
                flow_failed = True
        else:
            results.append(StepResult("apply plan prepared", SKIP))

        # 9. Create applied transition record
        if not flow_failed:
            before_active_hash = file_hash(active_task)
            apply_cmd = run_command([
                "python3", "scripts/apply-transition.py",
                "--transition", str(transition),
                "--plan", str(apply_plan),
                "--apply",
                "--applied-record-out", str(applied_record),
            ], cwd=workspace)
            token = parse_result_token(apply_cmd.stdout)
            after_active_hash = file_hash(active_task)
            ok_text = applied_record.is_file() and ensure_contains_task(applied_record, task_id)
            if apply_cmd.returncode == 0 and token == "APPLY_EVIDENCE_CREATED" and ok_text and before_active_hash == after_active_hash:
                results.append(StepResult("applied transition record created", PASS))
            else:
                results.append(StepResult("applied transition record created", FAIL, f"rc={apply_cmd.returncode}, result={token or 'unknown'}"))
                flow_failed = True
        else:
            results.append(StepResult("applied transition record created", SKIP))

        # 10. Prepare mutation plan
        if not flow_failed:
            complete_plan = run_command([
                "python3", "scripts/apply-transition.py",
                "--transition", str(transition),
                "--plan", str(apply_plan),
                "--applied-record", str(applied_record),
                "--complete-active-plan",
                "--json",
            ], cwd=workspace)
            payload = parse_json(complete_plan.stdout)
            if complete_plan.returncode == 0 and isinstance(payload, dict) and payload.get("result") == "COMPLETE_ACTIVE_PLAN_READY":
                build_mutation_plan_from_json(payload, mutation_plan)
                if mutation_plan.is_file():
                    results.append(StepResult("complete-active mutation plan prepared", PASS))
                else:
                    results.append(StepResult("complete-active mutation plan prepared", FAIL, "mutation plan artifact not written"))
                    flow_failed = True
            else:
                results.append(StepResult("complete-active mutation plan prepared", FAIL, f"rc={complete_plan.returncode}"))
                flow_failed = True
        else:
            results.append(StepResult("complete-active mutation plan prepared", SKIP))

        # 11. Controlled complete-active mutation
        if not flow_failed:
            mutate = run_command([
                "python3", "scripts/apply-transition.py",
                "--transition", str(transition),
                "--plan", str(apply_plan),
                "--applied-record", str(applied_record),
                "--mutation-plan", str(mutation_plan),
                "--complete-active",
            ], cwd=workspace)
            token = parse_result_token(mutate.stdout)
            if mutate.returncode == 0 and token == "COMPLETE_ACTIVE_APPLIED":
                results.append(StepResult("controlled complete-active mutation", PASS))
                ok_state, err = verify_temp_completed_state(workspace, task_id)
                if ok_state:
                    results.append(StepResult("temp workspace completed task verified", PASS))
                else:
                    results.append(StepResult("temp workspace completed task verified", FAIL, err))
                    flow_failed = True
            else:
                results.append(StepResult("controlled complete-active mutation", FAIL, f"rc={mutate.returncode}, result={token or 'unknown'}"))
                results.append(StepResult("temp workspace completed task verified", SKIP))
                flow_failed = True
        else:
            results.append(StepResult("controlled complete-active mutation", SKIP))
            results.append(StepResult("temp workspace completed task verified", SKIP))

        # 12. Validator and audit on real repo
        validator_path = root / "scripts" / "validate-lifecycle-apply.py"
        if validator_path.is_file() and not flow_failed:
            val = run_command(["python3", str(validator_path)], cwd=root)
            if val.returncode == 0:
                results.append(StepResult("lifecycle validator", PASS))
            else:
                results.append(StepResult("lifecycle validator", FAIL, "validator returned FAIL"))
                flow_failed = True
        elif validator_path.is_file() and flow_failed:
            results.append(StepResult("lifecycle validator", SKIP))
        else:
            results.append(StepResult("lifecycle validator", SKIP, "validator unavailable"))

        audit_path = root / "scripts" / "audit-lifecycle-mutation.py"
        if audit_path.is_file() and not flow_failed:
            aud = run_command(["python3", str(audit_path)], cwd=root)
            token = parse_result_token(aud.stdout)
            if aud.returncode != 0:
                results.append(StepResult("lifecycle audit", FAIL, "audit returned FAIL"))
                flow_failed = True
            elif token == "WARN":
                results.append(StepResult("lifecycle audit", WARN, "audit returned WARN"))
                overall_warn = True
            else:
                results.append(StepResult("lifecycle audit", PASS))
        elif audit_path.is_file() and flow_failed:
            results.append(StepResult("lifecycle audit", SKIP))
        else:
            results.append(StepResult("lifecycle audit", SKIP, "audit unavailable"))

        # 13. Snapshot after + safety compare
        after_snapshot = snapshot_protected_paths(root, protected)
        same, changed = assert_snapshots_equal(before_snapshot, after_snapshot)
        if same:
            results.append(StepResult("repository safety check", PASS))
        else:
            flow_failed = True
            results.append(StepResult("repository safety check", FAIL, "changed: " + ", ".join(changed)))

    for r in results:
        print(f"[{r.status}] {r.name}")
        if r.detail:
            print(f"  {r.detail}")

    print()
    if flow_failed:
        print("Result: FAIL")
        return 1
    if overall_warn:
        print("Result: WARN")
        return 0
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
