"""Color Plugin for @Colour
Syntax: .color <color_code>"""
import os

from PIL import Image, ImageColor



@modex.on(modified_cmd(pattern="color (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    if input_str.startswith("#"):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await event.edit(str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            im.save("Colour.png", "PNG")
            input_str = input_str.replace("#", "#COLOR_")
            await borg.send_file(
                event.chat_id,
                "Colour.png",
                force_document=False,
                caption=input_str,
                reply_to=message_id,
            )
            os.remove("Colour.png")
            await event.delete()
    else:
        await event.edit("Syntax: `.color <color_code>`\n example : `.color #ff0000`")


CMD_HELP.update(
    {
        "colors": "**Colors**\
\n\n**Syntax : **`.color <Hex Color Code>` or `.color #ff0000`\
\n**Usage :** This plugin uploades colour picture just with Hex Color code. ."
    }
)
