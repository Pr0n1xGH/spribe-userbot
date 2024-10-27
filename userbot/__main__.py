# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import sys
import traceback
from typing import NoReturn
from rich.console import Console
from sqlite3 import OperationalError

from .utils.logger import logger
import nest_asyncio

nest_asyncio.apply()
console = Console()

def check_python_version() -> bool:
    return sys.version_info >= (3, 9, 0)

def check_package_name() -> bool:
    return __package__ == "userbot"

async def main() -> NoReturn:
    if not check_python_version():
        console.print("[red]Ошибка: требуется Python версии 3.9.0 или выше[/red]")
        sys.exit(1)
        
    if not check_package_name():
        console.print("[red]Ошибка: запуск возможен только как пакет Python[/red]")
        sys.exit(1)
        
    try:
        from .main import UserBot
        await UserBot()._start()
        
    except OperationalError as e:
        logger.error("Ошибка базы данных: %s", traceback.format_exc())
        console.print("[red]Критическая ошибка при работе с базой данных[/red]")
        
    except Exception as e:
        logger.error("Необработанное исключение: %s", traceback.format_exc())
        console.print_exception()
        
if __name__ == "__main__":
    asyncio.run(main())
