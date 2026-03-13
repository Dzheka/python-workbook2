def print_weather(city, **details):
    forecast = f"In {city}: "

    parts = [f"{key} is {value}" for key, value in details.items()]

    forecast += ", ".join(parts)

    print(forecast)
