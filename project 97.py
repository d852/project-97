import random

num  = random.randint(1,9)

chances = 0

while True:
    guessedNum = int(input("Enter your guess: "))
    chances += 1
    if(chances < 5):
        if (guessedNum > num):
            print("Try a smaller number")
        elif(guessedNum < num):
            print("Try a bigger number")
        elif(guessedNum == num):
            print("You Won , you guessed the correct number")
            break
    else:
        print("You lost the number was " , num)
        break
        

