import random

Min,Max=1,100
x=random.randint(Min,Max)
guess = Min -1

left=Min
right=Max
counter=0

while(guess!=x):
    guess=(left+right)//2
    if (x>guess):
        left = guess +1
    elif (x<guess):
        right = guess -1
    counter +=1
    print(guess)

print("The Algorithm Fount It In",counter,"Tries")