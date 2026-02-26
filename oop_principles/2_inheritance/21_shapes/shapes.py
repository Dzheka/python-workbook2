import math

class Shape:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def move(self, new_x, new_y):
        self.x = self.new_x
        self.y = self.new_y
        return Shape(self.x, self.y)

    def get_info(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(color,x,y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def resize(self, new_width, new_height):
        new_width.width = self.width
        new_height.height = self.height
        return new_width.width, new_height.height

class Circle(Shape):
    def __init__(self, color, x, y, width, height, radius):
        super().__init__(color, x, y, width, height)
        self.radius = radius

    def area(self):
        return 3.14 * ((self.radius)**2)
    
    def perimeter(self):
        return 2*3.14*self.radius
    
    def diameter(self):
        return 2*self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius.radius
        return self.radius

class Triangle(Shape):
    def __init__(self, color, x, y, width, height, radius, side_a, side_b, side_c):
        super().__init__(color, x, y, width, height, radius)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


rectangle = Rectangle("blue", 0, 0, 5, 3)
circle = Circle("red", 10, 10, 4)
triangle = Triangle("green", 5, 5, 3, 4, 5)

print("Rectangle:")
print(f"Color: {rectangle.color}")
print(f"Position: ({rectangle.x}, {rectangle.y})")
print(f"Dimensions: {rectangle.width} × {rectangle.height}")
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

# Demonstrate polymorphism
shapes = [rectangle, circle, triangle]
print("\nAll shapes areas:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.area():.2f}")

print("\nAll shapes perimeters:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.perimeter():.2f}")

# Move shapes
rectangle.move(2, 3)
print(f"\nRectangle moved to: ({rectangle.x}, {rectangle.y})")

# Resize rectangle
rectangle.resize(6, 6)
print(f"Rectangle resized to: {rectangle.width} × {rectangle.height}")
print(f"Is square now: {rectangle.is_square()}")