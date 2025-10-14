import random

class Egg:
    def __init__(self, canvas, color, score):
        # Ініціалізація атрибутів
        self.canvas = canvas
        self.color = color
        self.score = score # Посилання на об'єкт рахунку
        # Створення овалу (яйця)
        self.id = canvas.create_oval(0, 0, 25, 25, fill=color)
        # Розміщення яйця у випадковій позиції вгорі
        self.canvas.move(self.id, random.randint(10, 490), -10)
        # Визначення випадкової швидкості падіння
        self.y = random.randint(1, 4)