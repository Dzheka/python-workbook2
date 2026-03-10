def describe_weather(temp):
    if temp > 60 or temp < -60:
        raise ValueError("Invalid temperature")
    if temp >= 25:
        return "hot"
    elif temp >= 10:
        return "warm"
    else:
        return "cold"


classifier = lambda temp: "hot" if temp >= 25 else ("warm" if temp >= 10 else "cold")
