#!/usr/bin/env python3
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

LLMS = ROOT / "llms.txt"
ROUTES = ROOT / "ROUTES-REGISTRY.md"
CANONICAL_MODULES = [
    "core-rules/MAIN.md",
    "state/MAIN.md",
    "workflow/MAIN.md",
    "quality/MAIN.md",
    "security/MAIN.md",
]
FORBIDDEN_ROUTE_TERMS = [
    "direct" + "-read",
    "trans" + "itional",
    "architecture/MAIN.md",
]


def fail(msg):
    print(f"FAIL {msg}")


def read(path):
    return path.read_text(encoding="utf-8")


def main():
    errors = 0
    llms_text = read(LLMS)
    routes_text = read(ROUTES)

    if "Canonical agent bootstrap order" not in llms_text:
        fail("llms.txt must declare canonical agent bootstrap order")
        errors += 1

    for module in CANONICAL_MODULES:
        if module not in llms_text:
            fail(f"llms.txt missing canonical module: {module}")
            errors += 1
        if module not in routes_text:
            fail(f"ROUTES-REGISTRY.md missing canonical module: {module}")
            errors += 1

    for term in FORBIDDEN_ROUTE_TERMS:
        if term in llms_text:
            fail(f"llms.txt contains non-canonical route term: {term}")
            errors += 1
        if term in routes_text:
            fail(f"ROUTES-REGISTRY.md contains non-canonical route term: {term}")
            errors += 1

    if "Current source" in routes_text:
        fail("ROUTES-REGISTRY.md must not contain Current source column")
        errors += 1

    if errors:
        print(f"\nFound {errors} route validation error(s).")
        return 1

    print("validate-route passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
