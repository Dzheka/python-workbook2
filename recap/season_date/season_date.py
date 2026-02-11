m = input("Enter month: ").strip().lower()
d = int(input("Enter day: "))

months = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}

if m not in months:
    print("Invalid month")
else:

    num = months[m]

    if (num == 3 and d >= 20) or (num in [4, 5]) or (num == 6 and d <= 20):
        print("Spring")
    elif (num == 6 and d >= 21) or (num in [7, 8]) or (num == 9 and d <= 21):
        print("Summer")
    elif (num == 9 and d >= 22) or (num in [10, 11]) or (num == 12 and d <= 20):
        print("Fall")
    else:
        print("Winter")
