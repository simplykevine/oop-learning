class Mammal:
    #list of mammals include cows, goats, sheep, and horses
    #most mammals have 4 legs except bats
    def _init_(self, name, NumberOfLegs):
        self.name=name
        self.NumberOfLegs=NumberOfLegs
    
    def move(self):
        print(f"This {self.name} has {self.NumberOfLegs} to walk")
    def eat(self):
        print("This animal eat")
        cat = Mammal("max", 4)
        cat.move ()


        


    