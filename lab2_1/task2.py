import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Wrong type!")
        if not denominator:
            raise ValueError("Wrong value!")
        numerator = abs(numerator)
        denominator = abs(denominator)
        x = math.gcd(numerator, denominator)
        self.__numerator = numerator // x
        self.__denominator = denominator // x

    def get(self):
        return f'{self.__numerator}/{self.__denominator}'

    def get1(self):
        return self.__numerator/self.__denominator


A = Rational(-2, -8)
print(A.get())
print(A.get1())

