import random


ans = 'y'
cash = 100
while(ans=='y'):
    bet=0
    while bet<5 :
        bet = int(input('place your bet (min 5$)'))
        if bet>cash:
            print('invalid amount')
            bet = 0


    player = (random.randint(1,6),random.randint(1,6))
    pc = (random.randint(1,6),random.randint(1,6))


    if (player[0]==player[1] and pc[0]==pc[1]):
        if player[0]>pc[0]:
            print(f'player wins{bet}$')
            cash +=bet
        elif player[0]==pc[0]:
            print('Tie')
        else:
            print(f'pc wins,you lost {bet}$')
            cash -=bet
    elif (player[0]+player[1]>pc[0]+pc[1]):
        print(f'player wins {bet}$')
        cash +=bet
    elif (player[0]+player[1]==pc[0]+pc[1]):
        print('Tie')
    else:
        print(f'pc wins,you lost {bet}$')
        cash -=bet

    while (ans!='y' or ans!='n'):
        ans = input('Do you want to play again? (y/n)')      #Not working properly
        