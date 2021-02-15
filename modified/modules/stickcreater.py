# Random RGB Sticklet by @PhycoNinja13b
# modified by @UniBorg
# imported from ppe-remix by @heyworld & @DeletedUser420
# modified by @mrconfused

import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument





@modbot.on(friday_on_cmd(pattern="stcr ?(?:(.*?) \| )?(.*)"))
@modbot.on(sudo_cmd(pattern="stcr ?(?:(.*?) \| )?(.*)", allow_sudo=True))
async def sticklet(event):
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_message = event.message
    # get the input text
    # the text on which we would like to do the magic on
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    if not sticktext and event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        sticktext = reply_message.message
    elif not sticktext:
        await event.edit("need something, hmm")
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    await event.delete()
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@wewfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "modbot.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    await event.client.send_file(
        event.chat_id,
        image_stream,
        caption=BOT_N_N,
        reply_to=event.message.reply_to_msg_id,
    )
    try:
        os.remove(FONT_FILE)
    except:
        pass



CMD_HELP.update(
    {
        "stickcreate": "**Sticker Creator**\
\n\n**Syntax : **`.stcr <text>`\
\n**Usage :** Creates sticker with given text."
    }
)
