class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaeryAfterIncrement(self):
        return self.salary * self.increment

    @salaeryAfterIncrement.setter
    def salaeryAfterIncrement(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.salaeryAfterIncrement)
print(e.increment)
e.salaeryAfterIncrement = 2000
print(e.increment)