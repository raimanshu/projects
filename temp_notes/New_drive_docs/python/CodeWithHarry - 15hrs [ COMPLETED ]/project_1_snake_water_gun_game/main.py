# snake, water and gun game project 
# rock, paper and sissors will also be same 

import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# a = input("Computer sTurn : Snake(s), Water(w) or Gun(g) : \n")

randonNumber = random.randint(1, 3)

if randonNumber == 1:
    comp = 's'
elif randonNumber == 2:
    comp = 'w'
elif randonNumber == 3:
    comp = 'g'


you = input("Your's Turn : Snake(s), Water(w) or Gun(g) : \n")

result = game(comp, you)

print(f"Computer choose : {comp}")
print(f"You choose : {you}")

if result == None:
    print("This game is a tie !!!")
elif result:
    print("You win")
else :
    print("You lose")