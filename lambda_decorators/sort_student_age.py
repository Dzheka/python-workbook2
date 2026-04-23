def sort_student_by_age(students):
    sorted_students = sorted(students, key=lambda student: student[1])
    return sorted_students
