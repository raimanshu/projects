names = ["A", "B", "C", "D"]

enteredName = input("Enter a name : \n")

if(enteredName in names):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")