import sqlite3

from Lab4_2.bd.interfaces import *

class Teacher(ITeacher):
    """A class describing a teacher"""
    def __init__(self, name:str):
        self.name = name
        self.courses = []

    def __iter__(self):
        """Iterator class teacher"""
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
        """A function that adds the right course to the teacher"""
        if not isinstance(value, (ILocalCourse, IOffsiteCourse)):
            raise TypeError
        self.courses.append(value)

    def __str__(self):
        """A function that outputs class data"""
        return f'{self.name} '


class Course(ICourse):
    """
    Class course
    """
    def __init__(self, name: str, topics: list[str], teacher: ITeacher):
        self.name = name
        self.topics = topics
        self.teacher = teacher

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def teacher(self) -> ITeacher:
        return self.__teacher

    @teacher.setter
    def teacher(self, value: ITeacher):
        if not isinstance(value, ITeacher):
            raise TypeError
        self.__teacher = value

    @property
    def topics(self) -> list[str]:
        return self.__topics

    @topics.setter
    def topics(self, value: list[str]):
        if not all([isinstance(v, str) for v in value]):
            raise TypeError
        self.__topics = value

    def __str__(self):
        """A function that outputs class data"""
        return f'{self.name} {self.teacher.name} {self.topics}'


class LocalCourse(Course, ILocalCourse):
    """A class that describes local courses"""
    def __init__(self, name,  topics, number_lab, teacher):
        super().__init__(name, topics, teacher)
        self.number_lab = number_lab

    @property
    def number_lab(self) -> int:
        return self.__number_lab

    @number_lab.setter
    def number_lab(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__number_lab = value

    def __str__(self) -> str:
        """A function that outputs class data"""
        return f'{self.name} Laboratoria: {self.number_lab} Teacher: {self.teacher}'


class OffsiteCourse(Course, IOffsiteCourse):
    """A class that describes offsite courses"""
    def __init__(self, name, topics, address, teacher):
        super().__init__(name, topics, teacher)
        self.address = address

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        self.__address = value

    def __str__(self) -> str:
        """A function that outputs class data"""
        return f'{self.name} Address: {self.address} Teacher: {self.teacher}'


class Factory(IFactory):
    """Factory class for creating courses in the programming academy"""
    def __init__(self, name: str):
        self.teachers = list()
        self.local_courses = list()
        self.offsite_courses = list()
        self.db = name

    def all_local_courses(self) -> list[ILocalCourse]:
        """A function that creates and returns local courses"""
        db = sqlite3.connect(self.db)
        local_course = db.cursor(). execute(f"SELECT course.id, course.name, course.teacher_id, local_course.number_lab FROM course JOIN local_course ON course.id = local_course.course_id;")
        for local in local_course:
            ind = None
            topics = db.cursor().execute(f"SELECT  topic_name FROM topic_course WHERE course_id = {local[0]};").fetchall()
            teacher = db.cursor().execute(
                f"SELECT teacher_name FROM teacher WHERE id = {local[2]}"
            ).fetchall()
            str = list((t[0] for t in teacher))
            for teach in self.teachers:
                if str[0] == teach.name:
                    ind = teach
            if not ind:
                ind = Teacher(str[0])
                self.teachers.append(ind)
            self.local_courses.append(LocalCourse(local[1], list((t[0] for t in topics)), local[3], ind))
        for local_course in self.local_courses:
            for teacher in self.teachers:
                if local_course.teacher.name == teacher.name:
                    teacher.add(local_course)
        return self.local_courses

    def all_offsite_courses(self) -> list[IOffsiteCourse]:
        """A function that creates and returns offsite courses"""
        db = sqlite3.connect(self.db)
        offsite_course = db.cursor(). execute(f"SELECT course.id, course.name, course.teacher_id, offsite_course.address FROM course JOIN offsite_course ON course.id = offsite_course.course_id;")
        for offsite in offsite_course:
            ind = None
            topics = db.cursor().execute(f"SELECT  topic_name FROM topic_course WHERE course_id = {offsite[0]};").fetchall()
            teacher = db.cursor().execute(
                f"SELECT teacher_name FROM teacher WHERE id = {offsite[2]}"
            ).fetchall()
            str = list((t[0] for t in teacher))
            for teach in self.teachers:
                if str[0] == teach.name:
                    ind = teach
            if not ind:
                ind = Teacher(str[0])
                self.teachers.append(ind)
            self.offsite_courses.append(OffsiteCourse(offsite[1], list((t[0] for t in topics)), offsite[3], ind))
        for offsite_course in self.offsite_courses:
            for teacher in self.teachers:
                if offsite_course.teacher.name == teacher.name:
                    teacher.add(offsite_course)
        return self.offsite_courses

    def all_teachers(self) -> list[ITeacher]:
        """A function that creates and returns teachers"""
        teachers = list()
        db = sqlite3.connect(self.db)
        response = db.cursor().execute("SELECT * FROM teacher;").fetchall()
        for teacher in response:
            courses = list()
            ind = Teacher(teacher[1])
            locals= db.cursor().execute(f"SELECT course.id, course.name, course.teacher_id, local_course.number_lab FROM course JOIN local_course ON course.id = local_course.course_id WHERE course.teacher_id = {teacher[0]}").fetchall()
            for local in locals:
                topics = db.cursor().execute(f"SELECT  topic_name FROM topic_course WHERE course_id = {local[0]};").fetchall()

                courses.append(LocalCourse(local[1], list((t[0] for t in topics)), local[3], ind))
            offsites = db.cursor().execute(f"SELECT course.id, course.name, course.teacher_id, offsite_course.address FROM course JOIN offsite_course ON course.id = offsite_course.course_id AND course.teacher_id = {teacher[0]};").fetchall()
            for offsite in offsites:
                topics = db.cursor().execute(f"SELECT  topic_name FROM topic_course WHERE course_id = {offsite[0]};").fetchall()
                courses.append(OffsiteCourse(offsite[1], list((t[0] for t in topics)), offsite[3], ind))
            ind.courses = courses
            teachers.append(ind)
        for teacher in teachers:
            for course in teacher.courses:
                course.teacher = teacher
        db.close()
        self.teachers = teachers
        return teachers


if __name__ == "__main__":
    X = Factory("./database.db")
    for l in X.all_local_courses():
        print(l)
    # for t in X.all_teachers():
    #     print(t)
    for o in X.all_offsite_courses():
        print(o)



