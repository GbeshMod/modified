import asyncio
import base64
import os
import random
import shutil
import time
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from . import AUTONAME, DEFAULT_BIO

DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else " ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ  "
CHANGE_TIME = 60
DEL_TIME_OUT = 60
DEFAULTUSER = str(AUTONAME) if AUTONAME else "Modified"

FONT_FILE_TO_USE = "./modified/tools/fonts/DroidSansMono.ttf"
global AUTOPICSTART
global DIGITALPICSTART
global BLOOMSTART
global AUTONAMESTART
global AUTOBIOSTART

BLOOMSTART = False
AUTOPICSTART = False
AUTOBIOSTART = False
AUTONAMESTART = False
DIGITALPICSTART = False


@bot.on(admin_cmd(pattern="autopic ?(.*)"))
async def autopic(event):
    if event.fwd_from:
        return
    global AUTOPICSTART
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(
        Config.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False
    )
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    input_str = event.pattern_match.group(1)
    if input_str:
        try:
            input_str = -int(input_str)
        except ValueError:
            input_str = -60
    else:
        input_str = 0
    if AUTOPICSTART:
        return await edit_delete(event, f"`Autopic is already enabled`")
    else:
        AUTOPICSTART = True
    counter = input_str
    await edit_delete(event, f"`Autopic has been started by my Master`")
    while AUTOPICSTART:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("  Time: %H:%M \n  Date: %d.%m.%y ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((150, 250), current_time, font=fnt, fill=(124, 252, 0))
        img.save(photo)
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            counter -= input_str
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return


@bot.on(admin_cmd(pattern="digitalpfp$"))
async def main(event):
    if event.fwd_from:
        return
    global DIGITALPICSTART
    poto = "userbot/poto_pfp.png"
    cat = str(
        base64.b64decode(
            "aHR0cHM6Ly90ZWxlZ3JhLnBoL2ZpbGUvYWVhZWJlMzNiMWYzOTg4YTBiNjkwLmpwZw=="
        )
    )[2:51]
    downloaded_file_name = "userbot/digital_pic.png"
    downloader = SmartDL(cat, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    if DIGITALPICSTART:
        return await edit_delete(event, f"`Digitalpfp is already enabled`")
    else:
        DIGITALPICSTART = True
    await edit_delete(event, f"`digitalpfp has been started by my Master`")
    while DIGITALPICSTART:
        shutil.copy(downloaded_file_name, poto)
        Image.open(poto)
        current_time = datetime.now().strftime("%H:%M")
        img = Image.open(poto)
        drawn_text = ImageDraw.Draw(img)
        cat = str(base64.b64decode("dXNlcmJvdC9oZWxwZXJzL3N0eWxlcy9kaWdpdGFsLnR0Zg=="))[
            2:36
        ]
        fnt = ImageFont.truetype(cat, 200)
        drawn_text.text((350, 100), current_time, font=fnt, fill=(124, 252, 0))
        img.save(poto)
        file = await event.client.upload_file(poto)
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.remove(poto)
        await asyncio.sleep(CHANGE_TIME)


@bot.on(admin_cmd(pattern="bloom$"))
async def autopic(event):
    if event.fwd_from:
        return
    global BLOOMSTART
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(
        Config.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=True
    )
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    if BLOOMSTART:
        return await edit_delete(event, f"`Bloom is already enabled`")
    else:
        BLOOMSTART = True
    await edit_delete(
        event, "`Bloom colour profile pic have been enabled by my master`"
    )
    while BLOOMSTART:
        # RIP Danger zone Here no editing here plox
        R = random.randint(0, 256)
        B = random.randint(0, 256)
        G = random.randint(0, 256)
        FR = 256 - R
        FB = 256 - B
        FG = 256 - G
        shutil.copy(downloaded_file_name, photo)
        image = Image.open(photo)
        image.paste((R, G, B), [0, 0, image.size[0], image.size[1]])
        image.save(photo)
        current_time = datetime.now().strftime("\n Time: %H:%M:%S \n \n Date: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(FR, FG, FB))
        drawn_text.text((95, 250), "      😈", font=ofnt, fill=(FR, FG, FB))
        img.save(photo)
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return


@bot.on(admin_cmd(pattern="autoname$"))
async def _(event):
    if event.fwd_from:
        return
    global AUTONAMESTART
    if AUTONAMESTART:
        return await edit_delete(event, f"`Autoname is already enabled`")
    else:
        AUTONAMESTART = True
    await edit_delete(event, "`Auto Name has been started by my Master `")
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚️ {HM}||›  {DEFAULTUSER} ‹||📅 {DM}"
        logger.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)


@bot.on(admin_cmd(pattern="autobio$"))
async def _(event):
    global AUTOBIOSTART
    if event.fwd_from:
        return
    if AUTOBIOSTART:
        return await edit_delete(event, f"`Autobio is already enabled`")
    else:
        AUTOBIOSTART = True
    await edit_delete(event, "`Autobio has been started by my Master`")
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DEFAULTUSERBIO} | ⌚️ {HM}"
        logger.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)


