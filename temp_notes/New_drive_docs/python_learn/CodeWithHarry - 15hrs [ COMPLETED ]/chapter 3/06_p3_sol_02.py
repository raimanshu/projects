letter = '''Dear <|name|>,
You are selected!

Date: <|DATE|>'''

name = input("Enter your name :\n")
date = input("Enter date :\n")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)
