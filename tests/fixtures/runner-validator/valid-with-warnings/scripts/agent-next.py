#!/usr/bin/env python3
"""Runner fixture with unsafe pattern guarded by dry-run marker."""
from pathlib import Path
def main():
    # --dry-run supported
    # approved mode not implemented
    Path("tasks/active-task.md").write_text("example")
if __name__ == "__main__":
    main()
