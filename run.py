from classes.game import colors
import random


# Players defined choices
def get_player_move():
    while True:
        print("")
        print(f"{colors.WHITE}{colors.BOLD}================================")
        print("")
        player_move = input("Please select(rock/paper/scissors): ").lower()
        if player_move not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
        else:
            return player_move


# To prompt the user if they want to play again
def continue_game():
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'")


# Winning conditions
def decide_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or
        (player_move == "scissors" and computer_move == "paper")
    ):
        return "player"
    else:
        return "computer"


# Title Display
def display_title():
    print(colors.CYAN)
    print(r"""
    █████    ██████   ██████
    ██   █   █    █  ██
    ██████   █████    █████
    ██   ██  ██           ██
    ██   ██  ██      ██████
    """)


# Display of rules to player
def display_rules():
    print(f"{colors.WHITE}{colors.BOLD}================================")
    print(f"\n{colors.GREEN}{colors.BOLD}RULES: {colors.END}")
    print("")
    print(f"{colors.CYAN}Choose Rock, Paper, or Scissors.{colors.END}")
    print("")
    print(f"{colors.CYAN}Computer then chooses at random.{colors.END}")
    print("")
    print(f"{colors.GREEN}First to win 2 out of 3 wins.{colors.END}")
    print("")
    print("You can also play a single game if you wish")
    print(f"{colors.WHITE}{colors.BOLD}================================")


# Start of game
def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    # Display of title
    display_title()
    print("\n" + colors.BOLD + "Welcome to RPS a rock paper scissors game")
    print("")

    # Input to skip game if user continues game
    if display_rules:
        input("Press Enter to view rules")
        display_rules()
    print("")
    input("Press Enter to start the game")
    while player_score < 2 and computer_score < 2:
        player_move = get_player_move()
        computer_move = random.choice(valid_moves)
        print(f"{colors.WHITE}{colors.BOLD}================================")
        print(f"{colors.BLUE}Player chose: {player_move}{colors.END}")
        print("")
        print(f"\n{colors.RED}Computer chose: {computer_move}{colors.END}")

        winner = decide_winner(player_move, computer_move)

        if winner == "player":
            player_score += 1
            print(f"\n{colors.BLUE}Player wins this round!{colors.END}")
        elif winner == "computer":
            computer_score += 1
            print(f"\n{colors.RED}Computer wins this round!{colors.END}")
        else:
            print(f"\n{colors.BOLD}Tie! Replay Round{colors.END}")
        print(f"{colors.WHITE}{colors.BOLD}================================")
        print(f"\n{colors.BLUE}Player score: {player_score}{colors.END}")
        print(f"\n{colors.RED}Computer score: {computer_score}{colors.END}")

    return player_score, computer_score


# Display of winners after two rounds
def display_winner(player_score, computer_score):
    if player_score > computer_score:
        print("Player Wins")
        print(colors.BLUE + colors.BOLD)
        print(r"""
        ██    ██  ██████  ██    ██   ██     ██ ██ ███    ██
         ██  ██  ██    ██ ██    ██   ██     ██ ██ ████   ██
          ████   ██    ██ ██    ██   ██  █  ██ ██ ██ ██  ██
           ██    ██    ██ ██    ██   ██ ███ ██ ██ ██  ██ ██
           ██     ██████   ██████     ███ ███  ██ ██   ████
        """)
    else:
        print("Computer Wins")
        print(colors.RED + colors.BOLD)
        print(r"""
        ██    ██  ██████  ██    ██   ██       ██████  ███████ ██████
         ██  ██  ██    ██ ██    ██   ██      ██    ██ ██      ██
          ████   ██    ██ ██    ██   ██      ██    ██ ███████ █████
           ██    ██    ██ ██    ██   ██      ██    ██      ██ ██
           ██     ██████   ██████    ███████  ██████  ███████ ██████
        """)


# Inputs to allow player to play again or not
def replay_game():
    display_rules()
    while True:
        if continue_game():
            player_score, computer_score = play_game()
            print("Final Scores:")
            print("")
            print("Player score:", player_score)
            print("")
            print("Computer score:", computer_score)
            print("")
            display_winner(player_score, computer_score)
        else:
            # Anscii art of end game screen
            print(colors.RED + colors.BOLD)
            print(r"""
             ████   ████  █      █ ████   ████  █    █ █████  ████
            █      █    █ ██    ██ █     █    █ █    █ █      █   █
            █  ██  ██████ █ █  █ █ ███   █    █ █    █ ███    ████
            █   █  █    █ █  ██  █ █     █    █  █  █  █      █   █
            ████   █    █ █      █ ████   ████    ██   █████  █    █
            """)
            print(">>>>>>>>>-------THANKS FOR PLAYING-------<<<<<<<<<")
            break


play_game()


replay_game()
