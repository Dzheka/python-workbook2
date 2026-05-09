from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        return math.sqrt(s*(s-self.side1) * (s-self.side2) * (s-self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    

# This should fail - cannot instantiate abstract class
try:
    shape = Shape("red")
except TypeError as e:
    print(f"Error: {e}")

# Create concrete shapes
rectangle = Rectangle("red", 10, 5)
circle = Circle("blue", 7)
triangle = Triangle("green", 5, 5, 6)

# All shapes have area() and perimeter()
print(f"Rectangle area: {rectangle.area():.2f}")        # 50.00
print(f"Rectangle perimeter: {rectangle.perimeter():.2f}") # 30.00

print(f"Circle area: {circle.area():.2f}")              # 153.94
print(f"Circle perimeter: {circle.perimeter():.2f}")    # 43.98

print(f"Triangle area: {triangle.area():.2f}")          # 12.00
print(f"Triangle perimeter: {triangle.perimeter():.2f}") # 16.00

# Function that works with ANY shape
def print_shape_info(shape: Shape):
    print(f"{shape.color} {shape.__class__.__name__}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

shapes = [rectangle, circle, triangle]
for shape in shapes:
    print_shape_info(shape)