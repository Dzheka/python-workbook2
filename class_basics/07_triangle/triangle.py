import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        if a+b<=c or a+c<=b or b+c<=a:
            raise ValueError("Invalid triangle")
    
    def calculate_perimeter(self):
        return self.a + self.b + self.c
    
    def calculate_area(self):
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area
    
    def get_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "scalene"
        
    def get_angles(self):
        a = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2*self.b*self.c)))
        b = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2*self.a*self.c)))
        c = 180-a-b
        return round(a, 2), round(b, 2), round(c, 2)
    
    def get_angle_type(self):
        a = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2*self.b*self.c)))
        b = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2*self.a*self.c)))
        c = 180-a-b

        if a < 90 and b < 90 and c < 90:
            return "acute"
        elif a == 90 or b == 90 or c == 90:
            return "right"
        else:
            return "obtuse"

    def scale(self, factor):
        return Triangle(self.a*factor, self.b*factor, self.c*factor)
    
    def is_similar(self, other_triangle):
        ratios = [
            self.a / other_triangle.a,
            self.b / other_triangle.b,
            self.c / other_triangle.c,
        ]
        return math.isclose(ratios[0], ratios[1]) and math.isclose(ratios[1], ratios[2])

triangle1 = Triangle(3, 4, 5)
print(triangle1.calculate_perimeter())
print(triangle1.calculate_area())
print(triangle1.get_type())
print(triangle1.get_angles())
print(triangle1.get_angle_type())

scaled = triangle1.scale(2)
print(scaled.a, scaled.b, scaled.c)

print(triangle1.is_similar(scaled))

try:
    Triangle(1, 1, 5)
except ValueError as e:
    print(e)
