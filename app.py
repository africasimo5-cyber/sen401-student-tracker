# app.py
# demo program for the student score tracker

from students import get_students, add_student, average_score, print_students
from utils.helpers import highest_score, lowest_score, grade


def main():
    print("=== Student Score Tracker ===")
    add_student("Ibrahim Musa", 47)
    add_student("Test Student", 150)  # invalid, Pydantic should reject it
    students = get_students()
    if not students:
        print("No students to show.")
        return
    print_students(students)

    top = highest_score(students)
    bottom = lowest_score(students)
    print("Highest:", top.name, top.score, grade(top.score))
    print("Lowest:", bottom.name, bottom.score, grade(bottom.score))
    print("Average:", average_score(students))


if __name__ == "__main__":
    main()
