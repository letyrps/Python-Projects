#class of titles that appear on screen
FONT = ('Arial', 12, 'bold')

from turtle import Turtle

class Title(Turtle):
    def __init__(self, name_of_country, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.write(f'{name_of_country}', align='center', font=FONT)
