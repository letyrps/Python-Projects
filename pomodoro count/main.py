from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
window = Tk()
num_of_checks = 0
timer_ap = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_donw(long_break_sec)
        title_timer.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_donw(short_break_sec)
        title_timer.config(text='Break', fg=PINK)
    else:
        count_donw(work_sec)
        title_timer.config(text='Work', fg=GREEN)


def reset():
    global num_of_checks
    global reps
    reps = 0
    window.after_cancel(timer_ap)
    canvas.itemconfig(timer, text=f'00:00')
    num_of_checks = 0
    check_box.config(text=(""))
    title_timer.config(text="Timer", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_donw(count):
    global num_of_checks
    global timer_ap
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')

    if count > 0:
        timer_ap = window.after(1000, count_donw, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps > 0:
            num_of_checks += 1
            check_box.config(text=("✅")*num_of_checks)
        elif num_of_checks > 4:
            num_of_checks = 0




# ---------------------------- UI SETUP ------------------------------- #

window.title('Pomodoro')
canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato = canvas.create_oval(20, 30, 180, 180, fill='red')
timer = canvas.create_text(100, 105, text='00:00', fill='white', font=(FONT_NAME ,35, 'bold'))
canvas.grid(column=1, row=1)





title_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, 'normal'))
title_timer.grid(column=1, row=0, sticky="NSEW")


#calls action() when pressed
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=4, sticky="NSEW")

#calls action() when pressed
reset = Button(text="Reset", command=reset, highlightthickness=0)
reset.grid(column=3, row=4, sticky="NSEW")

check_box = Label(fg=GREEN, font=(FONT_NAME, 24, 'normal'))
check_box.grid(column=1, row=3, sticky="NSEW")


start_label = Label(text="Start", fg=GREEN, font=(FONT_NAME, 14, 'normal'))
start_label.grid(column=0, row=3, sticky="NSEW")

reset_label = Label(text="Stop", fg=GREEN, font=(FONT_NAME, 14, 'normal'))
reset_label.grid(column=3, row=3, sticky="NSEW")

window.mainloop()
