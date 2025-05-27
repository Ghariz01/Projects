import random


replay = "yes"
tries_per_run = []

while (replay.lower()=="yes"):
    x = random.randint(1,100)

    guess = int(input("Guess A Number Between 1 And 100"))
    counter = 1

    while(guess!=x):
        if(guess>x):
            print("Too High")
        else:
            print("Too Low")
        guess = int(input("Try Again"))
        counter +=1
    tries_per_run.append(counter)
    print("You Guessed Correctly! It Took You",counter,"Tries")
    replay = input("Do You Want To Play Again? (yes/no)")

sum = 0
n = len(tries_per_run)

for i in range(len(tries_per_run)):
    sum += tries_per_run[i]

print("It Took You On Average",sum/n,"Tries")