from datetime import datetime


def timestamp():
    """Current timestamp."""

    return datetime.now().isoformat(timespec="seconds")