import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

import config


class ElytriumHelperBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.bot.prefix, intents=disnake.Intents.all())


if __name__ == '__main__':
    load_dotenv()
    bot = ElytriumHelperBot()


    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')


    for module in os.listdir('modules'):
        bot.load_extensions(f'modules/{module}')

    bot.run(os.getenv('TOKEN'))
