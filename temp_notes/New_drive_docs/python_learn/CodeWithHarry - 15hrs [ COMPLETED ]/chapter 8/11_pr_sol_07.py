def remove_and_split(str, word):
    newStr = str.replace(word, "")
    return newStr.strip()

comment = "      This is a sentence        "

n = remove_and_split(comment, "This")

print(n)