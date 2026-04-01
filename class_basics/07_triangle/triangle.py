import math


class Triangle:
    def init(self, a, b, c):
        self.a, self.b, self.c = a, b, c

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle")

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def get_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "scalene"

    def get_angles(self):
        # Using law of cosines
        A = math.degrees(
            math.acos((self.b2 + self.c2 - self.a**2) / (2 * self.b * self.c))
        )
        B = math.degrees(
            math.acos((self.a2 + self.c2 - self.b**2) / (2 * self.a * self.c))
        )
        C = 180 - A - B
        return [round(A, 2), round(B, 2), round(C, 2)]

    def get_angle_type(self):
        angles = self.get_angles()
        if any(abs(angle - 90) < 1e-5 for angle in angles):
            return "right"
        elif all(angle < 90 for angle in angles):
            return "acute"
        else:
            return "obtuse"

    def scale(self, factor):
        return Triangle(self.a * factor, self.b * factor, self.c * factor)

    def is_similar(self, other):

        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([other.a, other.b, other.c])
        ratio = sides1[0] / sides2[0]
        return all(abs(s1 / s2 - ratio) < 1e-5 for s1, s2 in zip(sides1, sides2))
