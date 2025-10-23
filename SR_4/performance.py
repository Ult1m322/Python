from abc import ABC, abstractmethod

class Performance(ABC):

    def __init__(self, subjects, grades):
        self.__subjects = subjects
        self.__grades = grades

    def get_subjects(self):
        return self.__subjects

    def get_grades(self):
        return self.__grades

    def set_subjects(self, subjects):
        self.__subjects = subjects

    def set_grades(self, grades):
        self.__grades = grades

    @abstractmethod
    def average_grade(self):
        #Абстрактний метод для обчислення середнього балу
        pass


class RealPerformance(Performance):

    #для реальної успішності

    def average_grade(self):
        if not self.get_grades():
            return 0.0
        return sum(self.get_grades()) / len(self.get_grades())


class DesiredPerformance(Performance):
    #для бажаної успішності

    def average_grade(self):
        if not self.get_grades():
            return 0.0
        return sum(self.get_grades()) / len(self.get_grades())