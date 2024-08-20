l = [i for i in range(1,50)]

a = filter(lambda a: a%5 == 0,l)

print(list(a))