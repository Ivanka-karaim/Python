class Student:
    """"A class describing a student"""
    surnames = []
    names = []

    def __new__(cls, name, surname, book, *grades):
        if surname in cls.surnames and name == cls.names[cls.surnames.index(surname)]:
            return None
        return super(Student, cls).__new__(cls)

    def __init__(self, name, surname, book, *grades):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(book, int):
            raise TypeError("Wrong type of surname, name or book")
        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError("Wrong type of grades")
        if not surname.isalpha() or not name.isalpha() or book <= 0:
            raise ValueError("Wrong value of surname, name or book")
        for grade in grades:
            if grade <= 0:
                raise ValueError("Wrong value of grades")
        self.name = name
        self.surname = surname
        self.book = book
        self.grades = grades
        self.average = 0
        self.average_score()
        Student.names.append(name)
        Student.surnames.append(surname)

    def average_score(self):
        """"A function that calculates the average value of a student"""
        self.average = sum(self.grades)/len(self.grades)


class Group:
    """"A class describing a group of students"""
    average_sc = []

    def __init__(self, students):
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("Wrong type of students")
        self.students = students

    def func(self):
        """"A function that finds the 5 students with the best score"""
        average_scores = []
        for st in self.students:
            average_scores.append(st.average)
        average_scores.sort()
        average_scores.reverse()
        i = 0
        while i < 5:
            for st in self.students:
                if average_scores[i] == st.average:
                    self.average_sc.append(f'{st.name} {st.surname} {st.average}\n')
                    i += 1

    def get(self):
        """"A function that returns the 5 students with the best score"""
        return ''.join(self.average_sc)


st1 = Student("Karaim", "Ivanna", 343, 12, 12, 12)
st2 = Student("Lys", "Viktoria", 564, 12, 9, 4)
st3 = Student("Krupko", "Diana", 345, 10, 12, 12)
st4 = Student("Omelchenko", "Iryna", 305, 10, 12, 12)
st5 = Student("Malykhina", "Ira", 635, 5, 12, 11)
st6 = Student("Doronyk", "Vlad", 325, 4, 12, 11)
st7 = Student("Datsiuk", "Lilya", 3235, 4, 8, 11)
st8 = Student("Shevchenko", "Vlad", 235, 9, 12, 11)
st9 = Student("Levchuk", "Diana", 35, 10, 12, 11)
st10 = Student("Valla", "Marta", 56, 3, 8, 6)
st11 = Student("Datsiuk", "Lilya", 32355, 46, 8, 11)
sc = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]
for i in sc:
    if not i:
        del sc[sc.index(i)]
Group = Group(sc)
Group.func()
print(Group.get())
