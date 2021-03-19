# webhook-aiogram-heroku

[![Generic badge](https://img.shields.io/badge/works-yes-<COLOR>.svg)](https://aahnik.github.io)
[![ MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://aahnik.github.io/)
[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)

A simple telegram echo bot made with [`aiogram`](https://github.com/aiogram/aiogram), that fetches updates using web-hook connection.

## Deploy

This bot can be easily deployed to [Heroku](https://heroku.com/) cloud platform.

The following steps assume that you have Heroku CLI installed in your system.

1. Clone the repo and move into the project directory.

```shell
git clone https://github.com/aahnik/webhook-aiogram-heroku.git
cd webhook-aiogram-heroku
```

2. Create a new Heroku app.

```shell
heroku create
```

3. Set the Config Vars.

<details>
<summary> 👉 Click here to know more </summary>

| Config Var | Description |
| -- | -- |
|`HEROKU_APP_NAME` | name of your Heroku app. You may set it manually or [turn on Dyno Metadata feature](https://devcenter.heroku.com/articles/dyno-metadata) which is currently in Heroku Labs.|
| `BOT_TOKEN` | the token for your bot given by [@BotFather](https://telegram.me/BotFather) after bot creation.|

</details>

```shell
heroku labs:enable runtime-dyno-metadata
heroku config:set BOT_TOKEN=<your token>
```

4. Push the code to Heroku.

```shell
git push heroku main
```

## Cheers

To confirm your bot is working:

- Run `heroku ps` which will show you details of your dyno.

- Send a message to your bot, and your bot will echo it back to you.

