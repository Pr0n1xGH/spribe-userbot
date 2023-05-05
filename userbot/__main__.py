# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import sys
import traceback
import nest_asyncio
from rich.console import Console
from sqlite3 import OperationalError

from .utils.logger import logger

nest_asyncio.apply()
console = Console()

if __name__ == "__main__":
    if sys.version_info < (3, 9, 0):
        print("Error: you must use at least Python version 3.9.0")

    elif __package__ != "userbot":
        print("Error: you cannot run this as a script, you must execute as a package")

    else:
        try:
            from .main import UserBot
            
            asyncio.run(UserBot()._start())
            
        except OperationalError:
            logger.error(f"{traceback.format_exc()}")

        except Exception as e:
            logger.error(f"{traceback.format_exc()}")
            console.print_exception()
