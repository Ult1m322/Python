class Student:
    def __init__(self, surname, name, patronymic, group_number, birth_date=None):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__group_number = group_number
        self.__birth_date = birth_date

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_patronymic(self):
        return self.__patronymic

    def get_group_number(self):
        return self.__group_number

    def get_birth_date(self):
        return self.__birth_date

    def get_full_name(self):
        return f"{self.__surname} {self.__name} {self.__patronymic}"

    def set_surname(self, surname):
        self.__surname = surname

    def set_name(self, name):
        self.__name = name

    def set_patronymic(self, patronymic):
        self.__patronymic = patronymic

    def set_group_number(self, group_number):
        self.__group_number = group_number

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date