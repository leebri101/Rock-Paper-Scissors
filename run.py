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


# To determine the winner through each scenario
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
    print(f"{colors.GREEN}{colors.BOLD}RULES OF THE GAME: {colors.END}")
    print("")
    print(f"{colors.BLUE}{colors.BOLD}PLAYER MUST SELECT BETWEEN ROCK PAPER OR SCISSORS{colors.END}")
    print(colors.BLUE + colors.BOLD + "THE COMPUTER THEN CHOOSES AT RANDOM" + colors.END)
    print(colors.RED + colors.BOLD + "THE WINNER IS DECIDED BY 3 ROUNDS" + colors.END)
    print()


def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    total_rounds = 3
    player_score = 0
    computer_score = 0

    display_title()
    rules_page()

    while player_score < 2 and computer_score < 2:
        player_move = get_player_move()

        # Random generation of computer's move
        computer_move = random.choice(valid_moves)

        print(f"\n{colors.BLUE}Player Chose: {player_move}{colors.END}")
        print("")
        print(f"\n{colors.RED}Computer Chose: {computer_move}{colors.END}")

        winner = decide_winner(player_move, computer_move)
        print(result)

        if winner == "Player":
            player_score += 1
            print(f"\n{colors.BLUE}{colors.BOLD}Player wins this round!{colors.END}")
        elif winner == "Computer":
            computer_score += 1
            print(f"\n{colors.RED}{colors.BOLD}Computer wins this round!{colors.END}")
        else:
            Print(f"\n{colors.CYAN}{colors.BOLD}It's a Tie, round is replayed{colors.END}")

    
    print(f"\n{colors.CYAN}{colors.BOLD}FINAL SCORES: {colors.END}")
    print(f"\n{colors.BLUE}Player Score: {player_score}{colors.END}")
    print(f"\n{colors.RED}Computer Score: {computer_score}{colors.END}")

    if player_score > computer_score:
        print(r"""
        ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗██╗
        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║██║
         ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║██║
          ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝╚═╝
           ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗██╗
           ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝
        """)
    else:
        print(r"""
        ██╗   ██╗ ██████╗ ██╗   ██╗   ██╗      ██████╗ ███████╗███████╗
        ╚██╗ ██╔╝██╔═══██╗██║   ██║   ██║     ██╔═══██╗██╔════╝██╔════╝
         ╚████╔╝ ██║   ██║██║   ██║   ██║     ██║   ██║███████╗█████╗
          ╚██╔╝  ██║   ██║██║   ██║   ██║     ██║   ██║╚════██║██╔══╝        
           ██║   ╚██████╔╝╚██████╔╝   ███████╗╚██████╔╝███████║███████╗
           ╚═╝    ╚═════╝  ╚═════╝    ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
        """)

    play_again = input("Do you want to play again? (y/n): ").lower()
    while play_again not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'no' .")
        play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again == "y":
        player_score = 0
        computer_score = 0
        continue
    else:
        break

play_game()
