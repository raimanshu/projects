# https://refactoring.guru/design-patterns/prototype

# It allows cloning objects, even complex ones, without coupling to their specific classes.

# https://www.geeksforgeeks.org/prototype-method-python-design-patterns/?ref=rp
"""
Prototype Design Pattern:
Definition: The Prototype Pattern is a creational design pattern that allows cloning existing objects to create new instances, rather than creating new objects from scratch.

Problem Before Implementation:
Issue: Creating a new object can be costly if it involves complex setup or resources. Cloning can save time and resources.


"""


import copy


# Base Prototype class
class Prototype:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def clone(self):
        # This method uses deepcopy to clone the object
        return copy.deepcopy(self)


# Concrete class 1
class Car(Prototype):
    def __init__(self, name, description, brand, model):
        super().__init__(name, description)
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car(Name: {self.name}, Description: {self.description}, Brand: {self.brand}, Model: {self.model})"


# Concrete class 2
class Bike(Prototype):
    def __init__(self, name, description, type_of_bike, color):
        super().__init__(name, description)
        self.type_of_bike = type_of_bike
        self.color = color

    def __str__(self):
        return f"Bike(Name: {self.name}, Description: {self.description}, Type: {self.type_of_bike}, Color: {self.color})"


# Client code
if __name__ == "__main__":
    # Creating an initial Car object
    car1 = Car("Sports Car", "A fast and luxurious sports car", "Ferrari", "488 Spider")

    # Cloning the Car object
    car2 = car1.clone()
    car2.model = "F8 Spider"  # Changing the model in the cloned object

    # Creating an initial Bike object
    bike1 = Bike("Mountain Bike", "A rugged mountain bike", "Mountain", "Red")

    # Cloning the Bike object
    bike2 = bike1.clone()
    bike2.color = "Blue"  # Changing the color in the cloned object

    # Print objects
    print(car1)  # Original car
    print(car2)  # Cloned car with modified model
    print(bike1)  # Original bike
    print(bike2)  # Cloned bike with modified color
