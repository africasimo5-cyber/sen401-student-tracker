# students.py
# holds the list of students and some functions to work with the scores

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


def print_students(student_list: list[Student]) -> None:
    for s in student_list:
        print(s.name, s.score)
