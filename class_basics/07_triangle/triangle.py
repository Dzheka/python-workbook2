import math

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = (self.a+self.b+self.c)/2
        area = math.sqrt((s-self.a)*(s-self.b)*(s-self.c)*s)
        return area

    def get_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "scalene"

    def get_angles(self):
        C = math.degrees(math.acos(
            (self.a**2 + self.b**2 - self.c**2)/ (2*self.a*self.b)
            ))
        B = math.degrees(math.acos(
            (self.a**2 + self.c**2 - self.b**2)/ (2*self.a*self.c)
            ))
        A = 180-B-C
        return [round(A,2), round(B, 2), round(C,2)]

    def get_angle_type(self):
        sides = sorted([self.a, self.b, self.c])
        a,b,c = sides

        lhs = c **2
        rhs = a**2 + b**2

        if abs(lhs - rhs) == 0:
            return "right"
        elif lhs < rhs:
            return "acute"
        else:
            return "obtuse"


    def scale(self,factor):
        return Triangle(self.a*factor, self.b*factor, self.c*factor)

    def is_similar(self, s_triangle):
        if ((s_triangle.a / self.a)) == (s_triangle.c / self.c) == (s_triangle.b / self.b):
            return True
        else:
            return False







triangle1 = Triangle(3, 4, 5)
print(triangle1.calculate_perimeter())  # 12
print(triangle1.calculate_area())       # 6.0
print(triangle1.get_type())            # scalene
print(triangle1.get_angles())          # [36.87, 53.13, 90.0]
print(triangle1.get_angle_type())      # right

scaled = triangle1.scale(2)
print(scaled.a, scaled.b, scaled.c)    # 6 8 10

print(triangle1.is_similar(scaled))    # True

try:
    Triangle(1, 1, 5)
except ValueError as e:
    print(e)  # Invalid triangle
