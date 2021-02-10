from telethon.events import ChatAction
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from modified import bot, sclient



"""Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict."""


@borg.on(ChatAction)
async def ok(event):
    juser = await event.get_user()
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if sclient is None:
        return
    if event.user_joined:
        hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
        if not hmmyep.is_admin:
            return
        user = sclient.is_banned(juser.id)
        if user:
            await event.reply(
                f"**#ᴍᴏᴅɪғɪᴇᴅ ᴀɴᴛɪsᴘᴀᴍ** \n**ᴅᴇᴛᴇᴄᴛᴇᴅ ᴍᴀʟɪᴄɪᴏᴜs ᴜsᴇʀ.** \n**ᴜsᴇʀ-ɪᴅ ➼  `{juser.id}`  \n**ʀᴇᴀsᴏɴ ➼  `{user.ban_code} - {user.reason}`"
            )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass
