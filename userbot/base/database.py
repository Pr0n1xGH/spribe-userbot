# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3

import time
import datetime

conn = sqlite3.connect(r'userbot/base/base.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user(
   first_start TEXT,
   first_time REAL);
""")
conn.commit()

check = cur.execute("SELECT first_start FROM user")

if check.fetchone() is None: 
    first_time = time.time()
    
    now = datetime.datetime.now()
    first_date = now.strftime(f"%Y-%m-%d %H-%M")
    
    cur.execute("INSERT INTO user VALUES(?, ?);", (first_date, first_time))
    conn.commit()
    
    
def get_fdate() -> any:
    fdate = conn.execute(f'SELECT first_start FROM user').fetchone()
    
    return fdate

def get_ftime() -> any:
    ftime = conn.execute(f'SELECT first_time FROM user').fetchone()
    secs = time.time() - float(ftime[0])
    
    return display_time(secs)

intervals = (
    ('нед', 604800),
    ('дн', 86400),
    ('ч', 3600),
    ('м', 60),
    ('с', 1),
)

def display_time(seconds, granularity=2):
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])