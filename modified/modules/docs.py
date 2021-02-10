# by @GbeshMod

from datetime import datetime
from io import BytesIO
from pathlib import Path

from telethon import functions, types, events
from telethon.errors import PhotoInvalidDimensionsError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import SendMediaRequest



if not os.path.isdir("./note"):
    os.makedirs("./note")



import os
import glob
import uuid
import time
import string 
import random 
import shutil
import asyncio
import zipfile
import time as t
from pdf2docx import parse
from datetime import datetime
from modified.function import convert_to_image, crop_vid, runcmd






@modbot.on(modified_cmd(pattern=r"pdf2docx"))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Pdf File.")
        return
    hmmu = await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TEMP_DOWNLOAD_DIRECTORY)
    hmmu = await event.edit("hmm... Please Wait..")
    pdf_file = starky
    gbesh = Config.TEMP_DOWNLOAD_DIRECTORY + "converted.docx"
    docx_file = gbesh
    parse(pdf_file, docx_file, start=0, end=None)
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by {BOT_LIN} bot.."
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()




CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)




@borg.on(admin_cmd(pattern="ttf ?(.*)"))
async def get(event):
    name = event.text[5:]
    m = await event.get_reply_message()
    with open(name, "w") as f:
        f.write(m.message)
    await event.delete()
    await borg.send_file(event.chat_id,name,force_document=True)
    
    
@borg.on(admin_cmd(pattern="docs ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as `.docs <file name> .txt or md`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as `.docs <file name> .txt or md`")

@borg.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    m = await event.get_reply_message()
    with open(name, "w") as f:
        f.write(m.message)
    await event.delete()
    await borg.send_file(event.chat_id,name,force_document=True)
	
             
"""reply to text message as `.doc <file name> .txt or md \nreply to text message as `.docx <file name> .txt or  md """

CMD_HELP.update(
    {
        "docs": "**Syntax :** `.docs` reply to text message as `.docs <file name> .txt or md\
    \n**Usage : **reply to text message as `.doc <file name> .txt or md` 📜\
    "
    }
)
