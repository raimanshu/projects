class Employee:
    company ="Google"
    def getSalary(self):
        print(self)
        print("Salary is 100k")


harry = Employee()

# Both line are same, if we remove self parameter from class method it throws an error as Employee.getSalary() takes 0 positional arguments but 1 was given because object harry is passed in class Employee implicitly 
harry.getSalary()
Employee.getSalary(harry)


# If an attribute is not mentioned in the class then use this method to avoid error 
class Employee1:
    company ="Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")


harry1 = Employee1()
harry1.salary = 100000
harry1.getSalary()