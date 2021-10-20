class Rectangle:

    def __init__(self, length=1.0, width=1.0):
        self.__length = length
        self.__width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, value):
        if not isinstance(value, float):
            raise TypeError("Wrong type!")
        if not 0 < value < 20:
            raise ValueError("Wrong value!")
        self.__length = value

    @width.setter
    def width(self, value):
        if not isinstance(value, float):
            raise TypeError("Wrong type!")
        if not 0 < value < 20:
            raise ValueError("Wrong value!")
        self.__width = value


rectangle1 = Rectangle()
rectangle1.width = 2.0
rectangle1.length = 3.0
print("Area: ", rectangle1.area())
