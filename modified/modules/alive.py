# modify by Gβε₷Ἥ
# Kang with credits else ☣️
""" 
Check if Robot is alive
Original Plugin By @Gβε₷ἭMod
"""
import os
import time
import random
import asyncio
import requests
import platform
from PIL import Image
from io import BytesIO
from datetime import datetime
from telethon import events, __version__, version
from platform import python_version, uname
from telethon.tl.types import ChannelParticipantsAdmins

#☄️🐍🐍🐍🚫🐍🐍🐍🐍🐍🐍🐍🐍🐍
#☄️🚫🚫🐍🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫
#☄️🐍🐍🐍🚫🐍🐍🐍🐍🐍🐍🐍🐍🐍
# https://telegra.ph/file/5912a12caa663de1f77da.jpg
# https://telegra.ph/file/c96b323b64468a140b9ac.jpg
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Modified"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , "https://telegra.ph/file/24f412762232e8656177a.jpg")



def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
    
uptime = get_readable_time((time.time() - StartTime))

global ghanti
ghanti = borg.uid
edit_time = 6
""" ===================CONSTANTS================== """
file1 = "https://telegra.ph/file/6a8a88f6c5125f90f17f6.jpg"
file2 = "https://telegra.ph/file/9b3cd5ece7b6dbb930f68.jpg"
file3 = "https://telegra.ph/file/5912a12caa663de1f77da.jpg"
file4 = "https://telegra.ph/file/9e7d8af3165382e7ad30b.jpg"
file5 = "https://telegra.ph/file/3e1a71e13b0700717d717.jpg"
file6 = "https://telegra.ph/file/67921155ae43fdf500730.jpg"
file7 = ALIVE_PHOTTO
file8 = "https://telegra.ph/file/59b391c52953c21f7b82b.jpg"
""" ===================CONSTANTS================== """
pm_caption = f"`{botnickname} is running...`\n"
pm_caption += f"`°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°`\n"
pm_caption += "**Master,** __Am Alive And Systems Are Working Perfectly...__\n"
pm_caption += f"👤 `USER`           ⁝⁝ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
pm_caption += f"🐍 `PYTHON`         ⁝⁝ V{python_version()} \n"
pm_caption += f"📱 `TELETHON`       ⁝⁝ v{version.__version__} \n"
pm_caption += f"🤖 `MODIFIED`       ⁝⁝ v{mod_version} \n"
pm_caption += f"⌚ `Bot UPTIME`     ⁝⁝ {uptime} \n\n"
pm_caption +=  "📝 `LICENSE`        ⁝⁝ [GNU LICENSE](https://raw.githubusercontent.com/GbeshMod/modified/master/LICENSE) \n"
pm_caption +=  "🏆 `Github ©2021`   ⁝⁝ [Modified bot](https://github.com/GbeshMod/modified) \n"
pm_caption += f"`°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°`\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
##
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file5)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file1)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file6)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file6)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file8)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file6)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(yes.chat_id, ok13, file=file7)


    await yes.delete()

""" For .alive command, check if the bot is running.  """
CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)

