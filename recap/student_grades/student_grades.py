def get_status(score):
    return "Pass" if score >= 50 else "Fail"


def process_grades(data):
    result = {}
    for name, score in data:
        result[name] = get_status(score)
    return result
