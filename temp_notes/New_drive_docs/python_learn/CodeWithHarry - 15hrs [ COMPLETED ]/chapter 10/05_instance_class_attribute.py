class Employee:
    # class attribute 
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# creating instance attributes 
# harry.salary = 300  # instance attribute
# rajni.salary = 400  # instance attribute

print(harry.salary)
print(rajni.salary)

# throws an error as address is not present in class 
# print(rajni.address)