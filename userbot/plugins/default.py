# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import importlib
import json
import os
import re
import time
import zipfile
from pathlib import Path
from platform import python_version

import glob
import pyunpack
import requests
from pyrogram import Client, filters
from pyrogram import __version__ as verpyro

from .help import add_command_help
from ..base.database import basetime
from ..main import clear
from ..plugins.help import CMD_HELP
from ..utils import messages
from ..utils.loading import Loader
from ..utils.logger import logger

@Client.on_message(filters.command('dlm', prefixes='.') & filters.me)
async def loadmod(client, message):
    reply_message = message.reply_to_message

    if not reply_message:
        text = ' '.join(message.command[1:])
        
        if text.startswith('https://') and text.endswith('.py'):
            response = requests.get(text)

            if response.status_code == 200:
                file_name = f"userbot/plugins/{text.split('/')[-1]}"

                with open(file_name, 'wb') as f:
                    f.write(response.content)
                
                await message.edit(
                    f'<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                    f'<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
                )

        elif text == '-all':
            url_all_modules = "https://gist.githubusercontent.com/Pr0n1xGH/906c4cc69c24d71ca7d838ba3f7a8504/raw/modules.json"
            response = requests.get(url_all_modules)

            if response.status_code == 200:
                jsn = json.loads(response.content)['modules']

                text = f"🛠️ **Установка всех модулей...**\n└ **Установленно**:\n"
                for module, url in jsn.items():
                    text += f"» **Идёт установка __{module}__**...\n"
                    await message.edit(text)

                    file_name = f"userbot/plugins/{url.split('/')[-1]}"
                    module_content = requests.get(url).content

                    with open(file_name, 'wb') as f:
                        f.write(module_content)

                    text = re.sub(f"» \*\*Идёт установка __{module}__\*\*...\n", f"» {module} ✅\n", text)
                    await message.edit(text)

                await message.edit(
                    f'<emoji id=5206607081334906820>⚙</emoji> ▸ Модули успешно установлены!\n\n'
                    f'<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
                )

        else:
            url_all_modules = "https://gist.githubusercontent.com/Pr0n1xGH/906c4cc69c24d71ca7d838ba3f7a8504/raw/modules.json"
            response = requests.get(url_all_modules)

            if response.status_code == 200:
                try:
                    url = json.loads(response.content)['modules'][f"{text}"]
                    response = requests.get(url)

                    file_name = f"userbot/plugins/{url.split('/')[-1]}"

                    with open(file_name, 'wb') as f:
                        f.write(response.content)

                    await message.edit(
                        f'<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                        f'<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
                    )

                except Exception as e:
                    await message.edit(
                        "<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.")

    else:
        if reply_message.document:
            file_name = reply_message.document.file_name
            file_id = reply_message.document.file_id

            if file_name.endswith(".zip"):
                clear()
                with Loader("Загрузка модулей... ", f"{messages.Logo_Message}\n{messages.Runned}"):
                    await client.download_media(
                        file_id, 
                        file_name = f'utils/misc/{file_name}'
                    )

                    zip_path = os.path.join(
                        os.getcwd(), 
                        "userbot/utils/misc/" + file_name
                    )

                    dest_path = os.path.join(
                        os.getcwd(), 
                        "userbot/plugins/"
                    )

                    pyunpack.Archive(zip_path).extractall(dest_path)

                    if os.path.isfile("userbot/utils/misc/" + file_name):
                        os.remove("userbot/utils/misc/" + file_name)

                    clear()
                
            else:
                await client.download_media(
                    file_id, 
                    file_name = f'plugins/{file_name}'
                )

            await message.edit(
                f'<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                f'<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
            )

        else:
            await message.edit(
                '<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.')

    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('delm', prefixes='.') & filters.me)
