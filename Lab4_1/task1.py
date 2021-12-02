import math


class Rational:
    """
    Rational

    Attributes
    __________
    numerator: int
        numerator rational number
    denominator: int
        denominator rational number
    """
    def __init__(self, numerator=1, denominator=1):
        """

        :param numerator:
            numerator rational number
        :param denominator:
            denominator rational number
        """
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        x = math.gcd(numerator, denominator)
        self.numerator = numerator // x
        self.denominator = denominator // x

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not value:
            raise ValueError
        self.__denominator = value

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    def get(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        return Rational((self.numerator * other.denominator + other.numerator * self.denominator),
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational((self.numerator * other.denominator - other.numerator * self.denominator),
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    def __lt__(self, other):
        if self.get() < other.get():
            return True
        return False

    def __le__(self, other):
        if self.get() <= other.get():
            return True
        return False

    def __gt__(self, other):
        if self.get() > other.get():
            return True
        return False

    def __ge__(self, other):
        if self.get() >= other.get():
            return True
        return False

    def __iadd__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        x = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // x
        self.denominator = self.denominator // x
        return self

    def __isub__(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        x = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // x
        self.denominator = self.denominator // x
        return self

    def __imul__(self, other):
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        x = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // x
        self.denominator = self.denominator // x
        return self

    def __itruediv__(self, other):
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        x = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // x
        self.denominator = self.denominator // x
        return self


a = Rational(-1, 2)
b = Rational(3, 4)
c = Rational(3, 4)
print(a+3)
a += 3
print(a)
print(c == b)

