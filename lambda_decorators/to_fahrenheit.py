def to_fahrenheit(func):
    def wrapper():
        celsius = func()
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    return wrapper