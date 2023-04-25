# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import os
import zipfile
import glob
from pathlib import Path

from pyrogram import Client, filters

from .help import add_command_help
from ..__main__ import logger


@Client.on_message(
    filters.command('loadmod', prefixes='.') & filters.me
)
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

                zip_path = os.path.join(os.getcwd(), "utils/misc/" + file_name)
                dest_path = os.path.join(os.getcwd(), "./modules/")

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(dest_path)

                if os.path.isfile("utils/misc/" + file_name):
                    os.remove("utils/misc/" + file_name)

            else:
                await client.download_media(file_id, file_name=f'modules/{file_name}')

            await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Модуль успешно добавлен!\n\n<emoji id=5341350410252723241>🛠️</emoji> Перезагрузите скрипт командой -reload что-бы модули заработали.')
        else:
            await message.edit('<emoji id=5210952531676504517>🔴</emoji> ▸ В этом сообщении не обнаружено модуля.')

    await asyncio.sleep(10)
    await message.delete()
    
    
@Client.on_message(
    filters.command('unloadmod', prefixes='.') & filters.me
)
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
    
    
@Client.on_message(
    filters.command('backup', prefixes='.') & filters.me
)
async def backup(client, message):
    await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Бэкап модулей. Подождите...')

    zip_file = zipfile.ZipFile('modules.zip', 'w', zipfile.ZIP_DEFLATED)

    modules = 0
    for root, dirs, files in os.walk("modules/"):
        for file in files:
            if file.endswith('.py'):
                if file != '_example.py' and file != 'default.py' and file != 'help.py':
                    zip_file.write(os.path.join(root, file), arcname=os.path.basename(file))
                    modules += 1

    zip_file.close()
    await message.delete()

    with open("modules.zip", "rb") as file:
        await client.send_document(chat_id=message.chat.id, document=file, caption=f"<emoji id=5449555539975481957>📦</emoji> ▸ Бэкап модулей ({modules})")

    if os.path.isfile("modules.zip"):
        os.remove("modules.zip")
        
        
@Client.on_message(
    filters.command('reload', prefixes='.') & filters.me
)
async def reload(client, message):
    block = ' '.join(message.command[1:])
    
    try:
        await message.edit('<emoji id=5438274168422409988>🔄️</emoji> ▸ Скрипт перезагружается...')
        await client.restart(block = block == "True")
        await message.edit('<emoji id=5438274168422409988>⚙</emoji> ▸ Скрипт перезагрузился.')
        
    except Exception as e:
        await message.edit(f'<emoji id=5438274168422409988>🔄️</emoji> ▸ Ошибка...\n\n<emoji id=5386757912607599167>🛠️</emoji> {e}')
    
    await asyncio.sleep(10)
    await message.delete()


@Client.on_message(
    filters.command("logs", ".") & filters.me
)
async def logs(client, message):
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
                chat_id = message.chat.id, 
                document = file, 
                caption = f"`logs from Spribe-Userbot`"
            )

        if os.path.isfile(zip_name):
            os.remove(zip_name)

    else:
        logs_dir = glob.glob("logs/*")
        latest_file = max(logs_dir, key = os.path.getctime)
        
        try:
            file_text = Path(latest_file).read_text(encoding='utf-8')
        except UnicodeDecodeError:
            file_text = Path(latest_file).read_text(encoding='latin-1')

        if len(file_text) > 3000:
            await message.delete()
            await client.send_document(
                chat_id = message.chat.id,
                document = latest_file,
                caption = "`logs from Spribe-Userbot`"
            )

        else:
            await message.edit(f"logs from Spribe-Userbot \n`{file_text}`")

    logger.info("Были взяты логи командой .logs")
    
add_command_help(
    "default",
    [
        [".loadmod", "Добавляет новый модуль(используется в ответ на сообщение)"],
        [".unloadmod [Название модуля]", "Удаляет модуль"],
        [".backup", "Делает бэкап всех модулей"],
        [".logs [all]", "Даёт логи последнего запуска скрипта(без all) / Даёт zip файл со всеми логами"],
        [".reload", "Перезагружает скрипт"],
    ],
)
