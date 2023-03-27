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
from utils import messages

logger = logging.getLogger(__name__)

plugins = dict(root="modules", exclude=['_example'])
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
        print(messages.logo_message)
        app.run()
    else:
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        print(messages.registration_message)

        app.start()
        app.stop()

        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        print(messages.logo_message)

        app.run()

if __name__ == "__main__":
    main()
