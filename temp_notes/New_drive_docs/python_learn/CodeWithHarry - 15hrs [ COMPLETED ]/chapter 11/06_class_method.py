class Employee:
    company = "camel"
    salary = 100 #class attribute
    location = "Delhi"

    # will add value to instance of Employee
    # def changeSalary(self, sal):
    #     self.salary = sal

    # will add value of class attribute of Employee
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    # will add value of class attribute of Employee
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)