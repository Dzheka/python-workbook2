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



data = [("Mon", 28), ("Tue", 35), ("Wed", 31), ("Thu", 22), ("Fri", 33)]

print(list(hot_days(data)))
print(first_n_hot(data, 2))
