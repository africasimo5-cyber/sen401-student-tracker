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
pip install -r requirements.txt
python app.py
```

Requires Python 3.10 or newer (tested on 3.11, compatible with 3.12).
Since v1.1 the project uses Pydantic to validate student records.

## Branches

| Branch | Purpose |
|---|---|
| `main` | Stable, released code (protected, changes go in through pull requests) |
| `dev` | Integration branch for ongoing work |
| `feature/*` | New features, e.g. `feature/grade-report` |
| `maint/*` | Maintenance work, e.g. `maint/bug-fixes` |
| `maintenance` | Lab 2 maintenance changes (released as v1.1) |

## Releases

- **v1.0**: baseline, first working version
- **v1.1**: corrective, adaptive, perfective and preventive maintenance

## Author

Emmanuel Oyebanji Oyebode (2024/C/SENG/0866)
