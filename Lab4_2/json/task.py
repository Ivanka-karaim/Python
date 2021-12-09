import json

from Lab4_2.json.interfaces import ICourse, IOffsiteCourse, ILocalCourse, ITeacher


class Course(ICourse):

    def __init__(self, name, teacher, topics):
        self.name = name
        self.teacher = teacher
        self.topics = topics

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, ITeacher):
            raise TypeError
        self.__teacher = value

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        if not all([isinstance(v, str) for v in value]):
            raise TypeError
        self.__topics = value

    def __str__(self):
        return f'{self.name} {self.teacher.name} {self.topics}'


class Teacher(ITeacher):

    def __init__(self, name):
        self.name = name
        self.courses = []

    def __iter__(self):
        return iter(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not all([isinstance(v, (ILocalCourse, IOffsiteCourse)) for v in value]):
            raise TypeError
        self.__courses = value

    def add(self, value):
        if not isinstance(value, (ILocalCourse, IOffsiteCourse)):
            raise TypeError
        self.courses.append(value)

    def __str__(self):
        return f'{self.name} {"".join(list(map(str, list(self.courses))))}'


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, topics, phone_number):
        super().__init__(name, teacher, topics)
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.isdigit():
            raise ValueError
        self.__phone_number = value


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, teacher, topics, address):
        super().__init__(name, teacher, topics)
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__address = value


class CoursesFactory:

    def __init__(self):
        self.teachers = []
        self.courses = []

    def create_courses(self):
        courses_dict = {
            "local": LocalCourse,
            "offsite": OffsiteCourse
        }
        courses_dict2 = {
            "local": "phone_number",
            "offsite": "address"
        }
        with open("file.json", 'r') as file:
            courses = json.load(file)
        for course in courses:
            ind = None
            for teacher in self.teachers:
                if teacher.name == course["teacher"]:
                    ind = teacher
            if not ind:
                ind = Teacher(course["teacher"])
                self.teachers.append(ind)
            self.courses.append(courses_dict[course["type"]](course["name"], ind,
                                                             course["topics"], course["connection"]))
        for course in self.courses:
            for teacher in self.teachers:
                if course.teacher.name == teacher.name:
                    teacher.add(course)


X = CoursesFactory()
X.create_courses()
for cours in X.courses:
    print(cours)

for teche in X.teachers:
    print(teche)
