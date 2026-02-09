m = int(input("Enter month (1-12): "))
d = int(input("Enter day: "))

holidays = {
    (1, 1): "New Year's Day",
    (3, 8): "International Women's Day",
    (5, 1): "Labour Day",
    (5, 9): "Victory Day",
    (6, 27): "National Unity Day",
    (9, 9): "Independence Day",
    (11, 6): "Constitution Day"
}

if m == 3 and d in [21, 22, 23, 24]:
    print("Navruz (Persian New Year)")
elif (m, d) in holidays:
    print(holidays[(m, d)])
else:
    print("Not a national holiday")
""" your code """

