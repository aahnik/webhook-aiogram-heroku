import sys
import asyncio
from bot import bot
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    args = sys.argv
    l = len(args)

    if l == 1:
        print('Starting bot, assuming webhook already set.')
        bot.main()
    elif l == 2:
        if args[1] == 'sethook':
            print('Setting webhook')
            asyncio.run(bot.set_hook())

        else:
            print('Invalid args')
    else:
        print('Incorrect number of args')
