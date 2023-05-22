from turtle import Turtle, Screen
import random

arrow = Turtle()
colors = ['AliceBlue', 'black', 'chartreuse', 'coral', 'dark red', 'DarkOrchid', 'DimGrey', 'goldenrod3',
          'LemonChiffon4', 'LightCyan1']

for x in range(3, 10):
    color = random.choice(colors)
    arrow.pencolor(color)

    for i in range(0, x):
        arrow.right(360/x)
        arrow.forward(100)
    x += 1


screen = Screen()
screen.exitonclick()
