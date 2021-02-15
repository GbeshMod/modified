import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP, bot
from fridaybot.utils import friday_on_cmd



@friday.on(friday_on_cmd("yo$"))
# @register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)


@friday.on(friday_on_cmd("Oof$"))
# @register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)




@friday.on(friday_on_cmd("fp$"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


#@friday.on(friday_on_cmd("moon$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("source$"))
# @register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/StarkGang/FridayUserbot")


@friday.on(friday_on_cmd("readme$"))
# @register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/StarkGang/FRIDAYUSERBOT/blob/master/README.md")



CMD_HELP.update({"readme": "Reedme."})
CMD_HELP.update({"source": "Gives the source of your fridaybot"})
