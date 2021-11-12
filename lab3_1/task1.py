import json
from const import *
from datetime import datetime, timedelta


class BaseTicket:
    """
    Base Ticket
    Attributes
    __________
    num_ticket: str
        id ticket
    name: str
        name event
    price: int, float
        price ticket
    seat: int
        seat event
    date: str
        date event

    Methods
    _______
    dict():
        returns the created dictionary with ticket data
    """
    def __init__(self, num_ticket, name, price, seat, date):
        """
        :param num_ticket:
            id ticket
        :param name:
            name event
        :param price:
            price ticket
        :param seat:
            seat for the event
        :param date:
            date event
        """
        self.num_ticket = num_ticket
        self.name = name
        self.price = price
        self.seat = seat
        self.date = date

    @property
    def num_ticket(self):
        return self.__num_ticket

    @num_ticket.setter
    def num_ticket(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.isdigit():
            raise ValueError
        self.__num_ticket = value

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
        if value < 0:
            raise ValueError
        self.__price = value

    @property
    def seat(self):
        return self.__seat

    @seat.setter
    def seat(self, value):
        if not isinstance(value, int):
            raise TypeError
        self.__seat = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__date = value

    def __str__(self):
        return f'Ticket\nInvention:{self.name} Price: {self.price} Seat: {self.seat}\n' \
               f'Date: {self.date} Code: {self.num_ticket}'

    def dict(self):
        """
        Dict base ticket
        :return: dict describing the base ticket
        """
        return {"id": self.num_ticket, "name": self.name, "price": self.price, "seat": self.seat, "date": self.date,
                "type": "BaseTicket"}


class AdvanceTicket(BaseTicket):
    """
    The class describes advance ticket
    """
    def __init__(self, num_ticket, name, price, seat, date):
        super().__init__(num_ticket, name, price*const_advance, seat, date)

    def __str__(self):
        return f'Advance ticket\nInvention:{self.name} Price: {self.price} Seat: {self.seat}\n' \
               f'Date: {self.date} Code: {self.num_ticket}'

    def dict(self):
        """
        Dict advance ticket
        :return: dict describing the advance ticket
        """
        return {"id": self.num_ticket, "name": self.name, "price": self.price, "seat": self.seat, "date": self.date,
                "type": "AdvanceTicket"}


class LateTicket(BaseTicket):
    """
    The class describes late ticket
    """
    def __init__(self, num_ticket, name, price, seat, date):
        super().__init__(num_ticket, name, price*const_late, seat, date)

    def __str__(self):
        return f'Late ticket\nInvention:{self.name} Price: {self.price} Seat: {self.seat}\n' \
               f'Date: {self.date} Code: {self.num_ticket}'

    def dict(self):
        """
        Dict late ticket
        :return: dict describing the late ticket
        """
        return {"id": self.num_ticket, "name": self.name, "price": self.price, "seat": self.seat, "date": self.date,
                "type": "LateTicket"}


class StudentTicket(BaseTicket):
    """
    The class describes student ticket
    """
    def __init__(self, num_ticket, name, price, seat, date):
        super().__init__(num_ticket, name, price*const_student, seat, date)

    def __str__(self):
        return f'Student ticket\nInvention:{self.name} Price: {self.price} Seat: {self.seat}\n' \
               f'Date: {self.date} Code: {self.num_ticket}'

    def dict(self):
        """
        Dict student ticket
        :return: dict describing the student ticket
        """
        return {"id": self.num_ticket, "name": self.name, "price": self.price, "seat": self.seat, "date": self.date,
                "type": "StudentTicket"}


def buy_ticket(code, seat, ind=None):
    """
    The function with which to buy a ticket
    :param code:
        code event
    :param seat:
        seat for the event
    :param ind:
        student indicator
    :return: the number of the purchased ticket
    """
    if len(str(code)) != const_len_code:
        print("The event code was entered incorrectly")
        return None
    with open("ticket_already_bought.json", 'r') as read_file:
        purchased_tickets = json.load(read_file)
    for purchased_ticket in purchased_tickets:
        if purchased_ticket["id"] == str(code) + str(seat):
            print("The place at the back event is taken")
            return None
    with open("events.json", 'r') as file:
        events = json.load(file)
    data = None
    for event in events:
        if event["code"] == str(code):
            data = event
    if not data:
        print("The event code was entered incorrectly")
        return None
    if ind:
        ticket = StudentTicket(str(code)+str(seat), data["name"], data["price"], seat, data["date"])
        purchased_tickets.append(ticket.dict())
    else:
        date = datetime.strptime(data["date"], "%y-%m-%d")
        time = date - datetime.today()
        if time > timedelta(days=const_day1):
            ticket = AdvanceTicket(str(code)+str(seat), data["name"], data["price"], seat, data["date"])
            purchased_tickets.append(ticket.dict())
        elif time < timedelta(days=const_day2):
            ticket = LateTicket(str(code)+str(seat), data["name"], data["price"], seat, data["date"])
            purchased_tickets.append(ticket.dict())
        elif time < timedelta(days=const_day3):
            print("This event has already taken place")
            return None
        else:
            ticket = BaseTicket(str(code)+str(seat), data["name"], data["price"], seat, data["date"])
            purchased_tickets.append(ticket.dict())
    with open("ticket_already_bought.json", 'w') as write_file:
        json.dump(purchased_tickets, write_file, indent=indent)
    return str(code)+str(seat)


def get_ticket(number):
    """
    The function that holds the ticket for it id
    :param number:
        id ticket
    :return: ticket
    """
    with open("ticket_already_bought.json", 'r') as file:
        tickets = json.load(file)
    gets = None
    for ticket in tickets:
        if ticket["id"] == number:
            gets = ticket

    if not gets:
        print("No such ticket found")
        return None
    if gets["type"] == "BaseTicket":
        return BaseTicket(gets["id"], gets["name"], gets["price"], gets["seat"], gets["date"])
    if gets["type"] == "LateTicket":
        return LateTicket(gets["id"], gets["name"], gets["price"]/const_late, gets["seat"], gets["date"])
    if gets["type"] == "StudentTicket":
        return StudentTicket(gets["id"], gets["name"], gets["price"]/const_student, gets["seat"], gets["date"])
    if gets["type"] == "AdvanceTicket":
        return AdvanceTicket(gets["id"], gets["name"], gets["price"]/const_advance, gets["seat"], gets["date"])


def display_all_events():
    with open("events.json", 'r') as file:
        events = json.load(file)
    for event in events:
        print("Code: " + event["code"]+" Name event: " + event["name"] +
              " Price: " + str(event["price"]) + " Date: " + event["date"])


display_all_events()
try:
    print("1 - Buy a ticket\n2 - Get a ticket\n")
    mod = int(input("Enter: "))
    if mod == 1:
        code = int(input("Select an event(enter the event code): "))
        seat = int(input("Enter seat: "))
        student = int(input("Are you a student?( 1- yes, 0- no): "))
        tick = buy_ticket(code, seat, student)
        if tick:
            print("Your id: " + tick)
    elif mod == 2:
        idd = int(input("Enter id ticket: "))
        my_ticket = get_ticket(str(idd))
        if my_ticket:
            print(my_ticket)
    else:
        print("Incorrectly data")
except (ValueError, FileNotFoundError):
    print("Error ")


