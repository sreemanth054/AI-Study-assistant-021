"""Functions for managing study-session history.

The functions in this file are intentionally incomplete. Complete the TODOs
during the appropriate assignment milestones.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_history(history_file: str) -> list[dict[str, Any]]:
    """Return all saved study sessions."""
    path = Path(history_file)
    if not path.exists():
        return []

    with open(path, "r") as f:
        return json.load(f)


def save_session(history_file: str, session: dict[str, Any]) -> None:
    """Append a study session to the history file."""
    history = load_history(history_file)
    history.append(session)

    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)


def display_history(history: list[dict[str, Any]]) -> None:
    """Print saved sessions in a readable format."""
    if not history:
        print("No study sessions found.")
        return

    for i, session in enumerate(history, start=1):
        print(f"\n{i}. [{session.get('timestamp')}] {session.get('topic')}")
        print(f"   Q: {session.get('question')}")
        print(f"   Notes: {session.get('notes')}")


def search_history(
    history: list[dict[str, Any]],
    keyword: str,
) -> list[dict[str, Any]]:
    """Return sessions matching a keyword.

    Milestone 3:
    Search the topic, question and notes using a case-insensitive comparison.
    """
    # TODO: Implement this function.
    return []


def export_session(
    session: dict[str, Any],
    export_directory: str,
) -> Path | None:
    """Export one selected study session as a Markdown file.

    Milestone 3:
    - Create the export directory if required.
    - Create a safe and meaningful filename.
    - Write the session details in Markdown format.
    - Return the path of the created file.
    """
    # TODO: Implement this function.
    return None