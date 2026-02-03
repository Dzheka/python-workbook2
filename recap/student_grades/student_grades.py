def get_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"


def process_grades(data):
    grades_dict = {}
    for item in data:
        student = item[0]
        scores = item[1]
        grades_dict[student] = get_status(scores)
    return grades_dict


def main():
    raw_scores = [
        ["Alice", 85],
        ["Bob", 42],
        ["Charlie", 60],
        ["David", 25],
        ["Eve", 95]
    ]

    result = process_grades(raw_scores)
    print(result)


if __name__ == "__main__":
    main()
