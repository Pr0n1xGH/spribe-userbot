# This file is part of Spribe Userbot
#
# Spribe Userbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Spribe Userbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Spribe Userbot.  If not, see <https://www.gnu.org/licenses/>.


# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html


import asyncio
import logging
import glob
import os
import colorama

from pyrogram import Client
from colorama import Fore, Back, Style

logger = logging.getLogger(__name__)
plugins = dict(root="modules", exclude=['_excample'])
app = Client("spribe-userbot",
            api_id=25532442,
            api_hash="d3ad1172bb28a27bed7622728d66aabb",
            plugins=plugins,
            lang_code="ru",
            app_version="1.4",
            device_model="PC",
            system_version="spribe-userbot")

def main():
    if os.path.isfile("/src/userbot.session"):
        print(tg_logo)
        app.run()
    else:

        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        colorama.init()

        reg_message = f"{Fore.GREEN}{Style.BRIGHT}>>> Руководство по авторизации в скрипте @tgscriptss\n\n" \
                      f"{Fore.BLUE}{Style.BRIGHT}>> Ввод своих данных:\n" \
                      f"{Fore.WHITE}{Style.RESET_ALL}1. Вводите свой номер телефона\n" \
                      f"2. Ввод Y для подтверждения номера\n" \
                      f"3. Вводите код который придёт в телеграме\n" \
                      f"4. Пароль от двухэтапной авторизации (если он есть)\n" \
                      f"{Fore.YELLOW}"

        print(reg_message)

        app.start()
        app.stop()

        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        tg_logo = f"{Fore.BLUE}{Style.BRIGHT} ___ ___ ___ ___ ___ ___ \n" \
                  f"/ __| _ \ _ \_ _| _ ) __|  _ __ _  _  \n" \
                  f"\__ \  _/   /| || _ \ _| _| '_ \ || | \n" \
                  f"|___/_| |_|_\___|___/___(_) .__/\_, | \n" \
                  f"                   {Fore.RED}{Style.BRIGHT}v.1.4.0{Fore.BLUE}{Style.BRIGHT}|_|   |__/ \n" \
                  f"{Fore.GREEN}{Style.BRIGHT}>>> Информация:\n" \
                  f"{Fore.YELLOW}{Style.BRIGHT}Support: @devspribe\nTelegram: @tgscriptss\nTikTok: @tgscript\nВ других соц.сетях нас нет!\n\n" \
                  f"{Fore.GREEN}{Style.BRIGHT}$ Скрипт запущен! Напишите {Fore.BLUE}{Style.BRIGHT}-modules{Fore.GREEN}{Style.BRIGHT}(в чат телеграма) что-бы посмотреть доступные модули"

        print(tg_logo)

        app.run()

if __name__ == "__main__":
    main()
