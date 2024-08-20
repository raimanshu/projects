
# for handeling all tyoes of error in one except 

# try:
#     a = int(input("Enter a number : "))
#     c = 1/a
#     print(c)
# except Exception as e:
#     print("Exception occured ")
#     print(e)

# print("Thanks for using this code !")

# for handeling different types of error in one except 
try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value ")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0 ")
    print(e)
except Exception as e:
    print("Exception Error")
    print(e)

print("Thanks for using this code !")