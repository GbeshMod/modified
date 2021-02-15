from telethon import events
from modified.modules.sql_helper.auto_post_sql import *


@bot.on(admin_cmd(pattern="autopost ?(.*)"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if str(sed).startswith("-100"):
        kk = str(sed).replace("-100", "")
    else:
        kk = sed
    if not kk.isdigit():
        await event.edit("`Channel ID Should be Integers`")
        return
    if is_post_data_in_db(kk , event.chat_id):
        await event.edit("Ah, This Channel Is Already DB")
        return
    add_new_post_data_in_db(kk, event.chat_id)
    await event.edit(f"`Added AutoPosting To This Chat From {sed}`")

@bot.on(admin_cmd(pattern="rmautopost ?(.*)"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if str(sed).startswith("-100"):
        kk = str(sed).replace("-100", "")
    else:
        kk = sed
    if not kk.isdigit():
        await event.edit("`Channel ID Should be Integers`")
        return
    if not is_post_data_in_db(kk, event.chat_id):
        await event.edit("Ah, This Channel Is Not In DB")
        return
    remove_post_data(kk, event.chat_id)
    await event.edit(f"`Oh, Okay I will Stop Posting From {sed}.`")

@bot.on(events.NewMessage())
async def what(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post_data(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await event.client.send_message(int(chat), event.message)
