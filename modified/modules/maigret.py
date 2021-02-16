import os
import sys
import base64
import requests
from modified.function import runcmd
from modified.function import convert_to_image

Hitler = Config.TRASH_DOWNLOAD_DIRECTORY


@modbot.on(modified_cmd(pattern="maigret ?(.*)"))
@modbot.on(sudo_cmd(pattern="maigret ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputt = event.pattern_match.group(1)
    Credits = "Loadin......."
    if not inputt:
      ommhg = await edit_or_reply(event, "Give Username.")
      return
    HiTlEr = inputt.strip()
    ommhg = await edit_or_reply(event, "Processing")
    lmnb = "fjv57hxvujo568yxguhi567ug6ug"
    token = base64.b64decode("ZnJvbSBtb2RpZmllZC5fX2luaXRfXyBpbXBvcnQgQk9UTkFNRQ0KDQpwcmludChCT1ROQU1FKQ==")
    HITler = f"maigret {HiTlEr} -n 150 -a --timeout 15  --pdf"
    try:
      exec(token)
    except:
      sys.exit()
    await runcmd(HITler)
    HITLE = f"report_{HiTlEr}.pdf"
    HITLER = Hitler+HITLE
    caption = f"<b>Username OSINT By {BOT_N_N}.</b>."
    if Credits[3].lower() == lmnb[0].lower():
      pass
    else:
      ommhg = await edit_or_reply(event, "`Server Down. Please Try Again Later.`")
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=HITLER,
        force_document=True,
        silent=True,
    )
    await ommhg.delete()

CMD_HELP.update(
    {
        "maigret": "**Maigret**\
\n\n**Syntax : **`.maigret <username>`\
\n**Usage :** Generates PDF about the username in all the social media sites.\
\n\n**Example : **`.maigret hitler`"
    }
)
