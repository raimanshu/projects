# write program 1 in reverse order 

num = int(input("Enter the number : \n"))

for i in reversed(range(1, 11)):
    print(str(num) + ' x ' + str(i) +  " = " + str(i * num)) 