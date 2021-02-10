import os
import logging
from sys import argv
import telethon.utils
from pathlib import Path
from modified import bot, clientz
from telethon import TelegramClient
from modified.Configs import Config
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
        gbeshmod.info("Warning : We Have Detected That You Have Not Turned On Inline Mode For Your Assistant Bot, Please Go To @BotFather And Enable This.")
    return


async def strmod(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multiple_client():
    if client2:
        gbeshmod.info("Starting Client 2")
        try:
            warnerstark = None
            client2.start()
            client2.loop.run_until_complete(strmod(client2))
        except:
            warnerstark = True
            gbeshmod.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        gbeshmod.info("Starting Client 3")
        try:
            warnergbesh = None
            cleint3.start
            client3.loop.run_until_complete(strmod(client3))
        except:
            warnergbesh = True
            gbeshmod.info("Client 3 Failed To Load.")
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
        gbeshmod.info("Բα¡ℓ૯∂ To load Others Modules ")
        return
    for unders in a_plugins:
        xmen = unders.media.document.attributes[-1].file_name
        pathh = "modified/modules/"
        if os.path.exists(os.path.join(pathh, xmen)):
            pass
        else:
            await client_s.download_media(unders.media, "modified/modules/")
    gbeshmod.info("Extra Plugins Downloaded.")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_TOKEN_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        failed4 = multiple_client()
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
    else:
        bot.loop.run_until_complete(add_bot("RnJpZGF5VXNlckJvdCBpcyBCZXN0"))
        failed4 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
        bot.loop.run_until_complete(get_other_plugins(Config, bot, gbeshmod))
        
import glob

path = "modified/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))    
        except Exception as ex:
            gbeshmod.info("°°°°°°°°°°°°°°°°°°°°°")
            gbeshmod.info("Failed To Load : " + str(shortname.replace(".py", "")) + f" Error : {str(ex)}")
            gbeshmod.info("°°°°°°°°°°°°°°°°°°°°°")
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), clientz)
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
    gbeshmod.info("Modified And Assistant Bot Have Been Installed Successfully !")
else:
    gbeshmod.info("Modified Has Been Installed Sucessfully !")
    gbeshmod.info(" \   |            | _)   _| _)            |\n |\/ |   _ \   _` |  |   _|  |   -_)   _` |\n_|  _| \___/ \__,_| _| _|   _| \___| \__,_|\n➠➠ Modified BOT is Online 🔮 all files installed ....\n  ➠➠ Modified BOT  (C) @GbeshMod ")

        
bot.tgbot.loop.run_until_complete(check_inline_on_warner(bot.tgbot))

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
