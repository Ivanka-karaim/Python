class Rectangle:
    length = 1
    width = 1

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def setter(self, length, width):
        try:
            length = float(length)
            width = float(width)
        except:
            print("Error. Variables must be of type float")
            return 0
        if not 0 < length < 20:
            print("Error. The length is entered incorrectly...")
        else:
            self.length = length

        if not 0 < width < 20:
            print("Error. The width is entered incorrectly...")
        else:
            self.width = width

    def getter(self):
        return self.length, self.width


rectangle1 = Rectangle()
print("Data: ", rectangle1.getter())
print("Area: ", rectangle1.area())
len = input("Enter length: ")
widt = input("Enter width: ")
rectangle1.setter(len, widt)
print("Data: ", rectangle1.getter())
print("Perimeter: ", rectangle1.perimeter())
