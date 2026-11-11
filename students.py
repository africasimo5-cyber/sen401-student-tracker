# students.py
# holds the list of students and some functions to work with the scores

import statistics

from pydantic import BaseModel, Field, ValidationError


class Student(BaseModel):
    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)


students: list[Student] = [
    Student(name="Adaeze Okafor", score=78),
    Student(name="Tunde Bakare", score=64),
    Student(name="Fatima Bello", score=91),
    Student(name="Chinedu Eze", score=55),
    Student(name="Grace Adeyemi", score=83),
]


def get_students() -> list[Student]:
    return students


def add_student(name: str, score: float) -> bool:
    try:
        students.append(Student(name=name, score=score))
        return True
    except ValidationError as e:
        print(f"Could not add {name!r}: {e.errors()[0]['msg']}")
        return False


def average_score(student_list: list[Student]) -> float:
    if len(student_list) == 0:
        return 0
    total = 0
    for s in student_list:
        total = total + s.score
    return total / len(student_list)


def median_score(student_list: list[Student]) -> float:
    if not student_list:
        return 0
    return statistics.median(s.score for s in student_list)


def pass_rate(student_list: list[Student], pass_mark: float = 40) -> float:
    if not student_list:
        return 0
    passed = [s for s in student_list if s.score >= pass_mark]
    return len(passed) / len(student_list) * 100


def print_students(student_list: list[Student]) -> None:
    print(f"{'No.':<4}{'Name':<20}{'Score':>7}")
    print("-" * 31)
    for i, s in enumerate(student_list, start=1):
        print(f"{i:<4}{s.name:<20}{s.score:>7.1f}")
    print("-" * 31)
