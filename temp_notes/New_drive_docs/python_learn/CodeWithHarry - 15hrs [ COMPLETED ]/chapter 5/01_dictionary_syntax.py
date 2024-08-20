myDict = {
    "Fast" : "In a quick manner",
    "Coder" : "Himanshu",
    "Marks" : [1, 2, 5], 
    "anotherDict" : {
        'name' : "raimanshu"
    }
}

print(myDict["Fast"])
print(myDict["Marks"])

myDict["Marks"] = [45, 28]
print(myDict["Marks"])

print(myDict["anotherDict"]['name'])

# Dot accessing is not possible in dictionary
# print(myDict.anotherDict)