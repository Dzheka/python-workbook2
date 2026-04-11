def season(month,day):
    if month == "April" or month == "May":
        return "Spring"
    elif month == "June":
        if day >= 21:
            return "Summer"
        return "Spring"
    if month == "July" or month == "August":
        return "Summer"
    elif month == "September":
        if day >= 22:
            return "Fall"
        return "Summer"
    if month == "October" or month == "November":
        return "Fall"
    elif month == "December":
        if day >= 21:
            return "Winter"
        return "Fall"
    if month == "January" or month == "February":
        return "Winter"
    elif month == "March":
        if day >= 20:
            return "Spring"
        return "Winter"
    
month = input("month: ")
day = int(input("day: "))
print(season(month,day))
    