##################### Extra Hard Starting Project ######################
from tkinter import *
import pandas
import datetime as dt
import random
import smtplib
window = Tk()
window.title('Birthday maker')
window.config(height=200, width=400)
#Labels
canvas = Canvas()
label_title = Label(text="Add a Birthday", font=('Arial', 24, 'bold'))
canvas.create_window(150, 50, window=label_title)
entry_birthday = Entry(width=30)
entry_birthday.insert(END, string="Name, email, year, month, day, time to send")
canvas.create_window(150, 100, window=entry_birthday)
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)
canvas.config(background='pale turquoise')
label_exemple = Label(text="Exemple: Letícia, leticiarochacorretora@gmail.com, 1998, 7, 16, 8", font=('Arial', 8, 'normal'))
canvas.create_window(150, 120, window=label_exemple)

# 1. Update the birthdays.csv
#Buttons
def action():
    entry = entry_birthday.get()
    with open('birthday - Página1.csv', 'a') as file:
        file.write(f'\n{entry}')
button_add = Button(text="Add", command=action)
canvas.create_window(150, 150, window=button_add)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
actual_month = today.month
actual_day = today.day
birthday_df = pandas.read_csv('birthday - Página1.csv')
for name in birthday_df.Name:
    row_name = birthday_df[birthday_df.Name == name]
    month_row = row_name.month
    month_row = month_row.values[0]
    month_row = int(month_row)
    day_row = row_name.day
    day_row = day_row.values[0]
    day_row = int(day_row)
    name_row = row_name.Name
    name_row = name_row.values[0]
    name_row = str(name_row)
    mail_row = row_name.email
    mail_row = mail_row.values[0]

    if month_row == actual_month:
        if day_row == actual_day:

            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            n = random.randint(1, 3)
            letter_choose = f'letter_{n}.txt'
            with open(f'/Users/vfx/Desktop/Python/birthday-wisher-extrahard-start/letter_templates/{letter_choose}', 'r') as file:
                contents = file.read()
                contents = contents.replace('[NAME]', name_row)
                my_email = 'leticiarochacorretora@gmail.com'
                password = 'mvuroguflzckogyn'

                # 4. Send the letter generated in step 3 to that person's email address.
                with smtplib.SMTP('smtp.gmail.com') as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs='leticiarochapimenteldesouza@gmail.com',
                                        msg=f'Subject:Happy Birthday\n\n{contents}')



#loop window
window.mainloop()



