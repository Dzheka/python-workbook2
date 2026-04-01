class RGBColor:
    def __init__(self, r, g, b):
        self.r = max(0, min(255, r))
        self.g = max(0, min(255, g))
        self.b = max(0, min(255, b))

    def __str__(self):
        return f"rgb({self.r}, {self.g}, {self.b})"

    def __repr__(self):
        return f"RGBColor({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if not isinstance(other, RGBColor):
            return False
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __add__(self, other):
        if not isinstance(other, RGBColor):
            return NotImplemented
        return RGBColor(
            (self.r + other.r) // 2,
            (self.g + other.g) // 2,
            (self.b + other.b) // 2,
        )

    def __contains__(self, channel_name):
        channel_name = channel_name.lower()
        if channel_name == "red":
            return self.r > 0
        if channel_name == "green":
            return self.g > 0
        if channel_name == "blue":
            return self.b > 0
        return False
