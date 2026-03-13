def get_status(score):
        if score>= 50 :
            return "Pass"
        return "Fail"


def process_grades(data):
    result = {}
    for datas in data:
        name, score = datas[0], datas[1]
        status = get_status(score)
        result[name] = status
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
