# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio

from pyrogram.types import Message
from pyrogram import Client, filters

from ..__main__ import logger

CMD_HELP = {}

@Client.on_message(
    filters.command("help", ".") & filters.me
)
async def help_command_handler(client: Client, message: Message):
    args = message.command
    
    try:
        if len(args) > 1:
            module_name = " ".join(args[1:])
            await send_help_message(message, module_name)

        elif message.reply_to_message and message.reply_to_message.text in CMD_HELP:
            help_arg = message.reply_to_message.text

            module_name = (help_arg.split("\n")[0]
                          .strip()
                          .replace("Информация о ", "")
                          .replace(":", ""))

            await send_help_message(message, module_name)
        else:
            await send_help_message(message)
    except Exception as e:
        await message.edit(f"<emoji id=5210952531676504517>🔴</emoji> Ошибка: {e}")
        logger.error(f"Error: help_command_handler: {e}")

    await asyncio.sleep(20)
    await message.delete()


def add_command_help(module_name: str, commands: list) -> None:
    command_dict = CMD_HELP.setdefault(module_name, {})
    
    for command, description in commands:
        command_dict[command] = description


def split_list(input_list: list, n: int) -> list:    
    n = max(1, n)
    return [input_list[x:x+n] for x in range(0, len(input_list), n)]


async def send_help_message(message: Message, module_name: str = None) -> None:
    if not module_name:
        all_commands = "**<emoji id=5447410659077661506>🛠️</emoji> __Список модулей__:**\n"
        for module_group in split_list(sorted(CMD_HELP.keys()), 2):
            all_commands += "• " + "\n• ".join(map(str, ["`" + cmd + "`" for cmd in module_group])) + "\n"
        all_commands += '\n<emoji id=5397782960512444700>⚙️</emoji> __Чтобы получить информацию по определенному модулю, используйте:__ `.help [Название модуля]`<a href="https://i.ibb.co/YW6RmJL/photo-2023-04-10-15-15-57.jpg">&#8203;</a>'
        await message.edit_text(all_commands)
    elif module_name in CMD_HELP:
        module_help = f'<emoji id=5443132326189996902>🍃</emoji> __Информация о__ **{module_name}**:<a href="https://i.ibb.co/Gv14bhw/photo-2023-04-10-15-16-04.jpg">&#8203;</a>\n'
        for command, description in CMD_HELP[module_name].items():
            module_help += f"**`{command}`** \n└ __{description}__\n"
        await message.edit_text(module_help)
    else:
        await message.edit_text("`<emoji id=5210952531676504517>🔴</emoji> Пожалуйста, укажите нормальное имя модуля.`")
