l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"The {index+1} element is {item}")
    