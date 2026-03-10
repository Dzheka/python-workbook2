def student_report(students):
    for student in students:
        grade = student["grade"]
        if grade >= 90:
            letter = "A"
        elif grade >= 80:
            letter = "B"
        elif grade >= 70:
            letter = "C"
        elif grade >= 60:
            letter = "D"
        else:
            letter = "F"
        yield f"{student['name']}: {letter}"
