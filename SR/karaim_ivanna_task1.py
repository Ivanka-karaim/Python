class Book:

    def __init__(self, author, name, publish, year, number):

        self.author = author
        self.name = name
        self.publish = publish
        self.year = year
        self.number = number

    def __str__(self):
        return f'{self.author} {self.name} {self.year}\n'

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def number(self):
        return self.__number

    @property
    def publish(self):
        return self.__publish

    @property
    def year(self):
        return self.__year

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type!")
        self.__name = value

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type!")
        self.__author = value

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong type of number")
        if not value > 0:
            raise ValueError("Wrong value of number")
        self.__number = value

    @publish.setter
    def publish(self, value):
        if not(isinstance(value, str)):
            raise TypeError("Wrong type of publish")
        self.__publish = value

    @year.setter
    def year(self, value):
        if not(isinstance(value, int)):
            raise TypeError("Wrong type of year")
        if not value > 0:
            raise ValueError("Wrong value of year")
        self.__year = value


class Library:

    def __init__(self, books):

        self.books = books

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, books):
        if not all([isinstance(book, Book) for book in books]):
            raise TypeError("Wrong type of book")
        self.__books = books

    def add_books(self, book):
        if not isinstance(book, Book):
            raise TypeError("Wrong type of book")
        self.books.append(book)

    def del_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Wrong type of book")
        if book not in self.books:
            raise ValueError
        self.books.remove(book)

    def find(self, value):
        find_books = []
        for book in self.books:
            if book.author == value and book.year > 2010:
                find_books.append(book)
        if not find_books:
            return 'Немає такого автора чи книг'
        return find_books

    def find_book(self, value):
        return "".join(list(map(str, list(self.find(value)))))


b1 = Book("Тарас Шевченко", "Кобзар", "Рукопис", 1860, 500)
b2 = Book("Ліна Костенко", "Маруся Чурай","А-ба-ба-га-ла-ма-га", 1979, 224)
b3 = Book("Ліна Костенко", "Річка Геракліта", "Либідь", 2011, 400)
b4 = Book("Ліна Костенко", "Мадонна перехресть", "Либідь", 2011, 112)

Library = Library([b1, b2, b3])
Library.add_books(b4)
print(Library.find_book("Ліна Костенко"))
