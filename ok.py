class Animal:
    def _init_(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"
    #create a function that can identify a class of animal
class Mammal (Animal):
    def _init_(self, name, sound, num_legs):
        super()._init_(name, sound)
        self.num_legs = num_legs
    
    def has_fur(self):
        return True
Dog = Mammal("dog", "bark", 4)

print(Dog.has_fur())