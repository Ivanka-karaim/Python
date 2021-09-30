import math


class Rational:
    __numerator = 1
    __denominator = 1

    def __init__(self, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int):
            ind = True
            if denominator == 0:
                ind = False
            elif numerator <= 0 and denominator < 0:
                numerator *= -1
                denominator *= -1
            if ind:
                x = math.gcd(numerator, denominator)
                self.__numerator = numerator//x
                self.__denominator = denominator//x

    def get(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def get1(self):
        return self.__numerator/self.__denominator


A = Rational(-2, -8)
print(A.get())
print(A.get1())
