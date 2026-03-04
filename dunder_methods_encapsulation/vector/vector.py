class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"rgb({self.red}, {self.green}, {self.blue})"

    def __repr__(self):
        return f"RGBColor({self.red}, {self.green}, {self.blue})"

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        return RGBColor((self.red + other.red) // 2, (self.green + other.green) // 2, (self.blue + other.blue) // 2)

    def __contains__(self, channel):
        if channel == "red":
            return self.red > 0
        elif channel == "green":
            return self.green > 0
        elif channel == "blue":
            return self.blue > 0
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