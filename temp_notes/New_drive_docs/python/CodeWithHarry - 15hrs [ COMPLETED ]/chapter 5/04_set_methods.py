# Create an empty set 
a = set()
print(a)
print(type(a))

# adding element in set but donot contain duplicate values
a.add(4)
a.add(4)
a.add(4)
a.add(5)
a.add(5)
a.add(5)

print(a)

# tuple can be added in set 
a.add((4, 5, 6))
print(a)

# dictionary cannot be added in set 
# a.add({"name" : "Himanshu"})
# print(a)

# list cannot be added in set 
# a.add([4, 5, 6])
# print(a)

# prints the length of set 
print(len(a))

# prints union 
print("The intersection of {5, 11} is : ", a.intersection({5, 11}))

# prints intersection 
print("The union of {5, 11} is : ", a.union({5, 11}))

# remove item from set 
# donot throw an error
a.remove(4) 
# throw an error
# a.remove(15) 
print(a)

# pop an item from set 
print(a)
print(a.pop())
print(a)



# empty the set 
a.clear()
print(a)