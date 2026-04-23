def calculate_average(student_name, *grades):
    return f"Student {student_name} has an average grade of {sum(grades) / len(grades)}"