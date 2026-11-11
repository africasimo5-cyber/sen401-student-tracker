# utils/helpers.py
# small helper functions used by app.py


def highest_score(student_list):
    if not student_list:
        return None
    best = student_list[0]
    for s in student_list:
        if s["score"] > best["score"]:
            best = s
    return best


def lowest_score(student_list):
    if not student_list:
        return None
    worst = student_list[0]
    for s in student_list:
        if s["score"] < worst["score"]:
            worst = s
    return worst


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
