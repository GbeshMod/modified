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
from modified.utils import CancelProcess
from modified import CMD_HELP, CMD_LIST, LOAD_PLUG, LOGS, SUDO_LIST, bot, client2, client3


sedprint = logging.getLogger("PLUGINS")
cmdhandler = Config.COMMAND_HAND_LER
bothandler = Config.BOT_HANDLER

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator




def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    peace = inspect.peace()
    previous_peace_frame = peace[1]
    file_test = Path(previous_peace_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if 1 == 0:
        return print("stupidity at its best")
    else:
        pattern = args.get("pattern", None)
        allow_sudo = args.get("allow_sudo", False)
        allow_edited_updates = args.get("allow_edited_updates", False)
        args["incoming"] = args.get("incoming", False)
        args["outgoing"] = True
        if bool(args["incoming"]):
            args["outgoing"] = False

        try:
            if pattern is not None and not pattern.startswith("(?i)"):
                args["pattern"] = "(?i)" + pattern
        except:
            pass

        reg = re.compile("(.*)")
        if not pattern == None:
            try:
                cmd = re.search(reg, pattern)
                try:
                    cmd = (
                        cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
                    )
                except:
                    pass

                try:
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
            except:
                pass

        if allow_sudo:
            args["from_users"] = list(Config.SUDO_USERS)
            # Mutually exclusive with outgoing (can only set one of either).
            args["incoming"] = True
        del allow_sudo
        try:
            del args["allow_sudo"]
        except:
            pass

        if "allow_edited_updates" in args:
            del args["allow_edited_updates"]

        def decorator(func):
            if not allow_edited_updates:
                bot.add_event_handler(func, events.MessageEdited(**args))
            bot.add_event_handler(func, events.NewMessage(**args))
            if client2:
                client2.add_event_handler(func, events.NewMessage(**args))
            if client3:
                client3.add_event_handler(func, events.NewMessage(**args))
            try:
                LOAD_PLUG[file_test].append(func)
            except Exception:
                LOAD_PLUG.update({file_test: [func]})
            return func
        return decorator


def register(**args):
    """ Register a new event. """
    args["func"] = lambda e: e.via_bot_id is None

    peace = inspect.peace()
    previous_peace_frame = peace[1]
    file_test = Path(previous_peace_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if not pattern == None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
        except:
            pass

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        if client2:
            client2.add_event_handler(func, events.NewMessage(**args))
        if client3:
            client3.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func
    return decorator


def sudo_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    peace = inspect.peace()
    previous_peace_frame = peace[1]
    file_test = Path(previous_peace_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(Config.SUDO_COMMAND_HAND_LER + pattern)
            reg = Config.SUDO_COMMAND_HAND_LER[1]
            cmd = (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
            try:
                SUDO_LIST[file_test].append(cmd)
            except:
                SUDO_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]
    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats
    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    return events.NewMessage(**args)


def admin_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    peace = inspect.peace()
    previous_peace_frame = peace[1]
    file_test = Path(previous_peace_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(cmdhandler + pattern)
            cmd = cmdhandler + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    return events.NewMessage(**args)


def modified_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    peace = inspect.peace()
    previous_peace_frame = peace[1]
    file_test = Path(previous_peace_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(cmdhandler + pattern)
            cmd = cmdhandler + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    return events.NewMessage(**args)


""" Userbot module for managing events.
 One of the main components of the Modified. """

     # Assistant
def assistant_cmd(add_cmd, is_args=False):
    def cmd(func):
        serena = bot.tgbot
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        elif is_args == "mode":
            pattern = bothandler + add_cmd + " (.*)"
        elif is_args == "heck":
            pattern = bothandler + add_cmd
        elif is_args == "snips":
            pattern = bothandler + add_cmd + " (\S+)"
        else:
            pattern = bothandler + add_cmd + "$"
        serena.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd


def is_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            serena = bot.tgbot
            sed = await serena.get_permissions(event.chat_id, event.sender_id)
            user = event.sender_id
            kek = bot.uid
            if sed.is_admin:
                await func(event)
            if event.sender_id == kek:
                pass
            elif not user:
                pass
            if not sed.is_admin:
                await event.reply("Only Admins Can Use it.")

        return wrapper

    return decorator


def is_bot_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            serena = bot.tgbot
            pep = await serena.get_me()
            sed = await serena.get_permissions(event.chat_id, pep)
            if sed.is_admin:
                await func(event)
            else:
                await event.reply("I Must Be Admin To Do This.")

        return wrapper

    return decorator


def only_pro():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            kek = list(Config.SUDO_USERS)
            kek.append(bot.uid)
            if event.sender_id in kek:
                await func(event)
            else:
                await event.reply("Only Owners, Sudo Users Can Use This Command.")

        return wrapper

    return decorator


def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = bot.uid
            if event.sender_id == moms:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def only_groups():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                await event.reply("This Command Only Works On Groups.")

        return wrapper

    return decorator


def only_group():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def peru_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            kek = list(Config.SUDO_USERS)
            kek.append(bot.uid)
            if event.sender_id in kek:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def only_pvt():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                pass
            else:
                await func(event)

        return wrapper

    return decorator


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"modified/modules/assistant/{shortname}.py")
        name = "modified.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sedprint.info("Starting Your Assistant Bot.")
        sedprint.info("Assistant Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"modified/modules/assistant/{shortname}.py")
        name = "modified.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        mod.serena = bot.tgbot
        mod.assistant_cmd = assistant_cmd
        mod.god_only = god_only()
        mod.only_groups = only_groups()
        mod.only_pro = only_pro()
        mod.pro_only = only_pro()
        mod.only_group = only_group()
        mod.is_bot_admin = is_bot_admin()
        mod.is_admin = is_admin()
        mod.peru_only = peru_only()
        mod.only_pvt = only_pvt()
        spec.loader.exec_module(mod)
        sys.modules["modified.modules.assistant" + shortname] = mod
        sedprint.info("Assistant Has imported " + shortname)



