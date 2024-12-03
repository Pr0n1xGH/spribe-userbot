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
from typing import Optional, List

import glob
import pyunpack
import requests
from pyrogram import Client, filters
from pyrogram import __version__ as verpyro
from pyrogram.types import Message

from .help import add_command_help
from ..base.database import DatabaseTime
from ..main import clear
from ..plugins.help import CMD_HELP
from ..utils import messages
from ..utils.loading import Loader
from ..utils.logger import logger


class ModuleManager:
    """Менеджер для работы с модулями"""
    
    EXCLUDE_MODULES = ["default", "default.py", "help", "help.py", "_example", "_example.py"]
    
    @staticmethod
    async def download_module(url: str, file_name: str) -> None:
        """Загружает модуль по URL"""
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
                
    @staticmethod
    async def install_all_modules(message: Message) -> None:
        """Устанавливает все доступные модули"""
        url = "https://gist.githubusercontent.com/Pr0n1xGH/906c4cc69c24d71ca7d838ba3f7a8504/raw/modules.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            modules = json.loads(response.content)['modules']
            text = "🛠️ **Установка всех модулей...**\n└ **Установленно**:\n"
            
            for module_name, module_url in modules.items():
                text += f"» **Идёт установка __{module_name}__**...\n"
                await message.edit(text)
                
                file_name = f"userbot/plugins/{module_url.split('/')[-1]}"
                await ModuleManager.download_module(module_url, file_name)
                
                text = re.sub(f"» **Идёт установка __{module_name}__**...\n", f"» {module_name} ✅\n", text)
                await message.edit(text)
                
            return True
        return False


@Client.on_message(filters.command('dlm', prefixes='.') & filters.me)
async def loadmod(client: Client, message: Message) -> None:
    """Загрузка модулей"""
    reply_message = message.reply_to_message
    
    if not reply_message:
        text = ' '.join(message.command[1:])
        
        if text.startswith('https://') and text.endswith('.py'):
            file_name = f"userbot/plugins/{text.split('/')[-1]}"
            await ModuleManager.download_module(text, file_name)
            await message.edit(
                '<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                '<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
            )
            
        elif text == '-all':
            if await ModuleManager.install_all_modules(message):
                await message.edit(
                    '<emoji id=5206607081334906820>⚙</emoji> ▸ Модули успешно установлены!\n\n'
                    '<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
                )
                
        else:
            url = "https://gist.githubusercontent.com/Pr0n1xGH/906c4cc69c24d71ca7d838ba3f7a8504/raw/modules.json"
            response = requests.get(url)
            
            if response.status_code == 200:
                try:
                    module_url = json.loads(response.content)['modules'][text]
                    file_name = f"userbot/plugins/{module_url.split('/')[-1]}"
                    await ModuleManager.download_module(module_url, file_name)
                    
                    await message.edit(
                        '<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                        '<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
                    )
                    
                except Exception:
                    await message.edit(
                        "<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля."
                    )
                    
    else:
        if reply_message.document:
            file_name = reply_message.document.file_name
            file_id = reply_message.document.file_id
            
            if file_name.endswith(".zip"):
                clear()
                with Loader("Загрузка модулей... ", f"{messages.Logo_Message}\n{messages.Runned}"):
                    zip_path = os.path.join(os.getcwd(), "userbot/utils/misc/" + file_name)
                    dest_path = os.path.join(os.getcwd(), "userbot/plugins/")
                    
                    await client.download_media(file_id, file_name=f'utils/misc/{file_name}')
                    pyunpack.Archive(zip_path).extractall(dest_path)
                    
                    if os.path.isfile("userbot/utils/misc/" + file_name):
                        os.remove("userbot/utils/misc/" + file_name)
                        
                    clear()
                    
            else:
                await client.download_media(file_id, file_name=f'plugins/{file_name}')
                
            await message.edit(
                '<emoji id=5206607081334906820>⚙</emoji> ▸ Модуль успешно добавлен!\n\n'
                '<emoji id=5386757912607599167>🛠️</emoji> Что-бы модули корректно загрузились используйте `.reload`'
            )
            
        else:
            await message.edit(
                '<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.'
            )
            
    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('delm', prefixes='.') & filters.me)
async def unloadmod(client: Client, message: Message) -> None:
    """Удаление модулей"""
    name_module = ' '.join(message.command[1:])
    if not name_module.endswith(".py"):
        name_module += ".py"
        
    try:
        if os.path.isfile("userbot/plugins/" + name_module):
            if name_module in ModuleManager.EXCLUDE_MODULES:
                await message.edit('<emoji id=5210952531676504517>🔴</emoji> ▸ Незя!')
            else:
                os.remove("userbot/plugins/" + name_module)
                CMD_HELP.pop(f"{name_module[:-3]}")
                await message.edit("<emoji id=5206607081334906820>🟢</emoji> ▸ Модуль был удалён!")
        else:
            await message.edit("<emoji id=5210952531676504517>🔴</emoji> ▸ Такого модуля не существует.")
            
    except Exception as e:
        await message.edit("<emoji id=5386757912607599167>🛠️</emoji> ▸ Произошла ошибка:\n\n" + str(e))
        
    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(filters.command('backup', prefixes='.') & filters.me)
