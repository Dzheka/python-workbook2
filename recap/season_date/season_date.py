month = input().lower()
day = int(input())
if month in ("april","may"):
    print("Spring")
elif month == "march":
    if day>=20:
        print("Spring")
    else:
        print("Winter")
elif month == "june":
    if day<=20:
        print("Spring")
    else:
        print("Summer")
elif month in ("july","august"):
    print("Summer")
elif month == "september":
    if day<=21:
        print("Summer")
    else:
        print("Fall")
elif month in ("october","november"):
    print("Fall")
elif month == "december":
    if day<=20:
        print("Fall")
    else:
        print("Winter")
elif month in ("january","february"):
    print("Winter")
else:
    print("Input the suitable value")
