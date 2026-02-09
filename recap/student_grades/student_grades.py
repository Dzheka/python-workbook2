def get_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

def process_grades(data):
    res = {}

    for k, v in data:
        res[k] = get_status(v)

    return  res


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
