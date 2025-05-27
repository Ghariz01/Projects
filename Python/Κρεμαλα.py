import random

word = "DELTA"
lives = 6
found = len(word)
letters = []


while (lives > 0 and found > 0):
    print("Exeis akoma" , lives , "zwes")
    print(letters)
    hit = input("Dwse ena gramma sta kefalaia")
    if (hit in word):
        if(hit in letters):
            print("Eipes idio gramma")
            lives = lives - 1
        else:
            found = found - 1
    else:
        lives = lives - 1


    letters.append(hit)




if (lives > 0):
    print("You Win")
if (found > 0):
    print("You Lose")