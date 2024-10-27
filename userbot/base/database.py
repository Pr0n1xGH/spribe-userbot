# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import sqlite3
import time
import datetime
from typing import Optional, Tuple, Union


class DatabaseTime:
    """Класс для работы с базой данных времени пользователя"""
    
    def __init__(self) -> None:
        """Инициализация подключения к БД и создание таблицы"""
        self.conn = sqlite3.connect('userbot/base/databases/datatime.db')
        self.cur = self.conn.cursor()
        
        self._create_table()
        
    def _create_table(self) -> None:
        """Создание таблицы пользователя если она не существует"""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                first_start TEXT NOT NULL,
                first_time REAL NOT NULL
            )
        """)
        self.conn.commit()
        
    def get_first_date(self) -> Optional[Tuple[str]]:
        """Получение даты первого запуска"""
        return self.conn.execute('SELECT first_start FROM user').fetchone()
    
    def get_uptime(self) -> str:
        """Получение времени работы в человекочитаемом формате"""
        ftime = self.conn.execute('SELECT first_time FROM user').fetchone()
        if not ftime:
            return "0с"
            
        elapsed = time.time() - float(ftime[0])
        return self._format_time_interval(elapsed)
    
    def _format_time_interval(self, seconds: float, granularity: int = 3) -> str:
        """
        Форматирование временного интервала в читаемый вид
        
        Args:
            seconds: Количество секунд
            granularity: Максимальное количество временных единиц в выводе
            
        Returns:
            Отформатированная строка времени
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
            value = int(seconds // count)
            if value:
                seconds -= value * count
                result.append(f"{value} {name}")
                
        return ', '.join(result[:granularity]) if result else '0с'


# Инициализация первого запуска
db = DatabaseTime()
if not db.get_first_date():
    current_time = time.time()
    current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    
    db.cur.execute("INSERT INTO user VALUES (?, ?)", (current_date, current_time))
    db.conn.commit()
