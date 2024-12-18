import random
from decouple import config

RANGE_MIN = config("range_min", cast=int)
RANGE_MAX = config("range_max", cast=int)
ATTEMPTS = config("attempts", cast=int)
STARTING_CAPITAL = config("starting_capital", cast=int)

def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    capital = STARTING_CAPITAL
    attempt = 1

    while attempt <= ATTEMPTS and capital > 0:
        print()
        print(f"\nПопытка {attempt}/{ATTEMPTS}. Капитал: {capital}")
        try:
            bet = int(input("Ставка: "))
            if bet > capital:
                print("Ставка больше капитала!")
                continue
            guess = int(input(f"Угадайте число ({RANGE_MIN}-{RANGE_MAX}): "))
            if guess > RANGE_MAX or guess < RANGE_MIN:
                print(f"введите число между 1{RANGE_MIN} и {RANGE_MAX}")
                continue
        except ValueError:
            print("Введите число!")
            continue

        number = random.randint(RANGE_MIN, RANGE_MAX)  # Генерация нового числа для каждой попытки

        if guess == number:
            print(f"Угадали! Число: {number}. Капитал удвоен!")
            capital += bet * 2
            break
        else:
            print(f"Не угадали! Число было: {number}.")
            capital -= bet

        attempt += 1

    if capital <= 0:
        print("Капитал закончился.")
    else:
        print(f"Игра окончена. Итоговый капитал: {capital}")


play_game()