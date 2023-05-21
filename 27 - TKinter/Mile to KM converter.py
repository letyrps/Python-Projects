from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=200)

#Entries the mile
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="")
entry.grid(column=1, row=0)

#Labels
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

#Labels
label_2 = Label(text="is equal to")
label_2.grid(column=0, row=2)

#Labels
label_3 = Label(text="result")
label_3.grid(column=1, row=1)

#Labels
label_4 = Label(text="Km")
label_4.grid(column=1, row=2)

#Buttons
def action():
    # Gets text in entry
    mile = entry.get()
    mile = int(mile) * 1.6
    mile = round(mile, 1)
    label_3.config(text=f"{mile}")

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)


window.mainloop()