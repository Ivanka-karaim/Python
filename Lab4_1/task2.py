class Product:
    """
    Product

    Attributes
    __________
    name: str
        name product
    count: int
        count product
    price: int, float
        price product


    """
    def __init__(self, name, count, price):
        """
        :param name:
            name product
        :param count:
            count products
        :param price:
            price product
        """
        self.name = name
        self.count = count
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__count = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__price = value

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError
        self.count += other
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        self.count -= other
        return self

    def __str__(self):
        return f'\nName: {self.name} Count: {self.count} Price: {self.price}'


class Composition:
    """
    Composition

    Attributes
    __________
    products: list

    """

    def __init__(self, products):
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if not all([isinstance(product, Product) for product in products]):
            raise TypeError
        self.__products = products

    def __getitem__(self, item):
        """
        Finding the product by its name
        :param item:
            name product
        :return:
            product with this name
        """
        if not isinstance(item, str):
            raise TypeError
        for product in self.products:
            if product.name == item:
                return product
        raise ValueError

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError
        if not isinstance(value, int):
            raise TypeError
        if not any([product.name == key for product in self.products]):
            raise ValueError
        for index, product in enumerate(self.products):
            if product.name == key:
                self.products[index].count = value

    def __iadd__(self, other):
        """
        Adding products to the warehouse
        :param other:
            product
        :return:
        """
        if not isinstance(other, Product):
            raise TypeError
        self.products.append(other)
        return self

    def __isub__(self, other):
        """
        Removal of products from the warehouse
        :param other:
            product
        :return:
        """
        if not isinstance(other, Product):
            raise TypeError
        self.products.remove(other)

    def __str__(self):
        """
        Returns class elements
        """
        return "".join(list(map(str, list(self.products))))


A = Product("Iphone 12", 5, 800)
B = Product("Iphone 13", 10, 1000)
C = Product("Iphone XR", 4, 600)
X = Composition([A, B])
X += C
X["Iphone 12"] = 4
print(X["Iphone 13"])
print(X)
