students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 72},
    {"name": "Carol", "grade": 95},
    {"name": "Dan",   "grade": 60},
]

sort_by_grade = lambda students: sorted(students, key=lambda s: s["grade"], reverse=True)

passing       = lambda students: list(filter(lambda s: s["grade"] >= 70, students))

get_names     = lambda students: list(map(lambda s: s["name"], students))


