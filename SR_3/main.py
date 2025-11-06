class Employee:
    def __init__(self, name, salary, days_worked, bonus_percent=0):
        self._name = name
        self._salary = salary
        self._days_worked = days_worked
        self._bonus_percent = bonus_percent

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_days_worked(self):
        return self._days_worked

    def set_days_worked(self, days):
        self._days_worked = days

    def get_bonus_percent(self):
        return self._bonus_percent

    def set_bonus_percent(self, percent):
        self._bonus_percent = percent

    def calculate_monthly_salary(self):
        return (self._salary / 30) * self._days_worked

    def calculate_bonus(self):
        return (self._salary / 100) * self._bonus_percent

    def get_info(self):
        monthly = self.calculate_monthly_salary()
        bonus = self.calculate_bonus()
        return (f"Ім'я: {self._name}\n"
                f"  Заробітна плата: {self._salary:.2f} грн\n"
                f"  Дні роботи: {self._days_worked}\n"
                f"  Відсоток бонусу: {self._bonus_percent}%\n"
                f"  Місячна зарплата: {monthly:.2f} грн\n"
                f"  Бонус: {bonus:.2f} грн")


class Manager(Employee):
    bonus_size = 700

    def __init__(self, name, salary, days_worked, subordinates, bonus_percent=0):
        super().__init__(name, salary, days_worked, bonus_percent)
        self._subordinates = subordinates

    def get_subordinates(self):
        return self._subordinates

    def set_subordinates(self, quantity):
        self._subordinates = quantity

    def generate_report(self):
        return f"Менеджер {self._name} керує {self._subordinates} працівниками."

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        bonus_from_subordinates = self._subordinates * Manager.bonus_size
        return base_bonus + bonus_from_subordinates

    def get_info(self):
        monthly = self.calculate_monthly_salary()
        bonus = self.calculate_bonus()
        base_bonus = super().calculate_bonus()
        bonus_from_subordinates = self._subordinates * Manager.bonus_size

        return (f"[МЕНЕДЖЕР] Ім'я: {self._name}\n"
                f"  Заробітна плата: {self._salary:.2f} грн\n"
                f"  Дні роботи: {self._days_worked}\n"
                f"  Кількість підлеглих: {self._subordinates}\n"
                f"  Відсоток бонусу: {self._bonus_percent}%\n"
                f"  Місячна зарплата: {monthly:.2f} грн\n"
                f"  Базовий бонус: {base_bonus:.2f} грн\n"
                f"  Бонус від підлеглих: {bonus_from_subordinates:.2f} грн\n"
                f"  Загальний бонус: {bonus:.2f} грн")

emp1 = Employee("Олександр", 30000, 10, 3)
emp2 = Employee("Дмитро", 21000, 22, 8)
emp3 = Employee("Владислав", 18000, 25, 9)
manager1 = Manager("Володимир", 45000, 18, 13, 12)
manager2 = Manager("Олексій", 32000, 21, 8, 10)

employees = [emp1, emp2, emp3, manager1, manager2]

print("\nЗВІТ ПРО ПРАЦІВНИКІВ:\n")
for i, emp in enumerate(employees, 1):
    print(f"Працівник {i}:")
    print(emp.get_info())

    if isinstance(emp, Manager):
        print(f" {emp.generate_report()}")

    print()
