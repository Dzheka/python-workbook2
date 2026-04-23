def get_season(month: str, day: int) -> str:
    month = month.lower()

    if month == "march":
        return "Spring" if day >= 20 else "Winter"
    if month == "april" or month == "may":
        return "Spring"
    if month == "june":
        return "Summer" if day >= 21 else "Spring"
    if month == "july" or month == "august":
        return "Summer"
    if month == "september":
        return "Fall" if day >= 22 else "Summer"
    if month == "october" or month == "november":
        return "Fall"
    if month == "december":
        return "Winter" if day >= 21 else "Fall"
    return "Winter"


if __name__ == "__main__":
    month = input("Write down the month").strip()
    day = int(input("Write down the day").strip())
    print(get_season(month, day))
