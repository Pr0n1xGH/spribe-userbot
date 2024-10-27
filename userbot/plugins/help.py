# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
from typing import Dict, List, Optional

from pyrogram.types import Message
from pyrogram import Client, filters

from ..utils.logger import logger

CMD_HELP: Dict[str, Dict[str, str]] = {}

@Client.on_message(filters.command("help", ".") & filters.me)
async def help_command_handler(client: Client, message: Message) -> None:
    """Обработчик команды help"""
    cmd = message.command
    
    if len(cmd) > 1:
        module_name = " ".join(cmd[1:]).lower()
        await send_help_message(message, module_name)
    elif message.reply_to_message:
        try:
            help_arg = message.reply_to_message.text
            if help_arg in CMD_HELP:
                module_name = (help_arg
                             .split("\n")[0]
                             .strip()
                             .replace("Информация о ", "")
                             .replace(":", ""))
                await send_help_message(message, module_name)
            else:
                await send_help_message(message)
        except Exception as e:
            print(f"<emoji id=5210952531676504517>🔴</emoji> Ошибка: {e}")
            logger.error(f"help_command_handler: {e}")
    else:
        await send_help_message(message)
        
    await asyncio.sleep(20)
    await message.delete()


def add_command_help(module_name: str, commands: List[tuple[str, str]]) -> None:
    """Добавляет команды в справочник помощи"""
    command_dict = CMD_HELP.setdefault(module_name, {})
    for command, description in commands:
        command_dict[command] = description


def split_list(input_list: list, n: int) -> List[list]:
    """Разделяет список на подсписки заданного размера"""
    n = max(1, n)
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]


async def send_help_message(message: Message, module_name: Optional[str] = None) -> None:
    """Отправляет сообщение с помощью"""
    if module_name:
        if module_name in CMD_HELP:
            commands = CMD_HELP[module_name]
            module_help = (
                f"<emoji id=5443132326189996902>🍃</emoji> __Информация о__ **{module_name}**:"
                f"<a href=\"https://i.ibb.co/Gv14bhw/photo-2023-04-10-15-16-04.jpg\">&#8203;</a>\n\n"
            )
            for command, description in commands.items():
                module_help += f"**`{command}`** \n└ __{description}__\n"
            await message.edit_text(module_help)
        else:
            await message.edit_text(
                "`<emoji id=5210952531676504517>🔴</emoji> Пожалуйста, укажите нормальное имя модуля.`"
            )
    else:
        all_commands = "**<emoji id=5447410659077661506>🛠️</emoji> __Список модулей__:**\n\n"
        for module_group in split_list(sorted(CMD_HELP.keys()), 2):
            all_commands += "• " + '\n• '.join(f"`{cmd}`" for cmd in module_group) + "\n"
            
        all_commands += (
            f"\n<emoji id=5397782960512444700>⚙</emoji> __Чтобы получить информацию по определенному модулю, используйте:__"
            f" `.help [Название модуля]`<a href=\"https://i.ibb.co/YW6RmJL/photo-2023-04-10-15-15-57.jpg\">&#8203;</a>"
        )
        await message.edit_text(all_commands)
