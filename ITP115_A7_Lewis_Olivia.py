# Olivia Lewis
# ITP 115, Fall 2019
# A7
# olewis@usc.edu
# Rock, Paper, Scissors
import random
# function to display to the user the main menu
def displayMenu():
    print("Welome! Let's play Rock, Paper, Scissors!")
    print("The rules of the game are:")
    print("\tRock smashes scissors.")
    print("\tScissors cut paper.")
    print("\tPaper covers rock.")
    print("\tIf both choices are the same, it is a tie.")
    print("Please choose (0) for Rock, (1) for Paper, or (2) for Scissors.")
# get the randomized choice from the computer
def getComputerChoice():
    computerChoice = random.randint(0, 2)
    return computerChoice
# get the inputted choice from the user
def getPlayerChoice():
    playerChoice = int(input(">"))
    return playerChoice
# compare the values from the player's choice and the computer's choice, and assign a result variable
def playRound(playerChoice, computerChoice):
    if playerChoice == 0:
        print("You chose Rock.")
        if computerChoice == 0:
            print("The computer also chose Rock.\nIt's a tie.")
            result = 0
            return result
        elif computerChoice == 1:
            print("The computer chose Paper.\nThe computer wins.")
            result = -1
            return result
        elif computerChoice == 2:
            print("The computer chose Scissors.\nYou win.")
            result = 1
            return result
    elif playerChoice == 1:
        print("You chose Paper.")
        if computerChoice == 0:
            print("The computer chose Rock.\nYou win.")
            result = 1
            return result
        elif computerChoice == 1:
            print("The computer also chose Paper.\nIt's a tie.")
            result = 0
            return result
        elif computerChoice == 2:
            print("The computer chose Scissors.\nThe computer wins.")
            result = -1
            return result
    elif playerChoice == 2:
        print("You chose Scissors.")
        if computerChoice == 0:
            print("The computer chose Rock.\nThe computer wins.")
            result = -1
            return result
        elif computerChoice == 1:
            print("The computer chose Paper.\nYou win.")
            result = 1
            return result
        elif computerChoice == 2:
            print("The computer also chose Scissors.\nIt's a tie.")
            result = 0
            return result
# determine whether or not the user wants to continue playing
def continueGame():
    anotherGame = input("Would you like to play again? (y/n): ")
    if anotherGame == "y" or anotherGame == "Y":
        runAgain = True
    else:
        runAgain = False
    return runAgain
# main function runs all the information from the functions above and displays the game to the user.
def main():
    playerWins = 0
    computerWins = 0
    ties = 0
    runAgain = True
    while runAgain:
        displayMenu()
        computer = getComputerChoice()
        player = getPlayerChoice()
        winner = playRound(player, computer)
        if winner == -1:
            computerWins += 1
        elif winner == 1:
            playerWins += 1
        elif winner == 0:
            ties += 1
        runAgain = continueGame()
        if runAgain == False:
            print()
            print("The computer won", computerWins, "game(s).")
            print("You won", playerWins, "game(s).")
            print("You tied with the computer", ties, "time(s).")

main()




