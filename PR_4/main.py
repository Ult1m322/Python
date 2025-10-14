from tkinter import *
import random
import time
from Score import Score # Імпортуємо новий клас

tk = Tk()
tk.title("Гра: Ловець!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

score = Score(canvas) # Ініціалізуємо клас рахунку

tk.update()
time.sleep(1)