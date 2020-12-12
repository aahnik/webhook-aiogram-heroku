''' Run a function by ado <func_name> '''


def set_hook():
    import asyncio
    from bot.settings import HEROKU_APP_NAME, WEBHOOK_URL, BOT_TOKEN
    from aiogram import Bot
    bot = Bot(token=BOT_TOKEN)

    async def set_hook():
        if not HEROKU_APP_NAME:
            print('You have forgot to set HEROKU_APP_NAME')
            quit()
        await bot.delete_webhook()
        await bot.set_webhook(WEBHOOK_URL)
        print(await bot.get_webhook_info())
        await bot.close()

    asyncio.run(set_hook())
    print('Webhook set')


def start():
    from bot.bot import main
    main()