async def backup(client: Client, message: Message) -> None:
    """Создание резервной копии модулей"""
    await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Бэкап модулей. Подождите...')
    
    with zipfile.ZipFile('plugins.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        modules_count = 0
        for root, dirs, files in os.walk("userbot/plugins/"):
            for file in files:
                if (file.endswith('.py') and 
                    file not in ModuleManager.EXCLUDE_MODULES):
                    zip_file.write(
                        os.path.join(root, file),
                        arcname=os.path.basename(file)
                    )
                    modules_count += 1
                    
    await message.delete()
    
    with open("plugins.zip", "rb") as file:
        await client.send_document(
            chat_id=message.chat.id,
            document=file,
            caption=f"<emoji id=5449555539975481957>📦</emoji> ▸ Бэкап модулей ({modules_count})"
        )
        
    if os.path.isfile("plugins.zip"):
        os.remove("plugins.zip")


@Client.on_message(filters.command('reload', prefixes='.') & filters.me)
async def reload(client: Client, message: Message) -> None:
    """Перезагрузка юзербота"""
    block = ' '.join(message.command[1:])
    
    try:
        await message.edit('<emoji id=5438274168422409988>🔄️</emoji> ▸ Скрипт перезагружается...')
        await client.restart(block=block == "True")
        reload_cache()
        await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Скрипт перезагрузился.')
        
    except Exception as e:
        await message.edit(
            f'<emoji id=5438274168422409988>🔄️</emoji> ▸ Ошибка...\n\n'
            f'<emoji id=5386757912607599167>🛠️</emoji> {str(e)}'
        )
        
    await asyncio.sleep(3)
    await message.delete()


@Client.on_message(filters.command("logs", ".") & filters.me)
async def _logs(client: Client, message: Message) -> None:
    """Получение логов"""
    cmds = ' '.join(message.command[1:])
    await message.edit("<emoji id=5438274168422409988>🔄️</emoji> Обработка...")
    
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
                caption="`logs from Spribe-Userbot`"
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
async def inf(client: Client, message: Message) -> None:
    """Информация о юзерботе или пользователе"""
    from userbot.utils import messages
    from .. import start_time
    
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        status = 'Онлайн' if user.status == 'UserStatus.ONLINE' else 'Офлайн'
        time_info = (f'Следующая офлайн дата: `{user.next_offline_date}`' 
                    if user.status == 'UserStatus.ONLINE' 
                    else f'Последний раз онлайн: `{user.last_online_date}`')
        
        await message.edit(
            f"Информация о пользователе @{user.username}: \n\n"
            f"🛠️ ID: `{user.id}`\n"
            f"├ Номер: `{user.phone_number if user.is_contact else 'Скрыт'}`\n"
            f"├ Взаимный контакт: `{'Есть' if user.is_mutual_contact else 'Нету'}`\n"
            f"├ Бот: `{'Да' if user.is_bot else 'Нет'}`\n"
            f"├ Проверен: `{'Да' if user.is_verified else 'Нет'}`\n"
            f"├ Ограничен: `{'Да' if user.is_restricted else 'Нет'}`\n"
            f"├ Скам метка: `{'Есть' if user.is_scam else 'Нету'}`\n"
            f"├ Фейк метка: `{'Есть' if user.is_fake else 'Нету'}`\n"
            f"├ Официальная поддержка Telegram: `{'Да' if user.is_support else 'Нет'}`\n"
            f"├ Премиум: `{'Есть' if user.is_premium else 'Нету'}`\n"
            f"├ Статус: `{status}`\n"
            f"├ {time_info}\n"
            f"└ Номер датацентра: `{user.dc_id}`\n"
        )
        
    else:
        uptime = time.time() - start_time
        modules_count = sum(
            1 for root, dirs, files in os.walk("userbot/plugins/")
            for file in files
            if file.endswith('.py') and file not in ModuleManager.EXCLUDE_MODULES
        )
        
        await message.edit(
            f"🍃 **`Spribe-Userbot`**\n"
            f"**└ Ссылки**: <i>[Github](https://github.com/Pr0n1xGH/spribe-userbot) | "
            f"[Support](https://t.me/devspribe) | [Channel](https://t.me/tgscriptss)</i>\n\n"
            f"**🛠️ Пользователь**: `{client.me.mention}`\n"
            f"**├ Кол-во модулей**: `{modules_count}` \n"
            f"**├ Версия юзербота**: `{messages.Version}` \n"
            f"**├ Версия Python**: `{python_version()}` \n"
            f"**├ Версия Pyrogram**: `{verpyro}` \n"
            f"**└ Время работы юзербота**: `{DatabaseTime()._format_time_interval(uptime)}` \n\n"
            f"**🕛 Первый запуск юзербота**: `{DatabaseTime().get_first_date()[0]}`\n"
            f"**└ Прошло времени**: `{DatabaseTime().get_uptime()}` \n\n",
            disable_web_page_preview=True
        )
        
        await asyncio.sleep(20)
        await message.delete()


def reload_cache() -> None:
    """Перезагрузка кэша модулей"""
    plugins_dir = os.path.join(os.getcwd(), "userbot/plugins")
    modules_to_reload = [
        f"userbot.plugins.{file[:-3]}"
        for file in os.listdir(plugins_dir)
        if file.endswith(".py")
    ]
    
    importlib.invalidate_caches()
    for module in modules_to_reload:
        importlib.import_module(module)


add_command_help(
    "default",
    [
        [".dlm [Ответ на сообщение/Название модуля/Ссылка на модуль/-all]", 
         "Добавляет новый модуль(Флаг `-all` скачивает сразу все доступные модули)"],
        [".delm [Название модуля]", "Удаляет модуль"],
        [".backup", "Делает бэкап всех модулей"],
        [".logs [all]", "Даёт логи последнего запуска скрипта(без all) / Даёт zip файл со всеми логами"],
        [".info", "Предоставляет информацию о юзерботе"],
        [".reload", "Перезагружает юзербота"],
    ],
)
