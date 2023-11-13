class Mammal:
    def __init__(self, name, NumberOfLegs):
        self.name = name
        self.NumberOfLegs = NumberOfLegs

    def move(self):
        print(f"This {self.name} uses {self.NumberOfLegs} legs to move.")

    def eat(self):
        print("This animal eats.")

# Create an instance of the Mammal class
choice = input("Enter the type of animal you want: ")
names = input("what is the name of that animal: ")
legs = input("what is the number of legs does it have: ")
choice=Mammal(names,legs)
# Call the move method
choice.move()