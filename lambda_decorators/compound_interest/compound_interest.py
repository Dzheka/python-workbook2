def compound_interest(principal, rate, years):
    if years == 0:
        return round(principal, 2)
    return compound_interest(principal * (1 + rate), rate, years - 1)
