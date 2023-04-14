<p align="center">
  <img src="https://github.com/Pr0n1xGH/scr/blob/main/logo.png" />
  <br>
  <b>Spribe-Userbot (beta)</b>
  <br>
  <b>Make your life in Telegram easier and more convenient with Spribe-Userbot</b>
  <br>
  <a href='https://github.com/Pr0n1xGH/spribe-userbot#installation'>
        Installation
  </a>
  –
  <a href='https://t.me/tgscriptss'>
        Telegram channel
  </a>
  –
  <a href="https://github.com/Pr0n1xGH/spribe-userbot/releases">
        Releases
  </a>
  -
  <a href="https://github.com/Pr0n1xGH/spribe-userbot/blob/main/README.md#example-of-creating-modules">
        Еxample of creating a module
  </a>
  <br>
</p>

# <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M392.8 1.2c-17-4.9-34.7 5-39.6 22l-128 448c-4.9 17 5 34.7 22 39.6s34.7-5 39.6-22l128-448c4.9-17-5-34.7-22-39.6zm80.6 120.1c-12.5 12.5-12.5 32.8 0 45.3L562.7 256l-89.4 89.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l112-112c12.5-12.5 12.5-32.8 0-45.3l-112-112c-12.5-12.5-32.8-12.5-45.3 0zm-306.7 0c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3l112 112c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L77.3 256l89.4-89.4c12.5-12.5 12.5-32.8 0-45.3z"/></svg> Installation
> Linux, Termux (use f-droid version) and Windows [only wsl]

<pre><code>pkg install --yes git python && yes | pkg update && pkg upgrade && git clone https://github.com/Pr0n1xGH/spribe-userbot.git && cd spribe-userbot && pip install -r requirements.txt && python main.py</pre></code>

> Windows

<pre><code>1. Install python 3.9 or higher
2. Run the winStart.cmd file</pre></code>

# Example of creating modules
<sup>To create modules, you need to know the basics of Python and the Pyrogram library.</sup>
> 1. Importing libraries
```python
from pyrogram import Client, filters
from modules.help import add_command_help
```
> 2. Then you need to create a function that will perform certain actions. In the example below, the decorator `@Client.on_message` is created, which calls the `exhelp` function when the userbot receives a message with the `.exhelp` command.
```python
@Client.on_message(
    filters.command('exhelp', prefixes='.') & filters.me
)
async def exhelp(client, message):
    await message.edit_text("example help message") # Just an example
```

<sub>It is important to remember that the function name should not be repeated anywhere. If the function name already exists somewhere, the module will not be loaded. The same applies to teams. If the command already exists somewhere, the module will not be loaded (or an error occurs).</sup>

> 3. To add a module to `.help`, use the `add_command_help` function. The example below shows the code that adds the `excample` module to `.help` and defines two commands: `.command` with the description `description` and `.exHelp` with the description `example help`.

```python
add_command_help(
    "excample",
    [
        [".command", "description"],
        [".exHelp", "example help"],
    ]
)
```

> The whole code:
```python
from pyrogram import Client, filters
from modules.help import add_command_help


@Client.on_message(
    filters.command('exhelp', prefixes='.') & filters.me
)
async def exhelp(client, message):
    await message.edit_text("example help message")


add_command_help(
    "excample",
    [
        [".exHelp", "example help"],
    ]
)
```

# About
<p>Spribe-Userbot is a Telegram userbot (in case you didn't know, selfbot/userbot are used to automate user accounts).
So how does it work? It works in a very simple way, using the pyrogram library, a python script connects to your account (creating a new session) and catches your commands.

Using selfbot/userbot is against Telegram's Terms of Service, and you may get banned for using it if you're not careful.

The developers are not responsible for any consequences you may encounter when using Spribe-Userbot. We are also not
responsible for any damage to chat rooms caused by using this userbot.</p>
