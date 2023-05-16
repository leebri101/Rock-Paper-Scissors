from classes.game import colors
import random


def get_player_move():
    while True:
        player_move = input("Please select(rock/paper/scissors): ").lower()

        if player_move not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
        else:
            return player_move


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


def display_title():
    print(colors.CYAN)
    print(r"""
    █████    ██████   ██████
    ██   █   █    █  ██
    ██████   █████    █████
    ██   ██  ██           ██
    ██   ██  ██      ██████
    """)


def display_rules():
    print(f"{colors.WHITE}{colors.BOLD}================================")
    print(f"\n{colors.GREEN}{colors.BOLD}RULES: {colors.END}")
    print("")
    print(f"{colors.CYAN}Choose Rock, Paper, or Scissors.{colors.END}")
    print("")
    print(f"{colors.CYAN}Computer then chooses at random.{colors.END}")
    print("")
    print(f"{colors.GREEN}First to win 2 out of 3 wins.{colors.END}")
    print("You can also play a single game if you wish")
    print(f"{colors.WHITE}{colors.BOLD}================================")


def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    display_title()
    print("\n" + "Welcome to RPS a simple rock paper scissors game")

    input("Press Enter to view rules")
    display_rules()

    input("Press Enter to start the game")
    while player_score < 2 and computer_score < 2:
        player_move = get_player_move()
        computer_move = random.choice(valid_moves)

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

        print(f"\n{colors.BLUE}Player score: {player_score}{colors.END}")
        print(f"\n{colors.RED}Computer score: {computer_score}{colors.END}")

    return player_score, computer_score


def display_winner(player_score, computer_score):
    if player_score > computer_score:
        print("Player Wins")
        print(colors.BLUE)
        print(r"""
        ██    ██  ██████  ██    ██   ██     ██ ██ ███    ██
         ██  ██  ██    ██ ██    ██   ██     ██ ██ ████   ██
          ████   ██    ██ ██    ██   ██  █  ██ ██ ██ ██  ██
           ██    ██    ██ ██    ██   ██ ███ ██ ██ ██  ██ ██
           ██     ██████   ██████     ███ ███  ██ ██   ████
        """)
    else:
        print("Computer Wins")
        print(colors.RED)
        print(r"""
        ██    ██  ██████  ██    ██   ██       ██████  ███████ ██████
         ██  ██  ██    ██ ██    ██   ██      ██    ██ ██      ██
          ████   ██    ██ ██    ██   ██      ██    ██ ███████ █████
           ██    ██    ██ ██    ██   ██      ██    ██      ██ ██
           ██     ██████   ██████    ███████  ██████  ███████ ██████
        """)


def replay_game():
    while True:
        play_again = input("\n" + "Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            player_score, computer_score = play_game()
            print("Final Scores:")
            print("")
            print("Player score:", player_score)
            print("")
            print("Computer score:", computer_score)
            display_winner(player_score, computer_score)
            break
        elif play_again == "n":
            print(colors.RED)
            print(r"""
             ████    ████  █      █ ████   ████  █    █ █████  ████
            █       █    █ ██    ██ █     █    █ █    █ █      █   █
            █   ██  ██████ █ █  █ █ ███   █    █ █    █ ███    ████
            █    █  █    █ █  ██  █ █     █    █  █  █  █      █   █
             ████   █    █ █      █ ████   ████    ██   █████  █    █
            """)
            print(">>>>>>>>>-------THANKS FOR PLAYING-------<<<<<<<<<")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue


play_game()


replay_game()
