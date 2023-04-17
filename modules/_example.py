# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

""" Пример создания модулей """

# Что-бы создавать модули вы должны знать основы языка Python и библиотеки Pyrogram

from modules.help import add_command_help 
from pyrogram import Client, filters # Импорт библиотек. 
                                     # Можно использовать любые другие, которые есть в requirements.txt, или
                                     # по умолчанию уже встроенные в Python.

                                     # Функция add_command_help нужна для добавления ваших модулей в .help

@Client.on_message(
    filters.command('exhelp', prefixes='.') & filters.me # Создаём декоратор.
)
async def exhelp(client, message): # ВАЖНО: название функции не должно повторяться где-либо.
                                   # Если название функции уже где-то существует, модуль не будет загружен.

                                   # Также работает с командами. Если где-то команда уже существует, модуль не будет загружен (или возникнет ошибка).

                                   # Можно перед названием использовать свой префикс, например,
                                   # если ваш канал/ник называется example, а ваша функция делает help сообщение, то можно назвать ее "exHelp".

    """ Далее создаём фрагмент кода """

    await message.edit_text("example help message") # Просто пример


"""
Добавление модуля в .help
"""

# Где "excample" это название модуля.
# Называйте свой файл так-же как и название модуля.

# [".command", "description"] - В первых - ковычках название команды, во вторых - описание команды

"""
add_command_help(
    "excample",
    [
        [".command", "description"],
        [".exHelp", "example help"],
    ]
)
"""

# Что-то пошло не так или вам нужна помощь? - tg: @devspribe
# Если хотите опубликовать свой модуль в канал @tgscriptss - напишите в телеграм который есть выше.