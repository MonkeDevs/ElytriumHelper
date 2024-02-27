import disnake

import config


class DevBuildEmbed(disnake.Embed):
    def __init__(self, plugin: str | None = None):
        super().__init__(
            title=f'Обновите/Update {config.plugins[plugin]["title"] if plugin else "Limbo/Velocity"}',
            url=config.plugins[plugin]['url'] if plugin else None,
            description='Скачайте последние версии по ссылкам ниже.\n'
                        'Download the latest versions from these links '
        )
