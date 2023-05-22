from turtle import Turtle, Screen
import random
draw = Turtle()

colors = ['AliceBlue', 'black', 'chartreuse', 'coral', 'dark red', 'DarkOrchid', 'DimGrey', 'goldenrod3',
          'LemonChiffon4', 'LightCyan1', 'peru', 'chartreuse', 'dark violet', 'magenta', 'dark orange']
ang = [0, 90, 270, 180]

draw.pensize(20)
draw.speed(7)
for i in range(0, 100):
    color = random.choice(colors)
    draw.color(color)
    x = random.choice(ang)
    draw.right(x)
    draw.forward(40)


screen = Screen()
screen.exitonclick()
