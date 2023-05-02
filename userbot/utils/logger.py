# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import datetime
import logging

now = datetime.datetime.now()
date_string = now.strftime(f"%Y-%m-%d-%H-%M")

log_path = f"logs/logs-{date_string}.txt"
logging.basicConfig(filename=log_path, 
                    level=logging.INFO, 
                    format=f"%(asctime)s:%(name)s:%(process)d:%(lineno)d | %(levelname)s %(message)s")

logger = logging.getLogger(__name__)