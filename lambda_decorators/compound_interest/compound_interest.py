def compound_interest(principal, rate, years):
    if years == 0:  # base case
        return round(principal, 2)
    new_principal = principal * (1 + rate)
    return compound_interest(new_principal, rate, years - 1)