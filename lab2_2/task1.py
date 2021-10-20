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

    def __str__(self):
        pass


class Customer:
    """"A class describing the customer"""
    def __init__(self, surname, name, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(phone, str):
            raise TypeError("Wrong type of surname or name or phone")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("The phone number was entered incorrectly")
        if not surname.isalpha() or not name.isalpha():
            raise ValueError("Wrong value of surname or name")
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        """"A function that returns customer data"""
        return f'{self.surname} {self.name} {self.phone}\n'


class Order:
    """A class that describes an Order."""

    def __init__(self, customer, products):
        if not all([isinstance(product, Product) for product in products]):
            raise TypeError("Wrong type of product")
        if not isinstance(customer, Customer):
            raise TypeError
        self.customer = customer
        self.products = products

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
