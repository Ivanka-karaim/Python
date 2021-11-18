import json
from datetime import datetime
from const import *


class PizzaOfTheDay:
    """
    Basic pizza class
    Attributes
    __________
    day: str
        day week
    name: str
        Name pizza
    price: int, float
        price pizza
    ingredients: str
        ingredients pizza
    toppings:
        toppings pizza

    Methods
    _______
    prices():
        returns a whole pizza with extra ingredients
    add_ingredient():
        adds ingredients to pizza
    del_ingredient():
        removes ingredients from pizza
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        """
        :param day:
            day week
        :param pizza_of_a_day:
            pizza_of_the_day
        :param price:
            price pizza
        :param ingredients:
            ingredients pizza
        :param toppings:
            toppings pizza
        """
        self.day = day
        self.name = pizza_of_a_day
        self.price = price
        self.ingredients = ingredients
        if not toppings:
            self.toppings = []
        else:
            self.toppings = toppings

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value not in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}:
            raise ValueError
        self.__day = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < const:
            raise ValueError
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not all([isinstance(v, str) for v in value]):
            raise TypeError
        self.__ingredients = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        if not all([isinstance(v, str) for v in value]):
            raise TypeError
        with open("pizza_topings.json", 'r') as file:
            toppings = json.load(file)
        if not all([v in toppings for v in value]):
            raise ValueError
        self.__toppings = value

    def prices(self):
        """
        Price pizza
        :return: returns a whole pizza with extra ingredients
        """
        price = const
        with open("pizza_topings.json", 'r') as file:
            topp = json.load(file)
        for top in self.toppings:
            for t in topp:
                if top == t:
                    price += topp[t]
        return self.price + price

    def add_ingredient(self, value):
        """
        Adds ingredients to pizza
        :param value: new ingredients
        """
        if not all([isinstance(v, str) for v in value]):
            raise TypeError
        with open("pizza_topings.json", 'r') as file:
            toppings = json.load(file)
        if not all([v in toppings for v in value]):
            raise ValueError
        for v in value:
            self.toppings.append(v)

    def del_ingredient(self, value):
        """
        Removes ingredients from pizza
        :param value: del ingredients
        """
        if value in self.toppings:
            self.toppings.remove(value)
        elif value in self.ingredients:
            self.ingredients.remove(value)
        else:
            raise ValueError

    def __str__(self):
        if len(self.toppings):
            return f'{self.name} {self.ingredients} add ingredients: {self.toppings}\n'
        return f'{self.name} {self.ingredients}\n'


class PizzaMonday(PizzaOfTheDay):
    """
    Pizza Monday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Monday\n {super().__str__()}'


class PizzaTuesday(PizzaOfTheDay):
    """
    Pizza Tuesday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Tuesday\n {super().__str__()}'


class PizzaWednesday(PizzaOfTheDay):
    """
    Pizza Wednesday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Wednesday\n {super().__str__()}'


class PizzaThursday(PizzaOfTheDay):
    """
    Pizza Thursday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Thursday\n {super().__str__()}'


class PizzaFriday(PizzaOfTheDay):
    """
    Pizza Friday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Friday\n {super().__str__()}'


