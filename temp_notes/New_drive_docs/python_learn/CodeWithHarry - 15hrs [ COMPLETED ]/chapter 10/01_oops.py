# procedural oriented programming 
a = 2
b = 5

print(f"The sum of a and b is : {a+b}")

# object oriented programming 
class Number:                              # class is defined
    def sum(self):
        return self.a + self.b

num = Number()                             # object instantiation
num.a = 2
num.b = 5
s = num.sum()
print(f"The sum of a and b is : {s}")

