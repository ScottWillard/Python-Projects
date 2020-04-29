import random

playAgain = ''

def guess():
    x = random.randint(1, 10)
    userNum = int(input("Guess the number: \n"))

    while userNum != x:

        if userNum > x:
            print("Too high, try again: ")
            userNum = int(input())

        elif userNum < x:
            print("Too low, try again: ")
            userNum = int(input())

        if userNum == x:
            print("Correct!\n")


while playAgain != "n":

    guess()
    try:
        input("Play again? y/n\n")

    except Exception:
        print("Error")
        input("Play again? y/n\n")

    finally:
        while playAgain != 'y' and playAgain != 'n':
            print("Wrong input, play again? y/n")
            playAgain = input()
