def sort_by_grade(students):
    return sorted(students, key=lambda s: s["grade"], reverse=True)


def passing(students):
    return list(filter(lambda s: s["grade"] >= 65, students))


def get_names(students):
    return list(map(lambda s: s["name"], students))
