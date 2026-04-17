def student_report(students):
    for student in students:
        name = student["name"]
        grade = student["grade"]

        if 90 <= grade <= 100:
            letter = "A"
        elif 80 <= grade <= 89:
            letter = "B"
        elif 70 <= grade <= 79:
            letter = "C"
        else:
            letter = "F"

        yield f"{name}: {letter}"


data = [{"name": "Alice", "grade": 95}, {"name": "Dan", "grade": 55}]
print(list(student_report(data)))
