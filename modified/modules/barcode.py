"""BarCode Generator
Command .barcode (your text) or (your link)         \n\n**Syntax : **`.makeqr` <content>\
        \n**Function : **__Make a QR Code from the given content.__\
        \nExample: .makeqr www.google.com\
        \n\n**Syntax : **`.barcode `<content>\
        \n**Function : **__Make a BarCode from the given content.__\
        \nExample: `.barcode` www.google.com\
        \n\n**Syntax : **`.decode` <reply to barcode/qrcode> \
"""

import os
import qrcode
import barcode
import asyncio
import requests
from telethon import events
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import quote
from PIL import Image, ImageColor
from barcode.writer import ImageWriter
from telethon.errors.rpcerrorlist import YouBlockedUserError


@modex.on(modified_cmd(pattern="barcode ?(.*)"))
@modex.on(sudo_cmd(pattern="barcode ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "...")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.barcode <long text to include>`"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await borg.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await edit_or_reply(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await edit_or_reply(event, "Created BarCode in {} seconds".format(ms))
    await asyncio.sleep(5)
    await event.delete()


@bot.on(admin_cmd(pattern=r"decode$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"decode$", allow_sudo=True))
async def parseqr(qr_e):
    downloaded_file_name = await qr_e.client.download_media(
        await qr_e.get_reply_message(), Config.TMP_DIR
    )
    # parse the Official ZXing webpage to decode the QRCode
    command_to_exec = [
        "curl",
        "-X",
        "POST",
        "-F",
        "f=@" + downloaded_file_name + "",
        "https://zxing.org/w/decode",
    ]
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if not t_response:
        return await edit_or_reply(qr_e, f"Failed to decode.\n`{e_response}`")
    soup = BeautifulSoup(t_response, "html.parser")
    qr_contents = soup.find_all("pre")[0].text
    await edit_or_reply(qr_e, qr_contents)
    if os.path.exists(downloaded_file_name):
        os.remove(downloaded_file_name)



@bot.on(admin_cmd(pattern=r"makeqr (?: |$)([\s\S]*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"makeqr (?: |$)([\s\S]*)", allow_sudo=True))
async def make_qr(makeqr):
    #  .makeqr command, make a QR Code containing the given content.
    input_str = makeqr.pattern_match.group(1)
    message = "SYNTAX: `.makeqr <long text to include>`"
    reply_msg_id = None
    if input_str:
        message = input_str
    elif makeqr.reply_to_msg_id:
        previous_message = await makeqr.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await makeqr.client.download_media(previous_message)
            m_list = None
            with open(downloaded_file_name, "rb") as file:
                m_list = file.readlines()
            message = ""
            for media in m_list:
                message += media.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("img_file.webp", "PNG")
    await makeqr.client.send_file(
        makeqr.chat_id, "img_file.webp", reply_to=reply_msg_id
    )
    os.remove("img_file.webp")
    await makeqr.delete()



CMD_HELP.update(
    {
        "barcode": "**Barcode**\
        \n\n**Syntax : **`.makeqr` <content>\
        \n**Function : **__Make a QR Code from the given content.__\
        \nExample: .makeqr www.google.com\
        \n\n**Syntax : **`.barcode `<content>\
        \n**Function : **__Make a BarCode from the given content.__\
        \nExample: `.barcode` www.google.com\
        \n\n**Syntax : **`.decode` <reply to barcode/qrcode> \
        \n**Function : **__to get decoded content of those codes.__"
    }
)
