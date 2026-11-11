"""utils/helpers.py

Helper functions for finding the best and worst student and for converting
a score to a letter grade (Nigerian university 5-point scale).
"""

from typing import Optional

# (minimum score, grade) from highest to lowest
GRADE_BANDS: list[tuple[float, str]] = [
    (70, "A"),
    (60, "B"),
    (50, "C"),
    (45, "D"),
    (40, "E"),
]


def highest_score(student_list: list) -> Optional[object]:
    """Return the student with the highest score, or None if the list is empty."""
    return max(student_list, key=lambda s: s.score, default=None)


def lowest_score(student_list: list) -> Optional[object]:
    """Return the student with the lowest score, or None if the list is empty."""
    return min(student_list, key=lambda s: s.score, default=None)


def grade(score: float) -> str:
    """Convert a score to a letter grade. Anything below 40 is an F."""
    for minimum, letter in GRADE_BANDS:
        if score >= minimum:
            return letter
    return "F"
