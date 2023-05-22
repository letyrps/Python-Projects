from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 24, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(-350)
        self.sety(350)
        self.write(f'Score: {self.score} High Socore: {self.high_score}', align='center', font=('Arial', 24, 'bold'))


    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Socore: {self.high_score}', align='center', font=('Arial', 24, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0


