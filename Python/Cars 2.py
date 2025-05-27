class Car:
    def __init__(self,year,doors,color):
        self.year = year
        self.doors = doors
        self.color = color


    def __str__(self):
        return f"Year: {self.year} / Doors: {self.doors} / Color: {self.color}"
    


    def setColor(self,color):
        self.color = color


def parkCar(car1,car2,car3):
    print(car1.year)
    print(car2.year)
    print(car3.year)


def parkCar2(*car):
    print(car[0])


c1 = Car(2010 , 4 , "Black")
c2 = Car(1999 , 4 , "Blue")
c3 = Car(2004 , 2 , "Red")
parkCar(c1,c2,c3)
parkCar2(c1)