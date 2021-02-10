
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from telethon import functions
from modified.function import get_all_admin_chats, is_admin
from telethon.tl.types import ChatBannedRights
from modified.modules.sql_helper.night_mode_sql import add_nightmode, rmnightmode, get_all_chat_id, is_nightmode_indb


hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
@modbot.on(modified_cmd(pattern="nighte"))
async def close_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Enable Night Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Already Enabled Night Mode.")
        return
    add_nightmode(str(event.chat_id))
    await event.edit(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Group Will Be Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


@modbot.on(modified_cmd(pattern="nightd"))
async def disable_ws(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Night Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Not Enabled Night Mode.")
        return
    rmnightmode(str(event.chat_id))
    await event.edit(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Database. This Group Will Be No Longer Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await gbesh.send_message(
              int(warner.chat_id), "`12:00 Am, Group Is Closing Till 6 Am. Night Mode Started !` \n**Powered By Modifiedbot**"
            )
            await gbesh(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=hehes
            )
            )
            if Config.CLEAN_GROUPS:
                async for user in gbesh.iter_participants(int(warner.chat_id)):
                    if user.deleted:
                        await gbesh.edit_permissions(int(warner.chat_id), user.id, view_messages=False)
        except Exception as e:
            logger.info(f"Unable To Open Group {warner} - {e}")

scheduler = AsyncIOScheduler(timezone=Config.TIMEZONE)
scheduler.add_job(job_close, trigger="cron", hour=23, minute=55)
scheduler.start()


async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await gbesh.send_message(
              int(warner.chat_id), "`06:00 Am, Group Is Opening.`\n**Powered By Modifiedbot**"
            )
            await gbesh(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=openhehe
            )
        )
        except Exception as e:
            logger.info(f"Unable To Open Group {warner.chat_id} - {e}")

# Run everyday at 06
scheduler = AsyncIOScheduler(timezone=Config.TIMEZONE)
scheduler.add_job(job_open, trigger="cron", hour=6, minute=10)
scheduler.start()


CMD_HELP.update(
    {
        "night_mode": "**NIGHT MODE**\
\n\n**Syntax : **`.nighte <groupchat>`\
\n**Usage :** to enable night mode on group chat.\
\n\n**Syntax : **`.nightd <groupchat>`\
\n**Usage :** to disable night mode on group chat ."
    }
)
