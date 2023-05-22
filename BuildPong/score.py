from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()


    def write_score(self):
        self.goto(x=-200, y=250)
        self.write(self.l_score, align='center', font=('Noto Sans', 40, 'normal'))
        self.goto(x=200, y=250)
        self.write(self.r_score, align='center', font=('Noto Sans', 40, 'normal'))

    def update_score_l(self):
        self.clear()
        self.l_score += 1
        self.write_score()


    def update_score_r(self):
        self.clear()
        self.r_score += 1
        self.write_score()
