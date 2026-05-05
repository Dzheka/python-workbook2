students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 72},
    {"name": "Carol", "grade": 95},
    {"name": "Dan",   "grade": 60},
]

sort_by_grade = lambda s: sorted(s, key=lambda x: x["grade"], reverse=True)
passing       = lambda s: list(filter(lambda x: x["grade"] >= 70, s))
get_names     = lambda s: list(map(lambda x: x["name"], s))

print(sort_by_grade(students))
print(passing(students))
print(get_names(students))