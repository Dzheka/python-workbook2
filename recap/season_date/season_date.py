month = input().strip().lower()
day = int(input())

if (month == "march" and day >= 20) or month in ["april", "may"] or (month == "june" and day <= 20):
    print("Spring")

elif (month == "june" and day >= 21) or month in ["july", "august"] or (month == "september" and day <= 21):
    print("Summer")

elif (month == "september" and day >= 22) or month in ["october", "november"] or (month == "december" and day <= 20):
    print("Fall")

else:
    print("Winter")


