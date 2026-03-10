def compound_interest(principal, rate, years):
    if years == 0:
        return round(principal, 2)

    principal = principal * (1 + rate)
    return compound_interest(principal, rate, years - 1)



print(compound_interest(1000, 0.05, 3))
