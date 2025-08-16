n = int(input("Enter Your  happy number: "))


def is_happy(n):
    seen_number = set()
    while n != 1 and n not in seen_number:
        seen_number.add(n)
        digits = [int(i) for i in str(n)]
        squared_digits = [i ** 2 for i in digits]
        print(f"Current number: {n} -> Digits: {digits} -> Squared: {squared_digits} -> Sum: {sum(squared_digits)}")
        n = sum(squared_digits)
    return n == 1


if __name__ == "__main__":
    if is_happy(n):
        print("\n","woooow! This is a happy number!")
    else:
        print("\n","ooooh no! This is not a happy number.")
