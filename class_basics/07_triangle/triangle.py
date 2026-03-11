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
        A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)))
        return [round(A, 2), round(B, 2), round(C, 2)]

    def get_angle_type(self):
        angles = self.get_angles()
        if any(abs(angle - 90) < 1e-5 for angle in angles):
            return "right"
        elif any(angle > 90 for angle in angles):
            return "obtuse"
        else:
            return "acute"

    def scale(self, factor):
        return Triangle(self.a * factor, self.b * factor, self.c * factor)

    def is_similar(self, other_triangle):
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([other_triangle.a, other_triangle.b, other_triangle.c])

        ratios = [sides1[i] / sides2[i] for i in range(3)]
        return abs(ratios[0] - ratios[1]) < 1e-5 and abs(ratios[1] - ratios[2]) < 1e-5


if __name__ == "__main__":
    triangle1 = Triangle(3, 4, 5)

    print(triangle1.calculate_perimeter())
    print(round(triangle1.calculate_area(), 2))
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
