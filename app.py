# app.py
# demo program for the student score tracker

from students import (get_students, add_student, average_score,
                      median_score, pass_rate, print_students)
from utils.helpers import highest_score, lowest_score, grade


def main():
    print("=== Student Score Tracker ===\n")
    add_student("Ibrahim Musa", 47)
    add_student("Test Student", 150)  # invalid, Pydantic should reject it
    students = get_students()
    if not students:
        print("No students to show.")
        return
    print()
    print_students(students)

    top = highest_score(students)
    bottom = lowest_score(students)
    print(f"Highest score : {top.name} ({top.score:.1f}, grade {grade(top.score)})")
    print(f"Lowest score  : {bottom.name} ({bottom.score:.1f}, grade {grade(bottom.score)})")
    print(f"Average score : {average_score(students):.2f}")
    print(f"Median score  : {median_score(students):.2f}")
    print(f"Pass rate     : {pass_rate(students):.0f}%")


if __name__ == "__main__":
    main()
