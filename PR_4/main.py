from tkinter import *
import random
import time
from Score import Score
from Catcher import Catcher
from Egg import Egg # Імпортуємо клас яйця

tk = Tk()
tk.title("Гра: Ловець!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update() # Оновлюємо, щоб отримати розміри canvas

score = Score(canvas)
catcher = Catcher(canvas, 'blue', score)
eggs = []

# Головний цикл гри
while 1:
    if random.randint(1, 100) == 1: # З шансом 1%
        eggs.append(Egg(canvas, 'red', score)) # Створюємо нове яйце

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)