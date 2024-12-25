num1 = int(input("Enter number 1 : \n"))
num2 = int(input("Enter number 2 : \n"))
num3 = int(input("Enter number 3 : \n"))
num4 = int(input("Enter number 4 : \n"))

if(num1 > num4):
    f1 = num1
else:
    f1 = num4 

if(num1 > num3):
    f2 = num1
else:
    f2 = num3

if(f1 > f2):
    print(str(f1) + " is the greatest")
else:
    print(str(f2) + " is the greatest")