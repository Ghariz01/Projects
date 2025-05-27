import random

word = ["D","E","L","T","A"]
lives = 6
found = len(word)
letters = []
keyword = ["_","_","_","_","_"]


while (lives > 0 and found > 0):
    print("Exeis akoma",lives,"zwes")
    print("Grammata pou exeis pei",letters)
    print("h leksi pou apomeni",keyword)
    hit = input("Dwse ena gramma sta kefalaia")
    if (hit in word):
        if (hit in letters):
            print("Eipes idio gramma")
            lives = lives - 1
        else:
            x = word.index(hit)
            keyword[x]=hit
            found = found -1
    else:
        lives = lives - 1


    letters.append(hit)


if (lives>0):
    print("You win")
if(found>0):
    print("You lose")
