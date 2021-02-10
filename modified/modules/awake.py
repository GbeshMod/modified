
"""Check if userbot is awake or not . 

"""

from math import ceil
import io, os, re, json, random, asyncio
from telethon import version, __version__
from telethon import events, errors, custom
from telethon.tl.types import ChannelParticipantsAdmins
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/59b391c52953c21f7b82b.jpg"

global ghanti
moddd = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else botnickname

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = f"**🔱{botnickname} BOT IS Awake🔱 \n\n\n**"
   ALIVE_MESSAGE += f"`°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°`\n 
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"️📱 `Telethon       : v{version.__version__}`\n"
   ALIVE_MESSAGE += f"🐍 `Python         : v{python_version()}`\n"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n`"
   ALIVE_MESSAGE +=  f"🤖 `[MODIFIED](https://github.com/GbeshMod/modified)       : v{mod_version}`\n"
   ALIVE_MESSAGE +=  f"`MY Master🕺🏽`      : [{DEFAULTUSER}](tg://user?id={moddd}) \n
   ALIVE_MESSAGE += f"`°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°`\n "



@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "**AWake**\
\n\n**Syntax : **`.awake`\
\n**Usage :** Check if UserBot is AWake"
    }
)