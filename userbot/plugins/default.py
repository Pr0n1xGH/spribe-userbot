# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import os
import zipfile
import glob
import time
from pathlib import Path
from platform import python_version

from pyrogram import Client, filters
from pyrogram import __version__ as verpyro

from .help import add_command_help
from ..utils.logger import logger
from ..base import database


@Client.on_message(filters.command('loadmod', prefixes='.') & filters.me)
async def loadmod(client, message):
    reply_message = message.reply_to_message

    if not reply_message:
        await message.edit("<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.")

    else:
        if reply_message.document:
            file_name = reply_message.document.file_name
            file_id = reply_message.document.file_id

            if file_name.endswith(".zip"):
                await client.download_media(file_id, file_name=f'utils/misc/{file_name}')

                zip_path = os.path.join(os.getcwd(), "userbot/utils/misc/" + file_name)
                dest_path = os.path.join(os.getcwd(), "userbot/plugins/")

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(dest_path)

                if os.path.isfile("utils/misc/" + file_name):
                    os.remove("utils/misc/" + file_name)

            else:
                await client.download_media(file_id, file_name=f'plugins/{file_name}')

            await message.edit(
                '<emoji id=5438274168422409988>⚙</emoji> ▸ Модуль успешно добавлен!\n\n<emoji id=5341350410252723241>🛠️</emoji> Перезагрузите скрипт командой -reload что-бы модули заработали.')
        else:
            await message.edit('<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.')

    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('unloadmod', prefixes='.') & filters.me)
async def unloadmod(client, message):
    name_module = ' '.join(message.command[1:])

    try:
        if name_module.endswith(".py"):
            pass
        else:
            name_module = name_module + ".py"

        exclude_modules = ["default", "default.py", "help",
                           "help.py", "_example", "_example.py"]

        if os.path.isfile("modules/" + name_module):
            if name_module in exclude_modules:
                await message.edit('<emoji id=5210952531676504517>🔴</emoji> ▸ Незя!')
            else:
                os.remove("modules/" + name_module)
                await message.edit("<emoji id=5206607081334906820>🟢</emoji> ▸ Модуль был удалён!")

        else:
            await message.edit("<emoji id=5210952531676504517>🔴</emoji> ▸ Такого модуля не существует.")

    except Exception as e:
        await message.edit("<emoji id=5386757912607599167>🛠️</emoji> ▸ Произошла ошибка:\n\n" + e)

    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('backup', prefixes='.') & filters.me)
async def backup(client, message):
    await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Бэкап модулей. Подождите...')

    zip_file = zipfile.ZipFile('plugins.zip', 'w', zipfile.ZIP_DEFLATED)

    modules = 0
    for root, dirs, files in os.walk("userbot/plugins/"):
        for file in files:
            if file.endswith('.py'):
                if file != '_example.py' and file != 'default.py' and file != 'help.py':
                    zip_file.write(os.path.join(root, file), arcname=os.path.basename(file))
                    modules += 1

    zip_file.close()
    await message.delete()

    with open("plugins.zip", "rb") as file:
        await client.send_document(chat_id=message.chat.id,
                                   document=file,
                                   caption=f"<emoji id=5449555539975481957>📦</emoji> ▸ Бэкап модулей ({modules})")

    if os.path.isfile("plugins.zip"):
        os.remove("plugins.zip")


@Client.on_message(filters.command('reload', prefixes='.') & filters.me)
async def reload(client, message):
    block = ' '.join(message.command[1:])

    try:
        await message.edit('<emoji id=5438274168422409988>🔄️</emoji> ▸ Скрипт перезагружается...')
        await client.restart(block=block == "True")
        await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Скрипт перезагрузился.')

    except Exception as e:
        await message.edit(f'<emoji id=5438274168422409988>🔄️</emoji> ▸ Ошибка...\n\n<emoji '
                           f'id=5386757912607599167>🛠️</emoji> {e}')

    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command("logs", ".") & filters.me)
async def _logs(client, message):
    cmds = ' '.join(message.command[1:])

    await message.edit(f"<emoji id=5438274168422409988>🔄️</emoji> Обработка...")
    if cmds == "all":
        zip_name = 'logs.zip'

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk('logs'):
                for file in files:
                    zipf.write(os.path.join(root, file))

        with open(zip_name, "rb") as file:
            await message.delete()
            await client.send_document(
                chat_id=message.chat.id,
                document=file,
                caption=f"`logs from Spribe-Userbot`"
            )

        if os.path.isfile(zip_name):
            os.remove(zip_name)

    else:
        logs_dir = glob.glob("logs/*")
        latest_file = max(logs_dir, key=os.path.getctime)

        try:
            file_text = Path(latest_file).read_text(encoding='utf-8')
        except UnicodeDecodeError:
            file_text = Path(latest_file).read_text(encoding='latin-1')

        if len(file_text) > 3000:
            await message.delete()
            await client.send_document(
                chat_id=message.chat.id,
                document=latest_file,
                caption="`logs from Spribe-Userbot`"
            )

        else:
            await message.edit(f"logs from Spribe-Userbot \n`{file_text}`")

    logger.info("Были взяты логи командой .logs")
    
    
@Client.on_message(filters.command("info", ".") & filters.me)
async def inf(client, message):
    from ..__main__ import start_time
    from ..utils import messages
    
    uptime = time.time() - start_time
    modules = 0
    for root, dirs, files in os.walk("userbot/plugins/"):
        for file in files:
            if file.endswith('.py'):
                if (file != '_example.py' 
                    and file != 'default.py' 
                    and file != 'help.py'
                    ):
                    modules += 1
    
    await message.edit(
        f"🍃 **`Spribe-Userbot`**\n\n"
        f"**🛠️ Пользователь**: `{client.me.mention}`\n"
        f"**├ Кол-во модулей**: `{modules}` \n"
        f"**├ Версия юзербота**: `{messages.Version}` \n"
        f"**├ Версия Python**: `{python_version()}` \n"
        f"**├ Версия Pyrogram**: `{verpyro}` \n"
        f"**└ Время работы бота**: `{database.display_time(uptime)}` \n\n"
        f"**🕛 Первый запуск юзербота**: `{database.get_fdate()[0]}`\n"
        f"**└ Прошло времени**: `{database.get_ftime()}` \n"
    )
    await asyncio.sleep(20)
    await message.delete()

add_command_help(
    "default",
    [
        [".loadmod", "Добавляет новый модуль(используется в ответ на сообщение)"],
        [".unloadmod [Название модуля]", "Удаляет модуль"],
        [".backup", "Делает бэкап всех модулей"],
        [".logs [all]", "Даёт логи последнего запуска скрипта(без all) / Даёт zip файл со всеми логами"],
        [".info", "Предостовляет информацию о юзерботе"]
        [".reload", "Перезагружает скрипт"],
    ],
)
