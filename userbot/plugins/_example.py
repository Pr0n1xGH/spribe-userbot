# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

"""
Это пример создания модуля для Spribe Userbot.
Здесь вы найдете базовые принципы создания своих команд.
"""

# Для создания модулей вам понадобятся:
# 1. Базовые знания Python
# 2. Понимание работы с библиотекой Pyrogram
# 3. Немного терпения :)

# Импортируем необходимые компоненты
from .help import add_command_help  # Для добавления команд в справочник .help
from ..utils.logger import logger   # Для логирования ошибок и событий

# Основные компоненты Pyrogram
from pyrogram import Client, filters

# Создаем простую команду
# filters.command('команда', prefixes='.') - указываем название команды и префикс
# filters.me - команда будет работать только от владельца юзербота
@Client.on_message(filters.command('exhelp', prefixes='.') & filters.me)
async def example_help(client, message):
    """
    Пример простой команды, которая отправляет сообщение.
    
    Важные замечания:
    1. Название функции должно быть уникальным во всем юзерботе
    2. Команда также должна быть уникальной
    3. Рекомендуется использовать префикс в названии функции 
       (например: ex_help, если ваш модуль называется example)
    """
    await message.edit_text("Это пример сообщения помощи!")

# Как добавить команду в справочник .help:
add_command_help(
    "example",  # Название модуля (должно совпадать с названием файла без .py)
    [
        [".exhelp", "Показывает пример сообщения помощи"],
        # Можно добавить больше команд:
        # [".команда", "описание команды"],
    ]
)

"""
Полезные советы:
1. Всегда добавляйте описание к своим функциям через docstring
2. Используйте logger для отлова ошибок
3. Соблюдайте уникальность названий команд и функций
4. Старайтесь писать понятный и читаемый код

Нужна помощь или есть вопросы?
- Telegram: @nob0dy_tg

Хотите поделиться своим модулем?
- Напишите нам в Telegram для публикации в @tgscriptss
"""

# ===========================================================================================

"""
This is an example of creating a module for Spribe Userbot.
Here you will find the basic principles of creating your own commands.
"""

# To create modules you will need:
# 1. Basic Python knowledge
# 2. Understanding of working with Pyrogram library
# 3. A little patience :)

# Import necessary components
from .help import add_command_help  # For adding commands to .help reference
from ..utils.logger import logger   # For logging errors and events

# Main Pyrogram components
from pyrogram import Client, filters

# Create a simple command
# filters.command('command', prefixes='.') - specify command name and prefix
# filters.me - command will only work from userbot owner
@Client.on_message(filters.command('exhelp', prefixes='.') & filters.me)
async def example_help(client, message):
    """
    Example of a simple command that sends a message.
    
    Important notes:
    1. Function name must be unique across the entire userbot
    2. Command must also be unique
    3. It is recommended to use a prefix in the function name
       (e.g., ex_help if your module is called example)
    """
    await message.edit_text("This is an example help message!")

# How to add a command to .help reference:
add_command_help(
    "example",  # Module name (must match filename without .py)
    [
        [".exhelp", "Shows example help message"],
        # You can add more commands:
        # [".command", "command description"],
    ]
)

"""
Useful tips:
1. Always add descriptions to your functions via docstring
2. Use logger to catch errors
3. Maintain uniqueness of command and function names
4. Try to write clear and readable code

Need help or have questions?
- Telegram: @nob0dy_tg

Want to share your module?
- Write to us on Telegram for publication in @tgscriptss
"""
