from classes.game import colors
import random

def get_player_move():
    while True:
        player_move = input("Please select a choice (rock/paper/scissors): ").lower()
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
    print(r"""
    ██████  ██████  ███████
    ██  ██  ██  ██  ██
    ██████  ██████  ███████
    ██   ██ ██           ██
    ██   ██ ██      ███████
    """)

def display_rules():
    print(f"{colors.WHITE}{colors.BOLD}================================")
    print("\n" + colors.GREEN + colors.BOLD + "RULES OF THE GAME:" + colors.END)
    print("")
    print(colors.CYAN + colors.BOLD + "You must choose Rock, Paper, or Scissors." + colors.END)
    print("")
    print(colors.CYAN + colors.BOLD + "The computer then chooses at random." + colors.END)
    print("")
    print(colors.GREEN + colors.BOLD + "The first player to win 2 out of 3 rounds wins the game." + colors.END)
    print(f"{colors.WHITE}{colors.BOLD}================================")

def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    display_title()
    display_rules()

    while player_score < 2 and computer_score < 2:
        print("\n" + colors.CYAN + colors.BOLD + ">>>---New Round---<<<" + colors.END)
        player_move = get_player_move()
        computer_move = random.choice(valid_moves)

        print("\n" + colors.BLUE + colors.BOLD + "player chose:", player_move)
        print("\n" + colors.RED + colors.BOLD + "Computer chose:", computer_move)

        winner = decide_winner(player_move, computer_move)

        if winner == "player":
            player_score += 1
            print("\n" + colors.BLUE + colors.BOLD + "Player wins this round!" + colors.END)
        elif winner == "computer":
            computer_score += 1
            print("\n" + colors.RED + colors.BOLD + "Computer wins this round!" + colors.END)
        else:
            print("\n" + colors.WHITE + colors.BOLD + "Tie! Round will be replayed." + colors.END)

        print("\n" + colors.BLUE + colors.BOLD + "Player score:", player_score, colors.END)
        print("\n" + colors.RED + colors.BOLD + "Computer score:", computer_score, colors.END)

    return player_score, computer_score

def display_winner(player_score, computer_score):
    if player_score > computer_score:
        print(r"""
       ██    ██  ██████  ██    ██   ██     ██ ██ ███    ██ ██ ██ 
        ██  ██  ██    ██ ██    ██   ██     ██ ██ ████   ██ ██ ██ 
         ████   ██    ██ ██    ██   ██  █  ██ ██ ██ ██  ██ ██ ██ 
          ██    ██    ██ ██    ██   ██ ███ ██ ██ ██  ██ ██       
          ██     ██████   ██████     ███ ███  ██ ██   ████ ██ ██                                                 
        """)
    else:
        print(r"""
        ██    ██  ██████  ██    ██   ██       ██████  ███████ ███████ 
         ██  ██  ██    ██ ██    ██   ██      ██    ██ ██      ██      
          ████   ██    ██ ██    ██   ██      ██    ██ ███████ █████   
           ██    ██    ██ ██    ██   ██      ██    ██      ██ ██      
           ██     ██████   ██████    ███████  ██████  ███████ ███████ 
        """)

def replay_game():
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            player_score, computer_score = play_game()
            print("\nFinal Scores:")
            print("Player score:", player_score)
            print("Computer score:", computer_score)
            display_winner(player_score, computer_score)
        elif play_again == "n":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue

play_game()
replay_game()