from decouple  import Config, RepositoryIni
from logic import load_settings, play_game
def main():
    config = config.getint('settings.ini')
    range_min = config.getint('GAME','range_min')
    range_max = config.getint('GAME','range_max')
    attempts = config.getint('GAME','attempts')
    initial_capital = config.getint('GAME','initial_capital')

    play_game(range_min,range_max,attempts,initial_capital)
if __name__=="__main__":
    main()