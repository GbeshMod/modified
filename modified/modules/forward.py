import string
import asyncio
from telethon import events, utils, sync
from telethon.tl import types, functions, Channel
 

global msg_cache
msg_cache = {}


global groupsid
groupsid = []


async def all_groups_id(cat):
    catgroups = []
    async for dialog in cat.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.megagroup:
            catgroups.append(entity.id)
    return catgroups


@bot.on(admin_cmd(pattern="frwd$"))
@bot.on(sudo_cmd(pattern="frwd$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_GROUP_ID` for this plugin to work"
        )
        return
    try:
        e = await borg.get_entity(Config.PRIVATE_GROUP_ID)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()



@bot.on(admin_cmd(pattern="resend$"))
@bot.on(sudo_cmd(pattern="resend$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        await event.delete()
    except:
        pass
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)


@bot.on(admin_cmd(pattern=r"fpost (.*)"))
@bot.on(sudo_cmd(pattern=r"fpost (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    global groupsid
    global msg_cache
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()
    if len(groupsid) == 0:
        groupsid = await all_groups_id(event)
    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in event.client.iter_messages(event.chat_id, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        if c not in msg_cache:
            for i in groupsid:
                async for msg in event.client.iter_messages(event.chat_id, search=c):
                    if msg.raw_text.lower() == c and msg.media is None:
                        msg_cache[c] = msg
                        break
        await event.client.forward_messages(destination, msg_cache[c])


@borg.on(events.NewMessage(outgoing=True))
async def _(event):
    _last_messages[event.chat_id] = event.message


@borg.on(events.NewMessage(pattern=r"\.(fix)?reply", outgoing=True))
async def _(event):
    if not event.is_reply or event.chat_id not in _last_messages:
        return

    message = _last_messages[event.chat_id]
    chat = await event.get_input_chat()
    await asyncio.wait([
        borg.delete_messages(chat, [event.id, message.id]),
        borg.send_message(chat, message, reply_to=event.reply_to_msg_id)
    ])


@borg.on(admin_cmd("repeat ?(.*)"))
@bot.on(sudo_cmd(pattern=r"repeat (.*)", allow_sudo=True))
async def _(event):
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await wait([event.respond(repmessage)for i in range(count)])
    await event.delete()
 


CMD_HELP.update(
    {
        "forward": "**FORWARD**\
    \n\n  •  **Synatax : **`frwd reply to any message`\
    \n  •  **Function :  **__Enable Seen Counter in any message, to know how many users have seen your message__\
    \n\n  •  **Syntax : **`.resend reply to message`\
    \n  •  **Function : **__Just resend the replied message again in that chat__\
    \n\n  •  **Syntax : **`.fpost text`\
    \n  •  **Function : **__Split the word and forwards each letter from the messages cache if exists__\
    \n**Syntax : **`.fixreply`\
    \n**Function : **Gbesh know something about this 🙄⪼ \
    \n\n**Syntax : **`.repeat <number of times to repeat> <text to repeat>`\
\n**Usage :** repeats the given text with given number of times."
    }
)
