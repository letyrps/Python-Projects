import time
from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
from score import Score

myscreen = Screen()
myscreen.tracer(0)
myscreen.bgcolor('black')
r_padle = Padle(350)
l_padle = Padle(-350)
ball = Ball()
score = Score()


myscreen.setup(height=600, width=800)

myscreen.title('Build Pong')
myscreen.listen()
myscreen.onkey(fun=r_padle.up, key='Up')
myscreen.onkey(fun=r_padle.down, key='Down')
myscreen.onkey(fun=l_padle.up, key='w')
myscreen.onkey(fun=l_padle.down, key='s')

is_on = True
while is_on:
    time.sleep(ball.level)
    myscreen.update()
    ball.move()

    #detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    #detect colision with padle
    if ball.distance(r_padle) < 60 and ball.xcor() > 320 or ball.distance(l_padle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #detect padle R miss
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        score.update_score_l()
        print(ball.speed_ball)

    #detect padle l miss
    if ball.xcor() < - 380:
        ball.reset_position()
        ball.bounce_x()
        score.update_score_r()
        print(ball.speed_ball)


myscreen.exitonclick()
