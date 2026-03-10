data = [
    {"name": "Alice", "grade": 95},
    {"name": "Bob",   "grade": 85},
    {"name": "Carol", "grade": 74},
    {"name": "Dan",   "grade": 55},
]


def student_report(students):
    for student in students:
        name  = student["name"]
        grade = student["grade"]

        if grade >= 90:
            letter = "A"
        elif grade >= 80:
            letter = "B"
        elif grade >= 70:
            letter = "C"
        else:
            letter = "F"

        yield f"{name}: {letter}"



for report in student_report(data):
    print(report)
