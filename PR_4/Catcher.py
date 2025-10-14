from tkinter import TclError
class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # Прив'язка методів до подій клавіатури
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        # Якщо ловець не на краю зліва, встановлюємо швидкість для руху вліво
        if self.canvas.coords(self.id)[0] > 0:
            self.x = -20

    def turn_right(self, evt):
        # Якщо ловець не на краю справа, встановлюємо швидкість для руху вправо
        if self.canvas.coords(self.id)[2] < self.canvas_width:
            self.x = 20

    def draw(self):
        # Оновлення позиції ловця на полотні
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # Обмеження руху ловця зліва
        if pos[0] <= 0:
            self.x = 0
        # Обмеження руху ловця справа
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def catch(self, eggs):
        catcher_pos = self.canvas.coords(self.id)
        # Перевірка координат, щоб уникнути помилок, якщо об'єкт вже видалено
        if not catcher_pos:
            return

        for egg in list(eggs):
            try:
                egg_pos = self.canvas.coords(egg.id)
                if not egg_pos:
                    continue

                # Умова перетину прямокутників (ловця та яйця)
                if (catcher_pos[0] < egg_pos[2] and catcher_pos[2] > egg_pos[0] and
                    catcher_pos[1] < egg_pos[3] and catcher_pos[3] > egg_pos[1]):
                    eggs.remove(egg)
                    self.canvas.delete(egg.id)
                    self.score.catched_egg()
            except TclError:
                # Ця помилка може виникнути, якщо яйце вже було видалено в іншому місці
                continue