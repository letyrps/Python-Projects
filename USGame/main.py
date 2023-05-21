import time
from turtle import Turtle
import turtle
import pandas
from title_class import Title
screen = turtle.Screen()
screen.title("U.S Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#    print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Liste of variables
NUMBER_OF_STATES = 50
score_ = 0
display_score = Turtle()
display_score.penup()
display_score.hideturtle()
screen.screensize(600, 800)
screen.tracer(0)
anser_write = False
answer_made = []

# Use a loop to allow user guesses ont the map
is_on = True

#keep track of high score
with open('score.txt', 'r') as file:
    high_score = file.read()

while is_on:
    if score_ < NUMBER_OF_STATES: #while score is less than 50 keep playing

        #saving the guess
        answer_state = screen.textinput(title='Gues the State', prompt="What is another state's name?")
        answer_state = answer_state.title()

        #reading the data of states and converting in to a variable
        data = pandas.read_csv('50_states.csv')
        state = data['state']
        x_collun = data['x']
        y_collun = data['y']

        #list to keep creating objects
        list_of_states_obecjects = []

        # Convert the guess in a Title case:
        # test = Title(answer_state,0,0)


        # Test if the guess is amoung the 50 states
        is_in_states = 0 #variable that find if the answer is in list of states
        for iten in range(0,50): #there are 50 states so if in more than 50 dont find answer is wrong
            if is_in_states < 50: #if is not 50 keep going
                for iten in state: #loop throuw the data
                    if iten == answer_state and answer_state not in answer_made: #try find the answer in data
                        is_in_states = 50
                        anser_write = True
                        answer_made.append(answer_state)
                    else:
                        is_in_states +=1 #sum to keep going until 50
        while anser_write:
            score_ += 1 # update the score
            if score_ > int(high_score): #update the high score
                with open('score.txt', 'w') as file:
                    file.write(f'{score_}')
            display_score.clear()
            display_score.goto(0, 250) #write the score on screeen
            display_score.write(f'SCORE: {score_} of 50 states', align='center', font=('Arial', 24, 'bold'))
            display_score.goto(250, 250) #write the high score on screen

            with open('score.txt', 'r') as file:
                high_score = file.read()

            display_score.write(f'HIGH SCORE: {high_score}', align='center', font=('Arial', 14, 'bold'))
            screen.update()

            # Write the correct guess on map
            collun_of_answer = data[data.state == answer_state]
            x = collun_of_answer['x']
            x = x.values[0]
            x = int(x)
            y = collun_of_answer['y']
            y = y.values[0]

            state_object = Title(answer_state, x, y)
            list_of_states_obecjects.append(state_object)
            anser_write = False



    else: #if score more then 50 so the player won the game
        display_score.color('blue')
        display_score.goto(0, 0)
        display_score.write(f'YOU WIN', align='center', font=('Arial', 54, 'bold'))
        time.sleep(2)
        display_score.color('red')
        display_score.write(f'YOU WIN', align='center', font=('Arial', 54, 'bold'))
        time.sleep(2)
        display_score.color('white')
        display_score.write(f'YOU WIN', align='center', font=('Arial', 54, 'bold'))
        time.sleep(2)
        screen.update()



turtle.mainloop() #keep open the screen until click in close