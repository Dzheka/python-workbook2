def calculate_average(student_name, *grades):
    if not grades:
        return f"Student {student_name} has no grades recorded."

    average = sum(grades) / len(grades)

    return f"Student {student_name} has an average grade of {average}"
