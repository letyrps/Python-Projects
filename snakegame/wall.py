from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.pensize(10)
        self.goto(-300,300)
        self.pendown()
        self.goto(-300, -300)
        self.goto(300, -300)
        self.goto(300, 300)
        self.goto(-300, 300)