#!/usr/bin/env python3
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

LLMS = ROOT / "llms.txt"
START = ROOT / "START.md"
ROUTES = ROOT / "ROUTES-REGISTRY.md"
ADAPTERS = [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "GEMINI.md"]
DEPRECATED_PRIMARY = ["LAYER-1/workflow.md", "LAYER-1/security.md", "LAYER-1/testing-guide.md"]
CORE_MAINS = ["core-rules/MAIN.md", "state/MAIN.md", "architecture/MAIN.md", "workflow/MAIN.md"]


def fail(msg):
    print(f"❌ {msg}")


def must_contain(path: pathlib.Path, needle: str):
    text = path.read_text(encoding="utf-8")
    return needle in text


def main():
    errors = 0

    if not must_contain(LLMS, "canonical agent bootstrap order"):
        fail("llms.txt no longer states canonical agent bootstrap role")
        errors += 1

    if not must_contain(LLMS, "ROUTES-REGISTRY.md"):
        fail("llms.txt must include ROUTES-REGISTRY.md in bootstrap route")
        errors += 1

    for core in CORE_MAINS:
        if not must_contain(LLMS, core):
            fail(f"llms.txt missing core route entry: {core}")
            errors += 1

    if not must_contain(START, "Primary human route"):
        fail("START.md must declare primary human route")
        errors += 1

    if not must_contain(START, "ROUTES-REGISTRY.md"):
        fail("START.md must route humans through ROUTES-REGISTRY.md")
        errors += 1

    routes_lines = ROUTES.read_text(encoding="utf-8").splitlines()
    if len(routes_lines) > 150:
        fail(f"ROUTES-REGISTRY.md exceeds 150 lines ({len(routes_lines)})")
        errors += 1

    for adoc in ADAPTERS:
        text = adoc.read_text(encoding="utf-8")
        if "Read `llms.txt` first" not in text:
            fail(f"{adoc.name} must point to llms.txt first")
            errors += 1
        if "ROUTES-REGISTRY.md" not in text:
            fail(f"{adoc.name} must reference ROUTES-REGISTRY.md")
            errors += 1

    llms_text = LLMS.read_text(encoding="utf-8")
    start_text = START.read_text(encoding="utf-8")
    for deprecated in DEPRECATED_PRIMARY:
        md_link = f"]({deprecated})"
        if md_link in llms_text or md_link in start_text:
            fail(f"Primary route links to deprecated legacy doc: {deprecated}")
            errors += 1

    if errors:
        print(f"\nFound {errors} route validation error(s).")
        return 1

    print("✅ validate-route passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
