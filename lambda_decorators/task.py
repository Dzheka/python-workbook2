def calculate_average(student_name, *grades):
    if len(grades) == 0:
        return f"Student {student_name} has an average grade of 0"

    average = sum(grades) / len(grades)
    return f"Student {student_name} has an average grade of {average}"

print(calculate_average ("Ilyos",20, 20, 20))

def print_weather(city, **details):
    if len (    )
