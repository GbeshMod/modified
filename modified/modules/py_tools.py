try:
    from PIL import Image
except ImportError:
    import Image

import os
import qrcode
import asyncio 
import pyjokes
import pytesseract
from howdoi import howdoi
from datetime import datetime
from bs4 import BeautifulSoup 

def progres(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )

 


@modbot.on(modified_cmd(pattern=r"pjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category="all"))


@modbot.on(modified_cmd(pattern="howdoi ?(.*)"))
async def __(event):
    query = event.pattern_match.group(1)
    if query == None:
        await event.edit("`Give Some Query First`")
        return
    output = howdoi.howdoi(query)
    lel = f"<b><u>Here is Your Answer</b></u> \n<code>{output}</code>"
    await event.edit(lel, parse_mode="HTML")


@modbot.on(modified_cmd(pattern="pyocr$"))
async def _(event):
    global images
    if event.fwd_from:
        return
    await event.edit("`Reading, Please Wait..`")
    if not os.path.isdir(Config.TRASH_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TRASH_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        imagez = await borg.download_media(
            await event.get_reply_message(), Config.TRASH_DOWNLOAD_DIRECTORY
        )
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    results = pytesseract.image_to_string(Image.open(imagez))
    mk = f"<b><u> OCR </u></b> \n<b></u>Here is What I Can Read From This.</u></b> \n<code>{results}</code>"
    await event.edit(mk, parse_mode="HTML")
    if os.path.exists(results):
        os.remove(results)


@modbot.on(modified_cmd(pattern="pygetqr"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    downloaded_file_name = await borg.download_media(
        await event.get_reply_message(),
        Config.TMP_DOWNLOAD_DIRECTORY,
        progress_callback=progres,
    )
    # parse the Official ZXing webpage to decode the QR
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
    os.remove(downloaded_file_name)
    if not t_response:
        logger.info(e_response)
        logger.info(t_response)
        await event.edit("oo0pps .. something wrongings. Failed to decode QRCode")
        return
    soup = BeautifulSoup(t_response, "html.parser")
    qr_contents = soup.find_all("pre")[0].text
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        "Obtained QRCode contents in {} seconds.\n{}".format(ms, qr_contents)
    )
    await asyncio.sleep(5)
    await event.edit(qr_contents)


@modbot.on(modified_cmd(pattern="pymakeqr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.pymakeqr <long text to include>`"
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
                progress_callback=progres,
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
        message = "SYNTAX: `.pymakeqr <long text to include>`"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("imgfile.webp", "PNG")
    await borg.send_file(
        event.chat_id,
        "imgfile.webp",
        caption=message,
        reply_to=reply_msg_id,
        progress_callback=progres,
    )
    os.remove("imgfile.webp")
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("Created QRCode in {} seconds".format(ms))
    await asyncio.sleep(5)
    await event.delete()



CMD_HELP.update(
    {
        "py_tools": "**Python Tools**\
\n\n**Syntax : **`.pyjoke`\
\n**Usage :** Get programmer jokes.\
\n\n**Syntax : **`.howdoi <programming query>`\
\n**Usage :** Gives Answers For Given Programming Questions.\
\n\n**Syntax : **`.pyocr <reply to image>`\
\n**Usage :** it automatically reads the image and shows text in the image. pyocr\
\n\n**Syntax : **`.pymakeqr <text>`\
\n**Usage :** makes QR code with given text.\
\n\n**Syntax : **`.pygetqr <reply to qr code>`\
\n**Usage :** Converts QR code into readible text."
    }
)
