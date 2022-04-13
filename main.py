import os
from bot import bot


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
