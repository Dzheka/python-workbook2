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
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "scalene"

    def get_angles(self):
        a, b, c = self.a, self.b, self.c
        angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_c = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        return [round(angle_a, 2), round(angle_b, 2), round(angle_c, 2)]

    def get_angle_type(self):
        angles = self.get_angles()
        max_angle = max(angles)
        if math.isclose(max_angle, 90.0, abs_tol=0.01):
            return "right"
        elif max_angle > 90:
            return "obtuse"
        else:
            return "acute"

    def scale(self, factor):
        return Triangle(self.a * factor, self.b * factor, self.c * factor)

    def is_similar(self, other):
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([other.a, other.b, other.c])
        ratio = sides1[0] / sides2[0]
        return (math.isclose(sides1[1] / sides2[1], ratio, rel_tol=1e-9) and
                math.isclose(sides1[2] / sides2[2], ratio, rel_tol=1e-9))


if __name__ == "__main__":
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
