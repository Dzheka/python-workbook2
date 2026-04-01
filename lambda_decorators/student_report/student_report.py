def student_report(students):
    for student in students:
        grade = student["grade"]

        if 90 <= grade <= 100:
            letter = "A"
        elif 80 <= grade <= 89:
            letter = "B"
        elif 70 <= grade <= 79:
            letter = "C"
        else:
            letter = "F"

        yield f"{student['name']}: {letter}"
