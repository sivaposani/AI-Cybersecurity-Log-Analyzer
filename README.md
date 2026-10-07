# AI Cybersecurity Log Analyzer

A beginner-friendly Python cybersecurity project that analyzes authentication logs, detects suspicious login activity, and uses AI to explain security alerts.

## Features

- Parses authentication log files
- Detects repeated failed login attempts
- Detects suspicious successful logins after multiple failures
- Assigns security severity levels
- Uses OpenAI for AI-powered security analysis
- Generates recommended security actions
- Saves alerts to a JSON file
- Generates a readable security report

## Project Structure

```text
AI-Cybersecurity-Log-Analyzer/
│
├── backend/
│   └── main.py
│
├── data/
│   ├── sample.log
│   └── alerts.json
│
├── models/
│   └── analyzer.py
│
├── docs/
│
├── .gitignore
├── .env
└── README.md