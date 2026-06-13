import random


choices = ["rock", "scissors", "paper"]

def get_player_choice():
    guess = input(f"Enter your choice {choices}: ").lower()
    return guess


def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice


def winner(player, computer):
    if player == computer:
        return "Equal"
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"


def show_result(player, computer, result):
    Display_result = f"Your choice: {player}, Computer's choice: {computer}. Result: {result}"
    print(Display_result)


def play_again():
    play = input("Enter Play Again (Y/N): ").lower()
    if play == "y":
        main()
    else:
        print("Goodbye!")


def main():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = winner(player_choice, computer_choice)
    show_result(player_choice, computer_choice, result)
    play_again()


if __name__ == "__main__":
    main()
