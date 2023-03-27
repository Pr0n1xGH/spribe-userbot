import colorama

from colorama import Fore, Style

colorama.init()

registration_message = f"{Fore.GREEN}{Style.BRIGHT}>>> Руководство по авторизации в скрипте @tgscriptss\n\n" \
                       f"{Fore.BLUE}{Style.BRIGHT}>> Ввод своих данных:\n" \
                       f"{Fore.WHITE}{Style.RESET_ALL}1. Вводите свой номер телефона\n" \
                       f"2. Ввод Y для подтверждения номера\n" \
                       f"3. Вводите код который придёт в телеграме\n" \
                       f"4. Пароль от двухэтапной авторизации (если он есть)\n" \
                       f"{Fore.YELLOW}"

logo_message = f"{Fore.BLUE}{Style.BRIGHT} ___ ___ ___ ___ ___ ___ \n" \
               f"/ __| _ \ _ \_ _| _ ) __|  _ __ _  _  \n" \
               f"\__ \  _/   /| || _ \ _| _| '_ \ || | \n" \
               f"|___/_| |_|_\___|___/___(_) .__/\_, | \n" \
               f"                   {Fore.RED}{Style.BRIGHT}v.1.4.0{Fore.BLUE}{Style.BRIGHT}|_|   |__/ \n" \
               f"{Fore.GREEN}{Style.BRIGHT}>>> Информация:\n" \
               f"{Fore.YELLOW}{Style.BRIGHT}Support: @devspribe\nTelegram: @tgscriptss\nTikTok: @tgscript\nВ других соц.сетях нас нет!\n\n" \
               f"{Fore.GREEN}{Style.BRIGHT}$ Скрипт запущен! Напишите {Fore.BLUE}{Style.BRIGHT}-modules{Fore.GREEN}{Style.BRIGHT}(в чат телеграма) что-бы посмотреть доступные модули"