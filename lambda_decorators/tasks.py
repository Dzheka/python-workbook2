# Task 1: The Average Grade (*args)
def calculate_average(student_name, *grades):
    result = sum(grades)/len(grades)
    print(f"Student {student_name} has an average grade of {result}")
calculate_average("Nizar", 99, 98)

# Task 2: Weather Report (**kwargs)
def print_weather(city, **details):
    print(f"In {city}: {details}")
print_weather("Dushanbe", temp=30, sky= "sunny", wind="5km/h")

# Task 3: Sorting Students by Age

