import io
import os
import os
import time
import modified
from os.path import exists, isdir
from modified.utils import humanbytes, progress, modified_cmd, sudo_cmd, modified_image

MAX_MESSAGE_SIZE_LIMIT = 4095
DELETE_TIMEOUT = 5
thumb_image_paths = modified_patht
thumb_image_pathd = modified_pathd
thumb_image_pathf = modified_pathf




@modbot.on(modified_cmd(pattern=r"ls (.*)"))
@modbot.on(sudo_cmd(pattern=r"ls (.*)", allow_sudo=True))
async def lst(event):
    if event.fwd_from:
        return
    pucy = event.pattern_match.group(1)
    path = pucy if pucy else os.getcwd()
    if not exists(path):
        await event.edit(
            f"oops🤔 no such directory or file with this 👉 `{pucy}`.\n Please check again!🔬"
        )
        return
    if isdir(path):
        msg = "**PATH:** `{}`\n\n".format(path) if pucy else "• **File Manager** •\n\n"
        lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in sorted(lists):
            catpath = path + "/" + contents
            if not isdir(catpath):
                size = os.stat(catpath).st_size
                if contents.endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += "🎵 " + f"`{contents}`\n"
                if contents.endswith((".opus")):
                    files += "🎙 " + f"`{contents}`\n"
                elif contents.endswith(
                    (".mkv", ".mp4", ".webm")
                ):
                    files += "🎞 " + f"`{contents}`\n"
                elif contents.endswith(
                    (".avi", ".mov", ".flv")
                ):
                    files += "🎬 " + f"`{contents}`\n"
                elif contents.endswith(
                    (".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")
                ):
                    files += "🗜 " + f"`{contents}`\n"
                elif contents.endswith(
                    (".jpg", ".jpeg", ".png")
                ):
                    files += "🖼 " + f"`{contents}`\n"
                elif contents.endswith(
                    (".gif", ".bmp", ".ico", ".webp")
                ):
                    files += "📸 " + f"`{contents}`\n"
                elif contents.endswith((".exe", ".deb")):
                    files += "️💾 " + f"`{contents}`\n"
                elif contents.endswith((".iso", ".img")):
                    files += "💿 " + f"`{contents}`\n"
                elif contents.endswith((".json")):
                    files += " **{ }** " + f"`{contents}`\n"
                elif contents.endswith(("LICENSE")):
                    files += "🔑 " + f"`{contents}`\n"
                elif contents.endswith((".apk", ".xapk")):
                    files += "📱 " + f"`{contents}`\n"
                elif contents.endswith((".py")):
                    files += "🐍 " + f"`{contents}`\n"
                elif contents.endswith((".md")):
                    files += "📜 " + f"`{contents}`\n"
                elif contents.endswith((".yml")):
                    files += "📋 " + f"`{contents}`\n"
                else:
                    files += "📄 " + f"`{contents}`\n"
            else:
                folders += f"📁 `{contents}`\n"
        msg = msg + folders + files if files or folders else msg + "__📂empty path__"
    else:
        size = os.stat(path).st_size
        msg = "The details of given file :\n\n"
        if path.endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵 "
        if path.endswith((".opus")):
            mode = "🎙 "
        elif path.endswith((".mkv", ".mp4", ".webm")):
            mode = "🎞 "
        elif path.endswith((".avi", ".mov", ".flv")):
            mode = "🎬 "
        elif path.endswith((".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")):
            mode = "🗜 "
        elif path.endswith((".jpg", ".jpeg", ".png")):
            mode = "🖼 "
        elif path.endswith((".gif", ".bmp", ".ico", ".webp")):
            mode = "📸 "
        elif path.endswith((".exe", ".deb")):
            mode = "💾 "
        elif path.endswith((".iso", ".img")):
            mode = "💿 "
        elif path.endswith((".json")):
            mode = "**{}** "
        elif path.endswith(("LICENSE")):
            mode = "🔑 "
        elif path.endswith((".apk", ".xapk")):
            mode = "📱 "
        elif path.endswith((".py")):
            mode = "🐍 "
        elif path.endswith((".md")):
            mode = "📜 "
        elif path.endswith((".yml")):
            mode = "📋 "
        else:
            mode = "📄 "
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**Location :** `{path}`\n"
        msg += f"**Icon :** `{mode}`\n"
        msg += f"**Size :** `{humanbytes(size)}`\n"
        msg += f"**Last Modified Time:** `{time2}`\n"
        msg += f"**Last Accessed Time:** `{time3}`"

    if len(msg) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ls.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=path,
            )
            await event.delete()
    else:
        await event.edit(msg)


