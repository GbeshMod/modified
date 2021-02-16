import os
import time
import uuid
import shutil
import img2pdf
import asyncio
import zipfile
import time as t
from Code2pdf import Code2pdf
from datetime import datetime
from telethon.tl.types import InputMessagesFilterPhotos
from modified.function import convert_to_image, crop_vid, runcmd

temp_dir = Config.TEMP_DOWNLOAD_DIRECTORY


@modbot.on(modified_cmd(pattern=r"img2pdf (?: |$)(.*)"))
async def heck(event):
    if event.fwd_from:
        return  
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    dir = f"./{rndm}/"
    media_count = 0
    text_count = 0
    os.makedirs(dir)
    if un:
        chnnl = un
    else:
        chnnl = event.chat_id
    await event.edit(f"**Fetching All Images From This Channel**")
    try:
        chnnl_msgs = await borg.get_messages(chnnl, limit=3000, filter=InputMessagesFilterPhotos)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF There Are Any Images :/`")
        return
    total = int(chnnl_msgs.total)
    await event.edit(f"**Downloading {total} Images**")
    for d in chnnl_msgs:
        media_count += 1
        await borg.download_media(d.media, dir)
    images_path = []
    images_names = os.listdir(dir)
    for i in images_names:
        path = os.path.join(dir, i)
        images_path.append(path)
    with open('imagetopdf.pdf', "wb") as f:
        f.write(img2pdf.convert(images_path))    
    await borg.send_file(event.chat_id, "imagetopdf.pdf", caption="Powered By ")  
    os.remove("imagetopdf.pdf")
    shutil.rmtree(dir)
    
    
@modbot.on(modified_cmd(pattern=r"pdf2docx"))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Pdf File.")
        return
    hmmu = await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TRASH_DOWNLOAD_DIRECTORY)
    hmmu = await event.edit("hmm... Please Wait..")
    pdf_file = starky
    docx_file = temp_dir+'document.docx'
    parse(pdf_file, docx_file, start=0, end=None)
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by {BOT_N_N} bot.."
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()
    
@modbot.on(modified_cmd(pattern=r"code2pdf$"))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any File.")
        return
    hmmu = await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    if not lol.document:
        await event.edit("Only Documents :/")
        return
    starky = await borg.download_media(lol.media)
    hmmu = await event.edit("hmm... Please Wait..")
    pdf = Code2pdf(starky, "test.pdf", "Ä4")
    pdf.init_print()
    await event.delete()
    await borg.send_file(
        event.chat_id, "test.pdf", caption=f"**Code2Pdf - ** "
    )
    os.remove("Code2Pdf.pdf")
    os.remove(starky)



@modbot.on(modified_cmd(pattern="p2dcl (?: |$)(.*)"))
async def starky(event):
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    midn = uuid.uuid4().hex
    diro = f"./{rndm}/"
    dirb = f"./{midn}/"
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




CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.img2pdf <reply to image>`\
\n**Usage :** Converts Given Image into PDF.\
\n\n**Syntax : **`.pdf2docx <reply to PDF>`\
\n**Usage :** Converts Given PDF Into Docx.\
\n\n**Syntax : **`.code2pdf <reply to code>`\
\n**Usage :** Converts Given code Into PDF.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)
