class Catcher:
    def __init__(self, canvas, color, score):
        # Ініціалізація атрибутів класу
        self.canvas = canvas
        self.score = score # Збереження посилання на об'єкт рахунку
        # Створення прямокутника (ловця)
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # Переміщення ловця на початкову позицію
        self.canvas.move(self.id, 200, 350)
        self.x = 0 # Початкова горизонтальна швидкість
        # Збереження ширини полотна
        self.canvas_width = self.canvas.winfo_width()