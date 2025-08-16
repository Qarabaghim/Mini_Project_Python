import random


def guess(user_guess):
    if not user_guess.isdigit():
        print("Invalid input. Please enter a number.")
        return False

    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > 100:
        print("Please enter a number between 1 and 100")
        return False

    return True


def start_game():
    random_num = random.randint(1, 100)
    score = 9
    print(f"Welcome to the Guess Game! You have {score} guesses left. and Press 'q' to exit the game.")

    while True:
        user_guess = input("Guess a number between 1 and 100: ")


        if user_guess == 'q':
            print("Goodbye!")
            break

        if not guess(user_guess):
            continue

        user_guess = int(user_guess)
        if user_guess == random_num:
            score += 1
            print(f"wooooooooooow You guessed right! Your score is {score}")
            new_game = input('new play game!?(y/n)')

            if new_game == 'y':
                random_num = random.randint(1, 100)
                score = 9
                continue
            elif new_game == 'n':
                print("Thank you for playing")
                break
            else:
                print("You entered the wrong option!")
                continue


        elif user_guess < random_num:
            print(f"Too low! score: {score}")


        elif user_guess > random_num:
            print(f"Too high! score: {score}")

        score -= 1
        if score == 0:
            print("Game over")
            break
        score = max(score, 0)


if __name__ == '__main__':
    start_game()