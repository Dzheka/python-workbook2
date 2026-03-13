def weather_report(city,**details):
    report = []
    for key, value in details.items():
        report.append(f"{key} is {value}")

    report = ", ".join(report)
    print(f"In {city}: {report}")


print(weather_report("Dushanbe", temp=30, sky="Sunny", wind="5km/h"))
