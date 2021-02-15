"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply





@borg.on(admin_cmd("get_id"))
@borg.on(sudo_cmd("get_id", allow_sudo=True))
async def _(event):
    totosweet = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await totosweet.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                )
            )
        else:
            await totosweet.edit(
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                )
            )
    else:
        await totosweet.edit("Current Chat ID: `{}`".format(str(event.chat_id)))


CMD_HELP.update(
    {
        "get_id": "**Get Id**\
\n\n**Syntax : **`.get_id <reply to media or any message>`\
\n**Usage :** Get ID of any Telegram media, or any user."
    }
)
