class Calculartor:
    def __init__(self, num):
        self.number = num

    @staticmethod
    def greet():
        print("Hello there, This is the best calculator in the world !!!")

    def square(self):
        print(f"The square of {self.number} is : {self.number ** 2}")

    def cube(self):
        print(f"The cube of {self.number} is : {self.number ** 3}")

    def squareRoot(self):
        print(f"The square root of {self.number} is : {self.number ** 0.5}")

a = Calculartor(3)
a.greet()
a.square()
a.squareRoot()
a.cube()