async def unloadmod(client, message):
    name_module = ' '.join(message.command[1:])

    try:
        if name_module.endswith(".py"):
            pass
        else:
            name_module = name_module + ".py"

        exclude_modules = ["default", "default.py", "help",
                           "help.py", "_example", "_example.py"]

        if os.path.isfile("userbot/plugins/" + name_module):
            if name_module in exclude_modules:
                await message.edit(
                    '<emoji id=5210952531676504517>🔴</emoji> ▸ Незя!'
                )
            else:
                os.remove(
                    "userbot/plugins/" + name_module)

                CMD_HELP.pop(
                    f"{name_module[:-3]}")
                
                await message.edit(
                    "<emoji id=5206607081334906820>🟢</emoji> ▸ Модуль был удалён!")
        else:
            await message.edit(
                "<emoji id=5210952531676504517>🔴</emoji> ▸ Такого модуля не существует.")

    except Exception as e:
        await message.edit(
            "<emoji id=5386757912607599167>🛠️</emoji> ▸ Произошла ошибка:\n\n" + e)

    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('backup', prefixes='.') & filters.me)
async def backup(client, message):
    await message.edit(
        '<emoji id=5438274168422409988>⚙</emoji> ▸ Бэкап модулей. Подождите...')

    zip_file = zipfile.ZipFile(
        'plugins.zip', 
        'w', zipfile.ZIP_DEFLATED
    )

    modules = 0
    for root, dirs, files in os.walk("userbot/plugins/"):
        for file in files: 
            if file.endswith('.py'):
                if (file != '_example.py' 
                    and file != 'default.py' 
                        and file != 'help.py'
                    ):
                    zip_file.write(
                        os.path.join(
                            root, file
                        ), 
                    arcname = os.path.basename(file))
                    modules += 1

    zip_file.close()
    await message.delete()

    with open("plugins.zip", "rb") as file:
        await client.send_document(
            chat_id=message.chat.id,
            document=file,
            caption=f"<emoji id=5449555539975481957>📦</emoji> ▸ Бэкап модулей ({modules})"
        )

    if os.path.isfile("plugins.zip"):
        os.remove("plugins.zip")


@Client.on_message(filters.command('reload', prefixes='.') & filters.me)
async def reload(client, message):
    block = ' '.join(message.command[1:])

    try:
        await message.edit(
            '<emoji id=5438274168422409988>🔄️</emoji> ▸ Скрипт перезагружается...')

        await client.restart(
            block = block == "True")
        
        reload_cache()
        
        await message.edit(
            '<emoji id=5438274168422409988>⚙</emoji> ▸ Скрипт перезагрузился.')

    except Exception as e:
        await message.edit(
            f'<emoji id=5438274168422409988>🔄️</emoji> ▸ Ошибка...\n\n<emoji '
            f'id=5386757912607599167>🛠️</emoji> {e}'
        )

    await asyncio.sleep(3)
    await message.delete()


