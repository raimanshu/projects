greeting = "Good morning, "
name = "Himanshu"

# Contating two strings 
print(greeting + name)

# Slicing a string 
# positive indexes 
print(name[0])
print(name[0:2])
print(name[2:])
print(name[:5])

print(name[:])

# negative indexes 
print(name[-2])
print(name[-3:-1])
print(name[-3:])
print(name[:-3])

# prints blank 
print(name[-3:0])
print(name[-1:-3])
print(name[-1:2])

# Skipping characters using slicing 
print(name[1:5:2])
print(name[0::2])

# prints error 
# print(name[15])

# name[3] = "t"
# print(name[3])