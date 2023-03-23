# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

from pyrogram import Client, filters

import os, inspect, importlib
import asyncio

@Client.on_message(filters.command('modules', prefixes='-') & filters.me)
async def modules(client, message):
    modules_dir = 'modules'
    modules_functions = {}
    files = os.listdir(modules_dir)

    for file_name in files:
        if file_name.endswith('.py'):
            module_name = file_name[:-3]
            module = importlib.import_module(f'{modules_dir}.{module_name}')

            functions = inspect.getmembers(module, inspect.isfunction)

            modules_functions[module_name] = [function_name for function_name, _ in functions]

    text = "🛠️ Все загруженные модули:\n\n"
    for module_name, functions in modules_functions.items():
        if module_name == "_excample":
            pass
        else:
            text = text+f"» {module_name}: ({', '.join(functions)})\n"

            await message.edit(text)

    text = text+"\nИспользование:\n» Название модуля: (Доступные команды)"
    await message.edit(text)

@Client.on_message(filters.command('add_module', prefixes='-') & filters.me)
async def add_module(client, message):
    reply_message = message.reply_to_message

    if reply_message.document:
        file_id = reply_message.document.file_id
        file_name = reply_message.document.file_name

        await client.download_media(file_id, file_name=f'modules/{file_name}')
        await message.edit('⚙️ Модуль успешно добавлен!\n\n🛠️ Перезагрузите скрипт командой -reload что-бы модули заработали.')
    else:
        await message.edit('🔴 В этом сообщении не обнаружено модуля.')

@Client.on_message(filters.command('del_module', prefixes='-') & filters.me)
async def del_module(client, message):
    name_module = ' '.join(message.command[1:])
    try:
        if name_module.endswith(".py") == True:
            pass
        else:
            name_module = name_module+".py"

        if os.path.isfile("modules/"+name_module):
            if name_module == "standart" or name_module == "standart.py":
                await message.edit('🔴 Незя!')
            elif name_module == "help" or name_module == "help.py":
                await message.edit('🔴 Незя!')
            elif name_module == "_excample" or name_module == "_excample.py":
                await message.edit('🔴 Незя!')
            else:
                os.remove("modules/"+name_module)
                await message.edit("🟢 Модуль был удалён!")
        else:
            await message.edit("🔴 Такого модуля не существует.")
    except Exception as e:
        await message.edit("🛠️ Произошла ошибка:\n"+e)

@Client.on_message(filters.command('reload', prefixes='-') & filters.me)
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

