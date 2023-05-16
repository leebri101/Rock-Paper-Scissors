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
    print("\n" + colors.GREEN + "RULES OF THE GAME:")
    print(colors.BLUE + colors.BOLD + "PLAYER MUST SELECT BETWEEN ROCK PAPER OR SCISSORS")
    print(colors.BLUE + colors.BOLD + "THE COMPUTER THEN CHOOSES AT RANDOM")
    print(colors.RED + colors.BOLD + "THE WINNER IS DECIDED BY 3 ROUNDS")
    print()


def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    total_rounds = 3
    player_score = 0
    computer_score = 0

    display_title()
    rules_page()

    while True:
        for round in range(1, total_rounds + 1):
            print(f"Round {round}:")
            player_move = get_player_move()

            # Random generation of computer's move
            computer_move = random.choice(valid_moves)

            print(f"{colors.BLUE}Player Chose: {player_move}{colors.END}")
            print(f"{colors.RED}Computer Chose: {computer_move}{colors.END}")

            result = decide_winner(player_move, computer_move)
            print(result)

            if result == "Player Wins!":
                player_score += 1
            elif result == "Computer Wins...":
                computer_score += 1
        
        print(f"{colors.CYAN}{colors.BOLD}FINAL SCORES:")
        print(f"{colors.BLUE}Player Score: {player_score}{colors.END}")
        print(f"{colors.RED}Computer Score: {computer_score}{colors.END}")

        if player_score > computer_score:
            print(r"""
            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗██╗
            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║██║
             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║██║
              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝╚═╝
               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗██╗
               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝
            """)
        elif player_score < computer_score:
            print(r"""
            ██╗   ██╗ ██████╗ ██╗   ██╗   ██╗      ██████╗ ███████╗███████╗
            ╚██╗ ██╔╝██╔═══██╗██║   ██║   ██║     ██╔═══██╗██╔════╝██╔════╝
             ╚████╔╝ ██║   ██║██║   ██║   ██║     ██║   ██║███████╗█████╗
              ╚██╔╝  ██║   ██║██║   ██║   ██║     ██║   ██║╚════██║██╔══╝        
               ██║   ╚██████╔╝╚██████╔╝   ███████╗╚██████╔╝███████║███████╗
               ╚═╝    ╚═════╝  ╚═════╝    ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
            """)
        else:
            print(r"""
            ████████╗██╗███████╗
            ╚══██╔══╝██║██╔════╝
               ██║   ██║█████╗
               ██║   ██║██╔══╝
               ██║   ██║███████╗██╗██╗██╗██╗
               ╚═╝   ╚═╝╚══════╝╚═╝╚═╝╚═╝╚═╝
            """)



"""

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