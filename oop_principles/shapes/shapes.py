import  math

class Shape:
    def __init__(self, color: str, x: float, y: float):
        self.color = color
        self.x = x
        self.y = y

    def area(self):
        pass
    def perimeter(self):
        pass
    def move(self,new_x, new_y):
        pass
    def get_info(self):
        pass

class Rectangle(Shape):
    def __init__(self, color,x,y,width,height):
        super().__init__(color, x, y)
        self.width =width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width * self.height)
    def is_square(self):
        return
    def resize(self,new_width,new_height):
        return new_width,new_height


rectangle = Rectangle("blue", 0, 0, 5, 3)
# Display basic information
print("Rectangle:")
print(f"Color: {rectangle.color}")
print(f"Position: ({rectangle.x}, {rectangle.y})")
print(f"Dimensions: {rectangle.width} × {rectangle.height}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Is square: {rectangle.is_square()}")