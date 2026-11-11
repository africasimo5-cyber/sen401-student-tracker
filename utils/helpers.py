# utils/helpers.py
# small helper functions used by app.py


def highest_score(student_list):
    if not student_list:
        return None
    return max(student_list, key=lambda s: s.score)


def lowest_score(student_list):
    if not student_list:
        return None
    return min(student_list, key=lambda s: s.score)


def grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    return "F"