@bot.on(admin_cmd(pattern="end (.*)"))
async def _(event):
    if event.fwd_from:
        return
    global AUTOPICSTART
    global DIGITALPICSTART
    global BLOOMSTART
    global AUTONAMESTART
    global AUTOBIOSTART
    input_str = event.pattern_match.group(1)
    if input_str == "autopic":
        if AUTOPICSTART:
            AUTOPICSTART = False
            await edit_delete(event, "`Autopic has been stopped now`")
        else:
            await edit_delete(event, "`Autopic haven't enabled`")
    elif input_str == "digitalpfp":
        if DIGITALPICSTART:
            DIGITALPICSTART = False
            await edit_delete(event, "`Digital profile pic has been stopped now`")
        else:
            await edit_delete(event, "`Digital profile pic haven't enabled`")
    elif input_str == "bloom":
        if BLOOMSTART:
            BLOOMSTART = False
            await edit_delete(event, "`Bloom has been stopped now`")
        else:
            await edit_delete(event, "`Bloom haven't enabled`")
    elif input_str == "autoname":
        if AUTONAMESTART:
            AUTONAMESTART = False
            await edit_delete(event, "`Autoname has been stopped now`")
        else:
            await edit_delete(event, "`Autoname haven't enabled`")
    elif input_str == "autobio":
        if AUTOBIOSTART:
            AUTOBIOSTART = False
            await edit_delete(event, "`Autobio has been stopped now`")
        else:
            await edit_delete(event, "`Autobio haven't enabled`")
    else:
        await edit_delete(event, "`What should i end ?..`")


import asyncio

import os

import random
import re
import urllib
import requests
from telethon.tl import functions



COLLECTION_STRING1 = [
    "awesome-batman-wallpapers",
    "batman-arkham-knight-4k-wallpaper",
    "batman-hd-wallpapers-1080p",
    "the-joker-hd-wallpaper",
    "dark-knight-joker-wallpaper",
]
COLLECTION_STRING2 = [
    "thor-wallpapers",
    "thor-wallpaper",
    "thor-iphone-wallpaper",
    "thor-wallpaper-hd",
]
COLLECTION_STRING3 = [
  "indian-actress-wallpapers",
  "latest-bollywood-actress-wallpapers-2018-hd",
  "bollywood-actress-wallpaper",
  "hd-wallpapers-of-bollywood-actress",
  "new-bollywood-actress-wallpaper-2018"
]
COLLECTION_STRING4 = [
  "pokemon-serena-wallpaper",
  "anime-girls-wallpapers",
  "sexy-anime-gilr-wallpaper",
  "cute-anime-girl-3d-wallpaper-2018",
  "ash-serena-love-wallpaper",
  "anime-girls-wallpapers"
]
COLLECTION_STRING5 = [
  "avengers-logo-wallpaper",
  "avengers-hd-wallpapers-1080p",
  "avengers-iphone-wallpaper",
  "iron-man-wallpaper-1920x1080",
  "iron-man-wallpapers"
]
COLLECTION_STRING6 = [
  "star-wars-wallpaper-1080p",
  "4k-sci-fi-wallpaper",
  "star-wars-iphone-6-wallpaper",
  "kylo-ren-wallpaper",
  "darth-vader-wallpaper"
]
COLLECTION_STRING7 = [
  "hacker-background"
]
COLLECTION_STRING8 = [
  "1920x1080-space-wallpapers",
  "4k-space-wallpaper",
  "cool-space-wallpapers-hd",
]
COLLECTION_STRING9 = [
  "Epic-Space-Wallpaper",
   "Acoustic-Guitar-Wallpaper-HD",
   "Taylor-Guitar-Wallpaper",
   "Classical-Music-Wallpapers-for-Desktop",
   "Prs-Guitar-Wallpaper",
   "Iron-Man-Wallpaper-1920x1080",
   "Dodge-Challenger-Black-Hellcat-Wallpaper",
   "V-for-Vendetta-Mask-Wallpaper",
   "Toxic-Mask-Wallpapers",
   "Minion-Desktop-Wallpaper",
   "Epic-1080p-Wallpapers",
   "Japanese-Desktop-Wallpaper",
   "Cool-Gold-Cars-Wallpapers",
   "Pretty-Wallpapers-for-iPhone-Quotes",
   "dark-abstract-wallpaper",
   "abstract-dark-wallpaper",
   "abstract-wallpapers-and-screensavers",
   "roaring-lion-wallpaper",
   "wolves-screensavers-and-wallpaper",
   "cool-wallpaper-for-men",
   "Epic-1080p-Wallpapers",
   "hacker-background",
   "Vietnam-War-Wallpapers",
   "War-of-the-Worlds-Wallpaper",
   "War-Plane-Wallpaper",
   "World-War-Ii-Wallpaper",
   "Cool-War-Wallpapers",
   "World-War-2-Wallpaper-HD"
  ]
