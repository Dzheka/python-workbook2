month = int(input("month: "))
day = int(input("day: "))
if month == 1 and day == 1:
    print("New year day")
elif month == 3 and day == 8:
    print("International women's day")
elif month == 3 and 21 <= day <= 24:
    print("Navruz")
elif month == 5 and day == 1:
    print("labour day")
elif month == 5 and day == 9:
    print("Victory day")
elif month == 6 and day == 27:
    print("National unity day")
elif month == 9 and day == 9:
    print("Independence day")
elif month == 11 and day == 6:
    print("New year day")
else:
    print("Not a national day")