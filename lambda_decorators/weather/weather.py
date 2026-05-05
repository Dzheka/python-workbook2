
def celsius_only(func):
    def wrapper(temp):
        if temp < -90 or temp > 60:
            raise ValueError("Invalid temperature")
        return func(temp)
    return wrapper



classifier = lambda temp: "cold" if temp < 10 else "warm" if temp < 25 else "hot"



@celsius_only
def describe_weather(temp):
    return classifier(temp)



print(describe_weather(30))
print(describe_weather(-5))
print(describe_weather(20))
print(describe_weather(100))