from bot import bot
from bot.settings import TIMEZONE
from datetime import datetime
from pytz import timezone
import logging


logging.basicConfig(level=logging.INFO)

logging.Formatter.converter = lambda *args: datetime.now(
    tz=timezone(TIMEZONE)).timetuple()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

bot.main()
