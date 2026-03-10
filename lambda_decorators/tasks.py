def calculate_average(student_name, *grades):
    avg = sum(grades) / len(grades)
    return f"Student {student_name} has an average grade of {avg}"


def print_weather(city, **details):
    parts = []
    for key, value in details.items():
        parts.append(f"{key} is {value}")
    print(f"In {city}: " + ", ".join(parts))


students = [("Ali", 22), ("Vali", 19), ("Zuhra", 20)]
sorted_students = sorted(students, key=lambda s: s[1])
print(sorted_students)


temps = [25, 38, 42, 28, 33, 41]
hot_days = list(filter(lambda t: t > 35, temps))
print(hot_days)


names = ["ali", "vali", "sami"]
capitalized = list(map(lambda n: n.capitalize(), names))
print(capitalized)


def get_student(list_of_students):
    for student in list_of_students:
        yield student


def weather_tracker(start_temp):
    temp = start_temp
    while True:
        yield temp
        temp += 1


def check_auth(func):
    def wrapper(*args, **kwargs):
        print("Checking access to the Gradebook...")
        return func(*args, **kwargs)
    return wrapper


@check_auth
def view_grades():
    print("Here are your grades: A, B, A+")


def to_fahrenheit(func):
    def wrapper(*args, **kwargs):
        celsius = func(*args, **kwargs)
        return (celsius * 9/5) + 32
    return wrapper


@to_fahrenheit
def get_temperature():
    return 30


def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*** {result} ***"
    return wrapper


@make_bold
def student_note():
    return "Ali is a top student"


if __name__ == "__main__":
    print(calculate_average("Ali", 90, 80, 70))
    print()
    print_weather("Dushanbe", temp=30, sky="Sunny", wind="5km/h")
    print()

    gen = get_student(["Ali", "Vali", "Zuhra", "Sami"])
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print()

    tracker = weather_tracker(20)
    print(next(tracker))
    print(next(tracker))
    print(next(tracker))
    print()

    view_grades()
    print()

    print(get_temperature())
    print()

    print(student_note())
