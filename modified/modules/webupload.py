""" .webupload  anfiles = anonfiles|amfiles = anonymousfiles|transfer|filebin|megaupload|bayfiles|fileio|oload|vshare|ninja)"""

import io
import os
import re
import time
import json
import asyncio
import requests
import subprocess
from telethon import events
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError


@bot.on(admin_cmd(pattern="webupload ?(.+?|) --(fileio|oload|anfiles|transfer|filebin|amfiles|vshare|bayfiles|megaupload|ninja)"))
@bot.on(sudo_cmd(pattern="webupload ?(.+?|) --(fileio|oload|anfiles|transfer|filebin|amfiles|vshare|bayfiles|megaupload|ninja)", allow_sudo=True,))
async def _(event):
    if event.fwd_from:
        return
    editor = await edit_or_reply(event, "processing ...")
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await modbot.download_media(reply.media, Config.TEMP_DOWNLOAD_DIRECTORY)
    CMD_WEB = {
        "anfiles": 'curl -F "file=@{}" https://anonfiles.com/api/upload',
        "oload": 'curl -F "file=@{full_file_path}" https://api.openload.cc/upload',
        "vshare": 'curl -F "file=@{full_file_path}" https://api.vshare.is/upload',
        "transfer": 'curl --upload-file "{full_file_path}" https://transfer.sh/'
        + os.path.basename(file_name),
        "filebin": 'curl -X POST --data-binary "@test.png" -H "filename: {}" "https://filebin.net"',
        "amfiles": 'curl -F file="@{}" https://api.anonymousfiles.io/',
        "megaupload": 'curl -F "file=@{}" https://megaupload.is/api/upload',
        "ninja": "curl -i -F file=@{} https://tmp.ninja/api.php?d=upload-tool",
        "fileio": 'curl -F "file=@{full_file_path}" https://file.io',
        "bayfiles": '.exec curl -F "file=@{}" https://bayfiles.com/api/upload',
    }
    filename = os.path.basename(file_name)
    try:
        selected_one = CMD_WEB[selected_transfer].format(
            full_file_path=file_name, bare_local_name=filename
        )
    except KeyError:
        await editor.edit("Invalid selected Transfer")
        return
    cmd = selected_one
    # start the subprocess $SHELL
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    error = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if t_response:
        try:
            t_response = json.dumps(json.loads(t_response), sort_keys=True, indent=4)
        except Exception:
            # some sites don't return valid JSONs
            pass
        urls = links = re.findall(link_regex, t_response)
        result = ""
        for i in urls:
            if not result:
                result = f"**Uploaded File🗃 🔗 link/links :**"
            result += f"\n{i[0]}"
        await editor.edit(result)
    else:
        await editor.edit(error)
    if catcheck:
        os.remove(file_name)


link_regex = re.compile(
    "((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL
)


@bot.on(admin_cmd(pattern="labstack( (.*)|$)"))
@bot.on(sudo_cmd(pattern="labstack( (.*)|$)", allow_sudo=True))
async def labstack(event):
    if event.fwd_from:
        return
    editor = await edit_or_reply(event, "Processing...")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if input_str:
        filebase = input_str
    elif reply:
        filebase = await event.client.download_media(
            reply.media, Config.TMP_DOWNLOAD_DIRECTORY
        )
    else:
        await editor.edit(
            "Reply to a media file or provide a directory to upload the file to labstack"
        )
        return
    filesize = os.path.getsize(filebase)
    filename = os.path.basename(filebase)
    headers2 = {"Up-User-ID": "IZfFbjUcgoo3Ao3m"}
    files2 = {
        "ttl": 604800,
        "files": [{"name": filename, "type": "", "size": filesize}],
    }
    r2 = requests.post(
        "https://up.labstack.com/api/v1/links", json=files2, headers=headers2
    )
    r2json = json.loads(r2.text)

    url = "https://up.labstack.com/api/v1/links/{}/send".format(r2json["code"])
    max_days = 7
    command_to_exec = [
        "curl",
        "-F",
        "files=@" + filebase,
        "-H",
        "Transfer-Encoding: chunked",
        "-H",
        "Up-User-ID: IZfFbjUcgoo3Ao3m",
        url,
    ]
    try:
        logger.info(command_to_exec)
        t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        logger.info("Status : FAIL", exc.returncode, exc.output)
        await editor.edit(exc.output.decode("UTF-8"))
        return
    else:
        logger.info(t_response)
        t_response_arry = "https://up.labstack.com/api/v1/links/{}/receive".format(
            r2json["code"]
        )
    await editor.edit(
        t_response_arry + "\nMax Days:" + str(max_days), link_preview=False
    )


CMD_HELP.update(
    {
        "webupload": "**Webupload**\
    \n\n**Syntax : **`.webupload` --(`fileio`|`oload`|`anfiles`|`transfer`|`filebin`|`amfiles`|`vshare`|`bayfiles`|`megaupload`|`ninja`) or \
    \n         `.webupload` (path of file) --(`fileio`|`oload`|`anfiles`|`transfer`|`filebin`|`amfiles`|`vshare`|`bayfiles`|`megaupload`|`ninja`)\
    \n**Usage : **Upload the file to web according to your choice\
    \n**Example : **`.webupload --anonfiles` tag this to a file\
    \n\n**Syntax :** `.labstack` Reply to a media file or provide a directory\
    \n**Usage : **Upload the file to labstack for 7 days."
    }
)
