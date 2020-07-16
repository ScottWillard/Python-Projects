import random

option = ""
pRCounter = 0
pPCounter = 0
pSCounter = 0
cRCounter = 0
cPCounter = 0
cSCounter = 0


def RPS():
    rps = ["rock", "paper", "scissors"]
    rps2 = ["rock", "paper", "scissors"]
    playerScore = 0
    computerScore = 0
    while playerScore < 10 and computerScore < 10:
        player = input("[Rock/Paper/Scissors] Choose 1 or PRESS 'x' TO QUIT: ")
        computer = random.choice(rps2)
        if player == "x":
            print("Thanks for playing!\n\n")
            exit(0)
        else:
            print("Computer chose: ", computer)

        if computer == player:
            print("Draw\n")
        elif computer == "paper" and player == "rock":
            print("Computer wins!\n")
            computerScore += 1
        elif computer == "rock" and player == "scissors":
            print("Computer wins!\n")
            computerScore += 1
        elif computer == "scissors" and player == "paper":
            print("Computer wins!\n")
            computerScore += 1
        elif player == "paper" and computer == "rock":
            print("You win!\n")
            playerScore += 1
        elif player == "rock" and computer == "scissors":
            print("You win!\n")
            playerScore += 1
        elif player == "scissors" and computer == "paper":
            print("You win!\n")
            playerScore += 1

        print("===========SCORE===========")
        print("Player:", playerScore, "    ", end = ' ')
        print("Computer:", computerScore)
        print("===========================")
        print("\n")
        if playerScore == 10 or computerScore == 10:
            exit(0)


def RPS2():
    playerScore = 0
    computerScore = 0
    while playerScore < 15 and computerScore < 15:
        rps = ["rock", "paper", "scissors"]
        player = random.choice(rps)
        computer = random.choice(rps)
        print("Player chose: ", player)
        print("Computer chose: ", computer)
        if computer == player:
            print("Draw\n")
        elif computer == "paper" and player == "rock":
            # print("Computer wins!\n")
            computerScore += 1
        elif computer == "rock" and player == "scissors":
            # print("Computer wins!\n")
            computerScore += 1
        elif computer == "scissors" and player == "paper":
            # print("Computer wins!\n")
            computerScore += 1
        elif player == "paper" and computer == "rock":
            # print("You win!\n")
            playerScore += 1
        elif player == "rock" and computer == "scissors":
            # print("You win!\n")
            playerScore += 1
        elif player == "scissors" and computer == "paper":
            # print("You win!\n")
            playerScore += 1

        print("===========SCORE===========")
        print("Player:", playerScore, "    ", end = ' ')
        print("Computer:", computerScore)
        print("===========================")
        print("\n")


print("1) You vs. CPU\n2) CPU vs. CPU")
option = input()
if option == '1':
    RPS()
elif option == '2':
    RPS2()
