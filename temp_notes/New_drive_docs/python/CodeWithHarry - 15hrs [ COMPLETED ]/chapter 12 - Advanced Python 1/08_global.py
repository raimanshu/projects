a = 54 #global variable

def func1():
    a = 8 #local variable
    print(a)
def func2():
    global a 
    a = 8 # changing global variable variable
    print(a)

func1()
print(a)

func2()
print(a)