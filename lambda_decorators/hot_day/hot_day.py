def hot_days(data):
    for day, temp in data:
        if temp > 30:
            yield (day, temp)


def first_n_hot(data, n):
    result = []
    for day, temp in data:
        if temp > 30:
            result.append((day, temp))
        if len(result) == n:
            break
    return result
