import random

computerScore = 0
playerScore = 0

# operations-----------------------------------------
def choiceGenerator():
    choices = ["R", "P", "S"]
    return random.choice(choices)

def printScore(myChoice, computerChoice):
    print(f"my choice is: {myChoice} \nComputer's choice: {computerChoice}")
    print(f"I won: {playerScore} times \nComputer won: {computerScore} times")


# interface------------------------------------------
print(f"press 'R' for rock \npress 'P' for paper \nAnd press 'S' for scissors \nBest of three wins \n")

while(playerScore < 3 and computerScore < 3):
    myChoice = input()
    computerChoice = choiceGenerator()

    if myChoice == computerChoice:
        print("Tie")
        printScore(myChoice, computerChoice)

    elif myChoice == "R":
        if computerChoice == "P":
            print("computer wins")
            computerScore += 1
            printScore(myChoice, computerChoice)

        elif computerChoice == "S":
            print("player wins")
            playerScore += 1
            printScore(myChoice, computerChoice)


    elif myChoice == "P":
        if computerChoice == "S":
            print("computer wins")
            computerScore += 1
            printScore(myChoice, computerChoice)

        elif computerChoice == "R":
            print("player wins")
            playerScore += 1
            printScore(myChoice, computerChoice)


    elif myChoice == "S":
        if computerChoice == "R":
            print("computer wins")
            computerScore += 1
            printScore(myChoice, computerChoice)

        elif computerChoice == "P":
            print("player wins")
            playerScore += 1
            printScore(myChoice, computerChoice)


#UI------------------------------------
if computerScore < playerScore:
    print("Player Wins")

else:
    print("Computer Wins")