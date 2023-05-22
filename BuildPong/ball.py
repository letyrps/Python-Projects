from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.turtlesize(1)
        self.shape("circle")
        self.penup()
        self.color('blue')
        self.setx(0)
        self.sety(0)
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0
        self.speed(self.speed_ball)
        self.level = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.level *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.level *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.home()
        self.showturtle()
        self.level = 0.1








