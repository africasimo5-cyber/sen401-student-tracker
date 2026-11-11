"""students.py

Data module for the Student Score Tracker.

It defines the Student model (validated with Pydantic), keeps the list of
students in memory and provides the functions that calculate statistics
on their scores. Printing is kept here only for the student table so that
app.py stays short.
"""

import statistics

from pydantic import BaseModel, Field, ValidationError

PASS_MARK: float = 40  # minimum score needed to pass a course
TABLE_WIDTH: int = 31


class Student(BaseModel):
    """One student record. Pydantic rejects empty names and scores outside 0-100."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)


# Sample data used by the demo. In a real system this would come from a file or database.
_students: list[Student] = [
    Student(name="Adaeze Okafor", score=78),
    Student(name="Tunde Bakare", score=64),
    Student(name="Fatima Bello", score=91),
    Student(name="Chinedu Eze", score=55),
    Student(name="Grace Adeyemi", score=83),
]


def get_students() -> list[Student]:
    """Return a copy of the student list so callers cannot change it by accident."""
    return list(_students)


def add_student(name: str, score: float) -> bool:
    """Validate and add a new student.

    Returns True if the student was added, or False if validation failed.
    """
    try:
        _students.append(Student(name=name, score=score))
        return True
    except ValidationError as err:
        print(f"Could not add {name!r}: {err.errors()[0]['msg']}")
        return False


def _scores(student_list: list[Student]) -> list[float]:
    """Helper that pulls out just the scores, used by the statistics below."""
    return [s.score for s in student_list]


def average_score(student_list: list[Student]) -> float:
    """Mean score of the list, or 0 if the list is empty."""
    scores = _scores(student_list)
    return statistics.fmean(scores) if scores else 0.0


def median_score(student_list: list[Student]) -> float:
    """Middle score of the list, or 0 if the list is empty."""
    scores = _scores(student_list)
    return statistics.median(scores) if scores else 0.0


def pass_rate(student_list: list[Student], pass_mark: float = PASS_MARK) -> float:
    """Percentage of students who scored at least pass_mark."""
    if not student_list:
        return 0.0
    passed = sum(1 for s in student_list if s.score >= pass_mark)
    return passed / len(student_list) * 100


def summary(student_list: list[Student]) -> dict[str, float]:
    """Collect all the statistics in one place so app.py does not repeat calls."""
    return {
        "count": len(student_list),
        "average": average_score(student_list),
        "median": median_score(student_list),
        "pass_rate": pass_rate(student_list),
    }


def print_students(student_list: list[Student]) -> None:
    """Print the students as a numbered table."""
    print(f"{'No.':<4}{'Name':<20}{'Score':>7}")
    print("-" * TABLE_WIDTH)
    for i, s in enumerate(student_list, start=1):
        print(f"{i:<4}{s.name:<20}{s.score:>7.1f}")
    print("-" * TABLE_WIDTH)
