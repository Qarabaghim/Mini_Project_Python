from typing import List


class BankAccount:
    Allan: List[int] = []
    lstan = 999

    def __init__(self, name: str) -> None:
        BankAccount.lstan += 1
        an = BankAccount.lstan
        self.account_number: int = an
        BankAccount.Allan.append(an)
        self.name = name
        self.balance: float = 0

    def display(self) -> None:
        print(44 * "_")
        print(f"hi, {self.name}\nYour current balance: {self.balance}")
        print(44 * "_")

    def deposit(self) -> None:
        amount = float(input("please enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        amount = float(input("please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
        self.display()


def main():
    acc1 = BankAccount("mamad")
    acc1.display()
    print(f"account_numbers: {acc1.account_number}")
    while True:
        choice = int(input("1-to see your balance\n2-to deposit\n3-to withdraw\n4-exit\nyour choice: "))
        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print("please enter a valid number.")


if __name__ == "__main__":
    main()
