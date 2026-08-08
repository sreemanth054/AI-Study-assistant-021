"""Main entry point for the AI Study Assistant.

Complete the TODOs gradually and create logical Git commits as the project
moves from Version 1 to Version 2.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from history import (
    display_history,
    export_session,
    load_history,
    save_session,
    search_history,
)
from prompts import APP_TITLE, format_study_prompt


# Version 1 begins with direct file-path values.
# Milestone 3 requires these values to be read from config.py.
from config import QUESTIONS_FILE, HISTORY_FILE, RECENT_ACTIVITY_LIMIT


def load_questions(question_file: str) -> list[dict[str, Any]]:
    try:
        with open(question_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Questions file '{question_file}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Questions file '{question_file}' contains invalid JSON.")
        return []
   


def select_question(
    questions: list[dict[str, Any]],
) -> dict[str, Any] | None:
    print("\nAvailable questions:")
    for i, q in enumerate(questions, start=1):
        print(f"{i}. [{q.get('topic', 'Unknown')}] {q.get('question', '')}")

    choice = input("\nSelect a question number: ").strip()
    if not choice.isdigit():
        print("Invalid selection.")
        return None

    index = int(choice) - 1
    if 0 <= index < len(questions):
        return questions[index]

    print("Invalid selection.")
    return None

def complete_study_session(
    selected_question: dict[str, Any],
) -> dict[str, Any]:
    """Conduct one session and return the session record."""
    topic = str(selected_question.get("topic", "Unknown Topic"))
    question = str(selected_question.get("question", ""))

    print("\n" + format_study_prompt(topic, question))
    notes = input("\nYour explanation or reflection: ").strip()

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "topic": topic,
        "question": question,
        "notes": notes,
    }


def start_study_session() -> None:
    """Run and save one study session."""
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        return

    selected_question = select_question(questions)
    if selected_question is None:
        return

    session = complete_study_session(selected_question)
    save_session(HISTORY_FILE, session)
    print("\nStudy session saved.")


def show_recent_activity(history: list[dict[str, Any]]) -> None:
    """Display the three most recent sessions when the application starts."""
    if not history:
        return
    print("\nRecent Activity:")
    recent = history[-RECENT_ACTIVITY_LIMIT:]
    display_history(recent)


def run_search() -> None:
    """Search previously saved sessions."""
    history = load_history(HISTORY_FILE)
    keyword = input("Enter a keyword: ").strip()
    results = search_history(history, keyword)
    display_history(results)


def run_export() -> None:
    """Allow the user to select and export one saved session."""
    history = load_history(HISTORY_FILE)

    if not history:
        print("No study sessions are available to export.")
        return

    display_history(history)

    choice = input("\nEnter the number of the session to export: ").strip()
    if not choice.isdigit():
        print("Invalid selection.")
        return

    index = int(choice) - 1
    if not (0 <= index < len(history)):
        print("Invalid selection.")
        return

    filepath = export_session(history[index], "exports")
    print(f"\nSession exported to: {filepath}")

def display_menu() -> None:
    """Print the main application menu."""
    print(f"\n{APP_TITLE}")
    print("1. Start a study session")
    print("2. View study history")
    print("3. Search study history")
    print("4. Export a study session")
    print("5. Exit")


def main() -> None:
    """Run the menu-driven application."""
    history = load_history(HISTORY_FILE)
    show_recent_activity(history)

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_study_session()
        elif choice == "2":
            display_history(load_history(HISTORY_FILE))
        elif choice == "3":
            run_search()
        elif choice == "4":
            run_export()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
