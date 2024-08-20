class Employee1:
    company ="Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(self)
        print("Employee is created !!")

    def getDetails(self):
        print(f"The name of the employee is : {self.name}")
        print(f"The salary of the employee is : {self.salary}")
        print(f"The subunit of the employee is : {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")
    
    @staticmethod
    def greet():
        print("Good morning sir")

    @staticmethod
    def time():
        print("Time is 09:00am")

harry = Employee1("harry", 100, "Youtube")

# throws an error ie Employee1.__init__() missing 3 required positional arguments: 'name', 'salary', and 'subunit'
# harry = Employee1() 

harry.getDetails()