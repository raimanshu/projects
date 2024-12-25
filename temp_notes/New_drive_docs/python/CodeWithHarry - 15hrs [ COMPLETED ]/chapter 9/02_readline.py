
f = open("1.txt") #By default, it takes read mode if not mentioned

# read first line 
data = f.readline()
print(data)

# read second line 
data = f.readline()
print(data)

f.close()