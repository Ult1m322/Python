class Person:
    def __init__(self, name, surname, grade=1):
        self.name = name
        self.surname = surname
        self.grade = grade

    def get_info(self):
        return f"Ім'я: {self.name}, Прізвище: {self.surname}, Оцінка: {self.grade}"

    def __del__(self):
        print(f"Ви отримали стипендію {self.name} {self.surname}")

student1 = Person("Олексій", "Кішко", 5)
student2 = Person("Влад", "Устименко", 4)
student3 = Person("Дмитро", "Вовченко")

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

input("\nНатисніть Enter для завершення програми...")