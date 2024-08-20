class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person....")
    def takeBreath(self):
        print("I am breathing ....")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee....")
    def getSalary(self):
        print(f"Salary is : {self.salary}")
    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am breathing")

class Programmer(Employee):
    company = "Fiver"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer....")
    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
        super().takeBreath()
        print("I am an programmer so I am breathing")

# p = Person()
# print(p.takeBreath())
# e = Employee()
# print(e.takeBreath())
pr = Programmer()
# print(pr.takeBreath())

