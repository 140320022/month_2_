import random
def load_settings(config):
    """Загружает  настройки из конфигурационного файла."""
    range_start, range_end = map(int,config("GameSettings", "number_range")).split((","))
    attempts = int (config("GameSettings","attempts"))
    capital = int (config("gameSettings","initial_capital"))
    return range_start,range_end,attempts,capital
def play_game(range_start,range_end,attempts,capital):
    """Основная логика игры."""
    secret_number = random.randint(range_start,range_end)
    print("Добро пожаловать в игру'Угадай число'")
    print(f"Загаданное число в диапазоне от {range_start} до {range_end}.\n")

    for attempt in range(attempts):
        print(f"Попытка {attempt + 1} из {attempts}. Текущий капитал:{capital}")
        bet = int(input(f"Введите вашу ставку:"))
        guess = int(input(f"Угадайте число от {range_start} до {range_end}:"))

        if bet > capital:
            print("Ваша ставка превышает текущий капитал!")
            continue
        if guess == secret_number:
            print("Поздравляем ! Вы угадали !")
            capital += bet
        else:
            print("Вы не угадали. Попробуйте снова.")
            capital -= bet
        if capital <= 0:
            print("Ваш капитал исчерпан. Игра окончена.")
            break
        print(f"Игра окончена. Ваш итоговый капитал: {capital}")
