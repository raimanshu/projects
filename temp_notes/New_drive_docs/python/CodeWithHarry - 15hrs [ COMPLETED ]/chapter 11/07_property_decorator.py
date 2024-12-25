class Employee:
    company = "Bharat Gas"
    salry = 4000
    salaryBonus = 500
    # totalSalary = 4500

    # makes a method like a property/variable 
    # @property decorator is a getter method
    @property
    def totalSalary(self):
        return self.salry + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salry


e = Employee()
print(e.totalSalary)

# to set the value of total salary we have to use getter and setters 
e.totalSalary = 5000
print(e.salry)
print(e.salaryBonus)