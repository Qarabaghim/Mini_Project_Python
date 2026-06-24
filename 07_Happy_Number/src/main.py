happy_number = int(input("Emter Your Happy Number : "))


def is_happy(happy_number):
    seen_number = set()
    while happy_number != 1 and happy_number not in seen_number:
        seen_number.add(happy_number)
        # print("****", seen_number, "****\n")
        digits = [int(i) for i in str(happy_number)]
        # print("****", digits, "****\n")
        squared_digits = [i ** 2 for i in digits]
        # print("****", squared_digits, "****\n")
        print(f"Current number: {happy_number} -> Digits: {digits} -> Squared: {squared_digits} -> Sum: {sum(squared_digits)}")
        happy_number = sum(squared_digits)
    return happy_number == 1


if __name__ == "__main__":
    if is_happy(happy_number):
        print("\n\n","woooow! This is a happy number!")
    else:
        print("\n\n","ooooh no! This is not a happy number.")
