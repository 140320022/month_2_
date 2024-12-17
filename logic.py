import random
from decouple import config

# Загружаем настройки из файла
RANGE_MIN = config("range_min", cast=int)
RANGE_MAX = config("range_max", cast=int)
ATTEMPTS = config("attempts", cast=int)
STARTING_CAPITAL = config("starting_capital", cast=int)


def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    number = random.randint(RANGE_MIN, RANGE_MAX)
    capital = STARTING_CAPITAL

    for attempt in range(1, ATTEMPTS + 1):
        print(f"\nПопытка {attempt} из {ATTEMPTS}")
        print(f"Ваш текущий капитал: {capital}")
        bet = int(input("Введите вашу ставку: "))
        guess = int(input(f"Угадайте число от {RANGE_MIN} до {RANGE_MAX}: "))

        if guess == number:
            print(f"Поздравляем! Вы угадали число {number}.")
            capital += bet * 2
            break
        else:
            print("Неправильно! Попробуйте снова.")
            capital -= bet

        if capital <= 0:
            print("У вас закончились деньги. Игра окончена.")
            return

    print(f"Игра завершена. Ваш итоговый капитал: {capital}")