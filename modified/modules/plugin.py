import os
import asyncio
from datetime import datetime
from pathlib import Path
from telethon import functions, types, events
from telethon.tl.types import InputMessagesFilterDocument

from modified import LOAD_PLUG
from modified.utils import remove_plugin, load_module, edit_or_reply as eor


DELETE_TIMEOUT = 5
thumb_image_path = modified_pathp
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else botnickname


@borg.on(modified_cmd(pattern='plug ?(.*)'))
async def _(event):
    lul = event.pattern_match.group(1)
    yesm, nope, total_p = await get_all_modules(event, borg, lul)
    await event.edit(f"Installed {yesm} PLugins. Failed To Install {nope} Plugins And There Were Total {total_p} Plugins")
    


@modbot.on(modified_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@modbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./modified/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**➠ Plugin name:** `{input_str}`\n**➠ Uploaded in {time_taken_in_ms}**\n**➠ Uploaded by:** {BOT_LIN}\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        mixv = f"**404**: __📂{input_str} is Missing__"
        await eor(event, mixv)



@modbot.on(modified_cmd(pattern=r"^uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"./modified/modules/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        moddc = f"Uninstalled {shortname} successfully"
        await event.edit(moddc)
    except OSError as e:
        modde = f"Error: %s : %s What do you think you are doing..🐍 try  .delplugin {shortname} "
        await event.edit(modde, % (dir_path, e.strerror))


@modbot.on(modified_cmd(pattern="install"))
@modbot.on(sudo_cmd(pattern="install", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "modified/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "Plugin successfully installed\n `{}`👊".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "**404 Plugin**\nPlugin NOT installed!\n INVALID {}📣.. Can't even pre-installed.👌".format(downloaded_file_name),
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@modbot.on(modified_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@modbot.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f"{BOT_N_N} BOT Has Successfully unloaded {shortname}")
    except Exception as e:
        await qwe.edit(
            " Oops there's and error.. {shortname} already unloaded\n{}👊".format(shortname, str(e))
        )


@modbot.on(modified_cmd(pattern=r"load (?P<shortname>\w+)$"))
@modbot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}👊")
    except Exception as e:
        await qwe.edit(
            f"{BOT_N_N}📂 could not load {shortname} because of the following error.\n{str(e)}"
        )

CMD_HELP.update(
    {
        "uninstall": "**Plugin : **`uninstall`\
    \n\n**Syntax : **`uninstall`\
    \n**Function : **use this plugin without . and small later"
    }
)


CMD_HELP.update(
    {
        "install": "**Install**\
\n\n**Syntax : **`.install <reply to plugin>`\
\n**Usage :** it installs replyed plugin"
    }
)



CMD_HELP.update(
    {
        "unload": "**Plugin : **`unload`\
    \n\n**Syntax : **`.unload`\
    \n**Function : **use to disable a command..  I think this is the best decision"
    }
)


CMD_HELP.update(
    {
        "load": "**Load**\
    \n\n**Syntax : **`.load`\
    \n**Function : **use this to Enable a command  "
    }
)


CMD_HELP.update(
    {
        "plugin": "**Plugin**\
    \n\n**Syntax : **`.load`\
    \n**Function : **use this to Enable a command \
    \n\n**Syntax : **`.unload`\
    \n**Function : **use to disable a command..  I think this is the best decision\
    \n\n**Syntax : **`.install <reply to plugin>`\
    \n**Usage :** it installs replyed plugin\
    \n\n**Syntax : **`uninstall`\
    \n**Function : **use this plugin without . and small later"
    }
)