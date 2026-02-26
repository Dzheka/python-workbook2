from math import gcd
class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Keep sign in numerator only
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify fraction
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        gcd(self.numerator,self.denominator,other.numerator,other.denominator)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)

    def __lt__(self, other):
        if self.numerator * other.denominator < other.numerator * self.denominator:
            return True
        return False

    def __repr__(self):
            return f"Fraction({self.numerator}/{self.denominator})"


a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)          # 1/2
print(a == c)     # True  (1/2 == 2/4)
print(a < b)      # False (1/2 > 1/3)

d = a + b
print(d)          # 5/6