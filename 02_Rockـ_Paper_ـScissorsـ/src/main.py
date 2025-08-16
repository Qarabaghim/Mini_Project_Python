import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choice: list[str] = ['rock', 'paper', 'scissors']

    def user(self) -> str:
        user_choice: str = input(f"enter your choices {self.choice}: ")
        if user_choice in self.choice:
            return user_choice
        else:
            print("invalid choice")
            return self.user()

    def computer(self) -> str:
        return random.choice(self.choice)

    def winner(self, user_choice: str, computer_choice: str) -> str:
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "you win!"
        else:
            return "oh no! the computer win"

    def play(self):
        user_choice = self.user()
        computer_choice = self.computer()
        print("choice user :", user_choice, " ;choice computer : ", computer_choice)
        print("winner :", self.winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissorsGame()

    while True:
        game.play()
        continue_game = input("Do you want to play again?(y/n) ")
        if continue_game.lower() == 'n':
            print("godboy!")
            break
        elif continue_game == 'y':
            continue