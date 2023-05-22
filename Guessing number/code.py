from art import logo
import random

print(logo)

print('Welcome to number guessing game!')
print('Im thinking in a number between 1 and 100!')

dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if dificulty == 'easy':
    chances = 10
else:
    chances = 5


def choose_number():
    lista_n = []
    for number in range(0, 101):
        lista_n.append(number)

    number_chosen = random.choice(lista_n)
    return number_chosen


number = choose_number()


def gessing(guess):
    global number
    if number < guess:
        print('To high')
        return True
    elif number > guess:
        print('To low')
        return True
    elif number == guess:
        print('You win')
        return False


var = True
i = 0
while var:

    if i < chances:
        print(f'You have {(chances - i)} attempts remaining to guess the number.')
        var = True
        gess = int(input('Make a guess:'))
        var = gessing(gess)
        i += 1
    elif i >= chances:
        print(f'You lost! Number was {number}')
        var = False
