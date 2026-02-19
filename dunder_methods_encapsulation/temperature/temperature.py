class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        return f"{self.celsius}°C"

    def __eq__(self, other) -> bool:
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __add__(self, other):
        return f"{self.celsius + other.celsius}°C"



t1 = Temperature(25)
t2 = Temperature(30)
t3 = Temperature(25)

print(t1)          # 25°C
print(t1 == t3)    # True
print(t1 < t2)     # True
t4 = t1 + t2
print(t4)          # 55°C
print(sorted([t2, t1, Temperature(10)]))  # [10°C, 25°C, 30°C]