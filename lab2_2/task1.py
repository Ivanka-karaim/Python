class Product:
    """"A class describing the product"""
    def __init__(self, description, dimensions, price):

        self.description = description
        self.dimensions = dimensions
        self.price = price

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @property
    def price(self):
        return self.__price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Wrong type of description")
        self.__description = description

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, int):
            raise TypeError("Wrong type of dimensions")
        if dimensions <= 0:
            raise ValueError("Incorrectly entered dimensions")
        self.__dimensions = dimensions

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Wrong type of prices")
        if price <= 0:
            raise ValueError("Incorrectly entered price")
        self.__price = price

    def __str__(self):
        pass


class Customer:
    """"A class describing the customer"""
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    @name.setter
    def name(self,name):
        if not isinstance(name, str):
            raise TypeError("Wrong type of name ")
        if not name.isalpha():
            raise ValueError("Wrong value of name")
        self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type of surname ")
        if not surname.isalpha():
            raise ValueError("Wrong value of surname")
        self.__surname = surname

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone ")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("The phone number was entered incorrectly")
        self.__phone = phone

    def __str__(self):
        """"A function that returns customer data"""
        return f'{self.surname} {self.name} {self.phone}\n'


class Order:
    """A class that describes an Order."""

    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    @property
    def customer(self):
        return self.__customer

    @property
    def products(self):
        return self.__products

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Wrong type of customer")
        self.__customer = customer

    @products.setter
    def products(self, products):
        if not all([isinstance(product, Product) for product in products]):
            raise TypeError("Wrong type of product")
        self.__products = products

    def add_product(self, new_product):
        if not isinstance(new_product, Product):
            raise TypeError
        """A function that adds the product to the order"""
        self.products.append(new_product)

    def del_product(self, name_product):
        if not isinstance(name_product, Product):
            raise TypeError
        self.products.remove(name_product)

    def sum_order(self):
        """"A function that calculates the total cost of an order"""
        prices = 0
        for product in self.products:
            prices += product.price
        return prices

    def __str__(self):
        """"A function that returns data about the customer and the total cost of the order"""
        return f'Customer: {self.customer}The total amount of the order: {self.sum_order()}'


Customer1 = Customer("Karaim", "Ivanna", "0667236485")
T_shirt = Product("White t-shirt", 42, 200)
Hoodie = Product("Hoodie with a pattern on the back", 46, 500)
Jeans = Product("Blue jeans with a lock", 38, 520)
Jacket = Product("Leather black jacket on the lock", 44, 800)
x = Order(Customer1, [T_shirt])
x.add_product(Jeans)
x.add_product(Hoodie)
x.del_product(Jeans)
print(x)
