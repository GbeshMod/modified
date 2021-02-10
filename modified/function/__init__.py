import os
import wget
import lottie
import asyncio
import hachoir
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from modified.utils import load_module
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from telethon.tl.types import DocumentAttributeAudio
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

import math, re, shlex, json, time, eyed3, aiohttp, zipfile
import telethon
import requests
import subprocess
import webbrowser
from typing import Union
from os.path import basename
from modified import logging
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from typing import List, Optional, Tuple
from telethon.tl.types import InputMessagesFilterDocument
from telethon import Button, custom, events, functions
from pymediainfo import MediaInfo
from telethon.tl.types import MessageMediaPhoto
SIZE_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]
BASE_URL = "https://isubtitles.org"
from modified.Configs import Config
from modified.function.FastTelethon import upload_file
import modified.utils
import modified.function.format
import modified.function.helpers


BASE_URL = "https://isubtitles.org"
sedpath = Config.TEMP_DOWNLOAD_DIRECTORY
tempath = Config.TRASH_DOWNLOAD_DIRECTORY

logger = logging.getLogger("[--WARNING--]")




async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


async def get_user_from_event(event, secondgroup=None):
    if secondgroup:
        args = event.pattern_match.group(2).split(" ", 1)
    else:
        args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_delete(event, "`Pass the user's username, id or reply!`", 5)
            return None, None
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj, extra
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            return None, None
    return user_obj, extra


def media_type(message):
    if message and message.photo:
        media = "Photo"
    elif message and message.audio:
        media = "Audio"
    elif message and message.voice:
        media = "Voice"
    elif message and message.video_note:
        media = "Round Video"
    elif message and message.gif:
        media = "Gif"
    elif message and message.sticker:
        media = "Sticker"
    elif message and message.video:
        media = "Video"
    elif message and message.document:
        media = "Document"
    else:
        media = None
    return media


async def edit_or_reply(event, text, parse_mode=None, link_preview=None, file_name=None, aslink=False, linktext=None, caption=None,
):
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096:
        parse_mode = parse_mode or "md"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        return await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
    asciich = ["*", "`", "_"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    if aslink:
        linktext = linktext or "Message was to big so pasted to bin"
        try:
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": text}
                )
                .json()
                .get("result")
                .get("key")
            )
            text = linktext + f" [here](https://nekobin.com/{key})"
        except:
            text = re.sub(r"•", ">>", text)
            kresult = requests.post(
                "https://del.dog/documents", data=text.encode("UTF-8")
            ).json()
            text = linktext + f" [here 🚪](https://del.dog/{kresult['key']})"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        return await event.edit(text, link_preview=link_preview)
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in Config.SUDO_USERS:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)


async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in Config.SUDO_USERS:
        reply_to = await event.get_reply_message()
        catevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        catevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await catevent.delete()


def get_readable_file_size(size_in_bytes: Union[int, float]) -> str:
    if size_in_bytes is None:
        return "0B"
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f"{round(size_in_bytes, 2)}{SIZE_UNITS[index]}"
    except IndexError:
        return "File too large"


def get_readable_time(secs: float) -> str:
    result = ""
    (days, remainder) = divmod(secs, 86400)
    days = int(days)
    if days != 0:
        result += f"{days}d"
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f"{hours}h"
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f"{minutes}m"
    seconds = int(seconds)
    result += f"{seconds}s"
    return result


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )



def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None, functools.partial(func, *args, **kwargs)
    )


def run_async(loop, coro):
    return asyncio.run_coroutine_threadsafe(coro, loop).result()


async def all_pro_s(Config, client2, client3, bot):
    if not Config.SUDO_USERS:
        lmao_s = []
    else:
        lmao_s = list(Config.SUDO_USERS)
    sed1 = await bot.get_me()
    lmao_s.append(sed1.id)
    if client2:
        sed2 = await client2.get_me()
        lmao_s.append(sed2.id)
    if client3:
        sed3 = await client3.get_me()
        lmao_s.append(sed3.id)
    return lmao_s



def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


