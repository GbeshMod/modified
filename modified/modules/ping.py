import time
import requests
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from modified.modules.sql_helper import server_pinger_sql as sevping





def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@modbot.on(modified_cmd(pattern="ping$"))
@modbot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    starkislub = await edit_or_reply(event, "`꧁་࿇ρσɳɠ࿇་꧂`")
    if event.fwd_from:
        return
    hmm = await bot.get_me()
    if not hmm.username:
        hmm.username = hmm.id
    bothmm = await tgbot.get_me()
    bot_u = bothmm.username
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await starkislub.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n➭ `{ms}` ➭ `{uptime}` \n➭ `@{hmm.username}` \n➭ `@{bot_u}`"
    )



if Config.PING_SERVERS:
    @modbot.on(modified_cmd(pattern="aping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if sevping.is_ping_indb(str(url)):
            await event.edit("**Server Already Found In Db !**")
            return
        sevping.add_ping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Added To Db**")


    @modbot.on(modified_cmd(pattern="rping"))
    async def _(event):
        if event.fwd_from:
            return
        await event.edit("`Processing..`")
        url = event.text.split(" ", maxsplit=1)[1]
        if not sevping.is_ping_indb(str(url)):
            await event.edit("**Server Not Found In Db !**")
            return
        sevping.rmping(url)
        await event.edit(f"**URL :** `{url}` **Sucessfully Removed From Db**")
    
    async def ping_servers():
        hmm_p = 0
        url_s = sevping.get_all_url()
        header_s = {"User-Agent": 'Server'}
        if len(url_s) == 0:
            return
        for i in url_s:
            try:
              ws = requests.get(url=i.url, headers=header_s).status_code
              logger.info(f"Pinged {i.url} // Status Code Recived : {ws}")
            except:
              hmm_p += 1
        success_l = len(url_s) - hmm_p
        logger.info(f"Sucessfully Pinged {success_l} Urls Out Of {len(url_s)}")
    
    
    scheduler = AsyncIOScheduler(
        executors={
    'default': AsyncIOExecutor(),
        }
    )
    scheduler.add_job(ping_servers, 'interval', minutes=Config.PING_SERVER_EVERY_MINUTE_VALUE)
    scheduler.start()

CMD_HELP.update(
    {
        "ping": "**Ping**\
\n\n**Syntax : **`.ping`\
\n**Usage :** Get uptime and speed of your bot.\
\n\n**Syntax : **`.aping`\
\n**Usage :** add & Get and uptime and speed of a website.\
\n\n**Syntax : **`.rping`\
\n**Usage :** remove & Get and uptime and speed of a website."
    }
)
