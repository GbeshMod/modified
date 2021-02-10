import os
import requests
from pornhub_api import PornhubApi
from telethon.tl.types import MessageMediaPhoto




@modbot.on(modified_cmd(pattern=r"nsfw"))
@modbot.on(sudo_cmd(pattern=r"nsfw", allow_sudo=True))
async def nsfw(event):
    url = "https://nsfw-categorize.it/api/upload"
    await event.edit("`Processing..`")
    sed = await event.get_reply_message()
    photo = None
    sedpath = "./trash/"
    if sed and sed.media:
        if isinstance(sed.media, MessageMediaPhoto):
            photo = await borg.download_media(sed.media, sedpath)
        elif "image" in sed.media.document.mime_type.split("/"):
            photo = await borg.download_media(sed.media, sedpath)
        else:
            await event.edit("Reply To Image")
            return
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        if os.path.exists(photo):
            os.remove(photo)
        else:
            await event.edit("Response UnsucessFull. Try Again.")
            if os.path.exists(photo):
                os.remove(photo)


@modbot.on(admin_cmd(pattern="pornh (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(
    input_str,
    ordering="mostviewed"
    )
    ok = 1
    oik = ""
    for vid in data.videos:
      if ok<=5:
        oik +=(f"""
Video title:- {vid.title}
Video link:- https://www.pornhub.com/view_video.php?viewkey={vid.video_id}



        """)
        ok = ok+1
      else:
        pass
    
    oiko = "<b>Links Generated Successfully</b>"+"\n"+"Search Query ➧ "+input_str+"\n"+oik
    
    await borg.send_message(
        event.chat_id,
        oiko,
        parse_mode="HTML",
    )
    await event.delete()




CMD_HELP.update(
    {
        "nsfw": "**NSFW**\
\n\n**Syntax : **`.nsfw <reply to image>`\
\n**Usage :** Checks if the replyed image is nsfw or not.\
\n\n**Syntax : **`.pornh <query>`\
\n**Usage :** Searches PornHub Website With Given Query."
    }
)
