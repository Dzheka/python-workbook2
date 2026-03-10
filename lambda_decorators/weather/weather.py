from idlelib.colorizer import prog_group_name_to_tag


def celsius_only(func):
    def wrapper(temp):
        if temp > 60 or temp < -90:
            raise ValueError("Invalid temperature")
        return func(temp)
    return wrapper

classifier = lambda  temp: "cold" if temp < 10 else("warm" if 10 <= temp < 25 else "hot")

@celsius_only
def describe_weather(temp):
    return classifier(temp)
