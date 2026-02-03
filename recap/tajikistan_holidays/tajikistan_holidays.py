def holiday(month, date):
    if month == 1 and date == 1:
        return "New Year's Day"
    elif month == 3 and date == 8:
        return "International Women's Day"
    elif (month == 3) and (date >= 21 and date <= 24):
        return "Navruz (Persian New Year)"
    elif month == 5 and date == 1:
        return "Labour Day"
    elif month == 5 and date == 9:
        return "Victory Day"
    elif month == 6 and date == 27:
        return "National Unity Day"
    elif month == 9 and date == 9:
        return "Independence Day"
    elif month == 11 and date == 6:
        return "Constitution Day"
    else:
        return "Not a national holiday"

user_month = int(input())
user_date = int(input())
print(holiday(user_month, user_date)) 