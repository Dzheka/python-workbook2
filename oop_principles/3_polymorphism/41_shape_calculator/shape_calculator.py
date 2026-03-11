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
    
def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)

def find_largest_shape(shapes):
    return max(shapes, key=lambda s: s.area())

def print_shape_report(shapes):
    total_area = 0
    for shape in shapes:
        print(f"{shape.color} {shape.__class__.__name__} - "
              f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
        total_area += shape.area()
    print("-" * 45)
    print(f"Total Area: {total_area:.2f}")

def filter_by_area(shapes, min_area):
    return [s for s in shapes if s.area() >= min_area]

def sort_shapes_by_area(shapes):
    return sorted(shapes, key=lambda s: s.area())

# Create a diverse collection of shapes
shapes = [
    Rectangle("red", 10, 5),
    Circle("blue", 7),
    Triangle("green", 5, 5, 6),
    Rectangle("yellow", 8, 8),
    Circle("purple", 3),
    Triangle("orange", 9, 9, 10)
]

# Polymorphic function - works with ANY shape
total = calculate_total_area(shapes)
print(f"Total area of all shapes: {total:.2f}")
# Output: Total area of all shapes: 345.63

# Find the largest shape polymorphically
largest = find_largest_shape(shapes)
print(f"Largest shape: {largest.color} {largest.__class__.__name__} with area {largest.area():.2f}")
# Output: Largest shape: blue Circle with area 153.94

# Print detailed report
print("\n=== Shape Report ===")
print_shape_report(shapes)
# Output:
# red Rectangle - Area: 50.00, Perimeter: 30.00
# blue Circle - Area: 153.94, Perimeter: 43.98
# green Triangle - Area: 12.00, Perimeter: 16.00
# yellow Rectangle - Area: 64.00, Perimeter: 32.00
# purple Circle - Area: 28.27, Perimeter: 18.85
# orange Triangle - Area: 37.42, Perimeter: 28.00
# ─────────────────────────────────────────────
# Total Area: 345.63

# Filter shapes by minimum area
large_shapes = filter_by_area(shapes, 50)
print(f"\nShapes with area >= 50: {len(large_shapes)}")
for shape in large_shapes:
    print(f"  - {shape.color} {shape.__class__.__name__}: {shape.area():.2f}")
# Output:
# Shapes with area >= 50: 3
#   - blue Circle: 153.94
#   - yellow Rectangle: 64.00

# Sort shapes by area
sorted_shapes = sort_shapes_by_area(shapes)
print("\nShapes sorted by area:")
for shape in sorted_shapes:
    print(f"  {shape.area():.2f} - {shape.color} {shape.__class__.__name__}")
# Output:
# Shapes sorted by area:
#   12.00 - green Triangle
#   28.27 - purple Circle
#   37.42 - orange Triangle
#   50.00 - red Rectangle
#   64.00 - yellow Rectangle
#   153.94 - blue Circle