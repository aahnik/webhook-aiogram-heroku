import os
import pytz
from dotenv import load_dotenv
from secrets import token_urlsafe

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
assert API_TOKEN

SUBDOMAIN = os.getenv('SUBDOMAIN')
assert SUBDOMAIN

webhook_secret = token_urlsafe(32)

# webhook settings
WEBHOOK_HOST = f'https://{SUBDOMAIN}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{webhook_secret}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = os.getenv('PORT', '8443')

# timezone
TIMEZONE = os.getenv('TIMEZONE', 'UTC')
assert TIMEZONE in pytz.all_timezones
