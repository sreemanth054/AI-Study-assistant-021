# AI Study Assistant

**Student Name:** Sreemanth Vaddi
**Roll Number:** AM.SC.P2CSN26021  

## Project Overview

The AI Study Assistant is a CLI based Python program for aiding users in going through study questions, reflecting on them in their own language, and keeping track of their progress. It allows users to launch a study session, view previous sessions, perform searches in their session history using keywords, and export sessions to markdown documents. The project grew incrementally using Git from a simple Version 1, which had core features of launching and storing sessions, to a better Version 2.

## Implemented Features

- Load study questions from a JSON file and select one to study
- Complete a study session and save a record 
- View previously saved study sessions
- Search study history by keyword 
- Export a selected study session 
- Display the three most recent sessions automatically on startup
- Configurable file paths and settings via `config.py`
- error handling for missing or invalid JSON files

## Project Structure

```text
study_assistant/
├── study_assistant.py
├── prompts.py
├── history.py
├── config.py
├── sample_questions.json
├── requirements.txt
├── README.md
└── .env.example
```

## Installation and Setup

1. Clone the repository and go into the project folder:

```bash
git clone <repository-url>
cd study_assistant
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment.

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

After activating the virtual environment, run the application using:

```bash
python3 study_assistant.py
```

The application will show a menu where you can start a study session, view previous sessions, search through the history, or export a session.


## Generated Files

The completed application may generate:

- `history.json` — stores all saved study sessions
- an `exports/` directory containing Markdown files for exported sessions

These are user-specific, generated at runtime rather than part of the source code, so they are excluded from version control via `.gitignore` and are not tracked by Git.

## Version Summary

### Version 1

Version 1 focused on building the basic application. It loads questions from sample_questions.json, lets the user select a question and write a personal reflection, saves the sessions to history.json, and allows the user to view previous sessions through a menu-driven interface.

### Version 2

Version 2 was developed on a separate branch and added some new features to Version 1. These included searching saved sessions using keywords, exporting individual sessions as Markdown files, showing the last three sessions as "Recent Activity" when the program starts, and moving the file paths to config.py instead of keeping them hardcoded. After completing the changes, the branch was merged back into main.
## Notes

- Do not include real API keys, passwords or access tokens.
- Complete the milestones in order.
- Maintain a meaningful Git history throughout development.