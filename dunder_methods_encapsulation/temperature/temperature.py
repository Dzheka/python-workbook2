class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return False
        return self.celsius == other.celsius

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius < other.celsius

    def __add__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return Temperature(self.celsius + other.celsius)
