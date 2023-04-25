# This file is part of Spribe Userbot
#
# Spribe Userbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Spribe Userbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Spribe Userbot.  If not, see <https://www.gnu.org/licenses/>.

# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import os
import asyncio

from pyrogram import Client, idle
from pyrogram.errors import SessionPasswordNeeded, BadRequest, \
                            FloodWait, PhoneCodeInvalid, PasswordHashInvalid

from .utils import messages

class UserBot(Client):
    def __init__(self):
        super().__init__(
            "spribe-userbot",
            api_id=18822408,
            api_hash="e2c5ab68e39c32c3a0ce94570204a0a4",
            plugins=dict(root=f"userbot/plugins", exclude=["_example"]),
            workdir="userbot/utils/misc/",
        )

    def main(self):
        if os.path.isfile("userbot/utils/misc/spribe-userbot.session"):   
            self.clear()
            print(messages.Logo_Message + "\n" + messages.Runned)
            self.run()

        else:
            self.clear()
            print(messages.Logo_Message)
            self.connect()
            
            while True:
                try:
                    phone_ = input(messages.Phone)
                    sent_code_info = self.send_code(f"+{str(phone_)}")
                    break
                
                except BadRequest:
                    print(messages.BadRequest)
                    
                except FloodWait as fw:
                    print(messages.FloodWait + fw.value + "секунд.")
                    break
                
                except Exception as e:
                    print(f"{messages.Error}{e}")
                    
            try:
                phone_code = input(messages.Code)
                
                self.sign_in(phone_number = phone_, 
                            phone_code_hash = sent_code_info.phone_code_hash,
                            phone_code = phone_code)
                
                self.clear()
                print(messages.Logo_Message + "\n" + messages.Runned)
                
                self.disconnect()
                self.run()

            except SessionPasswordNeeded:
                while True:
                    try:
                        password = str(input(messages.Password))
                        
                        self.check_password(password)
                        
                        self.clear()
                        print(messages.Logo_Message + "\n" + messages.Runned)
                        
                        self.disconnect()
                        self.run()
                        break
                    
                    except PasswordHashInvalid:
                        print(messages.PasswordHashInvalid)
                
            except PhoneCodeInvalid:
                print(messages.PhoneCodeInvalid)
                
            except Exception as e:
                print(f"{messages.Error}{e}")

    def clear(self):
        if os.sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
