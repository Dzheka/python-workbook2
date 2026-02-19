from math import  gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        pass


    def __add__(self, other):
        pass

    def __lt__(self, other) -> bool:
        return



a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)          # 1/2