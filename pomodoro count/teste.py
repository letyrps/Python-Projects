from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=200, height=224)
image = PIL.ImageTk.PhotoImage(image=None, size=None, **kw)
# note here use of Label
background_label = Label(window, image=tomato_pic)
# label.place is tk trick that is good for backgrounds
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

window.mainloop()