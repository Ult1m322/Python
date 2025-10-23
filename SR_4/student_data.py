from student import Student
from performance import RealPerformance, DesiredPerformance


class StudentData:

    def __init__(self, student, real_performance, desired_performance):
        self.__student = student
        self.__real_performance = real_performance
        self.__desired_performance = desired_performance
        self.__student_id = None

    def get_student(self):
        return self.__student

    def get_real_performance(self):
        return self.__real_performance

    def get_desired_performance(self):
        return self.__desired_performance

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def save_to_db(self, database):
        student_id = database.insert_student(self.__student)
        self.__student_id = student_id

        database.insert_performance(student_id,
                                    self.__real_performance.get_subjects(),
                                    self.__real_performance.get_grades(),
                                    'real_performance')

        database.insert_performance(student_id,
                                    self.__desired_performance.get_subjects(),
                                    self.__desired_performance.get_grades(),
                                    'desired_performance')

    def update_in_db(self, database):
        database.update_student(self.__student_id, self.__student)

        database.insert_performance(self.__student_id,
                                    self.__real_performance.get_subjects(),
                                    self.__real_performance.get_grades(),
                                    'real_performance')

        database.insert_performance(self.__student_id,
                                    self.__desired_performance.get_subjects(),
                                    self.__desired_performance.get_grades(),
                                    'desired_performance')

    def delete_from_db(self, database):
        database.delete_student(self.__student_id)
        self.__student_id = None

    @staticmethod
    def load_from_db(database, student_id):
        row = database.get_student(student_id)
        student = Student(row[1], row[2], row[3], row[4], row[5])

        real_subjects, real_grades = database.get_performance(student_id, 'real_performance')
        real_perf = RealPerformance(real_subjects, real_grades)

        desired_subjects, desired_grades = database.get_performance(student_id, 'desired_performance')
        desired_perf = DesiredPerformance(desired_subjects, desired_grades)

        student_data = StudentData(student, real_perf, desired_perf)
        student_data.set_student_id(student_id)

        return student_data