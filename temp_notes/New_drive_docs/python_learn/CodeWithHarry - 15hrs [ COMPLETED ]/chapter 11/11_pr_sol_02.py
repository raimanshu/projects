class Animals:
    animalType = "Mamal"

class Pet(Animals):
    color = "White"

class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow !!")

d = Dog()
d.bark()

