from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

#label
my_label = Label(text='I am a Label', font=('Arial', 24, 'italic'))
my_label.pack()

#button

def button_clicked():
    my_label.config(text=f'{input_.get()}')


button = Button(text='Click Me', command=button_clicked)
button.pack()



#entry

input_ = Entry(width=10)
input_.pack()


window.mainloop()