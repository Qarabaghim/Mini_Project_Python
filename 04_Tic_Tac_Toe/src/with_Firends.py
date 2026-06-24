from termcolor import colored

board = list(range(1, 10))
winner = (
    (0, 1, 2),( 3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)


def print_board():
    for i in range(9):
        value = board[i]
        if value == "X":
            print(colored(f"[{value}]", "red"), end=" ")
        elif value == "O":
            print(colored(f"[{value}]", "blue"), end=" ")
        else:
            print(f"[{value}]", end=" ")
        if (i + 1) % 3 == 0:
            print("\n")


def can_move(move):
    return move in range(1, 10) and isinstance(board[move - 1], int)


def make_move(player, move):
    if can_move(move):
        board[move - 1] = player
        return True
    return False


def is_winner(player):
    for combo in winner:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw():
    return all(
        isinstance(cell, str)
        for cell in board
    )


def main():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(
                input(
                    f"Player {current_player}, choose (1-9): "
                )
            )
        except ValueError:
            print("Please enter a number!")
            continue
        if not make_move(current_player, move):
            print("Invalid move!")
            continue
        if is_winner(current_player):
            print_board()
            if current_player == "X":
                print(
                    colored(
                        "Player X Wins!",
                        "green"
                    )
                )
            else:
                print(
                    colored(
                        "Player O Wins!",
                        "green"
                    )
                )
            break
        if is_draw():
            print_board()
            print(
                colored(
                    "Draw!",
                    "yellow"
                )
            )
            break
        current_player = (
            "O"
            if current_player == "X"
            else "X"
        )


if __name__ == "__main__":
    main()
