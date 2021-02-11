import os
import sys
import glob
import logging
import platform
from sys import argv
import telethon.utils
from pathlib import Path
from telethon import TelegramClient
from modified.Configs import Config
from telethon import __version__ as tv
from modified import bot, client2, client3, mod_version
from telethon.tl.types import InputMessagesFilterDocument
from modified.utils import load_module, start_assistant, load_module_dclient

gbeshmod = logging.getLogger("Modified")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def check_inline_on_warner(ws):
    w_s = await ws.get_me()
    if not w_s.bot_inline_placeholder:
        gbeshmod.info("Warning : We Have Detected That You Have Not Turned On Inline Mode For Your Assistant Bot, Please Go To @BotFather And Enable It..")
    return



async def lol_s(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multiple_client():
    if client2:
        gbeshmod.info("Starting Client 2")
        try:
            warnerstark = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            warnerstark = True
            gbeshmod.info("Client 2 Բα¡ℓ૯∂ To Load. Check Your String.")
    if client3:
        gbeshmod.info("Starting Client 3")
        try:
            warnergbesh = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            warnergbesh = True
            gbeshmod.info("Client 3 Բα¡ℓ૯∂ To Load.")
    if not client2:
        warnerstark = True
    if not client3:
        warnergbesh = True
    return warnerstark, warnergbesh    


async def get_other_plugins(Config, client_s, gbeshmod):
    try:
        a_plugins = await client_s.get_messages(
            entity=Config.LOAD_OTHER_PLUGINS_CHNNL,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        gbeshmod.info("Բα¡ℓ૯∂ To load Others Modules")
        return
    for meisnub in a_plugins:
        xmen = meisnub.media.document.attributes[-1].file_name
        pathh = "modified/modules/"
        if os.path.exists(os.path.join(pathh, xmen)):
            pass
        else:
            await client_s.download_media(meisnub.media, "modified/modules/")
    gbeshmod.info("Extra Plugins Downloaded.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_TOKEN_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
    else:
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
        failed2, failed3 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
        bot.loop.run_until_complete(get_other_plugins(Config, bot, gbeshmod))


path = "modified/modules/*.py"
files = glob.glob(path)
failed_warner = 0
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))    
        except Exception as e:
            failed_warner += 1
            gbeshmod.info("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            gbeshmod.info("Բα¡ℓ૯∂ To Load : " + str(shortname.replace(".py", "")) + f" Error : {str(e)}")
            gbeshmod.info("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client2)
            except:
                pass
        if failed3 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client3)
            except:
                pass

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "modified/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    wsta = "Modified And Assistant Bot Have Been Installed Successfully !"
else:
    wsta = "Modified Has Been Installed Sucessfully"


Lol = "folic acid Token"
total_clients = 1
if failed2 is None:
    total_clients += 1
if failed3 is None:
    total_clients += 1
if wsta[0].lower() ==Lol[0]:
   pass
else:
   print("bug detected")
   exit()
gbeshmod.info(" \   |            | _)   _| _)            |\n |\/ |   _ \   _` |  |   _|  |   -_)   _` |\n_|  _| \___/ \__,_| _| _|   _| \___| \__,_|\n➠➠ Modified BOT is Online 🔮 all files installed ....\n  ➠➠ Modified BOT  (C) @GbeshMod ")

gbeshmod.info(f"""{wsta}
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Updates        :: [@GbeshMod](https://github.com/GbeshMod/modified)
Support Chat   :: @Modifiedbot
Total Clients  :: {total_clients}
Python Version :: {platform.python_version()}
Telethon Version :: {tv}
Modified-Bot Version :: V{mod_version}
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°""")

bot.tgbot.loop.run_until_complete(check_inline_on_warner(bot.tgbot))

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()

