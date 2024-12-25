import random

randomNumber = random.randint(1, 100)
# print(randomNumber)
userGuess = None
gusses = 0

while userGuess != randomNumber:
    userGuess = int(input("Enter your guess : "))
    gusses +=1
    if(userGuess == randomNumber):
        print("You guessed it right !")
    else:
        if userGuess > randomNumber:
            print("You guessed it wrong ! Enter a smaller number")
        else:
            print("You guessed it wrong ! Enter a larger number")
        

print(f"You gussed the number in {gusses} gusses")

with open("highScore.txt") as f:
    highScore = int(f.read())

if gusses < highScore:
    print("You have just broken the high score")
    with open("highScore.txt", "w") as f:
        f.write(str(gusses))