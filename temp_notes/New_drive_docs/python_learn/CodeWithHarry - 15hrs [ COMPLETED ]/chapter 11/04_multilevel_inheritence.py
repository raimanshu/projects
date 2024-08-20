class Person:
    country = "India"
    def takeBreadth(self):
        print("I am breathing ....")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is : {self.salary}")
    def takeBreadth(self):
        print("I am an employee so I am breathing")

class Programmer(Employee):
    company = "Fiver"
    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreadth(self):
        print("I am an programmer so I am breathing")
p = Person()
print(p.takeBreadth())
# print(p.company) # throw an error
e = Employee()
print(e.company) 

print(e.takeBreadth())
pr = Programmer()
print(pr.company) 
print(pr.takeBreadth())