async def get_all_modules(event, borg, channel_id):
    await event.edit(f"Ìnstalling All Plugins from {channel_id}")
    try:
        a_plugins = await borg.get_messages(
            entity=channel_id,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        await event.edit("`Failed To Retrieve Modules. Please Check Channel Username / Id. Make Sure You Are On That Channel`")
        return
    yesm = 0
    nom = 0
    len_p = int(a_plugins.total)
    if len_p == 0:
        await event.edit("**No PLugins Found To Load !**")
        return
    await event.edit(f"**Found : {len_p} Plugins. Trying To Install**")
    for sed in a_plugins:
        try:
            downloaded_file_name = await borg.download_media(sed, "modified/modules/")
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("**Installed :** `{}`".format(os.path.basename(downloaded_file_name)
                                                              )
                                )
            else:
                nom += 1
                await event.edit("**Failed to Install [PLugin Already Found] :** `{}`".format(os.path.basename(downloaded_file_name)
                                                              )
                                )
                os.remove(downloaded_file_name)
        except:
                await event.edit("**Failed To Install :** `{}`".format(os.path.basename(downloaded_file_name)
                                                              )
                                )
                os.remove(downloaded_file_name)
                nom += 1
                pass
    yesm = len_p - nom
    return yesm, nom, len_p


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
            ((str(days) + " day(s), ") if days else "")
            + ((str(hours) + " hour(s), ") if hours else "")
            + ((str(minutes) + " minute(s), ") if minutes else "")
            + ((str(seconds) + " second(s), ") if seconds else "")
            + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


async def convert_to_image(event, borg):
    lmao = await event.get_reply_message()
    if not (
            lmao.gif
            or lmao.audio
            or lmao.voice
            or lmao.video
            or lmao.video_note
            or lmao.photo
            or lmao.sticker
            or lmao.media
    ):
        await event.edit("`Format Not Supported.`")
        return
    else:
        try:
            c_time = time.time()
            downloaded_file_name = await borg.download_media(
                lmao.media,
                sedpath,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "`Downloading...`")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(
                "Downloaded to `{}` successfully.".format(downloaded_file_name)
            )
    if not os.path.exists(downloaded_file_name):
        await event.edit("Download Unsucessfull :(")
        return
    if lmao and lmao.photo:
        lmao_final = downloaded_file_name
    elif lmao.sticker and lmao.sticker.mime_type == "application/x-tgsticker":
        rpath = downloaded_file_name
        image_name20 = os.path.join(sedpath, "SED.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {downloaded_file_name} {image_name20}"
        stdout, stderr = (await runcmd(cmd))[:2]
        os.remove(rpath)
        lmao_final = image_name20
    elif lmao.sticker and lmao.sticker.mime_type == "image/webp":
        pathofsticker2 = downloaded_file_name
        image_new_path = sedpath + "image.png"
        os.rename(pathofsticker2, image_new_path)
        if not os.path.exists(image_new_path):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        lmao_final = image_new_path
    elif lmao.audio:
        sed_p = downloaded_file_name
        hmmyes = sedpath + "stark.mp3"
        imgpath = sedpath + "starky.jpg"
        os.rename(sed_p, hmmyes)
        await runcmd(f"ffmpeg -i {hmmyes} -filter:v scale=500:500 -an {imgpath}")
        os.remove(sed_p)
        if not os.path.exists(imgpath):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        lmao_final = imgpath
    elif lmao.gif or lmao.video or lmao.video_note:
        sed_p2 = downloaded_file_name
        jpg_file = os.path.join(sedpath, "image.jpg")
        await take_screen_shot(sed_p2, 0, jpg_file)
        os.remove(sed_p2)
        if not os.path.exists(jpg_file):
            await event.edit("`Couldn't Fetch. SS`")
            return
        lmao_final = jpg_file
    await event.edit("`Almost Completed.`")
    return lmao_final


async def crop_vid(input_vid: str, final_path: str):
    media_info = MediaInfo.parse(input_vid)
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    if aspect_ratio != 1:
        crop_by = width if (height > width) else height
        os.system(f'ffmpeg -i {input_vid} -vf "crop={crop_by}:{crop_by}" {final_path}')
        os.remove(input_vid)
    else:
        os.rename(input_vid, final_path)



async def take_screen_shot(video_file: str, duration: int, path: str = "") -> Optional[str]:
    """ take a screenshot """
    logger.info(
        "[[[Extracting a frame from %s ||| Video duration => %s]]]",
        video_file,
        duration,
    )
    ttl = duration // 2
    thumb_image_path = path or os.path.join(sedpath, f"{basename(video_file)}.jpg")
    command = f'''ffmpeg -ss {ttl} -i "{video_file}" -vframes 1 "{thumb_image_path}"'''
    err = (await runcmd(command))[1]
    if err:
        logger.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


async def get_imdb_id(search, event):
    link = "https://yts-subs.com/search/ajax?mov=" + search
    lol = requests.get(link)
    warner_bros = lol.json()
    if warner_bros == []:
        await event.edit("`No Results Found.`")
        warner_media = None
        warner_s = None
    else:
        warner_media = warner_bros[0]["mv_mainTitle"]
        warner_s = warner_bros[0]["mv_imdbCode"]
    return warner_media, warner_s


async def get_subtitles(imdb_id, borg, event):
    await event.edit("`Processing..`")
    link = f"https://yts-subs.com/movie-imdb/" + imdb_id
    movie_response = requests.get(url=link)
    subtitles = []
    soup1 = BeautifulSoup(movie_response.content, "html.parser")
    rows = soup1.find_all("tr", class_="high-rating")
    for row in rows:
        td = row.find("td", class_="flag-cell")
        lang = td.find("span", class_="sub-lang").text
        if lang == "English":
            sub_link_tag = row.find("td", class_="download-cell")
            sub_link = sub_link_tag.find("a", class_="subtitle-download").get("href")
            sub_link = f"https://yts-subs.com/{sub_link}"
            sub_name_tag = row.find("td", class_=None)
            sub_name = (
                str(sub_name_tag.find("a").text)
                    .replace("subtitle", "")
                    .replace("\n", "")
            )
            sub = (sub_name, sub_link)
            subtitles.append(sub)
    await event.edit("`Almost Done.`")
    sub_response = requests.get(url=subtitles[0]["sub_link"])
    selected_sub_name = subtitles[0]["sub_name"]
    soup2 = BeautifulSoup(sub_response.content, "html.parser")
    link = soup2.find("a", class_="btn-icon download-subtitle").get("href")
    final_response = requests.get(link, stream=True)
    await event.edit("`Downloading Now`")
    if final_response.status_code == 200:
        with open(sedpath + f"{selected_sub_name}.zip", "wb") as sfile:
            for byte in final_response.iter_content(chunk_size=128):
                sfile.write(byte)
    final_paths = sedpath + f"{selected_sub_name}.zip"
    namez = selected_sub_name
    return final_paths, namez, subtitles[0]["sub_link"]


async def apk_dl(app_name, path, event):
    await event.edit('`Searching, For Apk File. This May Take Time Depending On Your App Size`')
    res = requests.get(f"https://m.apkpure.com/search?q={app_name}")
    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.select('.dd')
    for link in result[:1]:
        s_for_name = requests.get("https://m.apkpure.com" + link.get('href'))
        sfn = BeautifulSoup(s_for_name.text, 'html.parser')
        ttl = sfn.select_one('title').text
        noneed = [' - APK Download']
        for i in noneed:
            name = ttl.replace(i, '')
            res2 = requests.get("https://m.apkpure.com" + link.get('href') + "/download?from=details")
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            result = soup2.select('.ga')
        for link in result:
            dl_link = link.get('href')
            r = requests.get(dl_link)
            with open(f"{path}/{name}.apk", 'wb') as f:
                f.write(r.content)
    await event.edit('`Apk, Downloaded. Let me Upload It here.`')
    final_path = f'{path}/{name}.apk'
    return final_path, name


async def check_if_subbed(channel_id, event, bot):
    try:
            result = await bot(
                functions.channels.GetParticipantRequest(
                    channel=channel_id, user_id=event.sender_id
                )
            )
            if result.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False


async def _ytdl(url, is_it, event, tgbot):
    await event.edit("`Ok Downloading This Video / Audio - Please Wait.` \n**Powered By Modifiedbot**")
    if is_it:
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
    else:
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
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except Exception as e:
        await event.edit(f"**Failed To Download** \n**Error ➬ ** `{str(e)}`")
        return
    c_time = time.time()
    if song:
        await event.edit(
            f"**Uploading Audio**\
        \n**Title ➬ ** `{ytdl_data['title']}`\
        \n**Video Uploader ➬ ** `{ytdl_data['uploader']}`"
        )
        lol_m = await tgbot.upload_file(
            file=f"{ytdl_data['id']}.mp3",
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "**Uploading Audio To TG**", f"{ytdl_data['title']}.mp3"
                )
            ),
        )
        await event.edit(
            file=lol_m,
            text=f"{ytdl_data['title']} \n**Uploaded Using @Modifiedbot**"
        )
        os.remove(f"{ytdl_data['id']}.mp3")
    elif video:
        await event.edit(
            f"**Uploading Video**\
        \n**Title ➬ ** `{ytdl_data['title']}`\
        \n**Video Uploader ➬ ** `{ytdl_data['uploader']}`"
        )
        hmmo = await tgbot.upload_file(
            file=f"{ytdl_data['id']}.mp4",
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "**Uploading Video To TG**", f"{ytdl_data['title']}.mp4"
                )
            ),
        )
        await event.edit(
            file=hmmo,
            text=f"{ytdl_data['title']} \n**Uploaded Using @Modifiedbot**"
        )
        os.remove(f"{ytdl_data['id']}.mp4")



