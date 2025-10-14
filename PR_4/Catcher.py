class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # Прив'язка методів до подій натискання клавіш
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        # Перевірка, чи не на краю зліва
        if self.canvas.coords(self.id)[0] > 0:
            self.x = -20 # Встановлюємо швидкість для руху вліво

    def turn_right(self, evt):
        # Перевірка, чи не на краю справа
        if self.canvas.coords(self.id)[2] < self.canvas_width:
            self.x = 20 # Встановлюємо швидкість для руху вправо

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # Зупинка руху біля лівого краю
        if pos[0] <= 0:
            self.x = 0
        # Зупинка руху біля правого краю
        elif pos[2] >= self.canvas_width:
            self.x = 0