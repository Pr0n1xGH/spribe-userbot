# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import os
import inspect
import importlib
import asyncio
import zipfile

from pyrogram import Client, filters
from modules.help import add_command_help

@Client.on_message(
    filters.command('add_module', prefixes='-') & filters.me
)
async def add_module(client, message):
    reply_message = message.reply_to_message

    if not reply_message:
        await message.edit("🔴 В этом сообщении не обнаружено модуля.")
    else:
        if reply_message.document:
            file_name = reply_message.document.file_name
            file_id = reply_message.document.file_id

            if file_name.endswith(".zip"):
                await client.download_media(file_id, file_name=f'utils/misc/{file_name}')

                zip_path = os.path.join(os.getcwd(), "utils/misc/"+file_name)
                dest_path = os.path.join(os.getcwd(), "./modules/")

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(dest_path)

                if os.path.isfile("utils/misc/"+file_name):
                    os.remove("utils/misc/"+file_name)

            else:
                await client.download_media(file_id, file_name=f'modules/{file_name}')
            
            await message.edit('⚙️ Модуль успешно добавлен!\n\n🛠️ Перезагрузите скрипт командой -reload что-бы модули заработали.')
        else:
            await message.edit('🔴 В этом сообщении не обнаружено модуля.')

    await asyncio.sleep(10)
    await message.delete()

@Client.on_message(
    filters.command('del_module', prefixes='-') & filters.me
)
async def del_module(client, message):
    name_module = ' '.join(message.command[1:])
    try:
        if name_module.endswith(".py") == True:
            pass
        else:
            name_module = name_module+".py"

        exclude_modules = ["default", "default.py", "help",
                           "help.py", "_example", "_example.py"]

        if os.path.isfile("modules/"+name_module):
            if name_module in exclude_modules:
                await message.edit('🔴 Незя!')
            else:
                os.remove("modules/"+name_module)
                await message.edit("🟢 Модуль был удалён!")
        else:
            await message.edit("🔴 Такого модуля не существует.")
    except Exception as e:
        await message.edit("🛠️ Произошла ошибка:\n"+e)

    await asyncio.sleep(10)
    await message.delete()

@Client.on_message(
    filters.command('backup', prefixes='-') & filters.me
)
async def backup(client, message):
    await message.edit('⚙️ Бэкап модулей. Подождите...')

    zip_file = zipfile.ZipFile('modules.zip', 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk("modules/"):
        for file in files:
            if file.endswith('.py'):
                if file != '_example.py' and file != 'default.py' and file != 'help.py':
                    zip_file.write(os.path.join(root, file), arcname=os.path.basename(file))
    
    zip_file.close()
    await message.delete()

    with open("modules.zip", "rb") as file:
        await client.send_document(chat_id=message.chat.id, document=file, caption="🛠️ Бэкап модулей")

    if os.path.isfile("modules.zip"):
        os.remove("modules.zip")

@Client.on_message(
    filters.command('reload', prefixes='-') & filters.me
)
async def reload(client, message):
    rbool = ' '.join(message.command[1:])
    if rbool == "True":
        await message.edit('🔄️ Скрипт перезагружается...\n\n🛠️ Если это сообщение висит слишком долго то загляните в консоль(возможно вышла ошибка)')
        await client.restart(block=True)
        await message.edit('⚙️ Скрипт перезагрузился.')
    else:
        await message.edit('🔄️ Скрипт перезагружается...\n\n🛠️ Если это сообщение висит слишком долго то загляните в консоль(возможно вышла ошибка)')
        await client.restart(block=False)
        await message.edit('⚙️ Скрипт перезагрузился.')

    await asyncio.sleep(10)
    await message.delete()


add_command_help(
    "default",
    [
        ["-add_module", "Добавляет новый модуль(использывать в ответ на сообщение)"],
        ["-del_module <Название_модуля>", "Удаляет модуль"],
        ["-backup", "Делает бэкап всех модулей"],
        ["-reload", "Перезагружает скрипт"],
    ],
)