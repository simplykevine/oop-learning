class mammals:
    # name, height, breed, size, shape ,number of legs , colour 
    # mammals move,give birth, breast feed, eat , sleep, protect
    def __init__(self,name,NumberOfLegs):
        self.name=name
        self.NumberOfLegs=NumberOfLegs
    def move(self):
        print(f"This {self.name} uses {self.NumberOfLegs} to move")
    def eat(self):
        print("this animal eats")

dog=mammals("Chihuahua",4)
dog.move()