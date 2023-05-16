from classes.game import colors
import random


# Input for player to choose from
def get_player_move():
    while True:
        player_move = input("Please Select a choice: (rock/paper/scissors: ").lower()
        if player_move == "":
            print("Please enter an valid choice")
        elif player_move not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
        else:
            return player_move


# To detremine the winner through each scenario
def decide_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a Tie!"
    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or 
        (player_move == "scissors" and computer_move == "paper")
    ):
        return "Player Wins!"
    else:
        return "Computer Wins!"


def display_title():
    print(r"""
    ██████  ██████  ███████
    ██  ██  ██  ██  ██
    ██████  ██████  ███████
    ██   ██ ██           ██
    ██   ██ ██      ███████
    """)


def rules_page():
    print(colors.GREEN + "RULES OF THE GAME:")
    print(colors"THE PLAYER MUST SELECT BETWEEN ROCK PAPER OR SCISSORS")
    print("THE COMPUTER THEN CHOOSES AT RANDOM")
    print("THE WINNER IS DECIDED BY 3 ROUNDS")
    print()


def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    total_rounds = 3
    player_score = 0
    computer_score = 0

    display_title


"""
import random

def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    total_rounds = 3
    player_score = 0
    computer_score = 0

    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        for round in range(1, total_rounds + 1):
            print(f"Round {round}:")
            player_move = get_player_move()

            # Randomly generate the computer's move
            computer_move = random.choice(valid_moves)

            print("Player chooses:", player_move)
            print("Computer chooses:", computer_move)

            result = determine_winner(player_move, computer_move)
            print(result)

            if result == "Player wins!":
                player_score += 1
            elif result == "Computer wins!":
                computer_score += 1

        print("Final Scores:")
        print("Player score:", player_score)
        print("Computer score:", computer_score)

        if player_score > computer_score:
            print("Congratulations! Player wins the game!")
        elif player_score < computer_score:
            print("Computer wins the game!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "yes":
            player_score = 0
            computer_score = 0
            continue
        else:
            break

play_game()
