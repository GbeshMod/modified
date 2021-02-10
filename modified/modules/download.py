# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.c (the "License");

import asyncio
import math
import os
import time
from datetime import datetime
from pySmartDL import SmartDL
from modified.utils import admin_cmd, sudo_cmd, humanbytes


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else BOT_N_N




import aria2p
from telethon import events
import asyncio
import os
from userbot.utils import admin_cmd
cmd = "aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800  --max-connection-per-server=10 --rpc-max-request-size=1024M --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=10 --daemon=true"

aria2_is_running = os.system(cmd)

aria2 = aria2p.API(
		aria2p.Client(
			host="http://localhost",
			port=6800,
			secret=""
		)
	)

EDIT_SLEEP_TIME_OUT = 10

@borg.on(admin_cmd(pattern="fdownload ?(.*)"))
async def magnet_download(event):
	if event.fwd_from:
		return
	var = event.pattern_match.group(1)
	print(var)	
	uris = [var]

	#Add URL Into Queue 
	try:	
		download = aria2.add_uris(uris, options=None, position=None)
	except Exception as e:
		await event.edit("`Error:\n`"+str(e))
		return

	gid = download.gid
	complete = None
	await progress_status(gid=gid,event=event,previous=None)
	file = aria2.get_download(gid)
	if file.followed_by_ids:
		new_gid = await check_metadata(gid)
		await progress_status(gid=new_gid,event=event,previous=None)
	while complete != True:
		file = aria2.get_download(gid)
		complete = file.is_complete
		try:
			msg = "**Downloading File:** "+str(file.name) +"\n**Speed:** "+ str(file.download_speed_string())+"\n**Progress:** "+str(file.progress_string())+"\n**Total Size:** "+str(file.total_length_string())+"\n**ETA:**  "+str(file.eta_string())+"\n\n"  	
			await event.edit(msg)
			await asyncio.sleep(10)
		except Exception as e:
			# print(str(e))
			pass	
			
	await event.edit("**File Downloaded Successfully:** `{}`".format(file.name))


async def progress_status(gid,event,previous):
	try:
		file = aria2.get_download(gid)
		if not file.is_complete:
			if not file.error_message:
				msg = "Downloading File: `"+str(file.name) +"`\nSpeed: "+ str(file.download_speed_string())+"\nProgress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nStatus: "+str(file.status)+"\nETA:  "+str(file.eta_string())+"\n\n"
				if previous != msg:
					await event.edit(msg)
					previous = msg
			else:
				logger.info(str(file.error_message))
				await event.edit("Error : `{}`".format(str(file.error_message)))		
				return
			await asyncio.sleep(EDIT_SLEEP_TIME_OUT)	
			await progress_status(gid,event,previous)
		else:
			await event.edit("File Downloaded Successfully: `{}`".format(file.name))
			return
	except Exception as e:
		if " not found" in str(e) or "'file'" in str(e):
			await event.edit("Download Canceled :\n`{}`".format(file.name))
			return
		elif " depth exceeded" in str(e):
			file.remove(force=True)
			await event.edit("Download Auto Canceled :\n`{}`\nYour Torrent/Link is Dead.".format(file.name))
		else:
			logger.info(str(e))
			await event.edit("Error :\n`{}`".format(str(e)))
			return			


async def check_metadata(gid):
	file = aria2.get_download(gid)
	new_gid = file.followed_by_ids[0]
	logger.info("Changing GID "+gid+" to "+new_gid)
	return new_gid	






@bot.on(admin_cmd(pattern="download (?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="download (?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mone = await edit_or_reply(event, "`Processing ...`")
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        start = datetime.now()
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await event.client.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
        else:
            end = datetime.now()
            ms = (end - start).seconds
            await mone.edit(
                f"**  •  Downloaded in {ms} seconds.**\n**  •  Downloaded to :- ** `{downloaded_file_name}`\n**  •  Downloaded by :-** {DEFAULTUSER}"
            )
    elif input_str:
        start = datetime.now()
        url = input_str
        file_name = os.path.basename(url)
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        if "|" in input_str:
            url, file_name = input_str.split("|")
        url = url.strip()
        file_name = file_name.strip()
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        while not downloader.isFinished():
            total_length = downloader.filesize or None
            downloaded = downloader.get_dl_size()
            display_message = ""
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            downloader.get_speed()
            progress_str = "`{0}{1} {2}`%".format(
                "".join(["⬤" for i in range(math.floor(percentage / 5))]),
                "".join(["⊙" for i in range(20 - math.floor(percentage / 5))]),
                round(percentage, 2),
            )
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"Downloading the file\
                                \n\n**URL : **`{url}`\
                                \n**File Name :** `{file_name}`\
                                \n{progress_str}\
                                \n`{humanbytes(downloaded)} of {humanbytes(total_length)}`\
                                \n**ETA : **`{estimated_total_time}``"
                if round(diff % 10.00) == 0 and current_message != display_message:
                    await mone.edit(current_message)
                    display_message = current_message
            except Exception as e:
                logger.info(str(e))
        end = datetime.now()
        ms = (end - start).seconds
        if downloader.isSuccessful():
            await mone.edit(
                f"**  •  Downloaded in {ms} seconds.**\n**  •  Downloaded to ⪼ ** `{downloaded_file_name}`"
            )
        else:
            await mone.edit("Incorrect URL\n {}".format(input_str))
    else:
        await mone.edit("Reply to a message to download to my local server.")


CMD_HELP.update(
    {
        "download": "**Download**`.download`\
        \n\n  •  **Syntax : **`.download <link|filename> or reply to media`\
        \n  •  **Function : **__Downloads the file to the server.__ \
        \n\n  •  **Syntax : **`.fdownload <link|filename> or reply to media`\"
    }
)
