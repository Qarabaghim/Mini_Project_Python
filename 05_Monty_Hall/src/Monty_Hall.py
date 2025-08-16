import random


def monty_hall(switch_doors: bool) -> bool:
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    # print(doors)

    user_choice = random.choice(range(3))
    # print(user_choice)

    reveled_door = [i for i in range(3) if i != user_choice and doors[i] != 'car']
    Open_door = random.choice(reveled_door)
    # print(Open_door)

    if switch_doors:
        final_choice = [i for i in range(3) if i != user_choice and i != Open_door][0]
    else:
        final_choice = user_choice

    return doors[final_choice] == 'car'


def simulate_game(num_games: int = 1000):
    num_wins_without_switching = sum(monty_hall(False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall(True) for _ in range(num_games))

    return num_wins_without_switching, num_wins_with_switching


if __name__ == "__main__":
    number = 1000
    wins_without_switching, wins_with_switching = simulate_game(number)
    print(f"Winning percentage with out switching doors: {(wins_without_switching / number):.2%}")
    print(f"Winning percentage with switching doors: {(wins_with_switching / number):.2%}")
