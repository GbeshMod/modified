"""

Commands - .offline .online
Offline = Add an offline tag in your name and change profile pic to black.
Online = Remove Offline Tag from your name and change profile pic to vars PROFILE_IMAGE.
Note - If you have a last name remove it unless it automatically removed.
"""

import asyncio
import datetime

from telethon import events
from telethon.tl import functions, types
import os , urllib
from telethon import events
from telethon.tl import functions




OFFLINE_TAG = "[ㄖ千千ㄥ丨几乇]"
ONLINE_TAG = "[ㄖ几ㄥ丨几乇]"

onpiz = utils.modified_online
ofpiz = utils.modified_offline



@borg.on(admin_cmd(pattern="offline"))
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Already in Offline Mode.**")
        return
    await event.edit("**Changing Profile to Offline...**")
    urllib.request.urlretrieve(ofpiz ,"offlinepic.jpg")
    photo = "offlinepic.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await borg(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.edit("**Changed profile to OffLine.**")
    try:
        os.system("rm -fr offlinepic.jpg")
    except Exception as e:
        logger.warn(str(e))
    last_name = ""
    first_name = OFFLINE_TAG
    try:
        await borg(functions.account.UpdateProfileRequest(
            last_name=last_name,
            first_name=first_name
        ))
        result = "**`{} {}`\nI am Offline now.**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:
        await event.edit(str(e))



@borg.on(admin_cmd(pattern="online"))
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Changing Profile to Online...**")
    else:
      await event.edit("**Already Online.**")
      return
    urllib.request.urlretrieve(onpiz,"onlinepic.jpg")
    photo = "onlinepic.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await borg(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.edit("**Changed profile to Online.**")
    try:
        os.system("rm -fr onlinepic.jpg")
    except Exception as e:
        logger.warn(str(e))
    first_name = ONLINE_TAG
    last_name = ""
    try:
        await borg(functions.account.UpdateProfileRequest(
            last_name=last_name,
            first_name=first_name
        ))
        result = "**`{} {}`\nI am Online !**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:
        await event.edit(str(e))


global USER_night
global night_time
global last_night_message
USER_night = {}
night_time = None
last_night_message = {}

DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Modified"
)


@borg.on(events.NewMessage(outgoing=True))
async def set_not_night(event):
    global USER_night
    global night_time
    global last_night_message
    current_message = event.message.message
    if ".night" not in current_message and "yes" in USER_night:
        try:
            await borg.send_message(
                Config.PLUGIN_CHANNEL,
                f"Mine Owner has Gone to Sleep (Pure Din Sota hi Rehta He {DEFAULTUSER} )",
            )
        except Exception as e:
            await borg.send_message(
                event.chat_id,
                "Please set `PLUGIN_CHANNEL` "
                + "for the proper functioning of night functionality "
                + "report in {}\n\n `{}`".format(BOT_LIN, str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        USER_night = {}
        night_time = None


@borg.on(admin_cmd(pattern=r"night ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_night
    global night_time
    global last_night_message
    global reason
    USER_night = {}
    night_time = None
    last_night_message = {}
    reason = event.pattern_match.group(1)
    if not USER_night:
        last_seen_status = await borg(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            night_time = datetime.datetime.now()
        USER_night = f"yes: {reason}"
        if reason:
            await event.edit(f"My Boss Is Going To sleep  Dnd 🛏💤😴 ")
        else:
            await event.edit(f"My Boss is Going To Sleep")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(
                Config.PLUGIN_CHANNEL, f"My BOss Wants So Sleep"
            )
        except Exception as e:
            logger.warn(str(e))


@borg.on(
    events.NewMessage(
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_night(event):
    if event.fwd_from:
        return
    global USER_night
    global night_time
    global last_night_message
    night_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "night" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_night and not (await event.get_sender()).bot:
        if night_time:
            now = datetime.datetime.now()
            datime_since_night = now - night_time
            time = float(datime_since_night.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                night_since = "**ㄚ乇丂ㄒ乇尺ᗪ卂ㄚ**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    night_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    night_since = wday.strftime("%A")
            elif hours > 1:
                night_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                night_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                night_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"My Master Has Been Gone For {night_since}\nWhere He Is: **On Bed Sleeping** "
            + f"\n\n__ I'll back in a few Light years__\n**"
            if reason
            else f"**Important Notice**\n\n{DEFAULTUSER} Is Sleeping DND And Also Good [night To You...]({utils.modified_sleep}) "
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_night_message:
            await last_night_message[event.chat_id].delete()
        last_night_message[event.chat_id] = msg



CMD_HELP.update(
    {
        "mystatus": "**My Status**\
\n\n**Syntax : **`.online`\
\n**Usage :** Remove Offline Tag from your name and change profile pic to vars PROFILE_IMAGE...\
\n\n**Syntax : **`.offline `\
\n**Usage :** Add an offline tag in your name and change profile pic to black...\
\n\n **Syntax : ** .night   Same like AFK. But fixed reason and for sleeping purpose only. l"
    }
)