from art import *
from data import *
import time

cost = 0  # var that find the value of cust inside dic t.odo 3
num = 0 # global var that save the type of coffe
money = 0
coffe = ''
go = True

#TODO 1 F: LIGAR

def turn_on():
    global go
    print(logo)
    print('Turn the machine on to start! ')
    turn = input('ON/OFF: ').upper()
    if turn == 'ON':
        print(espresso)
        print(latte)
        print(cappuccino)
        numero = int(input('What would you like? 1, 2 ou 3: '))
        return numero
    elif turn == 'REPORT':
        print(resources)
        print(money)
        go = False
    elif turn == 'OFF':
        go = False
    else:
        print('Erro')
        go = False

#TODO 3 F: CALCULAR PAGAMENTO

def payment():
    global cost
    print()
    print('Please insert coins $$')
    quarters = float(input('How many quarters? $0.25 '))
    soma = quarters * 0.25
    short = cost - soma
    round(short, 2)
    print(f' Money entered = {soma}')
    print(f' Money short = {short}')
    if soma < cost:
        print()
        dimes = float(input('How many dimes? $0.10 '))
        soma += dimes * 0.10
        short = cost - soma
        round(short, 2)
        print(f' Money entered = {soma}')
        print(f' Money short = {short}')
        if soma < cost:
            print()
            nickles = float(input('How many nickles? $0.05 '))
            soma += nickles * 0.05
            short = cost - soma
            round(short, 2)
            print(f' Money entered = {soma}')
            print(f' Money short = {short}')
            if soma < cost:
                print()
                pennies = float(input('How many pennies? $0.01 '))
                soma += pennies * 0.01
                short = cost - soma
                round(short, 2)
                print(f' Money entered = {soma}')
                print(f' Money short = {short}')

    global money
    if soma > cost:
        change = soma - cost
        money += soma
        print(f'Here is your change: {change}')
        return True
    elif soma == cost:
        print('No change')
        return True
    elif soma < cost:
        change = soma - cost
        print(f'You are {change} dollars short! Sorry')
        return False


#TODO 4 F: CHECK STOCK

def make_coffe():
    enough = True
    for item in MENU[coffe]["ingredients"]:
        stock = resources.get(item)
        ele_r = MENU[coffe]["ingredients"][item]
        if stock >= ele_r:
            stock = stock - ele_r
            resources[item] = stock

        else:
            enough = False

    if enough == False:
        print('Recharg machine')
        return False
    else:
        print()
        print('Here is your coffe!')
        print(cup)
        return True



while go == True:

    #TODO 1: LIGAR
    num = turn_on()
    if go == False:
        break

    #TODO 2: DEFINIR O CAFFE
    if num == 1:
        coffe = 'espresso'
        cost = MENU['espresso']['cost']
        print(coffe)
    elif num == 2:
        coffe = 'latte'
        cost = MENU['latte']['cost']
        print(coffe)
    elif num == 3:
        coffe = 'cappuccino'
        cost = MENU['cappuccino']['cost']
        print(coffe)
    else:
        print('Erro')
        go = False

    if go == False:
        break

    #TODO 3: CALCULAR PAGAMENTO
    go = payment()  #go var that can be in a while

    if go == True:
        print()
        print('Warming up the watter')
        time.sleep(5)
        print()
        print('Preparing coffe')
        time.sleep(5)
    if go == False:
        break


    #TODO 4: CHECK STOCK
    go = make_coffe()
    if go == False:
        break
    if go == True:
        time.sleep(10)


