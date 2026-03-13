def get_season(month, day):
    month = month.lower()

    if (month == "march" and day >= 20) or month in ["april", "may"] or (month == "june" and day <= 20):
        return "Spring"
    if (month == "june" and day >= 21) or month in ["july", "august"] or (month == "september" and day <= 21):
        return "Summer"
    if (month == "september" and day >= 22) or month in ["october", "november"] or (month == "december" and day <= 20):
        return "Fall"
    return "Winter"


if __name__ == "__main__":
    month = input().strip()
    day = int(input())
    print(get_season(month, day))
