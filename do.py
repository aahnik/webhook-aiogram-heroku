''' Run a function by ado <func_name> '''


def set_hook():
    import asyncio
    from bot.bot import set_hook
    asyncio.run(set_hook())
    print('Webhook set')


def start():
    from bot.bot import main
    main()
