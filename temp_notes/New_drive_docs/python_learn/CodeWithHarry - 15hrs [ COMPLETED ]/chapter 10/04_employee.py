class Employee:
    # class attribute 
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

harry.salary = 300  # instance attribute
rajni.salary = 400  # instance attribute

print(harry.salary)
print(rajni.salary)

print(harry.company)
print(rajni.company)
Employee.company = "Youtube"
print(harry.company)
print(rajni.company)

