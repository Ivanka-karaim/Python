class Product:
    """"A class describing the product"""
    def __init__(self, description, dimensions, price):
        if not isinstance(description, str) or not isinstance(dimensions, int) or not isinstance(price, (float, int)):
            raise TypeError("Wrong type of description, dimensions or prices")
        if dimensions <= 0 or price <= 0:
            raise ValueError("Incorrectly entered dimensions or price")
        self.description = description
        self.dimensions = dimensions
        self.price = price


class Customer:
    """"A class describing the customer"""
    def __init__(self, surname, name, phone):
        if not phone.isdigit():
            raise ValueError("The phone number was entered incorrectly")
        if not isinstance(surname, str) or not isinstance(name, str):
            raise TypeError("Wrong type of surname or name")
        if not surname.isalpha() or not name.isalpha():
            raise ValueError("Wrong value of surname or name")
        self.surname = surname
        self.name = name
        self.phone = phone

    def get(self):
        """"A function that returns customer data"""
        return f'{self.surname} {self.name} {self.phone}\n'


class Order:
    """A class that describes an Order."""
    prices = 0
    Products = []

    def __init__(self, customer, *products):
        self.Customer = customer
        self.Products += products

    def add_product(self, new_product):
        """A function that adds the product to the order"""
        self.Products.append(new_product)

    def sum_order(self):
        """"A function that calculates the total cost of an order"""
        for product in self.Products:
            self.prices += product.price
        return self.prices

    def get(self):
        """"A function that returns data about the customer and the total cost of the order"""
        return f'Customer: {self.Customer.get()}The total amount of the order: {self.sum_order()}'


Customer1 = Customer("Karaim", "Ivanna", "066723685")
T_shirt = Product("White t-shirt", 42, 200)
Hoodie = Product("Hoodie with a pattern on the back", 46, 500)
Jeans = Product("Blue jeans with a lock", 38, 520)
Jacket = Product("Leather black jacket on the lock", 44, 800)
x = Order(Customer1, T_shirt)
x.add_product(Jeans)
x.add_product(Hoodie)
print(x.get())