async def _deezer_dl(word, event, tgbot):
    await event.edit("`Ok Downloading This Audio - Please Wait.` ")
    urlp = f"https://starkapi.herokuapp.com/deezer/{word}"
    datto = requests.get(url=urlp).json()
    mus = datto.get("url")
    mello = datto.get("artist")
    #thums = urlhp["album"]["cover_medium"]
    sname = f'''{datto.get("title")}.mp3'''
    doc = requests.get(mus)
    with open(sname, 'wb') as f:
      f.write(doc.content)
    car = f"""
**Song Name :** {datto.get("title")}
**Duration :** {datto.get('duration')} Seconds
**Artist :** {mello}

Music Downloaded And Uploaded By Modified Userbot

Get Your Modified From @GbeshMod"""
    await event.edit("Song Downloaded.  Waiting To Upload. 🥳🤗")
    c_time = time.time()
    uploaded_file = await upload_file(
        	file_name=sname,
            client=tgbot,
            file=open(sname, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading..", sname
                )
            ),
        )
    
    await event.edit(
            file=uploaded_file,
            text=car
    )
    os.remove(sname)


async def get_all_admin_chats(event):
    lul_stark = []
    all_chats = [
        d.entity
            for d in await event.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
    for i in all_chats:
        if i.creator or i.admin_rights:
            lul_stark.append(i.id)
    return lul_stark


async def is_admin(event, user):
    sed = await event.client.get_permissions(event.chat_id, user)
    if sed.is_admin:
        is_mod = True
    else:
        is_mod = False
    return is_mod


def tgs_to_gif(sticker_path: str, quality: int = 256) -> str:                  
    dest = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "animation.gif")
    with open(dest, 'wb') as t_g:
        lottie.exporters.gif.export_gif(lottie.parsers.tgs.parse_tgs(sticker_path), t_g, quality, 1)
    os.remove(sticker_path)
    return dest


