class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiver"
    level = 0

    def upgradeLevel(self):
        self.level = self.level +1

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()

# In class programmer, Employee is written first so it will print Visa 
print(p.company)
