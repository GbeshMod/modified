import os
import time
import glob
import uuid
import string 
import random 
import zipfile
import asyncio
import time as t
from pdf2docx import parse
from datetime import datetime
from modified.function import convert_to_image, crop_vid, runcmd




if not os.path.isdir(Config.TRASH_DOWNLOAD_DIRECTORY):
  os.makedirs(Config.TRASH_DOWNLOAD_DIRECTORY)
  

@modbot.on(modified_cmd(pattern="p2dcl(?: |$)(.*)"))
async def starky(event):
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    frid = uuid.uuid4().hex
    diro = f"./{rndm}/"
    dirb = f"./{frid}/"
    os.makedirs(diro)
    os.makedirs(dirb)
    media_count = 0
    text_count = 0
    if un:
        chnnl = un
    else:
        chnnl = event.chat_id
    
    await event.edit(f"**Fetching All Files From This Channel**")
    try:
        chnnl_msgs = await borg.get_messages(chnnl, limit=3000)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF THere Are Any Media :/`")
        return
    
    
    total = int(chnnl_msgs.total)
    
    await event.edit(f"**Downloading {total} Media/Messages**")
    for d in chnnl_msgs:
        if d.media:
            media_count += 1
            await borg.download_media(d.media, diro)
        if d.text:
            text_count += 1
            
    await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts :** `{text_count}` \n**Now Converting Files.**")
    
    
    Azx = glob.glob(f"{diro}*.pdf")
    
    for modified in Azx:
      N = 9
      
      res =''.join(random.choices(string.ascii_uppercase+string.digits, k = N))
      pdf_file = modified
      docx_file = f'{dirb}{str(res)}.docx'
      
      parse(pdf_file, docx_file, start=0, end=None)
      
      
    Ax = glob.glob(f"{dirb}*.docx")
    for pop in Ax:
      await borg.send_file(event.chat_id, pop, caption=f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts  :** `{text_count}` \n**By @Modifiedbot**")
    Azx = glob.glob(f"{diro}*")
    Azpx = glob.glob(f"{dirb}*")
    for x in Azx:
      os.remove(x)
    
    for pop in Azpx:
      os.remove(pop)
    
    
    os.rmdir(diro)
    os.rmdir(dirb)


  
@modbot.on(modified_cmd(pattern=r"pdf2docx"))
@modbot.on(sudo_cmd(pattern=r"pdf2docx", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Pdf File.")
        return
    hmmu = await event.reply("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TRASH_DOWNLOAD_DIRECTORY)
    
    hmmu = await event.reply("hmm... Please Wait...🚶")
    
    pdf_file = starky
    docx_file = './modified/trash/modpdf.docx'
    
    parse(pdf_file, docx_file, start=0, end=None)
    
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by {BOT_LIN} ."
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