@Client.on_message(filters.command("logs", ".") & filters.me)
async def _logs(client, message):
    cmds = ' '.join(message.command[1:])

    await message.edit(
        f"<emoji id=5438274168422409988>🔄️</emoji> Обработка...")
    
    if cmds == "all":
        zip_name = 'logs.zip'

        with (
            zipfile.ZipFile(
                zip_name, 
                'w', 
                zipfile.ZIP_DEFLATED)
            ) as zipf:
            for root, dirs, files in (
                    os.walk('logs')
                ):
                for file in files:
                    (
                    zipf.write(
                        os.path.join(root, file)
                        )
                    )

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
        logs_dir = (
            glob.glob("logs/*")
        )
        latest_file = (
            max(
                logs_dir, 
                key = os.path.getctime)
        )

        try:
            file_text = (
                Path(latest_file)
                    .read_text(
                        encoding='utf-8')
            )
        except UnicodeDecodeError:
            file_text = (
                Path(latest_file)
                    .read_text(
                        encoding='latin-1')
            )

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
    from userbot.utils import messages
    from .. import start_time

    if message.reply_to_message:
        await message.edit(
            f"Информация о пользователе @{message.reply_to_message.from_user.username}: \n\n"
            f"🛠️ ID: `{message.reply_to_message.from_user.id}`\n"
            f"├ Номер: `{message.reply_to_message.from_user.phone_number if message.reply_to_message.from_user.is_contact else 'Скрыт'}`\n"
            f"├ Взаимный контакт: `{'Есть' if message.reply_to_message.from_user.is_mutual_contact else 'Нету'}`\n"
            f"├ Бот: `{'Да' if message.reply_to_message.from_user.is_bot else 'Нет'}`\n"
            f"├ Проверен: `{'Да' if message.reply_to_message.from_user.is_verified else 'Нет'}`\n"
            f"├ Ограничен: `{'Да' if message.reply_to_message.from_user.is_restricted else 'Нет'}`\n"
            f"├ Скам метка: `{'Есть' if message.reply_to_message.from_user.is_scam else 'Нету'}`\n"
            f"├ Фейк метка: `{'Есть' if message.reply_to_message.from_user.is_fake else 'Нету'}`\n"
            f"├ Официальная поддержка Telegram: `{'Да' if message.reply_to_message.from_user.is_support else 'Нет'}`\n"
            f"├ Премиум: `{'Есть' if message.reply_to_message.from_user.is_premium else 'Нету'}`\n"
            f"├ Статус: `{'Онлайн' if message.reply_to_message.from_user.status == 'UserStatus.ONLINE' else 'Офлайн'}`\n"
            f"├ {f'Следующая офлайн дата: `{message.reply_to_message.from_user.next_offline_date}`' if message.reply_to_message.from_user.status == 'UserStatus.ONLINE' else f'Последний раз онлайн: `{message.reply_to_message.from_user.last_online_date}`'}\n"
            f"└ Номер датацентра: `{message.reply_to_message.from_user.dc_id}`\n"
        )

    else:
        uptime = time.time() - start_time
        modules = 0
        for (root, 
                dirs, 
                    files) in (
                os.walk("userbot/plugins/")
            ):
            for file in files:
                if file.endswith('.py'):
                    if (file != '_example.py' 
                        and file != 'default.py' 
                            and file != 'help.py'):
                        modules += 1
        
        await message.edit(
            f"🍃 **`Spribe-Userbot`**\n"
            f"**└ Ссылки**: <i>[Github](https://github.com/Pr0n1xGH/spribe-userbot) | [Support](https://t.me/devspribe) | [Channel](https://t.me/tgscriptss)</i>\n\n"
            f"**🛠️ Пользователь**: `{client.me.mention}`\n"
            f"**├ Кол-во модулей**: `{modules}` \n"
            f"**├ Версия юзербота**: `{messages.Version}` \n"
            f"**├ Версия Python**: `{python_version()}` \n"
            f"**├ Версия Pyrogram**: `{verpyro}` \n"
            f"**└ Время работы юзербота**: `{basetime().display_time(seconds = uptime)}` \n\n"
            f"**🕛 Первый запуск юзербота**: `{basetime().get_fdate()[0]}`\n"
            f"**└ Прошло времени**: `{basetime().get_ftime()}` \n\n",
            disable_web_page_preview = True
        )

        await asyncio.sleep(20)
        await message.delete()


def reload_cache():
    plugins_dir = os.path.join(os.getcwd(), "userbot/plugins")
    modules_to_reload = []

    for file in os.listdir(plugins_dir):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = f"userbot.plugins.{module_name}"

            modules_to_reload.append(module)

    importlib.invalidate_caches()

    for module in modules_to_reload:
        importlib.import_module(module)


add_command_help(
    "default",
    [
        [".dlm [Ответ на сообщение/Название модуля/Ссылка на модуль/-all]", "Добавляет новый модуль(Флаг `-all` скачивает сразу все доступные модули)"],
        [".delm [Название модуля]", "Удаляет модуль"],
        [".backup", "Делает бэкап всех модулей"],
        [".logs [all]", "Даёт логи последнего запуска скрипта(без all) / Даёт zip файл со всеми логами"],
        [".info", "Предоставляет информацию о юзерботе"],
        [".reload", "Перезагружает юзербота"],
    ],
)
