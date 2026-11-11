"""app.py

Demo program for the Student Score Tracker. Run with:  python app.py
"""

from students import get_students, add_student, summary, print_students
from utils.helpers import highest_score, lowest_score, grade


def describe(label: str, student) -> str:
    """Format one line such as 'Highest score : Fatima Bello (91.0, grade A)'."""
    return f"{label:<14}: {student.name} ({student.score:.1f}, grade {grade(student.score)})"


def main() -> None:
    print("=== Student Score Tracker ===\n")

    # Show that validation works: the first is added, the second is rejected.
    add_student("Ibrahim Musa", 47)
    add_student("Test Student", 150)

    students = get_students()
    if not students:
        print("No students to show.")
        return

    print()
    print_students(students)
    print(describe("Highest score", highest_score(students)))
    print(describe("Lowest score", lowest_score(students)))

    stats = summary(students)
    print(f"{'Average score':<14}: {stats['average']:.2f}")
    print(f"{'Median score':<14}: {stats['median']:.2f}")
    print(f"{'Pass rate':<14}: {stats['pass_rate']:.0f}%")


if __name__ == "__main__":
    main()
