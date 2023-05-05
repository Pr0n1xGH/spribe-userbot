# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3

import time
import datetime


class basetime():
    def __init__(self) -> None:
        self.conn = sqlite3.connect(r'userbot/base/databases/datatime.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user(
            first_start TEXT,
            first_time REAL);
        """)
        self.conn.commit()
        
    def get_fdate(self) -> any:
        self.fdate = self.conn.execute(f'SELECT first_start FROM user').fetchone()
        
        return self.fdate
    
    def get_ftime(self) -> any:
        ftime = self.conn.execute(f'SELECT first_time FROM user').fetchone()
        secs = time.time() - float(ftime[0])
        
        return self.display_time(secs)
    
    def display_time(self, seconds, granularity=3) -> any:
        """Turns seconds into a more pleasant view

        Args:
            - seconds (int): seconds
            - granularity (int, optional): maximum output of internals. Defaults to 3.

        Returns:
            Turns it into finished text
        """
        intervals = (
            ('нед', 604800),
            ('дн', 86400),
            ('ч', 3600),
            ('м', 60),
            ('с', 1),
        )
        
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result[:granularity])

check = basetime().cur.execute("SELECT first_start FROM user")

if check.fetchone() is None: 
    first_time = time.time()
    
    now = datetime.datetime.now()
    first_date = now.strftime(f"%d.%m.%Y %H:%M")
    dt = basetime()
    
    dt.cur.execute("INSERT INTO user VALUES(?, ?);", (first_date, first_time))
    dt.conn.commit()
