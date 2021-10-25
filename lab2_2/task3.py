class Student:
    """"
    A class describing a student

    Attributes
    __________
    name: str
        name student
    surname: str
        surname student
    num_book: int
        num_book student
    grades: int[]
        grades student

    Methods
    _______
    average_score():
        returns the average value of a student
    """

    def __init__(self, surname, name, num_book, grades):
        """"
        Sets all the necessary attributes for the student
        :param:name: str
            name student
        :param:surname: str
            surname student
        :param:num_book: int
            num_book student
        :param:grades: int[]
            grades student
        """
        self.name = name
        self.surname = surname
        self.num_book = num_book
        self.grades = grades

    def average_score(self):
        """"
        A function that returns the average value of a student
        :return: value
            returns average value grades of a student
        """
        return sum(self.grades)/len(self.grades)

    def __lt__(self, other):
        """
        Used to sort a list that includes instances of a class
        """
        return self.average_score() > other.average_score()

    def __str__(self):
        """
        Returns class elements
        """
        return f'{self.name} {self.surname} {self.average_score()}\n'

    def add_grade(self, grade):
        """
        Add new grade
        :param grade:
            new grade
        :return:
        """
        if not isinstance(grade, int):
            raise TypeError("Wrong type!")
        if not 0 < grade < 13:
            raise ValueError("Wrong value!")
        self.grades.append(grade)

    @property
    def name(self):
        """
        Getter name
        :return:
        """
        return self.__name

    @property
    def surname(self):
        """
        Getter surname
        :return:
        """
        return self.__surname

    @property
    def grades(self):
        """
        Getter grades
        :return:
        """
        return self.__grades

    @property
    def num_book(self):
        """
        Getter num_book
        :return:
        """
        return self.__num_book

    @name.setter
    def name(self, value):
        """
        Setter name
        :param value:
            New name
        :return:
        """
        if not isinstance(value, str):
            raise TypeError("Wrong type!")
        if not value.isalpha():
            raise ValueError("Wrong value of name")
        self.__name = value

    @surname.setter
    def surname(self, value):
        """
        Setter surname
        :param value:
            new surname
        :return:
        """
        if not isinstance(value, str):
            raise TypeError("Wrong type!")
        if not value.isalpha():
            raise ValueError("Wrong value of surname")
        self.__surname = value

    @grades.setter
    def grades(self, value):
        """
        Setter grades
        :param value:
            new grades
        :return:
        """
        if not all([isinstance(grade, int) for grade in value]):
            raise TypeError("Wrong type of grades")
        if not all([0 < grade < 13 for grade in value]):
            raise ValueError("Wrong value of grades")
        self.__grades = value

    @num_book.setter
    def num_book(self, value):
        """
        Setter num_book
        :param value:
            new num_book
        :return:
        """
        if not(isinstance(value, int)):
            raise TypeError("Wrong type of num_book")
        if not value > 0:
            raise ValueError("Wrong value of num_book")
        self.__num_book = value


class Group:
    """"
    A class describing a group of students
    Attributes
    _________
    surnames_names:str[]
        name and surname of all students
    students: list
        sequence of data about each student group
    Methods
    _______
    add_students(student):
        adds a student to the group
    del_students(students):
        removes the student from the group
    check(student):
        checks if there is a student with the same name and surname in the class
    func():
        returns 5 students with the best grade point average
    """

    def __init__(self, students):
        """
        Sets all the necessary attributes for the student
        :param:student: list
            sequence of data about each student group
        """
        self.students = students

    @property
    def students(self):
        """
        Getter students
        :return:
        """
        return self.__students

    @students.setter
    def students(self, students):
        """
        Setter students
        :param students:
            new students
        :return:
        """
        if not all([isinstance(student, Student) for student in students]):
            raise TypeError("Wrong type of students")
        if len(students) > 20:
            raise ValueError("A lot of students")
        for i in range(len(students)):
            if any(students[i].surname == st.surname for st in students[i+1:])\
                    and any(students[i].name == st.name for st in students[i+1:]):
                raise ValueError("There are students with the same name and surname")
        self.__students = students

    def add_student(self, student):
        """
        Adds a student to the group
        :param student: Student
            new student
        :return: None
        """
        if not isinstance(student, Student):
            raise TypeError("Wrong type of students")
        if len(self.students) == 20:
            raise ValueError("A lot of students")
        for st in self.students:
            if student.name == st.name and student.surname == student.surname:
                raise ValueError("There are students with the same name and surname")
        self.students.append(student)

    def del_student(self, student):
        """
        Removes the student from the group
        :param student: Student
            whose student needs to be removed from the group
        :return: None
        """
        if not isinstance(student, Student):
            raise TypeError("Wrong type of students")
        if student not in self.students:
            raise ValueError
        self.students.remove(student)

    @property
    def top_5(self):
        """
        Returns 5 students with the best grade point average
        :return: students
        """
        self.students = sorted(self.__students)
        return self.students[:5]

    def __str__(self):
        """
        Returns class elements
        """
        return "".join(list(map(str, list(self.top_5))))


st1 = Student("Karaim", "Ivanna", 343, [12, 12, 12])
st1.add_grade(11)
st2 = Student("Lys", "Viktoria", 564, [12, 9, 4])
st3 = Student("Krupko", "Diana", 345, [10, 12, 12])
st4 = Student("Omelchenko", "Iryna", 305, [10, 12, 12])
st5 = Student("Malykhina", "Ira", 635, [5, 12, 11])
st6 = Student("Doronyk", "Vlad", 325, [4, 12, 11])
st7 = Student("Datsiuk", "Lilya", 3235, [4, 8, 11])
st8 = Student("Shevchenko", "Vlad", 235, [9, 12, 11])
st9 = Student("Levchuk", "Diana", 35, [10, 12, 11])
st10 = Student("Valla", "Marta", 56, [3, 8, 6])
st11 = Student("Datsiuk", "Lilya", 32355, [5, 8, 11])
Group = Group([st1, st2, st3, st4, st5, st6, st7, st8, st9])
Group.add_student(st10)
print(Group)
