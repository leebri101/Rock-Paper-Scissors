from random import randint

#Creates a list of playable actions
t = ["Rock", "Paper", "Scissors"]

#Assigns a random player to the computer
computer = t[randint(0, 2)]

#Sets Palyer to false
player = True

while player == False:
    player = input("Choose either: Rock, Paper, Scissors?")
    if player == computer:
        print("It's a Tie!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose...", computer, "Paper Covers Rock", player)
        else:
            print("You Win!", player, "Rock smashes Scissors", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose...", computer, "Scissors cuts Paper", player)
        else:
            print("You Win!", player, "Rock smashes Scissors", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose...", computer, "Rock smashes Scissors", player)
        else:
            print("You win!", player, "Scissors cuts Paper", computer)
    else:
        print("Invalid in put please check your spelling")
    player = False
    computer = t[randint(0,2)]
