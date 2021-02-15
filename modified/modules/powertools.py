"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown and  .sleep"""

import sys
from os import execl
from time import sleep
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP


@borg.on(modified_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(2)
    await event.edit("Restarting █░░░ \n`Please wait. ")
    await asyncio.sleep(2)
    await event.edit("Restarting ██░░ \n`Please wait.. ")
    await asyncio.sleep(2)
    await event.edit("Restarting ███░ \n`Please wait... ")
    await asyncio.sleep(2)
    await event.edit("Restarting ████ \n`Please wait.... ")
    await asyncio.sleep(2)
    await event.edit("Restarting ░░░░ \n`Please wait. ")
    await asyncio.sleep(2)
    await event.edit("Restarting █░░░ \n`Please wait.. ")
    await asyncio.sleep(2)
    await event.edit("Restarting ██░░ \n`Please wait... ")
    await asyncio.sleep(2)
    await event.edit("Restarting ███░ \n`Please wait.... ")
    await asyncio.sleep(2)
    await event.edit("Restarting ████ \n`Please wait..... ")
    await asyncio.sleep(2)
    await event.edit("Restarted. `.ping` me or `.alive` to check if I am back online.. Actually it takes 1-2 min for restarting")
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)



@borg.on(modified_cmd(pattern="shutdown$"))
@borg.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down")
    await edit_or_reply(event, "`Turning off bot now ...Manually turn me on later`")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


@borg.on(modified_cmd(pattern="sleep( [0-9]+)?$"))
@borg.on(sudo_cmd(pattern="sleep( [0-9]+)?$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "Syntax: `.sleep time`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "You put the bot to sleep for " + str(counter) + " seconds",
        )
    event = await edit_or_reply(event, f"`ok, let me sleep for {counter} seconds`")
    sleep(counter)
    await event.edit("`OK, I'm awake now.`")



CMD_HELP.update(
    {
        "powertools": "**Powertools**\
        \n\n  •  **Syntax : **`.restart`\
        \n  •  **Function : **__Restarts the bot !!__\
        \n\n  •  **Syntax : **`.sleep <seconds>`\
        \n  •  **Function: **__Userbots get tired too. Let yours snooze for a few seconds.__\
        \n\n  •  **Syntax : **`.shutdown`\
        \n**  •  Function : **__To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use__ @hk_heroku_bot"
    }
)
