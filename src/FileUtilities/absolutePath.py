from pathlib import Path


def absolutePath(filepath):
    relative = Path(filepath)
    return relative.absolute()
