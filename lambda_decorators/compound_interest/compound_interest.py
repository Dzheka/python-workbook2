def compound_interest(principal, rate, years):

    if years == 0:
        return round(principal, 2)


    return compound_interest(principal * (1 + rate), rate, years - 1)



print(compound_interest(1000, 0.1, 1))
print(compound_interest(1000, 0.1, 3))
print(compound_interest(1000, 0.05, 5))