myDict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item"
}

print("Options are : ", myDict.keys())
enteredKey = input("Enter the Hindi word : \n")

print("The meaning of your word is : \n",myDict.get(enteredKey))
