# when try throws an  exception print("We were done") will not run because of exit() method

# try:
#     i = int( input("Enter a number : ") )
#     c = 1/i 
# except Exception as e:
#     print(e)
#     exit()

# print("We were done")



# when try throws an  exception print("We were done") will also run even it has exit() method
try:
    i = int( input("Enter a number : ") )
    c = 1/i 
except Exception as e:
    print(e)
    exit()
finally:
    print("We were done")

print("Thanks for using the program")