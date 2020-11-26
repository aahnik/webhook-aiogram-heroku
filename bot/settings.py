import os
from secrets import token_urlsafe


API_TOKEN = os.getenv('API_TOKEN')
assert API_TOKEN

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
assert HEROKU_APP_NAME

webhook_secret = token_urlsafe(32)

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{webhook_secret}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))
