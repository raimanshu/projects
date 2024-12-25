num = int(input("Enter the number : \n"))

for i in range(1, 11):
    print(str(num) + ' x ' + str(i) +  " = " + str(i * num)) 


# Using f strings 
print("Using f strings")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")