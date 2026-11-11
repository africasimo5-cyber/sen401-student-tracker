# Student Score Tracker

A small modular Python project for SEN 401 (Software Configuration Management and Maintenance), Lab 1.
It keeps a list of students and their scores and prints simple statistics.

## Project structure

```
student-tracker/
├── app.py              # main script, runs the demo
├── students.py         # student data and score functions
├── utils/
│   ├── __init__.py
│   └── helpers.py      # highest score, lowest score, grade
├── requirements.txt    # dependencies
└── README.md
```

## How to run

```bash
python app.py
```

Requires Python 3.10 or newer. No external packages are needed for v1.0.

## Branches

| Branch | Purpose |
|---|---|
| `main` | Stable, released code (protected, changes go in through pull requests) |
| `dev` | Integration branch for ongoing work |
| `feature/*` | New features, e.g. `feature/grade-report` |
| `maint/*` | Maintenance work, e.g. `maint/bug-fixes` |

## Author

Emmanuel Oyebanji Oyebode (2024/C/SENG/0866)
