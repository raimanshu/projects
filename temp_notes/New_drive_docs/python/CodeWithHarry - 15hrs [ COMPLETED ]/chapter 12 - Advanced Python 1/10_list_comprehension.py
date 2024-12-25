a = [3, 6, 77, 34, 47]

# to append the divisible members of a in b 
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
# print(b)

# to append the divisible members of a in b : Same but in simpler terms
b = [i for i in a if i % 2 == 0]
print(b)


t = [1, 3, 3, 2, 5, 5]
s = {i for i in t}
print(s)