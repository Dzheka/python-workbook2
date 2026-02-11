def get_status(score):
    if score >= 50:
          return "pass"
    else:
          return "fail"


def process_grades(data):
     bigdict = dict()
     for i in range (len(data)):
          set = data[i]
          name = set[0]
          score = set[1]
          bigdict[name] = get_status(score)
     return bigdict

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
