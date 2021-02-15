"""Execute GNU/Linux commands inside Telegram
Syntax: .lsroot , .lslocal .delsave .delocal .delplugin ⪼⪼ mvsaved to ./SAVED/  :)  mvlocal to  /download/ ➠➠@GbeshMod➠➠"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# ©left by @GbeshMod
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
import os

dwnnnl = Config.TEMP_DOWNLOAD_DIRECTORY
trassss = Config.TRASH_DOWNLOAD_DIRECTORY



@borg.on(events.NewMessage(pattern=r"\.lslocal", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100

    cmd = "ls -lh " + dwnnnl

    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**📁Files in download Folder**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

@borg.on(events.NewMessage(pattern=r"\.lsroot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "ls -lh"
	
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**📁Files in root directory**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

@borg.on(events.NewMessage(pattern=r"\.lstrash", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "ls " + trassss
	
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**📁Files in TRASH directory**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

@borg.on(events.NewMessage(pattern=r"\.mvtrash ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    trassss = Config.TRASH_DOWNLOAD_DIRECTORY
    cmd = f"mv {trassss}{src} {trassss}{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**📁Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"File renamed `{src}` to `{dst}`")
	
@borg.on(events.NewMessage(pattern=r"\.mvlocal ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    dwnnnl = Config.TEMP_DOWNLOAD_DIRECTORY
    cmd = f"mv {dwnnnl}{src} {dwnnnl}{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**📁Files in root directory**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"File renamed `{src}` to `{dst}`")
        
@borg.on(events.NewMessage(pattern=r"\.deltrash (.*)", outgoing=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"{trassss}{input_str}"

	
    if os.path.isfile(pathtofile):
     os.remove(pathtofile)
     await event.edit("File Deleted ♻️")
	 
    else:
         await event.edit(" **404** __ {pathtofile} 💀 Not found __")
        
@borg.on(events.NewMessage(pattern=r"\.delocal (.*)", outgoing=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"{dwnnnl}{input_str}"

	
    if os.path.isfile(pathtofile):
     os.remove(pathtofile)
     await event.edit("File Deleted ♻️")
	 
    else:
         await event.edit(" **404** __ {pathtofile} 💀 Not found __")
        
         
@borg.on(events.NewMessage(pattern=r"\.delplugin (.*)", outgoing=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"./modified/modules/{input_str}.py"

	
    if os.path.isfile(pathtofile):
     os.remove(pathtofile)
     await event.edit(f"🔌 {input_str} Deleted ♻️")
	 
    else:
         await event.edit(f" **404** __ {input_str} 💀 Not found __")



@bot.on(admin_cmd(pattern="del (.*)"))
@bot.on(sudo_cmd(pattern="del (.*)", allow_sudo=True))
async def lst(event):
    mod = event.pattern_match.group(1)
    if mod:
        path = Path(mod)
    else:
        await edit_or_reply(event, "what should i delete")
        return
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"there is no such directory or file with the name `{mod}` check again",
        )
        return
    modcmd = f"rm -rf {path}"
    if os.path.isdir(path):
        await _modutils.runcmd(modcmd)
        await edit_or_reply(event, f"Succesfully removed `{path}` directory")
    else:
        await _modutils.runcmd(modcmd)
        await edit_or_reply(event, f"Succesfully removed `{path}` file")


@bot.on(admin_cmd(pattern="mkdir(?: |$) (.*)"))
@bot.on(sudo_cmd(pattern="mkdir(?: |$) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    pwd = "./"
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What should i create ?",
            parse_mode=parse_pre,
        )
    original = os.path.join(pwd, input_str.strip())
    if os.path.exists(original):
        await edit_delete(
            event,
            f"Already a directory named {original} exists",
        )
        return
    mone = await edit_or_reply(
        event, "creating the directory ...", parse_mode=parse_pre
    )
    await asyncio.sleep(2)
    try:
        await _modutils.runcmd(f"mkdir {original}")
        await mone.edit(f"Successfully created the directory `{original}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@bot.on(admin_cmd(pattern="cpto(?: |$) (.*)"))
@bot.on(sudo_cmd(pattern="cpto(?: |$) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    pwd = "./"
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i move the file/folder.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .cpto from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"there is no such directory or file with the name `{mod}` check again",
        )
        return
    mone = await edit_or_reply(event, "copying the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        await _modutils.runcmd(f"cp -r {original} {location}")
        await mone.edit(f"Successfully copied the `{original}` to `{location}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@bot.on(admin_cmd(pattern="mvto(?: |$) (.*)"))
@bot.on(sudo_cmd(pattern="mvto(?: |$) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    pwd = "./"
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i move the file/folder.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .mvto from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"there is no such directory or file with the name `{mod}` check again",
        )
        return
    mone = await edit_or_reply(event, "Moving the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        shutil.move(original, location)
        await mone.edit(f"Successfully moved the `{original}` to `{location}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)




CMD_HELP.update(
    {
        "filemanager": "**Filemanager**``\
     \n\nList Files plugin for userbot \
     \n  •  **Syntax :** `.lslocal`\
     \n  •  **Usage :** will return files from current download directory\
     \n\n  •  **Syntax :** .lsroot\
     \n  •  **Usage :** will return output according to path with more info \
     \n\n  •  **Syntax :** .lstrash file path\
     \n  •  **Usage : it will list trash directory for you. \
     \n\n  •  **Syntax :** `.del(ocal|trash|plugin) nicepic.jpg`\
     \n  •  **Usage :** To delete the required item from the bot server please take note plugins don't not require <.py> meme.py ... e.g delplugin meme 👍\
     \n\n  •  **Syntax :** `.mkdir foldername`\
     \n  •  **Usage :** Creates a new empty folder in the server\
     \n\n  •  **Syntax :** `.mv(local|trash) frompath ; topath`\
     \n  •  **Usage :** Move a file from one location to other location in bot server  .mvto\
     \n\n  •  **Syntax :** `.cpto frompath ; topath`\
     \n  •  **Usage :** Copy a file from one location to other location in bot server\
"
    }
)
