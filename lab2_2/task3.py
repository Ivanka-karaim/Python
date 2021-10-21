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
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(num_book, int):
            raise TypeError("Wrong type of surname, name or book")
        if not all([isinstance(grade, int) for grade in grades]):
            raise TypeError("Wrong type of grades")
        if not surname.isalpha() or not name.isalpha() or num_book <= 0:
            raise ValueError("Wrong value of surname, name or book")
        if not all([0 < grade < 13 for grade in grades]):
            raise ValueError("Wrong value of grades")
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
        if not all([isinstance(student, Student) for student in students]):
            raise TypeError("Wrong type of students")
        if len(students) > 20:
            raise ValueError
        self.surnames_names = []
        if not all([self.check(student) for student in students]):
            raise ValueError

        self.students = students

    def add_student(self, student):
        """
        Adds a student to the group
        :param student: Student
            new student
        :return: None
        """
        if not isinstance(student, Student):
            raise TypeError("Wrong type of students")
        if not self.check(student):
            raise ValueError
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
        self.students.remove(student)

    def check(self, student):
        """
        Checks if there is a student with the same name and surname in the class
        :param student: Student
            whose student needs to be removed from the group
        :return: (True or False)
        """
        st = student.surname+student.name
        if st in self.surnames_names:
            return False
        else:
            self.surnames_names.append(st)
        return True

    def func(self):
        """
        Returns 5 students with the best grade point average
        :return: average_sc: str[]
            array of 5 students an array of 5 students with the best score
        """
        average_sc = []
        self.students = sorted(self.students)
        for i in range(5):
            average_sc.append(
                f'{self.students[i].name} {self.students[i].surname} {self.students[i].average_score()}\n')
        return "".join(average_sc)


st1 = Student("Karaim", "Ivanna", 343, [12, 12, 12])
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
print(Group.func())
