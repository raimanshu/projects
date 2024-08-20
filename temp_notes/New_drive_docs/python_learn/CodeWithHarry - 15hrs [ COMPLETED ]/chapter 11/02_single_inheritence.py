# Parent / Base class 
class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee")

# Child / Derived class 
class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmer")

e = Employee()
e.showDetails()

p = Programmer()
# overriding parent class method 
p.showDetails()