import math


class Shape:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_info(self):
        return f"Color: {self.color}, Position: ({self.x}, {self.y})"


class Rectangle(Shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


class Circle(Shape):
    def __init__(self, color, x, y, radius):
        super().__init__(color, x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return self.radius * 2

    def set_radius(self, new_radius):
        self.radius = new_radius


class Triangle(Shape):
    def __init__(self, color, x, y, side_a, side_b, side_c):
        super().__init__(color, x, y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def is_valid(self):
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)

    def triangle_type(self):
        if self.side_a == self.side_b == self.side_c:
            return "equilateral"
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c:
            return "isosceles"
        return "scalene"
