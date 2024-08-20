from functools import reduce

l = [3, 6, 2 ,9]

a = reduce(max, l)
print(a)