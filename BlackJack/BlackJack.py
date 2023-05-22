from art import logo
import random

A = [1, 11]
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

again = True
while again:
    playgame = input('Do you wanna play blackjack? y or n? ')

    if playgame == 'y':
        print(logo)


        def taking_cards(number_of_cards):
            list_cards = []
            for i in range(0, number_of_cards):
                choose_card = random.choice(cards)
                if choose_card == A:
                    list_cards.append(A[1])
                else:
                    list_cards.append(choose_card)
                i += 1

            return list_cards


        your_cards = taking_cards(2)
        computer_cards = taking_cards(1)


        def score(lista):
            score_ = 0
            for item in lista:
                score_ += item

            return score_


        your_score = score(your_cards)
        computer_score = score(computer_cards)
        print(f'Your cards: {your_cards}, your score = {your_score}')
        print(f'Computer first card: {computer_cards}, computer_score = {computer_score}')

        take_c = True
        while take_c:
            another_card = input('Type y to get another card and n for pass: ')
            if another_card == 'y':
                new_card = taking_cards(1)
                for item in new_card:
                    your_cards.append(item)

                your_score = score(your_cards)
                computer_score = score(computer_cards)
                print(f'Your cards: {your_cards}, your score = {your_score}')
                print(f'Computer first card: {computer_cards}, computer_score = {computer_score}')

                if your_score < 21:
                    take_c = True
                elif your_score == 21:
                    print(f' Your score: {your_score}, you WIN! 🤩 🥳')
                    take_c = False
                elif your_score > 21:
                    for item in your_cards:
                        if item == A:
                            your_cards.remove(A)
                            your_cards.append(1)
                            your_score = score(your_cards)
                            if your_score > 21:
                                print(f'You Bust! Computer win, computer score: {computer_score} 😭')
                                take_c = False
                        else:
                            pass
                    print(f'You Bust! Computer win, computer score: {computer_score} 😭')
                    take_c = False
            elif another_card == 'n':
                less_than_21 = True
                while less_than_21:
                    new_card = taking_cards(1)
                    for item in new_card:
                        computer_cards.append(item)
                        computer_score = score(computer_cards)

                    print(f'Your cards: {your_cards}, your score = {your_score}')
                    print(f'Computer first card: {computer_cards}, computer_score = {computer_score}')
                    if computer_score < 21:
                        if computer_score < your_score:
                            less_than_21 = True
                        elif computer_score > your_score:
                            print(f'You lost! Computer win, computer score: {computer_score} 😭')
                            less_than_21 = False
                    elif computer_score == 21:
                        print(f'You lost! Computer win, computer score: {computer_score} 😭')
                        less_than_21 = False
                        take_c = False
                    elif computer_score > 21:
                        for item in computer_cards:
                            if item == A:
                                computer_cards.append(A[0])
                                computer_cards.remove(A)
                                computer_score = score(computer_cards)
                                if computer_score < 21:
                                    less_than_21 = True
                                else:
                                    less_than_21 = False
                                    take_c = False

                        else:
                            print(f' Computer Bust! Computer score: {computer_score}')
                            print(f' Your score: {your_score}, you WIN! 🤩 🥳')
                            less_than_21 = False
                            take_c = False
                take_c = False

    elif playgame == 'n':
        again = False
        replit.clear()