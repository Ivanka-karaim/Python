class Rectangle:

    def __init__(self):
        self.length = 1.0
        self.width = 1.0

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def setter(self, length, width):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("Wrong type!")
        if not 0 < length < 20 or not 0 < width < 20:
            raise ValueError("Wrong value!")
        self.length = length
        self.width = width

    def getter(self):
        return self.length, self.width


rectangle1 = Rectangle()
print("Data: ", rectangle1.getter())
print("Area: ", rectangle1.area())
rectangle1.setter(2.0, 3)
print("Data: ", rectangle1.getter())
print("Perimeter: ", rectangle1.perimeter())
