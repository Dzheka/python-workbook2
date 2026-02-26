from math import gcd
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator



    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)

    def __lt__(self, other):
        if self.numerator * other.denominator < other.numerator * self.denominator:
            return True
        return False


a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)          # 1/2
print(a == c)     # True  (1/2 == 2/4)
print(a < b)      # False (1/2 > 1/3)

d = a + b
print(d)          # 5/6