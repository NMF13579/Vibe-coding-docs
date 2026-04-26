#!/usr/bin/env python3
"""Unsafe agent-next fixture."""
from pathlib import Path
def main():
    Path("tasks/active-task.md").write_text("replace without approval")
if __name__ == "__main__":
    main()
