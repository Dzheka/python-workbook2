def celsius_only(func):
    def wrapper(temp, *args, **kwargs):
        if temp < -90 or temp > 60:
            raise ValueError("Invalid temperature")
        return func(temp, *args, **kwargs)

    return wrapper


classifier = lambda temp: "cold" if temp < 10 else "warm" if 10 <= temp < 25 else "hot"


@celsius_only
def describe_weather(temp):
    return classifier(temp)
