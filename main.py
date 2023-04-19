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

import logging
import os

from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded, BadRequest, FloodWait, PhoneCodeInvalid, Unauthorized

from utils import messages

logger = logging.getLogger(__name__)

modules = dict(root="modules", exclude=['_example'])
app = Client("spribe-userbot",
             api_id=25532442,
             api_hash="d3ad1172bb28a27bed7622728d66aabb",
             plugins=modules,
             workdir="utils/misc/")


def main():
    if os.path.isfile("utils/misc/spribe-userbot.session"):
        if not os.path.exists("utils/misc"):
            os.makedirs("utils/misc")
            
        clear()
        print(messages.Logo_Message)
        print(messages.Runned)
        app.run()

    else:
        if not os.path.exists("utils/misc"):
            os.makedirs("utils/misc")

        clear()
        print(messages.Logo_Message)
        app.connect()
        
        while True:
            try:
                phone_ = input(messages.Phone)
                sent_code_info = app.send_code(f"+{str(phone_)}")
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
            
            app.sign_in(phone_number = phone_, 
                        phone_code_hash = sent_code_info.phone_code_hash,
                        phone_code = phone_code)
            
            clear()
            print(messages.Logo_Message + messages.Runned)
            
            app.disconnect()
            app.run()
            
        except SessionPasswordNeeded:
            password = str(input(messages.Password))
            
            app.check_password(password)
            
            clear()
            print(messages.Logo_Message + messages.Runned)
            
            app.disconnect()
            app.run()
            
        except PhoneCodeInvalid:
            print(messages.PhoneCodeInvalid)
            
        except Exception as e:
            print(f"{messages.Error}{e}")


def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
   main()
