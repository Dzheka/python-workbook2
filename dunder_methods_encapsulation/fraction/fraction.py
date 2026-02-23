from math import  gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        common = gcd(numerator, denominator)

        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        return False