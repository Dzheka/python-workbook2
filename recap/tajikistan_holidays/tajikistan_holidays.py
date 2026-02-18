def get_holiday(month: int, day: int) -> str:
    holidays = {
        (1, 1): "New Year's Day",
        (3, 8): "International Women's Day",
        (5, 1): "Labour Day",
        (5, 9): "Victory Day",
        (6, 27): "National Unity Day",
        (9, 9): "Independence Day",
        (11, 6): "Constitution Day"
    }

    if month == 3 and 21 <= day <= 24:
        return "Navruz (Persian New Year)"

    return holidays.get((month, day), "Not a national holiday")


if __name__ == "__main__":
    month = int(input())
    day = int(input())
    print(get_holiday(month, day))
