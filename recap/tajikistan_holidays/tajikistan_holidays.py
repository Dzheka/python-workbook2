month = int(input())
day = int(input())
match (month, day):
    case (1, 1):
        print("New Year's Day")
    case (3, 8):
        print("International Women's Day")
    case (3,21) | (3,22) | (3,23) | (3,24):
        print("Navruz (Persian New Year)")
    case (5,1):
        print("Labour Day")
    case (5,9):
        print("Victory Day")
    case (6,27):
        print("National Unity Day")
    case(9,9):
        print("Independence Day")
    case(11,6):
        print("Constitution Day")
    case _:
        print("Not a national holiday")

