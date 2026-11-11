# students.py
# holds the list of students and some functions to work with the scores

students = [
    {"name": "Adaeze Okafor", "score": 78},
    {"name": "Tunde Bakare", "score": 64},
    {"name": "Fatima Bello", "score": 91},
    {"name": "Chinedu Eze", "score": 55},
    {"name": "Grace Adeyemi", "score": 83},
]


def get_students():
    return students


def add_student(name, score):
    students.append({"name": name, "score": score})


def average_score(student_list):
    if len(student_list) == 0:
        return 0
    total = 0
    for s in student_list:
        total = total + s["score"]
    return total / len(student_list)


def print_students(student_list):
    for s in student_list:
        print(s["name"], s["score"])
