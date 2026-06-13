def get_secret_number():
    while True:

        try:
            guess = int(input("Enter the Number Must be 3 Digits: "))
            if 100 <= guess <= 999:
                return guess

        except ValueError:
            print("Please Enter a Valid Number!")


def get_guess():
    while True:

        try:
            return int(input("Guess the Number : "))

        except ValueError:
            print("Please Enter a Valid Number!")


def check_guess(secret, guess):

    if secret == guess:
        return "Correct"

    elif guess < secret:
        return "Higher"

    else:
        return "Lower"


def calculate_score(chances_left):
    return chances_left * 20


def play_game():
    secret_number = get_secret_number()
    print("\n" * 44)
    chances = 5

    while chances > 0:
        print(f"\nRemainig Chances: {chances}")
        guess = get_guess()
        result = check_guess(secret_number, guess)

        if result == "Correct":
            score = calculate_score(chances)
            print("\nCongratulations!")
            print("You Guessed Correctly.")
            print(f"Score: {score}")
            return

        elif result == "Higher":
            print("The Number is Bigger.")

        else:
            print("The Number is Smaller.")

        chances -= 1
    print("\nGame Over!")
    print(f"The Correct Number Was : {secret_number}")


def play_again():
    while True:
        answer = input("\nPlay Again?(y/n) : ").lower()

        if answer in ["y", "n"]:
            return answer == "y"
        print("Please Enter y or n")


def main():
    while True:
        play_game()

        if not play_again():
            print("Goodbye")
            break


if __name__ == '__main__':
    main()
    