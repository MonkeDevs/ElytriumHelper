from disnake.ui import Button

import config


class PluginButton(Button):
    def __init__(self, plugin: str | None = None):
        super().__init__(url=config.plugins[plugin]['url'] if plugin else 'https://modrinth.com/user/hevav', label=config.plugins[plugin]['title'] if plugin else 'Limbo')


class VelocityButton(Button):
    def __init__(self, build: int | None = None):
        super().__init__(url=config.velocity_link.format(build=build) if build else 'https://papermc.io/downloads/velocity', label='Velocity')
