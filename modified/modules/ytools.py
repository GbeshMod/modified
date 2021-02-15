import os
import glob
import time
import wget
import math
import shutil
import asyncio
from youtubesearchpython import SearchVideos
from telethon.tl.types import DocumentAttributeAudio
from modified.function.FastTelethon import upload_file
from modified.function import humanbytes, time_formatter
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)



@modbot.on(modified_cmd(pattern="ytsong ?(.*)"))
@modbot.on(sudo_cmd(pattern="ytsong ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    gbeshz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{gbeshz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out=path)
    stark = (
        f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k '
        + mo
    )
    os.system(stark)
    await asyncio.sleep(4)
    km = f"./music/{thum}.mp3"
    if os.path.exists(km):
        await myself_stark.edit("`Song Downloaded Sucessfully. Let Me Upload it Here.`")
    else:
        await myself_stark.edit("`SomeThing Went Wrong. Try Again After Sometime..`")
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await borg.send_file(
        event.chat_id,
        km,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        performer=thums,
        supports_streaming=True,
    )
    await myself_stark.edit("`Song Uploaded. By Modifiedbot`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)



@modbot.on(modified_cmd(pattern="ytmusic ?(.*)"))
@modbot.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    print(urlissed)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    dur = mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    path = Config.TMP_DOWNLOAD_DIRECTORY
    url = mo
    sedlyf = wget.download(kekme, out=path)
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "720",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
    except Exception as e:
        await event.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    await asyncio.sleep(20)
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp3"
    lol_m = await upload_file(
            file_name=f"{ytdl_data['title']}.mp3",
            client=borg,
            file=open(file_stark, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Song!", str(ytdl_data["title"])
                )
            ),
        )
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await event.delete()
    await borg.send_file(
        event.chat_id,
        lol_m,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
        supports_streaming=True,
    )
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@modbot.on(modified_cmd(pattern="utubevid ?(.*)"))
@modbot.on(sudo_cmd(pattern="utubevid ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    path = Config.TMP_DOWNLOAD_DIRECTORY
    url = mo
    sedlyf = wget.download(kekme, out=path)
    opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    lol_m = await upload_file(
            file_name=f"{ytdl_data['title']}.mp4",
            client=borg,
            file=open(file_stark, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Video!", str(ytdl_data["title"])
                )
            ),
        )
    capy = f"**Video Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await event.delete()
    await borg.send_file(
        event.chat_id,
        lol_m,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                )
            ],
        supports_streaming=True,
    )
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@modbot.on(modified_cmd(pattern="ytm4a ?(.*)"))
@modbot.on(sudo_cmd(pattern="ytm4a ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Config.TMP_DOWNLOAD_DIRECTORY
    url = mo
    sedlyf = wget.download(kekme, out=path)
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "m4a",
                    "preferredquality": "720",
                }
            ],
            "outtmpl": "%(id)s.m4a",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except Exception as e:
        await event.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    await asyncio.sleep(20)
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.m4a"
    lol_m = await upload_file(
            file_name=f"{ytdl_data['title']}.m4a",
            client=borg,
            file=open(file_stark, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Song!", str(ytdl_data['title'])
                )
            ),
        )
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await event.delete()
    await borg.send_file(
        event.chat_id,
        lol_m,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
        supports_streaming=True,
    )
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)



CMD_HELP.update(
    {
        "ytools": "**Ytools**\
\n\n**Syntax : **`.ytmusic or .ytsong <song name>`\
\n**Usage :** Downloads songs from ytmusic\
\n\n**Syntax : **`.utubevid <video name>`\
\n**Usage :** Downloads video from ytmusic\
\n\n**Syntax : **`.ytm4a <song name>`\
\n**Usage :** Downloads songs from ytmusic with best quality"
    }
)
