import math


class Shape:
    def __init__(self, color, x, y):
        self.color = color
        self.x     = x
        self.y     = y

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
        super().__init__(color, x, y)   # get color, x, y from Shape
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width  = new_width
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
        a, b, c = self.side_a, self.side_b, self.side_c
        return a + b > c and a + c > b and b + c > a

    def triangle_type(self):
        if self.side_a == self.side_b == self.side_c:
            return "equilateral"
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c:
            return "isosceles"
        return "scalene"



rectangle = Rectangle("blue",  0,  0, 5, 3)
circle    = Circle("red",     10, 10, 4)
triangle  = Triangle("green",  5,  5, 3, 4, 5)

print("Rectangle:")
print(f"Color: {rectangle.color}")
print(f"Position: ({rectangle.x}, {rectangle.y})")
print(f"Dimensions: {rectangle.width} x {rectangle.height}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Is square: {rectangle.is_square()}")

print("\nCircle:")
print(f"Color: {circle.color}")
print(f"Position: ({circle.x}, {circle.y})")
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter()}")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")

print("\nTriangle:")
print(f"Color: {triangle.color}")
print(f"Position: ({triangle.x}, {triangle.y})")
print(f"Sides: {triangle.side_a}, {triangle.side_b}, {triangle.side_c}")
print(f"Is valid: {triangle.is_valid()}")
print(f"Type: {triangle.triangle_type()}")
print(f"Area: {triangle.area():.2f}")
print(f"Perimeter: {triangle.perimeter()}")


shapes = [rectangle, circle, triangle]
print("\nAll shapes areas:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.area():.2f}")

print("\nAll shapes perimeters:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.perimeter():.2f}")

rectangle.move(2, 3)
print(f"\nRectangle moved to: ({rectangle.x}, {rectangle.y})")

rectangle.resize(6, 6)
print(f"Rectangle resized to: {rectangle.width} x {rectangle.height}")
print(f"Is square now: {rectangle.is_square()}")