class PizzaSaturday(PizzaOfTheDay):
    """
    Pizza Saturday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Saturday\n {super().__str__()}'


class PizzaSunday(PizzaOfTheDay):
    """
    Pizza Sunday
    """
    def __init__(self, day, pizza_of_a_day, price, ingredients, toppings=None):
        super().__init__(day, pizza_of_a_day, price, ingredients, toppings)

    def __str__(self):
        return f'Day: Sunday\n {super().__str__()}'


class Order:
    """
    Class order
    Attributes
    __________
    pizzas: Pizza
        array of pizzas
    customer: str
        customer

    Methods
    _______
    add():
        adds new ingredients
    dell():
        removes ingredients
    all_pizzas():
        returns pizza
    write_date():
        writes data to json
    """
    def __init__(self, pizza, customer):
        """

        :param pizza:
            pizzas
        :param customer:
            customer
        """
        self.pizzas = pizza
        self.customer = customer

    @property
    def pizzas(self):
        return self.__pizzas

    @pizzas.setter
    def pizzas(self, value):
        if not all([isinstance(v, PizzaOfTheDay) for v in value]):
            raise TypeError
        self.__pizzas = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value: str):
        self.__customer = value

    @property
    def order_amount(self):
        price = const
        for pizza_day in self.pizzas:
            price = price + pizza_day.prices()
        return price

    def add(self, value, number=const_number):
        """
        Adds ingredients
        :param value:
            new ingredients
        :param number:
            pizza to which you need to add ingredients
        """
        if not isinstance(number, int):
            raise TypeError
        if number > len(self.pizzas) or number < const:
            raise ValueError
        self.pizzas[number - const_number].add_ingredient(value)

    def dell(self, value, number=const_number):
        """
        Removes ingredient
        :param value:
            ingredient
        :param number:
            pizza from which you need to remove the ingredients
        """
        if not isinstance(number, int):
            raise TypeError
        if number > len(self.pizzas) or number < const:
            raise ValueError
        self.pizzas[number - const_number].del_ingredient(value)

    def all_pizzas(self):
        """
        All pizzas
        :return: mas pizza
        """
        return "\n".join(map(str, self.pizzas))

    def write_date(self):
        """
        Writes data
        """
        with open("order.json", 'r') as file:
            orders = json.load(file)
            orders.append({"customer": self.customer, "day": self.pizzas[const].day,
                           "pizza": self.pizzas[const].name, "price": self.order_amount})
        with open("order.json", 'w') as file:
            json.dump(orders, file, indent=indent)

    def __str__(self):
        return f'Customer: {self.customer} \nPizza:\n{self.all_pizzas()}To pay: {self.order_amount}'


def pizza_of_the_day(day):
    """
    Returns the pizza of the day
    :param day:
        today
    :return: pizza of the day
    """
    pizza_dict = {

        "Monday": PizzaMonday,
        "Tuesday": PizzaTuesday,
        "Wednesday": PizzaWednesday,
        'Thursday': PizzaThursday,
        "Friday": PizzaFriday,
        "Saturday": PizzaSaturday,
        "Sunday": PizzaSunday
    }
    with open("pizza_of_the_day.json", 'r') as file:
        pizza_days = json.load(file)
    for pizza_day in pizza_days:
        if pizza_day["day"] == day:
            return pizza_dict[day](pizza_day["day"], pizza_day["name"], pizza_day["price"], pizza_day["ingredients"])
    print("Incorrect data")
    return None


pizza_today = []

try:
    name_customer = input("Enter name: ")
    num = int(input("How many pizzas do you want: "))
    for i in range(num):
        pizza_today.append(pizza_of_the_day(datetime.today().strftime('%A')))
    x = Order(pizza_today, name_customer)
    print(x.pizzas[0])
    while True:
        mod = int(input("1 - add ingredient\n2 - del_ingredient\n3 - exit\nEnter:"))
        if mod == mod1:
            mass = []
            ind_ingredients = int(input("Enter the number of ingredients you want to add: "))
            ind_pizza = int(input("Which pizza do you want to add ingredients to: "))
            print("Enter ingredients: ")
            for i in range(ind_ingredients):
                mass.append(str(input()))
            x.add(mass, ind_pizza)
        elif mod == mod2:
            ingredient = str(input("Enter the ingredient you want to remove: "))
            ind_pizza = int(input("Which pizza do you want to dell ingredients to: "))
            x.dell(ingredient, ind_pizza)
        elif mod == mod3:
            print(x)
            x.write_date()
            exit(1)
        else:
            print("Incorrectly data")
except (ValueError, FileNotFoundError):
    print("Error")
