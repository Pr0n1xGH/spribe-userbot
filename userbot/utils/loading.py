# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import threading
import itertools
import time
import shutil
import sys
from typing import Optional

class Loader:
    """
    Класс для отображения анимированного индикатора загрузки в терминале.
    
    Attributes:
        desc (str): Описание загрузки
        end (str): Сообщение по завершении
        timeout (float): Задержка между кадрами анимации
        done (bool): Флаг завершения анимации
    """
    
    def __init__(
        self,
        desc: str = "Загрузка...",
        end: str = "Готово!",
        timeout: float = 0.1
    ) -> None:
        self.desc = desc
        self.end = end 
        self.timeout = timeout
        self.done = False
        
        self._animation_chars = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self._thread = threading.Thread(target=self._animate, daemon=True)
        
    def start(self) -> 'Loader':
        """Запускает анимацию в отдельном потоке"""
        self._thread.start()
        return self
        
    def stop(self) -> None:
        """Останавливает анимацию и выводит финальное сообщение"""
        self.done = True
        self._thread.join()
        
        # Очищаем текущую строку
        cols = shutil.get_terminal_size().columns
        sys.stdout.write('\r' + ' ' * cols)
        sys.stdout.write(f'\r{self.end}\n')
        sys.stdout.flush()

    def _animate(self) -> None:
        """Основной цикл анимации"""
        for char in itertools.cycle(self._animation_chars):
            if self.done:
                break
                
            sys.stdout.write(f'\r{self.desc} {char} ')
            sys.stdout.flush()
            time.sleep(self.timeout)

    def __enter__(self) -> 'Loader':
        """Поддержка контекстного менеджера"""
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Автоматическая остановка при выходе из контекста"""
        self.stop()
