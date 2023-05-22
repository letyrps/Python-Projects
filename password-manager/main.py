import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice
import pyperclip
import simplejson

# def motion(event): ##mouse position
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for l in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2, 4))]
    password_numbers = [choice(numbers) for n in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letter

    password = ''.join(password_list)

    entry_password.focus()
    entry_password.delete(0, END)
    entry_password.insert(END, f'{password}')
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
# window.bind('<Motion>', motion) ##mouse position

#canvas
canvas = Canvas(width=200, height=140)
canvas.create_line(50, 10, 150, 10, width=3, fill='red', capstyle='round')
canvas.create_line(50, 10, 50, 100, width=3, fill='red', capstyle='round')
canvas.create_line(150, 10, 150, 30, width=3, fill='red', arrow='last', capstyle='round')
canvas.create_line(50, 100, 150, 100, width=3, fill='red', capstyle='round')
canvas.create_line(150, 100, 150, 50, width=3, fill='red', capstyle='round')
canvas.create_line(150, 50, 50, 50, width=3, fill='red', capstyle='round')
canvas.grid(row=0, column=0, columnspan=3)

#labels
logo_title = Label(text='MyPass', font=('Arial', 23, 'bold'), fg='red')
logo_title.grid(row=0, column=0, columnspan=3)
website_label = Label(text='Website:', font=('Arial', 10, 'bold'), fg='black')
website_label.grid(row=1, column=0)
email_user_label = Label(text='Email/Username:', font=('Arial', 10, 'bold'), fg='black')
email_user_label.grid(row=2, column=0)
password_label = Label(text='Password:', font=('Arial', 10, 'bold'), fg='black')
password_label.grid(row=3, column=0)

# Entries
entry_website = Entry(width=21)
entry_website.grid(row=1, column=1)
entry_email_user = Entry(width=35)
entry_email_user.focus()
entry_email_user.insert(END, 'leticiarochacorretora@gmail.com')
entry_email_user.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def action():
    website = entry_website.get()
    email = entry_email_user.get()
    password = entry_password.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}

    if len(website) <1 or len(password) <1:
        erro = messagebox.showinfo(title='ERRO', message='You have missed an entry')


    else:
        try:
            with open('mypass.json', 'r') as file:
                #reading new data
                data = json.load(file)

        except FileNotFoundError:
            with open('mypass.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            #updating old data
            data.update(new_data)

            with open('mypass.json', 'w') as file:
                #saving updated data
                json.dump(data, file, indent=4)

        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)

def search_generate():
    website_key = entry_website.get()
    try:
        with open('mypass.json', 'r') as file:
            # reading new data
            data = json.load(file)
            try:
                info = data[website_key]
            except KeyError:
                error = messagebox.showinfo(title='ERRO', message='Website not found')
            else:
                info = messagebox.showinfo(title=f'{website_key}', message=f'Email: {data[website_key]["email"]}\nPassword: {data[website_key]["password"]}')
    except FileNotFoundError:
        error = messagebox.showinfo(title='ERRO', message='Ooups! Nothing saved yet, save info to search')
#Buttons
generate_password = Button(text="Generate Pass", command=generate_password)
generate_password.grid(row=3, column=2)
add = Button(text="Add", command=action, width=34)
add.grid(row=4, column=1, columnspan=2)
search = Button(text='Search', command=search_generate, width=11)
search.grid(row=1, column=2)

window.mainloop()
