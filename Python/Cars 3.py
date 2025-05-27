class Car:
    def __init__(self,year,doors,color):
        self.year = year
        self.doors = doors
        self.color = color


    def __str__(self):
        return f"Year: {self.year} / Doors: {self.doors} / Color: {self.color}"
    


    def setColor(self,color):
        self.color = color


def parkCar(*car):
    print(type(car))
    print(len(car))
    print(lots)


    for i in car:
        print(i)


lots = 20
c1 = Car(2010 , 4 , "Black")
c2 = Car(1999 , 4 , "Blue")
c3 = Car(2004 , 2 , "Red")
parkCar(c1,c2,c3)

for j in "banana":
    if j == "n":
        continue
    print(j)