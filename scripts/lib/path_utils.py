from pathlib import Path


def resolve_task_dir(path) -> Path:
    """Always return task directory regardless of file or directory input."""
    p = Path(path)
    if p.is_file():
        return p.parent
    return p


def resolve_task_file(path) -> Path:
    """Always return path to TASK.md."""
    p = Path(path)
    if p.is_file() and p.name == "TASK.md":
        return p
    return p / "TASK.md"
