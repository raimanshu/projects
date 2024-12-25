
# use open() function to read the content of a file 
# f = open("1.txt", "r")
f = open("1.txt") #By default, it takes read mode if not mentioned


# data = f.read()
data = f.read(5) # reads first 5 characters of file


print(data)

f.close()