def get_holiday(month, day):
    if month == 1 and day == 1:
        return "New Year's Day"
    if month == 3 and day == 8:
        return "International Women's Day"
    if month == 3 and 21 <= day <= 24:
        return "Navruz (Persian New Year)"
    if month == 5 and day == 1:
        return "Labour Day"
    if month == 5 and day == 9:
        return "Victory Day"
    if month == 6 and day == 27:
        return "National Unity Day"
    if month == 9 and day == 9:
        return "Independence Day"
    if month == 11 and day == 6:
        return "Constitution Day"
    return "Not a national holiday"


if __name__ == "__main__":
    month = int(input())
    day = int(input())
    print(get_holiday(month, day))