async def fetch_audio(event, ws):
    if not event.reply_to_msg_id:
        await event.edit("`Reply To A Video / Audio.`")
        return
    warner_stark = await event.get_reply_message()    
    if not warner_stark.audio or warner_stark.video:
        await event.reply("`Format Not Supported`")
        return
    if warner_stark.video:
        await event.edit("`Video Detected, Converting To Audio !`")
        warner = await ws.download_media(warner_stark.media)
        warner_bros = "Modified.mp4"
        os.rename(warner, warner_bros)
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a Modified.mp3"
        stdout, stderr = (await runcmd(cmd))[:2]
        os.remove(warner)
        final_warner = "Modified.mp3"
    elif warner_stark.audio:
        warner = await ws.download_media(warner_stark.media)
        final_warner = "Modified.mp3"
        os.rename(warner, final_warner)
        try:
           os.remove(warner)
        except:
           pass
    await event.edit("`Almost Done!`")    
    return final_warner

def save_img(inp , img , i, directory):
    try:
        filename = inp + str(i) + '.jpg'
        response = requests.get(img,stream=True)
        image_path = os.path.join(directory, filename)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    except Exception:
        pass


def find_urls(inp,url,driver, directory):
    driver.get(url)
    for j, imgurl in enumerate(driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')):
        try:
            imgurl.click()
            img = driver.find_element_by_xpath('//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            save_img(inp,img,j, directory)
            time.sleep(1.5)
        except:
            pass



