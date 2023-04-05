from tkinter import *
import time

tk = Tk()
tk.title("Ball")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color, x, y, up, down, left, right):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
        self.canvas.bind_all(right, self.turn_right)
        self.canvas.bind_all(left, self.turn_left)
        self.canvas.bind_all(up, self.turn_up)
        self.canvas.bind_all(down, self.turn_down)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def turn_right(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[2] >= self.canvas_width:
            self.x = 2
            self.y = 0

    def turn_left(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[0] <= 0:
            self.x = -2
            self.y = 0

    def turn_up(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[1] <= 0:
            self.x = 0
            self.y = -2

    def turn_down(self, event):
        pos = self.canvas.coords(self.id)
        if not pos[3] >= self.canvas_height:
            self.x = 0
            self.y = 2

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        if pos[3] >= self.canvas_height:
            self.y = 0


ball_one = Ball(canvas, "red", 150, 150, "<KeyPress-Up>", "<KeyPress-Down>", "<KeyPress-Left>", "<KeyPress-Right>")
ball_two = Ball(canvas, "green", 100, 100, "<w>", "<s>", "<a>", "<d>")

while not False:
    ball_one.draw()
    ball_two.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
