month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def season(month, date):
    if (month not in month_list) and (date <= 0 or date > 31):
        return "Invalid month and date input"
    elif month not in month_list:
        return "Invalid month input"
    elif date <= 0 or date > 31 or date == str:
        return "Invalid date input"
    
    elif (month == "March" and date >= 20) or (month in ["April", "May"]) or (month == "June" and date <= 20):
        return "Spring"
    elif (month == "June" and date >= 21) or (month in ["July", "August"]) or (month == "September" and date <= 21):
        return "Summer"
    elif (month == "September" and date >= 22) or (month in ["October", "November"]) or (month == "December" and date <= 20):
        return "Fall"
    else:
        return "Winter"


user_month = input().title()
user_date = int(input())
print(season(user_month, user_date))