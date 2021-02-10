import os 
import re
import sys
import math
import time
import asyncio
import inspect
import logging
import datetime
import importlib
import traceback
import functools
from pathlib import Path
from telethon import events
from time import gmtime, strftime
from modified.Configs import Config
from modified import CMD_HELP, CMD_LIST, LOAD_PLUG, LOGS, SUDO_LIST, bot, client2, client3
from modified import BOT_LIN, BOT_N_N, Lastupdate, StartTime, mod_version


sedprint = logging.getLogger("PLUGINS")
cmdhandler = Config.COMMAND_HAND_LER
bothandler = Config.BOT_HANDLER

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

import modified.modules
import modified.function
import .gbesh 
from .chrome import *
from .wraptools import *
from .bytesformat import *
from .administration import *
from .loading import progress
from .google_images_download import *


class Loader:
    def __init__(self, func=None, **args):
        self.Config = Config
        bot.add_event_handler(func, events.NewMessage(**args))


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import sys
        import importlib
        import modified.utils
        import modified.modules
        from pathlib import Path

        path = Path(f"modified/modules/{shortname}.py")
        name = "modified.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sedprint.info("Successfully (re)imported " + shortname)
    else:
        import sys
        import modified
        import importlib
        import modified.utils
        import modified.modules
        import modified.function 
        from pathlib import Path
        from modified.utils import edit_delete, edit_or_reply, media_type 

        path = Path(f"modified/modules/{shortname}.py")
        name = "modified.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.borg = bot
        mod.modx = bot
        mod.modex = bot
        mod.modbot = bot
        mod.friday = bot
        mod.modified = bot
        mod.tgbot = bot.tgbot
        mod.Var = Config
        mod.Config = Config
        mod.BOT_N_N = BOT_N_N
        mod.BOT_LIN = BOT_LIN
        mod.command = command
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.run_sync = run_sync
        mod.reply_id = reply_id
        mod.progress = progress
        mod.run_async = run_async
        mod.admin_cmd = admin_cmd
        mod.parse_pre = parse_pre
        mod.StartTime = StartTime
        mod.Lastupdate = Lastupdate
        mod.media_type = media_type
        mod.ALIVE_NAME = ALIVE_NAME
        mod.mod_version = mod_version
        mod.edit_delete = edit_delete
        mod.ALIVE_IMAGE = ALIVE_IMAGE
        mod.install_pip = install_pip
        mod.modified_cmd = modified_cmd
        mod.friday_on_cmd = modified_cmd
        mod.edit_or_reply = edit_or_reply
        mod.BOT_NICK_NAME = BOT_NICK_NAME 
        mod.logger = logging.getLogger(shortname)
        # support for others
        sys.modules["uniborg.util"] = modified.utils
        sys.modules["userbot.utils"] = modified.utils
        sys.modules["userbot.plugins"] = modified.modules
        sys.modules[".events"] = .utils
        sys.modules[".plugins"] = .modules
        sys.modules["userbot"] = modified
        sys.modules["fridaybot"] = modified
        mod.ignore_grp = ignore_grp()
        mod.ignore_pm = ignore_pm()
        mod.ignore_bot = ignore_bot()
        mod.am_i_admin = am_i_admin()
        mod.ignore_fwd = ignore_fwd()
        spec.loader.exec_module(mod)
        sys.modules["modified.modules." + shortname] = mod
        sedprint.info("Successfully imported " + shortname)


def load_module_dclient(shortname, client):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import sys
        import importlib
        import modified.utils
        import modified.modules
        from pathlib import Path

        path = Path(f"modified/modules/{shortname}.py")
        name = "modified.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sedprint.info("Successfully (re)imported " + shortname)
    else:
        import sys
        import modified
        import importlib
        import modified.utils
        import modified.modules
        import modified.function 
        from pathlib import Path
        from modified.utils import edit_delete, edit_or_reply, media_type 

        path = Path(f"modified/modules/{shortname}.py")
        name = "modified.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = client
        mod.borg = client
        mod.modx = client
        mod.modex = client
        mod.modbot = client
        mod.friday = client
        mod.modified = client
        mod.tgbot = client.tgbot
        mod.Var = Config
        mod.Config = Config
        mod.BOT_N_N = BOT_N_N
        mod.BOT_LIN = BOT_LIN
        mod.command = command
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.run_sync = run_sync
        mod.reply_id = reply_id
        mod.progress = progress
        mod.run_async = run_async
        mod.admin_cmd = admin_cmd
        mod.parse_pre = parse_pre
        mod.StartTime = StartTime
        mod.Lastupdate = Lastupdate
        mod.media_type = media_type
        mod.ALIVE_NAME = ALIVE_NAME
        mod.mod_version = mod_version
        mod.edit_delete = edit_delete
        mod.ALIVE_IMAGE = ALIVE_IMAGE
        mod.install_pip = install_pip
        mod.modified_cmd = modified_cmd
        mod.friday_on_cmd = modified_cmd
        mod.edit_or_reply = edit_or_reply
        mod.BOT_NICK_NAME = BOT_NICK_NAME 
        mod.logger = logging.getLogger(shortname)
        # support for others
        sys.modules["uniborg.util"] = modified.utils
        sys.modules["userbot.utils"] = modified.utils
        sys.modules["userbot.plugins"] = modified.modules
        sys.modules[".events"] = .utils
        sys.modules[".plugins"] = .modules
        sys.modules["userbot"] = modified
        sys.modules["fridaybot"] = modified
        mod.ignore_grp = ignore_grp()
        mod.ignore_pm = ignore_pm()
        mod.ignore_bot = ignore_bot()
        mod.am_i_admin = am_i_admin()
        mod.ignore_fwd = ignore_fwd()
        spec.loader.exec_module(mod)
        sys.modules["modified.modules." + shortname] = mod
        sedprint.info("Successfully imported " + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except:
            name = f"modified.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except:
        raise ValueError


def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:

            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            new = {"error": str(sys.exc_info()[1]), "date": datetime.datetime.now()}

            text = "**USERBOT CRASH REPORT**\n\n"

            link = "[Here 🚪 ](https://t.me/GbeshMod)"
            text += "If you wanna you can report it"
            text += f"- just forward this message {link}.\n"
            text += "Nothing is logged except the fact of error and date\n"

            ftext = "\nDisclaimer:\nThis file uploaded ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"

            ftext += "--------BEGIN MODIFIED  USERBOT TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

            command = 'git log --pretty=format:"%an: %s" -5'

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            ftext += result

    return wrapper





