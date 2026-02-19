class RGBColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"rgb({self.r}, {self.g}, {self.b})"

    def __repr__(self):
        return f"RGBColor({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other):
        return RGBColor((self.r + other.r) // 2, (self.g + other.g) // 2, (self.b + other.b) // 2)

    def __contains__(self, channel):
        if channel == "red":
            return self.r > 0
        elif channel == "green":
            return self.g > 0
        elif channel == "blue":
            return self.b > 0
        return False


red = RGBColor(255, 0, 0)
blue = RGBColor(0, 0, 255)

print(red)
print(repr(blue))
print(red == RGBColor(255, 0, 0))

purple = red + blue
print(purple)

print("red" in red)
print("green" in red)
print("blue" in blue)
