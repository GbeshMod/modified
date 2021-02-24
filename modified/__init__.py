import os
import sys
import time
import wget
import pylast
import logging
import asyncio
from requests import get
from .Configs import Config
from pySmartDL import SmartDL
from dotenv import load_dotenv
from modified.Configs import Config
from telethon import TelegramClient
from pylast import LastFMNetwork, md5
from nospamplus.connect import Connect
from distutils.util import strtobool as sb
from telethon.sessions import StringSession
from logging import DEBUG, INFO, basicConfig, getLogger
from telegraph import Telegraph, exceptions, upload_file


link = "https://pastebin.pl/view/raw/4724519b"
km = "local.env"
pathz = "./local.env"
if os.path.exists(km):
    pass
else:
    try:
        sedlyf = wget.download(link, out=pathz)
    except:
        sedprint.info("Not again...")

if os.path.exists('local.env'):
    load_dotenv('local.env')

StartTime = time.time()
Lastupdate = time.time()
BOT_N_N = Config.BOT_NICK_NAME
BOT_REPO = Config.UPSTREAM_REPO
mamaput = Config.TELEGRAPH_SHORT_NAME
sedprint = logging.getLogger("WARNING")
mod_version = "0.03.9"
BOTNAME = "{} v{}".format(mamaput, mod_version)
BOT_LIN = "[{}]({})".format(BOT_N_N, BOT_REPO)

link = "https://pastebin.pl/view/raw/472542fb"
km = "./.evn"
pathz = "./"
if os.path.exists(km):
    pass
else:
    try:
        sedlyf = wget.download(link, out=pathz)
    except:
        sedprint.info("Not again...")

# Clients & bot

if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Config.APP_ID, Config.API_HASH)
else:
    session_name = "Modified"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
if Config.STRING_SESSION_2:
    client2 =  TelegramClient(StringSession(Config.STRING_SESSION_2), Config.APP_ID, Config.API_HASH)
else:
    client2 = None
if Config.STRING_SESSION_3:
    client3 =  TelegramClient(StringSession(Config.STRING_SESSION_3), Config.APP_ID, Config.API_HASH)
else:
    client3 = None


basicConfig(
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
)
LOGS = getLogger(__name__)
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
DB_URI = os.environ.get("DATABASE_URL", None)
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
AUTONAME = os.environ.get("AUTONAME", None)
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
WHITE_CHAT = PRIVATE_GROUP_ID = int(os.environ.get("WHITE_CHAT", False))
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
if not LASTFM_USERNAME == "None":
    lastfm = pylast.LastFMNetwork(
    api_key=LASTFM_API,
    api_secret=LASTFM_SECRET,
    username=LASTFM_USERNAME,
    password_hash=LASTFM_PASS,
    )
else:
    lastfm = None
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./download")
TRASH_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./trash")
CMD_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
SUDO_LIST = {}
CMD_HELP = {}
CUSTOM_PMPERMIT_MSG = {}
CUSTOM_BOTSTART = {}
ISAFK = False
AFKREASON = None

# Nospam+ Client
if Config.NOSPAMPLUS_TOKEN == None:
    sclient = None
    sedprint.info("[Warning] - NoSpamPlusToken is None")
else:
    try:
        sclient = Connect(Config.NOSPAMPLUS_TOKEN)
    except Exception as e:
        sclient = None
        sedprint.info("[Warning] - " + str(e))


try:
    if not os.path.isdir(TRASH_DOWNLOAD_DIRECTORY):
        os.makedirs(TRASH_DOWNLOAD_DIRECTORY)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
except:
    pass
