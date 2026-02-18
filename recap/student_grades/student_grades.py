def get_status(score):
    return "Pass" if score >= 50 else "Fail"


def process_grades(data):
    result = {}
    for name, score in data:
        result[name] = get_status(score)
    return result


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
