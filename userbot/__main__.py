# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import datetime
import logging

import sys

# logs
now = datetime.datetime.now()
date_string = now.strftime(f"%Y-%m-%d_%H-%M")

dir_path = os.getcwd()
log_path = os.path.join(dir_path, f"userbot/utils/misc/logs/logs-{date_string}.txt")

with open(log_path, 'w') as f:
    f.write("-- logging --")

logging.basicConfig(filename=log_path, level=logging.INFO)

# launch point
if sys.version_info < (3, 9, 0):
    print("Error: you must use at least Python version 3.9.0")

elif __package__ != "userbot":
    print("Error: you cannot run this as a script, you must execute as a package")

else:
    try:
        from .main import UserBot
        
        try:
            ubot = UserBot()
            ubot.main()
        except KeyboardInterrupt:
            sys.exit()

    except Exception as e:
        from .main import messages

        print(f"{messages.Error}{e}")
