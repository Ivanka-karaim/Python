import math


class Rational:
    __numerator = 1
    __denominator = 2

    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("Error. Division by zero...")
        elif not isinstance(numerator, int) or not isinstance(denominator, int):
            print("Error. Incorrect data entered...")
        elif numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        else:
            x = math.gcd(numerator, denominator)
            self.__numerator = numerator/x
            self.__denominator = denominator/x

    def get(self):
        print(int(self.__numerator), '/', int(self.__denominator))

    def get1(self):
        print(self.__numerator/self.__denominator)


num = input("Enter numerator: ")
den = input("Enter denominator: ")
try:
    num = int(num)
    den = int(den)
except:
    print("Error. Variables must be of type int")
    exit(1)
A = Rational(num, den)
A.get()
A.get1()
