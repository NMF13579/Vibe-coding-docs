#!/usr/bin/env python3
"""Unsafe agent-complete fixture."""
import shutil
def main():
    shutil.move("tasks/queue/task-a.md", "tasks/done/task-a.md")
if __name__ == "__main__":
    main()
