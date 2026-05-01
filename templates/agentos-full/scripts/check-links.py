#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

RUNTIME_MODULES = [
    "core-rules/MAIN.md",
    "state/MAIN.md",
    "workflow/MAIN.md",
    "quality/MAIN.md",
    "security/MAIN.md",
]

SUPPORT_DOCS = [
    "llms.txt",
    "README.md",
    "START.md",
    "ROUTES-REGISTRY.md",
    "ARCHITECTURE.md",
    "architecture/CANON.md",
    "architecture/MAIN.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(msg):
    print(f"❌ {msg}")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def normalize(target: str) -> str:
    return target.split("#", 1)[0].split("?", 1)[0].strip()


def main():
    errors = 0
    for rel in RUNTIME_MODULES + SUPPORT_DOCS:
        path = ROOT / rel
        if not path.exists():
            fail(f"Target file for link-check is missing: {rel}")
            errors += 1
            continue

        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            t = normalize(raw)
            if not t or is_external(t):
                continue
            resolved = (path.parent / t).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{rel}: link escapes repository: {raw}")
                errors += 1
                continue
            if not resolved.exists():
                fail(f"{rel}: broken local link -> {raw}")
                errors += 1

    if errors:
        print(f"\nFound {errors} broken link issue(s).")
        return 1

    print("✅ check-links passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
