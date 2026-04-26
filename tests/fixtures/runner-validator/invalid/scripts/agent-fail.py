#!/usr/bin/env python3
"""Unsafe agent-fail fixture."""
import os
def main():
    os.rename("tasks/queue/task-a.md", "tasks/failed/task-a.md")
if __name__ == "__main__":
    main()