@modbot.on(modified_cmd(pattern=r"sendf (?P<shortname>\w+)"))
@modbot.on(sudo_cmd(pattern=r"sendf (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_pathf
    input_str = event.pattern_match.group(1)
    the_bot_filess = "./{}".format(input_str)
    if os.path.exists(the_bot_filess):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_bot_filess,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**➠ File name 💻:** `{input_str}`\n**➠ Uploaded in : ⏳{time_taken_in_ms} .*\n**➠ Uploaded by:** {BOT_LIN}\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await eor(event, "**404**: __📂{the_bot_filess} is Missing__")


@modbot.on(modified_cmd(pattern=r"sendd (?P<shortname>\w+)"))
@modbot.on(sudo_cmd(pattern=r"sendd (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_pathd
    dowxl = Config.TEMP_DOWNLOAD_DIRECTORY
    input_str = event.pattern_match.group(1)
    the_down_load = "{}{}".format(dowxl, input_str)
    if os.path.exists(the_down_load):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_down_load,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**➠ Downloaded 💾** `{input_str}`\n**➠ Uploaded in {time_taken_in_ms} seconds only.**\n**➠ Uploaded by:** {BOT_LIN}\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await eor(event, "**404**: __📂{the_down_load} is Missing__")


@modbot.on(modified_cmd(pattern=r"sendt (?P<shortname>\w+)"))
@modbot.on(sudo_cmd(pattern=r"sendt (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_paths
    tshh = Config.TRASH_DOWNLOAD_DIRECTORY
    input_str = event.pattern_match.group(1)
    the_save_file = "{}{}".format(tshh, input_str)
    if os.path.exists(the_save_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_save_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**➠ TRASH name:** `{input_str}`\n**➠ Uploaded in {time_taken_in_ms} seconds only.**\n**➠ Uploaded by:** {BOT_LIN}\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await eor(event, "**404**: __📂{the_save_file} is Missing__")


@modbot.on(modified_cmd(pattern="rmls (.*)"))
@modbot.on(sudo_cmd(pattern="rmls (.*)", allow_sudo=True))
async def lst(event):
    remov = event.pattern_match.group(1)
    if remov:
        path = Path(remov)
    else:
        await edit_or_reply(event, "What should i delete♻️")
        return
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"oops🤔 no such directory or file with this 👉 `{remov}` check again🔍",
        )
        return
    modcmd = f"rm -rf {path}"
    if os.path.isdir(path):
        await runcmd(modcmd)
        await edit_or_reply(event, f"Succesfully Deleted•°♻️ `{path}` 📂")
    else:
        await runcmd(modcmd)
        await edit_or_reply(event, f"Succesfully Deleted•°♻️ `{path}`🗂")

@modbot.on(modified_cmd(pattern="mkdir (?: |$)(.*)"))
@modbot.on(sudo_cmd(pattern="mkdir (?: |$)(.*)", allow_sudo=True))
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
            f"Already exists 👉 {original} ",
        )
        return
    mone = await edit_or_reply(
        event, "creating the directory ...", parse_mode=parse_pre
    )
    await asyncio.sleep(2)
    try:
        await runcmd(f"mkdir {original}")
        await mone.edit(f"Successfully created the directory 👉 `{original}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@modbot.on(modified_cmd(pattern="cpls (?: |$)(.*)"))
@modbot.on(sudo_cmd(pattern="cpls (?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    pwd = "./"
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i copy the 🗂 OR 📁.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .cpls from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"oops🤔 no such directory or file with this 👉 `{cat}` check again🔍",
        )
        return
    mone = await edit_or_reply(event, "copying the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        await runcmd(f"cp -r {original} {location}")
        await mone.edit(f"Successfully copied the 👉 `{original}` to `{location}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)


@modbot.on(modified_cmd(pattern="mvls (?: |$)(.*)"))
@modbot.on(sudo_cmd(pattern="mvls (?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    pwd = "./"
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await edit_delete(
            event,
            "What and where should i move the 🗂 OR 📁.",
            parse_mode=parse_pre,
        )
    loc = input_str.split(";")
    if len(loc) != 2:
        return await edit_delete(
            event, "use proper syntax .mvls from ; to destination", parse_mode=parse_pre
        )
    original = os.path.join(pwd, loc[0].strip())
    location = os.path.join(pwd, loc[1].strip())

    if not os.path.exists(original):
        await edit_delete(
            event,
            f"oops🤔 no such directory or file with this 👉 `{cat}` check again🔍",
        )
        return
    mone = await edit_or_reply(event, "Moving the file ...", parse_mode=parse_pre)
    await asyncio.sleep(2)
    try:
        shutil.move(original, location)
        await mone.edit(f"Successfully moved the 👉 `{original}` to `{location}`")
    except Exception as e:
        await edit_delete(mone, str(e), parse_mode=parse_pre)

CMD_HELP.update(
    {
        "file": "**Filemanager**\
     \n\nList Files plugin for modified \
     \n**Syntax :** `.ls`\
     \n**Usage :** will return files from current working directory\
     \n\n**Syntax :** .ls path\
     \n**Usage :** will return output according to path  \
      \n\n**Syntax :** `.rmls path`\
     \n**Usage :** To delete the required item from the bot server\
      \n\n  •  **Syntax :** `.mkdir foldername`\
     \n  •  **Usage :** Creates a new empty folder in the server\
     \n\n  •  **Syntax :** `.mvls frompath ; topath`\
     \n  •  **Usage :** Move a file from one location to other location in bot server\
     \n\n  •  **Syntax :** `.cpls frompath ; topath`\
     \n  •  **Usage :** Copy a file from one location to other location in bot server ** please take** about sending \
     .sendd to send download files |  .sendp to send plugins please take note not all userbot can use yours but you can use other bot is Modified | .sendf to send files from directory.. e.g sendf README.md| .sendt to send trash files 😀"
    }
)
