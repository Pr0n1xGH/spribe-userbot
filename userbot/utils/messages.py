import colorama
from colorama import Fore, Style

from rich import print
from rich.panel import Panel
from rich.tree import Tree

colorama.init()

Version = "v1.0.3"

Logo_Message = f"{Fore.BLUE}{Style.BRIGHT} ___ ___ ___ ___ ___ ___ \n" \
               f"/ __| _ \ _ \_ _| _ ) __|  _ __ _  _  \n" \
               f"\__ \  _/   /| || _ \ _| _| '_ \ || | \n" \
               f"|___/_| |_|_\___|___/___(_) .__/\_, | \n" \
               f"                    {Fore.RED}{Style.BRIGHT}{Version}{Fore.BLUE}{Style.BRIGHT}|_|   |__/ \n\n" \
               f"{Fore.GREEN}{Style.BRIGHT}>>> Информация:\n" \
               f"{Fore.YELLOW}{Style.BRIGHT}Support: @devspribe\nTelegram: @tgscriptss\nTikTok: @tgscript\nВ других соц.сетях нас нет!\n"

Phone = f"{Fore.GREEN}{Style.BRIGHT}>>> Авторизация:\n{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введите свой номер телефона(без +):{Fore.WHITE}{Style.RESET_ALL} "

Close = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Что-бы выйти из юзербота нажмите Enter: "

Closed = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Вы вышли из юзербота."

BadRequest = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Ошибка ввода{Fore.WHITE}{Style.RESET_ALL}"

FloodWait = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} У вас флуд на авторизацию, подождите "

PhoneCodeInvalid = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Ошибка: Не правильно введён код"

PasswordHashInvalid = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Ошибка: Не правильно пароль"

Error = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Ошибка: {Fore.YELLOW}"

Code = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введите код с телеграма:{Fore.WHITE}{Style.RESET_ALL} "

Password = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введите пароль от двухэтапной аутентификации:{Fore.WHITE}{Style.RESET_ALL} "

Runned = f"{Fore.GREEN}{Style.BRIGHT}$ Скрипт запущен! Напишите {Fore.BLUE}{Style.BRIGHT}.help{Fore.GREEN}{Style.BRIGHT}(в чат телеграма) что-бы посмотреть доступные модули"

newRun = Tree("\n[green bold]>>> Информация:[/green bold]")
newRun.add("[yellow bold]Telegram:[/yellow bold] [link=https://t.me/tgscriptss]Тут можно скачать новые модули[/link]")
newRun.add("[yellow bold]Github:[/yellow bold] [link=https://github.com/Pr0n1xGH/spribe-userbot]Поставьте звёздочку :3[/link]")
newRun.add("[yellow bold]Support:[/yellow bold] [link=https://t.me/devspribe]Написать[/link]\n")

newLogo = Panel("", title="[blue bold]Spribe-Userbot[/blue bold]")
