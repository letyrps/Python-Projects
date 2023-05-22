import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Quiz_interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('FLF - FlashCards Learning Fast')
        self.window.minsize(width=340, height=510)
        self.canvas = Canvas(height=510, width=340, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f'Score: {self.score}', font=('Arial', 18, 'normal'), fg='white',
                                 background=THEME_COLOR)
        self.score_title = self.canvas.create_window(280, 40, window=self.score_label)
        self.rec = self.canvas.create_rectangle(20, 80, 320, 350, fill='white', outline='white')
        self.question_text = self.canvas.create_text(175, 200, font=('Arial', 20, 'italic'), text=f'Some text',
                                                     width=250, fill='black', justify="center")
        self.image_false = PhotoImage(file='/Users/vfx/Desktop/Python/quizzler-app-start/images/false.gif')
        self.image_true = PhotoImage(file='/Users/vfx/Desktop/Python/quizzler-app-start/images/true.gif')

        self.button_true = Button(image=self.image_true, command=self.button_true_action)
        self.button_true_w = self.canvas.create_window(110, 440, window=self.button_true)
        self.button_false = Button(image=self.image_false, command=self.button_false_action)
        self.button_false_w = self.canvas.create_window(215, 440, window=self.button_false)
        self.canvas.grid(row=0, column=0, columnspan=2, rowspan=3)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
            q_text = self.quiz.next_question()
            if q_text == False:
                self.canvas.itemconfig(self.question_text, text=f'Game over')
            else:
                self.canvas.itemconfig(self.question_text, text=f'{q_text}')



    def button_true_action(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.feedback(is_right)

    def button_false_action(self):
        is_right = self.quiz.check_answer(user_answer='False')
        self.feedback(is_right)


    def feedback(self, is_right):
        if is_right == True:
            self.canvas.itemconfig(self.rec, fill='green')
            self.window.update()
            time.sleep(1)
            self.canvas.itemconfig(self.rec, fill='white')
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.window.update()
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.rec, fill='red')
            self.window.update()
            time.sleep(1)
            self.canvas.itemconfig(self.rec, fill='white')
            self.window.update()
            self.get_next_question()

