# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio

from pyrogram.types import Message
from pyrogram import Client, filters

CMD_HELP = {}

@Client.on_message(
    filters.command("help", ".") & filters.me
)
async def help_command_handler(client: Client, message: Message):
    cmd = message.command
    if len(cmd) > 1:
        module_name = " ".join(cmd[1:])
        await send_help_message(message, module_name)
    elif message.reply_to_message:
        try:
            help_arg = message.reply_to_message.text
            if help_arg in CMD_HELP:
                module_name = help_arg.split("\n")[0].strip().replace("Информация о ", "").replace(":", "")
                await send_help_message(message, module_name)
            else:
                await send_help_message(message)
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        await send_help_message(message)

    await asyncio.sleep(10)
    await message.delete()

def add_command_help(module_name: str, commands: list):
    command_dict = CMD_HELP.setdefault(module_name, {})
    for command, description in commands:
        command_dict[command] = description

def split_list(input_list: list, n: int):
    n = max(1, n)
    return [input_list[i: i + n] for i in range(0, len(input_list), n)]

async def send_help_message(message: Message, module_name: str = None):
    if module_name:
        if module_name in CMD_HELP:
            commands = CMD_HELP[module_name]
            module_help = f"**Информация о {module_name}:**\n\n"
            for command, description in commands.items():
                module_help += f"`{command}` - {description}\n"
            await message.edit_text(module_help)
        else:
            await message.edit_text("`Пожалуйста, укажите нормальное имя модуля.`")
    else:
        all_commands = "**Список модулей:**\n\n"
        for module_group in split_list(sorted(CMD_HELP.keys()), 2):
            all_commands += "» "+f"{' '.join(module_group)}\n"
        all_commands += "\nЧтобы получить информацию по определенному модулю, используйте `.help [название_модуля]`"
        await message.edit_text(all_commands)