from abc import ABC, abstractmethod


class ICourse:
    """Course interface"""
    @property
    @abstractmethod
    def name(self):
        """Getter name for the course"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """Setter name for the course"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """Getter teacher for the course"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """Setter teacher for the course"""
        pass

    @property
    @abstractmethod
    def topics(self):
        """Getter topics for the course"""
        pass

    @topics.setter
    @abstractmethod
    def topics(self, value):
        """Setter topics for the course"""
        pass


class ILocalCourse(ICourse, ABC):
    """Local course interface"""
    @property
    @abstractmethod
    def number_lab(self):
        """Getter number_lab for the course"""
        pass

    @number_lab.setter
    @abstractmethod
    def number_lab(self, value):
        """Setter number_lab for the course"""
        pass


class IOffsiteCourse(ICourse, ABC):
    """Offsite course interface"""
    @property
    @abstractmethod
    def address(self):
        """Getter address for the course"""
        pass

    @address.setter
    @abstractmethod
    def address(self, value):
        """Setter address for the course"""
        pass


class ITeacher(ABC):
    """Teacher interface"""
    @property
    @abstractmethod
    def name(self):
        """Getter name for the teacher"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """Setter name for the teacher"""
        pass

    @property
    @abstractmethod
    def courses(self):
        """Getter courses for the teacher"""
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        """Setter courses for the teacher"""
        pass

    @abstractmethod
    def add(self, value):
        """Func add courses in teacher"""
        pass


class IFactory(ABC):
    """Factory interface"""
    @abstractmethod
    def all_teachers(self):
        """All teachers in the program academy"""
        pass

    @abstractmethod
    def all_local_courses(self):
        """All local courses in the program academy"""
        pass

    @abstractmethod
    def all_offsite_courses(self):
        """All offsite courses in the program academy"""
        pass
