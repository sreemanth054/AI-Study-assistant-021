"""Functions for managing study-session history.

The functions in this file are intentionally incomplete. Complete the TODOs
during the appropriate assignment milestones.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_history(history_file: str) -> list[dict[str, Any]]:
    path = Path(history_file)
    if not path.exists():
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"History file '{history_file}' contains invalid JSON. Starting with empty history.")
        return []


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
    """Return sessions matching a keyword."""
    keyword_lower = keyword.lower()
    return [
        session for session in history
        if keyword_lower in session.get("topic", "").lower()
        or keyword_lower in session.get("question", "").lower()
        or keyword_lower in session.get("notes", "").lower()
    ]

def export_session(
    session: dict[str, Any],
    export_directory: str,
) -> Path | None:
    """Export one selected study session as a Markdown file."""
    Path(export_directory).mkdir(parents=True, exist_ok=True)

    timestamp = session.get("timestamp", "unknown").replace(":", "-")
    topic = session.get("topic", "session").replace(" ", "_")
    filename = f"{timestamp}_{topic}.md"
    filepath = Path(export_directory) / filename

    content = (
        f"# Study Session: {session.get('topic')}\n\n"
        f"**Date:** {session.get('timestamp')}\n\n"
        f"**Question:** {session.get('question')}\n\n"
        f"**Notes:**\n\n{session.get('notes')}\n"
    )

    with open(filepath, "w") as f:
        f.write(content)

    return filepath