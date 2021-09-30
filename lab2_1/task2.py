import math


class Rational:
    __numerator = 1
    __denominator = 2

    def __init__(self, numerator, denominator):
        if isinstance(numerator, int) or isinstance(denominator, int):
            pass
        else:
            ind = True
            if denominator == 0:
            # print("Error. Division by zero...")
                ind = False
            elif numerator < 0 and denominator < 0:
                numerator *= -1
                denominator *= -1
            elif ind:
                x = math.gcd(numerator, denominator)
                self.__numerator = numerator//x
                self.__denominator = denominator//x

    def get(self):
        return str(self.__numerator)+'/' + str(self.__denominator)

    def get1(self):
        return self.__numerator/self.__denominator



A = Rational(-1, -2)
print(A.get())
print(A.get1())
