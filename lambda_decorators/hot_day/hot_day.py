def hot_days(temperatures):
    for day, temp in temperatures:
        if temp > 30:
            yield (day, temp)


def first_n_hot(temperatures, n):
    result = []
    for day in hot_days(temperatures):
        result.append(day)
        if len(result) == n:
            break
    return result
