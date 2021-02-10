# Thanks to @AvinashReddy3108 for this plugin

"""
Audio and video downloader using Youtube-dl
.yta To Download in mp3 format
.ytv To Download in mp4 format
"""

import os
import time
import math
import asyncio
from telethon.tl.types import DocumentAttributeAudio

from .function import humanbytes, time_formatter, progressp as progress
from youtube_search import YoutubeSearch
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



@modbot.on(modified_cmd(pattern="yt(a|v) (.*)"))
@modbot.on(sudo_cmd(pattern="yt(a|v) (.*)", allow_sudo=True))
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()
    friday = await edit_or_reply(v_url, "Trying To Download......")
    await friday.edit("`Preparing to download...`")

    if type == "a":
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
                    "preferredquality": "480",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        video = False
        song = True

    elif type == "v":
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
        song = False
        video = True

    try:
        await friday.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await friday.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await friday.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await friday.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await friday.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await friday.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await friday.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await friday.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await friday.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await friday.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await friday.edit(
            f"`Preparing to upload song:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp3"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await friday.edit(
            f"`Preparing to upload video:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data["title"],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp4"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp4")
        await v_url.delete()



@modbot.on(modified_cmd(pattern="yt ?(.*)"))
@modbot.on(sudo_cmd(pattern="yt ?(.*)", allow_sudo=True))
async def yt_search(video_q):
    """For .yt command, do a YouTube search from Telegram."""
    query = video_q.pattern_match.group(1)
    if not query:
        await video_q.edit("`Enter query to search`")
    await video_q.edit("`Processing...`")
    try:
        results = json.loads(YoutubeSearch(query, max_results=7).to_json())
    except KeyError:
        return await video_q.edit(
            "`Youtube Search gone retard.\nCan't search this query!`"
        )
    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n"
    for i in results["videos"]:
        output += f"⎋⎋ `{i['title']}` \nhttps://www.youtube.com{i['url_suffix']} ⎋⎋\n\n"
    await video_q.edit(output, link_preview=False)



@modbot.on(modified_cmd(pattern="yts ?(.*)"))
@modbot.on(sudo_cmd(pattern="yts ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        fin = event.pattern_match.group(1)
        stark_result = await edit_or_reply(event, "Fectching Result this May Take Time")
        results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
        noob = "<b>YOUTUBE SEARCH</b> \n\n"
        for moon in results:
            hmm = moon["id"]
            kek = f"https://www.youtube.com/watch?v={hmm}"
            stark_name = moon["title"]
            stark_chnnl = moon["channel"]
            total_stark = moon["duration"]
            stark_views = moon["views"]
            noob += (
                f"<b><u>VIDEO-TITLE</u></b> ➠ <code>{stark_name}</code> \n"
                f"<b><u>LINK</u></b> ➠ <code>{kek}</code> \n"
                f"<b><u>CHANNEL</u></b> ➠ <code>{stark_chnnl}</code> \n"
                f"<b><u>DURATION</u></b> ➠ <code>{total_stark}</code> \n"
                f"<b><u>TOTAL-VIEWS</u></b> ➠ <code>{stark_views}</code> \n\n"
            )
        await stark_result.edit(noob, parse_mode="HTML")
    except:
        await event.edit("Some Thing Went Wrong.")
        


CMD_HELP.update(
    {
        "ytdl": "**Ytdl**\
\n\n**Syntax : **`.yta <song link> OR .ytv <video link>`\
\n**Usage :** download songs or videos from YouTube just with a link\
\n\n**Syntax : **`.yts <query>`\
\n**Usage :** searches the query on YouTube and give results. or   .yt <text>"
    }
)
