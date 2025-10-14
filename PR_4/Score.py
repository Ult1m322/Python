class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0 # Початковий рахунок спійманих яєць
        self.lost = 0 # Початкова кількість пропущених яєць
        self.text = "" # Змінна для текстового елемента
        self.show_text() # Метод для відображення рахунку

    def show_text(self):
        # Метод створює або оновлює текст рахунку на полотні
        if (self.text == ""):
            self.text = self.canvas.create_text(
                350, 10, text=f"Спіймав: 0 Пропустив: 0", font=('Helvetica', 16)
            )
        else:
            self.canvas.itemconfig(
                self.text, text=f"Спіймав: {self.score} Пропустив: {self.lost}"
            )

    def catched_egg(self):
        self.score += 1 # Збільшує рахунок спійманих
        self.show_text() # Оновлює текст

    def lost_egg(self):
        self.lost += 1 # Збільшує кількість пропущених
        self.show_text() # Оновлює текст