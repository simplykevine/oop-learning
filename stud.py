class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

john = Student("John", "Computer Science")
type(john)
class __main__Student:

    john.__class__ = Person
type(john)