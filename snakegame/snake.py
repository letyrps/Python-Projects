from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DONW = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.pensize(20)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment((self.segments[-1].position()))

    def move(self):
        for iten in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[iten - 1].xcor()
            new_y = self.segments[iten - 1].ycor()
            self.segments[iten].setposition(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DONW:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DONW)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
