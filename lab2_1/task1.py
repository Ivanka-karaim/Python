class Rectangle:

    def __init__(self):
        self.length = 1
        self.width = 1

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def setter(self, length, width):
        try:
            length = float(length)
        except:
            pass
        try:
            width = float(width)
        except:
            pass
        if isinstance(length, float) and 0 < length < 20:
            self.length = length

        if isinstance(width, float) and 0 < width < 20:
            self.width = width

    def getter(self):
        return self.length, self.width


rectangle1 = Rectangle()
print("Data: ", rectangle1.getter())
print("Area: ", rectangle1.area())
length_my = input("Enter length: ")
width_my = input("Enter width: ")
rectangle1.setter(length_my, width_my)
print("Data: ", rectangle1.getter())
print("Perimeter: ", rectangle1.perimeter())
