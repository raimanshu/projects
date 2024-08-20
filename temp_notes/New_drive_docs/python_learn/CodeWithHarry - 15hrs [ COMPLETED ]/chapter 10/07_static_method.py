class Employee1:
    company ="Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")
    
    @staticmethod
    def greet():
        print("Good morning sir")

    @staticmethod
    def time():
        print("Time is 09:00am")


harry1 = Employee1()
harry1.salary = 100000
harry1.getSalary("Thanks") # Employee1.getSalary(harry1)
harry1.greet()
