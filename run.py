from random import randint

#Creates a list of playable actions
t = ["Rock", "Paper", "Scissors"]

#Assigns a random player to the computer
computer = t[randint(0, 2)]

#Sets Palyer to false
player = False

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





#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]