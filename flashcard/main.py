import random
import time
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas

#variables
value_row = 0
value = 0
random_word_key = 0
#------------------------------- creating new flash cards ----------------------------------

#calls action() when pressed
def action_():
    print("Do something")

#calls action() when pressed
def new_word():
    global value_row
    global value
    global random_word_key
    canvas.itemconfig(rec, fill='white')
    lenguage_label.config(text='English', background='white')

    contents = pandas.read_csv('/Users/vfx/Desktop/Python/Portifólio/flashcard/data/words_to_learn.csv')
    random_word_key = random.choice(contents.word)
    print(random_word_key)
    value_row = contents[contents.word == random_word_key]
    value = value_row['translate']
    value = value.values[0]
    print(value)

    word_title_label.config(text=random_word_key, background='white')
    window.update()
    time.sleep(3)
    canvas.itemconfig(rec, fill='LightSteelBlue1')
    lenguage_label.config(text='Tradução Português', background='LightSteelBlue1')
    word_title_label.config(text=value, background='LightSteelBlue1')

def check_button():
    new_word()

#--------------------------------------- User interface ---------------------------------------

#canvas
window = Tk()
window.title('FLF - FlashCards Learning Fast')
window.minsize(width=800, height=526)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
rec = canvas.create_rectangle(50, 50, 750, 400, fill='white', outline='white')
lenguage_label = Label(text="English",  font=('Arial', 40, 'italic'))
lenguage_title = canvas.create_window(400, 150, window=lenguage_label)
word_title_label = Label(text="This is old text",  font=('Arial', 40, 'italic'))
word_title = canvas.create_window(400, 263, window=word_title_label)

#Buttons
button_check = Button(canvas, text="✅", command=check_button, font=('arial', 54, 'normal'))
canvas.create_window(186, 464, anchor='nw', window=button_check)
button_x = Button(canvas, text="❌", command=check_button, font=('arial', 54, 'normal'))
canvas.create_window(511, 464, anchor='nw', window=button_x)
canvas.grid(row=0, column=0, columnspan=2)


window.mainloop()