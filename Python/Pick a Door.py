import random

prize=random.randint(1,3)

guess=int(input('select a door:(1,2,3)'))

while (guess not in {1,2,3}):
    guess=int(input('select a valid number'))


doors=[0,0,0]
doors[prize-1] = 1
guess[prize-1] = 1


for i in range (len(doors)):
    if (doors[i]==0):
        print('door' + str(i+1) + 'is empty')
        break


choise = input('do you want other door?(yes/no)')

while(choise!='yes' and choise!='no'):
    choise=input('yes or no')

if(choise=='no'):
    if(guess==prize):
        print('you won')
    else:
        print('you lose') #Same Problem with 2