async def animeppbat():
    rnd = random.randint(0, len(COLLECTION_STRING1) - 1)
    pack = COLLECTION_STRING1[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppthor():
    rnd = random.randint(0, len(COLLECTION_STRING2) - 1)
    pack = COLLECTION_STRING2[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppactress():
    rnd = random.randint(0, len(COLLECTION_STRING3) - 1)
    pack = COLLECTION_STRING3[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animepppoke():
    rnd = random.randint(0, len(COLLECTION_STRING4) - 1)
    pack = COLLECTION_STRING4[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppaven():
    rnd = random.randint(0, len(COLLECTION_STRING5) - 1)
    pack = COLLECTION_STRING5[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppgame():
    rnd = random.randint(0, len(COLLECTION_STRING6) - 1)
    pack = COLLECTION_STRING6[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animepphack():
    rnd = random.randint(0, len(COLLECTION_STRING7) - 1)
    pack = COLLECTION_STRING7[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppspace():
    rnd = random.randint(0, len(COLLECTION_STRING8) - 1)
    pack = COLLECTION_STRING8[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppwall():
    rnd = random.randint(0, len(COLLECTION_STRING9) - 1)
    pack = COLLECTION_STRING9[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

@bot.on(admin_cmd(pattern="batmandp$"))
async def main(event):
    await event.edit("Actibated Batman Dp\nEnjoy 💜") 
    while True:
        await animeppbat()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs


@bot.on(admin_cmd(pattern="thordp$"))
async def main(event):
    await event.edit("Activated Thor Dp\nEnjoy 💜") 
    while True:
        await animeppthor()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs

@bot.on(admin_cmd(pattern="actressdp$"))
async def main(event):
    await event.edit("Activated Actress Dp\nEnjoy 💜")
    while True:
        await animeppactress()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="animedp$"))
async def main(event):
    await event.edit("Activated Anime Dp\nEnjoy 💜")
    while True:
        await animepppoke()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="avengersdp$"))
async def main(event):
    await event.edit("Activated Avengers Dp\nEnjoy 💜")
    while True:
        await animeppaven()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="gamerdp$"))
async def main(event):
    await event.edit("Activated Gamers Dp\nEnjoy 💜")
    while True:
        await animeppgame()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="hackerdp$"))
async def main(event):
    await event.edit("Activated Hackers Dp\nEnjoy 💜")
    while True:
        await animepphack()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="spacedp$"))
async def main(event):
    await event.edit("Activated Space Dp\nEnjoy 💜")
    while True:
        await animeppspace()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="wallpapers$"))
async def main(event):
    await event.edit("Activated Wallappers on your DP\nEnjoy 💜")
    while True:
        await animeppwall()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) 
 





CMD_HELP.update(
    {
        "autoprofile": """**`autoprofile`**
🏌try .help autodp

  •  **Syntax : **`.autopic angle`
  •  **Function : **__Rotating image along with the time on it with given angle if no angle is given then doesnt rotate. You need to set __`DOWNLOAD_PFP_URL_CLOCK`__ in heroku__

  •  **Syntax : **`.digitalpfp`
  •  **Function : **__Your profile pic changes to digitaltime profile picutre__

  •  **Syntax : **`.bloom`
  •  **Function : **__Random colour profile pics will be set along with time on it. You need to set__ `DOWNLOAD_PFP_URL_CLOCK`__ in heroku__

  •  **Syntax : **`.autoname`
  •  **Function : **__for time along with name, you must set __`AUTONAME`__ in the heroku vars first for this to work__

  •  **Syntax : **`.autobio`
  •  **Function : **__for time along with your bio, Set __`DEFAULT_BIO`__ in the heroku vars first__

  •  **Syntax : **`.end function`
  •  **Function : **__To stop the given functions like autopic ,difitalpfp , bloom , autoname and autobio__

**⚠️DISCLAIMER⚠️**
__USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN. WE ARE NOT RESPONSIBLE FOR YOUR BAN.__
"""
    }
)


CMD_HELP.update(
    {
        "autodp": """`auto dp`
    
**Commands found in auto_dp are **
  •  `.batmandp`
  •  `.thordp`
  •  `.actressdp`
  •  `.animedp`
  •  `.avengersdp`
  •  `.gamerdp`
  •  `.hackerdp`
  •  `.spacedp`
  •  `.wallpapers`
**Function : **__Changes your profile pic every 10 minutes with the command you used(mean the batman or thor or blah blah blah......)__"""
    }
)
