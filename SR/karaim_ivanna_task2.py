import datetime
moon = {1: "січня", 2: "лютого", 3: "березня", 4: "квітня", 5: "травня", 6: "червня",
        7: "липня", 8: "серпня", 9: "вересня", 10: "жовтня", 11: "листопада", 12: "грудня"}


class Date:
    def __init__(self, year, month, day):
        try:
            new_date = datetime.datetime(year, month, day)
        except ValueError:
            raise ValueError
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @year.setter
    def year(self, value):
        try:
            new_date = datetime.datetime(value, self.month, self.day)
        except ValueError:
            raise ValueError("Such a date does not exist")
        self.__year = value

    @month.setter
    def month(self, value):
        try:
            new_date = datetime.datetime(self.year, value, self.day)
        except ValueError:
            raise ValueError("Such a date does not exist")
        self.__month = value

    @day.setter
    def day(self, value):
        try:
            new_date = datetime.datetime(self.year, self.month, value)
        except ValueError:
            raise ValueError("Such a date does not exist")
        self.__month = value

    def new_date(self, year, month, day):
        try:
            new_date = datetime.datetime(year, month, day)
        except ValueError:
            raise ValueError("Such a date does not exist")
        self.__year = year
        self.__month = month
        self.__day = day

    def get1(self):
        ind1 = ''
        ind2 = ''
        if self.day < 10:
            ind1 = '0'
        if self.month < 10:
            ind2 = '0'
        return f'{ind1}{self.day}.{ind2}{self.month}.{self.year}'

    def get2(self):
        return f'{self.day} {moon[self.month]} {self.year} року'


d = Date(2021, 10, 28)
print(d.get1())
d.new_date(2020, 2, 29)
print(d.get1())
print(d.get2())
d.year = 2016
print(d.get2())
