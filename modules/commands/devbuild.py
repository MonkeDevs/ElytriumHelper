from enum import Enum

from disnake import ApplicationCommandInteraction
from disnake.ext import commands

import config
from bot import ElytriumHelperBot
from ui import buttons, embeds


class PluginChoice(str, Enum):
    LimboAPI = 'api'
    LimboAuth = 'auth'
    LimboFilter = 'filter'
    LimboHub = 'hub'
    LimboReconnect = 'reconnect'
    SocialAddon = 'addon'


@commands.slash_command(name='devbuild', description='Download links')
@commands.has_role(config.roles.support)
async def devbuild(interaction: ApplicationCommandInteraction, plugin: PluginChoice | None = None, velocity: int | None = None):
    await interaction.send(embed=embeds.DevBuildEmbed(plugin), components=[buttons.PluginButton(plugin), buttons.VelocityButton(velocity)])


def setup(bot: ElytriumHelperBot):
    bot.add_slash_command(devbuild)
