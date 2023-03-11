import logging
from pathlib import Path
from TgBot import start_telegram_bot


def main():
    path = Path(__file__).parent.resolve()
    logging.basicConfig(filename=f'{path}/bot.log', encoding='utf-8',
                        level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')
    start_telegram_bot()


if __name__ == "__main__":
    main()
