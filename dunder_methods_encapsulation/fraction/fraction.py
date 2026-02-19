from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        g = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator


a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)
print(a == c)
print(a < b)

d = a + b
print(d)
