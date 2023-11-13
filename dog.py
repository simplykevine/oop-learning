class Mammal:
    def __init__(self, name, NumberOfLegs):
        self.name = name
        self.NumberOfLegs = NumberOfLegs

    def move(self):
        print(f"This {self.name} uses {self.NumberOfLegs} legs to move")

    def eat(self):
        print("This animal eats")

dog = Mammal("Chihuahua", 4)
dog.move()