from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
from wall import Wall
import time

myscreen = Screen()
myscreen.bgcolor('black')
myscreen.screensize(canvheight=300, canvwidth=300)
myscreen.title('Snake Game')
myscreen.tracer(0)

turtle = Turtle
snake = Snake()
food = Food()
score = Score()
wall = Wall()
myscreen.listen()
myscreen.onkey(snake.up, 'Up')
myscreen.onkey(snake.down, 'Down')
myscreen.onkey(snake.left, 'Left')
myscreen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    myscreen.update()
    time.sleep(0.1)
    snake.move()

    #detecting colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        score.update_score()

    #detecting colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        score.update_score()
        snake.reset_snake()


    #detec colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.update_score()
            snake.reset_snake()



myscreen.exitonclick()
