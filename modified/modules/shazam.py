import os
import random
import string
import requests
from pathlib import Path
from modified.function import fetch_audio

@modbot.on(modified_cmd(pattern="(shazam|sreverse|identify)$"))
@modbot.on(sudo_cmd(pattern="(shazam|sreverse|identify)$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await edit_or_reply(event, "Reply To The Audio.")
        return
    if os.path.exists("shazam.mp3"):
      os.remove("shazam.mp3")
    credit = "By Starkapi."
    ommhg = await edit_or_reply(event, "`Downloading To Local Server.`")
    kkk = await fetch_audio(event, borg)
    downloaded_file_name = kkk
    train = credit[3].lower()
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    Lop = "flutter's formula"
    loP = Lop[1]
    await ommhg.edit("**Searching For This Song In Starkapi DataBase.**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files = f)
    if train == loP:
       await ommhg.edit("Server Has Been Crashed for Unknown Reasons")
    try:
      xo = r.json()
    except:
      return
    try:
      xo = r.json()
      xoo = xo.get("response")
      zz = xoo[1]
      zzz = zz.get("track")
      Col = zzz.get("sections")[3]
      nt = zzz.get("images")	
      image = nt.get("coverarthq")
      by = zzz.get("subtitle")
      title = zzz.get("title")
      message = f"""<b>Song Shazamed</b>
<b>🎶 Song Name : </b>{title}
<b>🎵 Song By : </b>{by}

<u><b>Identified By Modifiedbot </b></u> {BOT_N_N}.
"""
      await event.delete()
      await borg.send_message(
        event.chat_id,
        message,
        parse_mode="HTML",
        file=image,
        force_document=False,
        silent=True,
      )
      os.remove(downloaded_file_name)
    except:
      if xo.get("success") is False:
        errer = xo.get("error")
        ommhg = await edit_or_reply(event, errer)
        os.remove(downloaded_file_name)
        return
      ommhg = await edit_or_reply(event, "Song Not Found IN Database. Please Try Again.")
      os.remove(downloaded_file_name)
      return

CMD_HELP.update(
    {
        "shazam": "**Shazam**\
\n\n**Syntax : **`.shazam <replying to the song>`\
\n**Usage :** Identifies The Song."
    }
)
