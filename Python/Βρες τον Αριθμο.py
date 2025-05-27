import random

lives = 3
lot = 10
select = random.randint(1,lot)

while lives > 0:
    hit = input("Dwse enan ari8mo apo 1 mexri 10")


    try:
        hit = int(hit)
    except:
        print("Ari8mo mono!")
        continue
    if(hit>10):
        print("1 ews 10")
        continue
    if(hit<1):
        print("1 ews 10")
        continue



    if hit>select:
        print("Shot too far")
        lives = lives - 1
    if hit<select:
        print("Shot too close")
        lives = lives - 1
    if hit == select:
        print("Score")
        break

if (lives>0):
    print("You Win")
else:
    print("You Lose")