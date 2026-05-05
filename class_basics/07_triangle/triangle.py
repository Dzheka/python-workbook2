import math

class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle")
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        return "scalene"

    def get_angles(self):
        A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)))
        return [round(A, 2), round(B, 2), round(C, 2)]

    def get_angle_type(self):
        angles = self.get_angles()
        if any(abs(angle - 90) < 1e-9 for angle in angles):
            return "right"
        if any(angle > 90 for angle in angles):
            return "obtuse"
        return "acute"

    def scale(self, factor):
        return Triangle(self.a * factor, self.b * factor, self.c * factor)

    def is_similar(self, other_triangle):
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([other_triangle.a, other_triangle.b, other_triangle.c])
        ratios = [sides1[i] / sides2[i] for i in range(3)]
        return abs(ratios[0] - ratios[1]) < 1e-9 and abs(ratios[1] - ratios[2]) < 1e-9
