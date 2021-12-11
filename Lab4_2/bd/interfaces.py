from abc import ABC, abstractmethod


class ICourse:

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def topics(self):
        pass

    @topics.setter
    @abstractmethod
    def topics(self, value):
        pass


class ILocalCourse(ICourse, ABC):

    @property
    @abstractmethod
    def number_lab(self):
        pass

    @number_lab.setter
    @abstractmethod
    def number_lab(self, value):
        pass


class IOffsiteCourse(ICourse, ABC):

    @property
    @abstractmethod
    def address(self):
        pass

    @address.setter
    @abstractmethod
    def address(self, value):
        pass


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        pass

    @abstractmethod
    def add(self, value):
        pass


class IFactory(ABC):

    @abstractmethod
    def all_teachers(self):
        pass

    @abstractmethod
    def all_local_courses(self):
        pass

    @abstractmethod
    def all_offsite_courses(self):
        pass
