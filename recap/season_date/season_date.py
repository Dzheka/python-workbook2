def is_spring(month, day):
    return (month == "march" and day >= 20) or month in ("april", "may") or (month == "june" and day <= 20)


def is_summer(month, day):
    return (month == "june" and day >= 21) or month in ("july", "august") or (month == "september" and day <= 21)


def is_fall(month, day):
    return (month == "september" and day >= 22) or month in ("october", "november") or (month == "december" and day <= 20)


def season(month, day):
    if is_spring(month, day):
        return "Spring"
    if is_summer(month, day):
        return "Summer"
    if is_fall(month, day):
        return "Fall"
    return "Winter"


def main():
    month = input().strip().lower()
    day = int(input())
    print(season(month, day))


if __name__ == "__main__":
    main()

