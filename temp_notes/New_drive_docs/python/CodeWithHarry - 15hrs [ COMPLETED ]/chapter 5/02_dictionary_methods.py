myDict = {
    "fast" : "In a quick manner",
    "coder" : "Himanshu",
    "marks" : [1, 2, 5], 
    "anotherDict" : {
        'name' : "raimanshu"
    },
    1 : 2
}

# prints the keys of dictionary 
print(myDict.keys())

# prints the values of dictionary 
print(myDict.values())

# prints the (keys, value) pair ofdictionary as tuples
print(myDict.items())

# add contents in the dictionary 
updateDict = {
    "lovish" : "friends"
}
myDict.update(updateDict)
print(myDict)

# access the dictionary 
print(myDict.get("coder")) # not throw an error if not found
print(myDict["coder"]) # throw an error if not found

# prints type of dictionary variable 
print(type(myDict.keys()))

# typecasting dictionary into list 
print(list(myDict.keys()))