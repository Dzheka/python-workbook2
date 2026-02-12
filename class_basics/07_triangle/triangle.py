import math


class Triangle:
    def __init__(self, a, b, c):
        # Ensure sides are positive numbers
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be positive numbers.")

        # Triangle inequality check
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle: violates triangle inequality theorem.")

        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        sum(self.a+self.b+self.c)

    def calculate_area(self):
        s = (self.a+self.b+self.c) / 2
        area = math.sqrt(s(s-self.a)(s-self.b)(s-self.c))
        return area

    def get_type(self):
        if self.a == self.b == self.c:
            return f"equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "scalene"

    def get_angles(self):
        a = math.degrees(self.a)
        b = math.degrees(self.b)
        c = math.degrees(self.c)

        return  a,b,c

    def get_angle_type(self):
        pass
