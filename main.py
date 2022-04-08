import os
from dotenv import load_dotenv
from bot import bot


def main():
    load_dotenv()
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
