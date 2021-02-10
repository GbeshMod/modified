


@bot.on(admin_cmd(pattern="scan ?(.*)"))
@bot.on(sudo_cmd(pattern="scan ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "Reply to any user message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "Reply to a media message")
        return
    chat = "@DrWebBot"
    if reply_message.sender.bot:
        await edit_or_reply(event, "Reply to actual users message.")
        return
    hellevent = await edit_or_reply(event, " `Scanning This media..... wait👀`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await hellevent.edit("`Please unblock `@DrWebBot `and try again`")
            return
        if response.text.startswith("Forward"):
            await hellevent.edit(
                "Can you kindly disable your forward privacy settings for good?"
            )
        else:
            if response.text.startswith("Select"):
                await hellevent.edit(
                    "`Please go to` @DrWebBot `and select your language.`"
                )
            else:
                await hellevent.edit(
                    f"**Antivirus scan was completed. I got the final results.**\n {response.message.message}"
                )


@bot.on(admin_cmd(pattern="xkcd ?(.*)"))
@bot.on(sudo_cmd(pattern="xkcd ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hellevent = await edit_or_reply(event, "`processiong...........`")
    input_str = event.pattern_match.group(1)
    xkcd_id = None
    if input_str:
        if input_str.isdigit():
            xkcd_id = input_str
        else:
            xkcd_search_url = "https://relevantxkcd.appspot.com/process?"
            queryresult = requests.get(
                xkcd_search_url, params={"action": "xkcd", "query": quote(input_str)}
            ).text
            xkcd_id = queryresult.split(" ")[2].lstrip("\n")
    if xkcd_id is None:
        xkcd_url = "https://xkcd.com/info.0.json"
    else:
        xkcd_url = "https://xkcd.com/{}/info.0.json".format(xkcd_id)
    r = requests.get(xkcd_url)
    if r.ok:
        data = r.json()
        year = data.get("year")
        month = data["month"].zfill(2)
        day = data["day"].zfill(2)
        xkcd_link = "https://xkcd.com/{}".format(data.get("num"))
        safe_title = data.get("safe_title")
        data.get("transcript")
        alt = data.get("alt")
        img = data.get("img")
        data.get("title")
        output_str = """[\u2060]({})**{}**
[XKCD ]({})
Title ➼ {}
Alt ➼ {}
Day ➼ {}
Month ➼ {}
Year ➼ {}""".format(
            img, input_str, xkcd_link, safe_title, alt, day, month, year
        )
        await hellevent.edit(output_str, link_preview=True)
    else:
        await hellevent.edit("xkcd n.{} not found!".format(xkcd_id))


import re
import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from telethon.utils import get_inner_text



logger.info(Config.OPEN_LOAD_LOGIN)


@borg.on(admin_cmd(pattern="rapidl"))
async def _(event):
    if event.fwd_from:
        return
    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    reply_message = await event.get_reply_message()
    if len(cmt) > 1:
        list_of_urls = cmt[1:]
    else:
        list_of_urls = get_inner_text(
            reply_message.message, reply_message.entities)
    converted_links = ""
    if len(list_of_urls) > 0:
        converted_links += "Trying to generate IP specific link\n"
        for a_url in list_of_urls:
            converted_link_infos = await get_direct_ip_specific_link(a_url)
            if "url" in converted_link_infos:
                converted_link = converted_link_infos["url"]
                converted_links += f"[{a_url}]({converted_link}) \n\n"
            elif "err" in converted_link_infos:
                err = converted_link_infos["err"]
                converted_links += f"`{a_url}` returned `{err}`\n\n"
    await event.reply(converted_links)


async def get_direct_ip_specific_link(link: str):
    # https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/openload.py#L246-L255
    OPEN_LOAD_DOMAINS = r"(?:openload\.(?:co|io|link|pw)|oload\.(?:tv|biz|stream|site|xyz|win|download|cloud|cc|icu|fun|club|info|press|pw|life|live|space|services|website)|oladblock\.(?:services|xyz|me)|openloed\.co)"
    OPEN_LOAD_VALID_URL = r"(?x)https?://(?P<host>(?:www\.)?%s)/(?:f|embed)/(?P<id>[a-zA-Z0-9-_]+)" % OPEN_LOAD_DOMAINS
    # https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/openload.py#L246-L255
    # https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/googledrive.py#L16-L27
    GOOGLE_DRIVE_VALID_URLS = r"(?x)https?://(?:(?:docs|drive)\.google\.com/(?:(?:uc|open)\?.*?id=|file/d/)|video\.google\.com/get_player\?.*?docid=)(?P<id>[a-zA-Z0-9_-]{28,})"
    # https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/googledrive.py#L16-L27
    dl_url = None
    if "zippyshare.com" in link:
        async with aiohttp.ClientSession() as session:
            http_response = await session.get(link)
            http_response_text = await http_response.text()
            response_b_soup = BeautifulSoup(http_response_text, "html.parser")
            scripts = response_b_soup.find_all(
                "script", {"type": "text/javascript"})
            # calculations
            # check https://github.com/LameLemon/ziggy/blob/master/ziggy.py
            for script in scripts:
                if "getElementById('dlbutton')" in script.text:
                    regex_search_exp = re.search(
                        '= (?P<url>\".+\" \+ (?P<math>\(.+\)) .+);', script.text)
                    url_raw = regex_search_exp.group("url")
                    math = regex_search_exp.group("math")
                    dl_url = url_raw.replace(math, '"' + str(eval(math)) + '"')
                    break
            #
            base_url = re.search("http.+.com", link).group()
            dl_url = {
                "url": base_url + eval(dl_url)
            }
    elif re.search(OPEN_LOAD_VALID_URL, link):
        # https://stackoverflow.com/a/47726003/4723940
        async with aiohttp.ClientSession() as session:
            openload_id = re.search(OPEN_LOAD_VALID_URL, link).group("id")
            step_one_url = "https://api.openload.co/1/file/dlticket?file={}&login={}&key={}".format(
                openload_id, Config.OPEN_LOAD_LOGIN, Config.OPEN_LOAD_KEY)
            http_response = await session.get(step_one_url)
            http_response_text = await http_response.text()
            http_response_json = json.loads(http_response_text)
            logger.info(http_response_json)
            if http_response_json["msg"] == "OK":
                # wait till wait time
                await asyncio.sleep(int(http_response_json["result"]["wait_time"]))
                # TODO: check if captcha is required
                step_two_url = "https://api.openload.co/1/file/dl?file={}&ticket={}".format(
                    openload_id, http_response_json["result"]["ticket"])
                http_response = await session.get(step_two_url)
                http_response_text = await http_response.text()
                http_response_json = json.loads(http_response_text)
                logger.info(http_response_json)
                if http_response_json["msg"] == "OK":
                    dl_file_url = http_response_json["result"]["url"]
                    dl_file_name = http_response_json["result"]["name"]
                    dl_file_size = http_response_json["result"]["size"]
                    dl_url = {
                        "url": dl_file_url,
                        "name": dl_file_name,
                        "size": dl_file_size
                    }
                else:
                    dl_url = {
                        "err": http_response_text
                    }
            else:
                dl_url = {
                    "err": http_response_text
                }
        # https://stackoverflow.com/a/47726003/4723940
    elif re.search(GOOGLE_DRIVE_VALID_URLS, link):
        file_id = re.search(GOOGLE_DRIVE_VALID_URLS, link).group("id")
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:
            step_zero_url = "https://drive.google.com/uc?export=download&id={}".format(file_id)
            http_response = await session.get(step_zero_url, allow_redirects=False)
            if "location" in http_response.headers:
                # in case of small file size, Google downloads directly
                file_url = http_response.headers["location"]
                if "accounts.google.com" in file_url:
                    dl_url = {
                        "err": "Private Google Drive URL"
                    }
                else:
                    dl_url = {
                        "url": file_url
                    }
            else:
                # in case of download warning page
                http_response_text = await http_response.text()
                response_b_soup = BeautifulSoup(http_response_text, "html.parser")
                warning_page_url = "https://drive.google.com" + response_b_soup.find("a", {"id": "uc-download-link"}).get("href")
                file_name_and_size = response_b_soup.find("span", {"class": "uc-name-size"}).text
                http_response_two = await session.get(warning_page_url, allow_redirects=False)
                if "location" in http_response_two.headers:
                    file_url = http_response_two.headers["location"]
                    if "accounts.google.com" in file_url:
                        dl_url = {
                            "err": "Private Google Drive URL"
                        }
                    else:
                        dl_url = {
                            "url": file_url,
                            "name": file_name_and_size
                        }
                else:
                    dl_url = {
                        "err": "Unsupported Google Drive URL"
                    }
    else:
        dl_url = {
            "err": "Unsupported URL"
        }
    return dl_url


import os
import random
import string
import requests
from pathlib import Path
from modified.function import fetch_audio

@modbot.on(modified_cmd(pattern="(shazam|sreverse|identify)"))
@modbot.on(sudo_cmd(pattern="(shazam|sreverse|identify)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await edit_or_reply(event, "Reply To The Audio.")
        return
    if Path("shazam.mp3").is_file():
      os.remove("shazam.mp3")
    credit = "By Modified. Get Your Modifiedbot"
    ommhg = await edit_or_reply(event, "`Downloading To Local Server.`")
    kkk = await fetch_audio(event, borg)
    downloaded_file_name = str("shazam.mp3")
    train = credit[3].lower()
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    Lop = "flutter's formula"
    loP = Lop[1]
    await ommhg.edit("**Searching For This Song In Modified's DataBase.**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files = f)
    if train == loP:
       await ommhg.edit("Server Has Been Crashed for Unknown Reasons")
    try:
      xo = r.json()
    except:
      return
    try:
      xo = r.json()
      xoo = xo.get("response")
      zz = xoo[1]
      zzz = zz.get("track")
      Col = zzz.get("sections")[3]
      nt = zzz.get("images")	
      image = nt.get("coverarthq")
      by = zzz.get("subtitle")
      title = zzz.get("title")
      message = f"""<b>Song Shazamed.</b>
<b>Song Name ➼ </b>{title}
<b>Song By ➼ </b>{by}

<u><b>Identified By Modified.
Get Your Modified From</b></u> ➻➻   {BOT_LIN}
"""
      await event.delete()
      await borg.send_message(
        event.chat_id,
        message,
        parse_mode="HTML",
        file=image,
        force_document=False,
        silent=True,
      )
      os.remove(downloaded_file_name)
    except:
      if xo.get("success") is False:
        errer = xo.get("error")
        ommhg = await edit_or_reply(event, errer)
        os.remove(downloaded_file_name)
        return
      ommhg = await edit_or_reply(event, "Song Not Found IN Database. Please Try Again.")
      os.remove(downloaded_file_name)
      return



import os
import cv2
import html
import wget
import requests
import cv2 as cv
import numpy as np
from shutil import rmtree
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file
from fridaybot.function import convert_to_image, crop_vid, runcmd, tgs_to_gif
from fridaybot.utils import modified_cmd, sudo_cmd
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
sedpath = "./image/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)



# Firstly Released By @DELETEDUSER420
@modbot.on(modified_cmd(pattern=r"nst"))
@modbot.on(sudo_cmd(pattern=r"nst", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Colourzing..")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/nsfw-detector"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedcopy = r["output"]
    hmmyes = sedcopy["detections"]
    game = sedcopy["nsfw_score"]
    final = f"**IMG RESULT** \n**Detections :** `{hmmyes}` \n**NSFW SCORE :** `{game}`"
    await borg.send_message(event.chat_id, final)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


            
@modbot.on(modified_cmd(pattern=r"tni"))
@modbot.on(sudo_cmd(pattern=r"tni", allow_sudo=True))
async def toony(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("`Converting Toonized Image..`")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    imagez = cv2.imread(img)
    cartoon_image_style_2 = cv2.stylization(
        imagez, sigma_s=60, sigma_r=0.5
    )  ## Cartoonify process.
    # Save it
    file_name = "Tooned.png"
    ok = sedpath + "/" + file_name
    cv2.imwrite(ok, cartoon_image_style_2)
    # Upload it
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    # Remove all Files
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@modbot.on(modified_cmd(pattern=r"tig"))
@modbot.on(sudo_cmd(pattern=r"tig", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Triggered This Image`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/triggered?avatar={imglink}"
    r = requests.get(lolul)
    open("triggered.gif", "wb").write(r.content)
    lolbruh = "triggered.gif"
    await borg.send_file(
        event.chat_id, lolbruh, caption="You got triggered....", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@modbot.on(modified_cmd(pattern=r"geyuser"))
@modbot.on(sudo_cmd(pattern=r"geyuser", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Meking This Guy Gey.`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/gay?avatar={imglink}"
    r = requests.get(lolul)
    open("geys.png", "wb").write(r.content)
    lolbruh = "geys.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="`You iz Gey.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
            
@modbot.on(modified_cmd(pattern=r"pix"))
@modbot.on(sudo_cmd(pattern=r"pix", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Pixing This Image.`")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/pixelate?avatar={imglink}"
    r = requests.get(lolul)
    open("Pixe.png", "wb").write(r.content)
    lolbruh = "pixe.png"
    await borg.send_file(
        event.chat_id, lolbruh, caption="`Pixeled This Image.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)

@modbot.on(modified_cmd(pattern=r"ytc"))
@modbot.on(sudo_cmd(pattern=r"ytc", allow_sudo=True))
async def lolmetrg(event):
    if event.fwd_from:
        return
    await event.edit("`Making Comment`")
    sed = await event.get_reply_message()
    hmm_s = await event.client(GetFullUserRequest(sed.sender_id))
    if not hmm_s.profile_photo:
        imglink = 'https://telegra.ph/file/b9684cda357dfbe6f5748.jpg'
    elif hmm_s.profile_photo:
        img = await borg.download_media(hmm_s.profile_photo, sedpath)
        url_s = upload_file(img)
        imglink = f"https://telegra.ph{url_s[0]}"
    first_name = html.escape(hmm_s.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    if sed.text is None:
        comment = 'Give Some Text'
    else:
        comment = sed.raw_text
    lolul = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&username={first_name}&comment={comment}"
    r = requests.get(lolul)
    open("ytc.png", "wb").write(r.content)
    lolbruh = "ytc.png"
    await event.delete()
    await borg.send_file(
        event.chat_id, lolbruh, caption="`Hmm Nice.`", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)


@modbot.on(modified_cmd(pattern=r"lg"))
@modbot.on(sudo_cmd(pattern=r"lg", allow_sudo=True))
async def lottiepie(event):
    if event.fwd_from:
        return
    await event.edit("`Prooooooccccesssssssinggggg.....`")
    message = await event.get_reply_message()
    if message.media and message.media.document:
        mime_type = message.media.document.mime_type
        if not "tgsticker" in mime_type:
            await event.edit("Not Supported Yet.")
            return
        await message.download_media("tgs.tgs")
        await runcmd("lottie_convert.py tgs.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = (
            jsn.replace("[1]", "[2]")
            .replace("[2]", "[3]")
            .replace("[3]", "[4]")
            .replace("[4]", "[5]")
            .replace("[5]", "[6]")
        )
        open("json.json", "w").write(jsn)
        await event.delete()
        await runcmd(f"lottie_convert.py json.json tgs.tgs")
        await borg.send_file(event.chat_id, file="tgs.tgs", force_document=False)
        os.remove("json.json")
        os.remove("tgs.tgs")


@modbot.on(modified_cmd(pattern="(flip|blur|tresh|hsv|lab)"))
async def warnerstark_s(event):
    if event.fwd_from:
        return
    ws = event.pattern_match.group(1)
    img = await convert_to_image(event, borg)
    image = cv2.imread(img)
    await event.edit("`Processing..`")
    if ws == "flip":
        flipped = cv2.flip(image, 0)
        file_name = "Flipped.png"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, flipped)
        warnerstark = "Hehe, Flipped"
    elif ws == "blur":
        blurred = cv2.blur(image, (8,8))
        file_name = "Blurred.png"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, blurred)
        warnerstark = "Hehe, Blurred"
    elif ws == "tresh":
        treshold, fridaydevs = cv2.threshold(image, 150, 225, cv2.THRESH_BINARY)
        file_name = "Tresh.png"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, fridaydevs)
        warnerstark = "Hehe, TreshHolded."
    elif ws == "hsv":
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        file_name = "Hsv.png"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, hsv)
        warnerstark = "Hehe, Hsv"
    elif ws == "lab":
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        file_name = "Lab.png"
        ok = sedpath + "/" + file_name
        cv2.imwrite(ok, lab)
        warnerstark = "Hehe, Lab"
    await event.delete()
    await borg.send_file(event.chat_id, file=ok, caption=warnerstark)
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)
     
@modbot.on(modified_cmd(pattern="aic$"))
async def warnerstarkgang(event):
    if event.fwd_from:
        return
    img = await convert_to_image(event, borg)
    await event.edit("`Coverting This Media To Image Now.`")
    so = "**Powered By @FridayOT**"
    await event.delete()
    await borg.send_file(event.chat_id, file=img, caption=so)
    
@modbot.on(modified_cmd(pattern="tgstogif(?: |$)(.*)"))
async def warnerstarkgangz(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Please Reply To Tgs To Convert To Gif.`")
        return
    if event.pattern_match.group(1):
        quality = event.pattern_match.group(1)
    else:
        quality = 512
    kk = await event.edit("`Processing..`")
    hmm_ws = await event.get_reply_message()
    warner_s = await modbot.download_media(hmm_ws.media)
    ok_stark = tgs_to_gif(warner_s, quality)
    so = "**Powered By Modifiedbot **"
    lol_m = await kk.edit("`Converting This Tgs To Gif Now !`")
    await lol_m.delete()
    await borg.send_file(event.chat_id, file=ok_stark, caption=so)

CMD_HELP.update(
    {
        "tools": "**Tools**\
        \n\n**Syntax : **`.scan` reply to media or file\
        \n**Function : **__it scans the media or file and checks either any virus is in the file or media__\
        \n\n**Syntax : **`.xkcd` <query>\
        \n**Function : **__Searches for the query for the relevant XKCD comic __  try  **.rapidl \
        \n\n**Syntax : **`.shazam <replying to the song>`\
        \n**Usage :** Identifies The Song .shazam|sreverse|identify\
        \n\n**Syntax : **`.cit`\
        \n**Usage :** colourizes the given picture.\
        \n\n**Syntax : **`.nst`\
        \n**Usage :** removes colours from image.\
        \n\n**Syntax : **`.tni`\
        \n**Usage :** Toonify the image.\
        \n\n**Syntax : ** `.tig`\
        \n**Usage :** Makes a triggered gif of the replied image.\
        \n\n**Syntax : ** `.geyuser .pix  .ytc  .lg .aci   .tgstogif  .(flip|blur|tresh|hsv|lab) `**"
    }
)
