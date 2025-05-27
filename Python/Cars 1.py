class Car:
    def __init__(self,year,doors,color):
        self.year = year
        self.doors = doors
        self.color = color
    


    def setColor(self,color):
        self.color = color


c1 = Car(2000,5,"Black")
c2 = Car(1999,4,"Silver")
c3 = Car(2004,4,"Red")
c1.setColor("Blue")
print(c1.color)
