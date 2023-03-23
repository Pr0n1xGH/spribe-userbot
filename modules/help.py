# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

from pyrogram import Client, filters

@Client.on_message(filters.command('spr_help', prefixes='.') & filters.me)
async def spr_help(client, message):
    msg = f"🛠️ Инструкция по spribe-userbot\n\n" \
          f"`-modules` - Показывает все доступные модули\n" \
          f"`-add_module` (использывать в ответ на сообщение с модулем) - Добавляет модуль\n" \
          f"`-del_module` <Название модуля> - Удаляет модуль\n" \
          f"`-reload` - Перезапускает скрипт\n\n" \
          f"🍃 Все остальные команды начинаются на точку вместо тире, список всех команд можно посмотреть в `-modules`"

    await message.edit_text(msg)