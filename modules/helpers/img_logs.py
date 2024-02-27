import io

import aiohttp
import pytesseract
from PIL import Image
from disnake import Message

import config
import ui
from bot import ElytriumHelperBot


async def img_read(message: Message):
    if not message.attachments:
        return
    attachments = [
        attachment for attachment in message.attachments if
        attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.webp'))
    ]
    async with (aiohttp.ClientSession() as session):
        for attachment in attachments:
            async with session.get(attachment.url) as resp:
                data = await resp.content.read()
                image = Image.open(io.BytesIO(data))
                ocr_text = pytesseract.image_to_string(image, lang='eng', config='--psm 1 --oem 3', timeout=5).split('\n')
                plugins = []
                for text in ocr_text:
                    if 'ProxyInitializeEvent' in text:
                        plugin = text.split('ProxyInitializeEvent to ')[1].replace('limbo', '').replace('linbo', '')
                        plugins.append(plugin)
                    elif 'OutOfMemoryError' in text:
                        await message.reply('Увеличьте значения/Increase values of -Xmx')

                if plugins:
                    embed = ui.embeds.DevBuildEmbed()
                    buttons = []
                    for plugin in plugins:
                        buttons.append(ui.buttons.PluginButton(plugin))
                    buttons.append(ui.buttons.VelocityButton())
                    await message.reply(embed=embed, components=buttons)


def setup(bot: ElytriumHelperBot):
    pytesseract.pytesseract.tesseract_cmd = config.tesseract_cmd
    bot.add_listener(img_read, 'on_message')
