import os
import sys
import wget
import time
import pylast
import asyncio
import logging
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from distutils.util import strtobool as sb
from telethon.tl.types import ChatBannedRights

if os.path.exists('local.env'):
    load_dotenv('local.env')
    
class Config(object):
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    STRING_SESSION_2 = os.environ.get("STRING_SESSION_2", None)
    STRING_SESSION_3 = os.environ.get("STRING_SESSION_3", None)
    LANG = os.environ.get("LANG", "en")
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    DB_URI = os.environ.get("DATABASE_URL", None)
    TRASH_DOWNLOAD_DIRECTORY = os.environ.get("TRASH_DOWNLOAD_DIRECTORY", './trash/')
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", './download/')
    TEMP_DIR = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
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
    WOLFRAM_ID = os.environ.get("WOLFRAM_ID", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)
    TZ = os.environ.get("TZ", None)
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    WHITE_CHAT = PRIVATE_GROUP_ID = int(os.environ.get("WHITE_CHAT", False))
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
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
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    CLEAN_GROUPS = os.environ.get("CLEAN_GROUPS", False)
    ENABLE_HAREM = os.environ.get("ENABLE_HAREM", False)
    DB_URI = os.environ.get("DATABASE_URL", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    PING_SERVERS = bool(os.environ.get("PING_SERVERS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    t_file.write(AUTH_TOKEN_DATA)
    t_file.close()
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())
    LOCATION = os.environ.get("LOCATION", None)
    ALIVE_TEXT = os.environ.get("ALIVE_TEXT", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
    GPLINKS_API_KEY = os.environ.get("GPLINKS_API_KEY", None)
    NSFW_FILTER_PM = os.environ.get("NSFW_FILTER_PM", True)
    SUPERHERO_API_KEY = os.environ.get("SUPERHERO_API_KEY", None)
    FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY", None)
    SUB_TO_MSG_ASSISTANT = os.environ.get("SUB_TO_MSG_ASSISTANT", False)
    AUTO_SPELL_FIX = os.environ.get("AUTO_SPELL_FIX", False)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
    "SCREEN_SHOT_LAYER_ACCESS_KEY", None
    )
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Modified")
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    DEEP_API_KEY = os.environ.get("DEEP_API_KEY", None)
    PING_SERVER_EVERY_MINUTE_VALUE = int(os.environ.get("PING_SERVER_EVERY_MINUTE_VALUE", 30))
    DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
    NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS_TOKEN", None)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    PRIVATE_GROUP_BOT_API_ID = int(
    os.environ.get("PRIVATE_GROUP_BOT_API_ID", False)
    )
    DISABLE_MARKDOWN = os.environ.get("DISABLE_MARKDOWN", False)
    # Load Spammy Plugins, Which can be harmful.
    LOAD_OTHER_PLUGINS = os.environ.get("LOAD_OTHER_PLUGINS", False)
    LOAD_OTHER_PLUGINS_CHNNL = os.environ.get("LOAD_OTHER_PLUGINS_CHNNL", "@deadplugins")
    UB_BLACK_LIST_CHAT = set(
    int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
    MAX_ANTI_FLOOD_MESSAGES = 10
    MAX_MESSAGE_SIZE_LIMIT = 4095
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_messages=True
    )
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
    # define "spam" in PMs
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
    PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    DB_URI = os.environ.get("DATABASE_URL", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", "\.")
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    WHITELIST_USERS = set(
    int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
    )
    BLACKLIST_USERS = set(
    int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()
    )
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    # Very Stream
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
    "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    # Google Chrome Stuff
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN", "/usr/bin/google-chrome"
    )
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
    os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
    t_file.write(AUTH_TOKEN_DATA)
    t_file.close()
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    # MongoDB
    MONGO_URI = os.environ.get("MONGO_URI", None)
    # Lydia API
    LYDIA_API = os.environ.get("LYDIA_API", None)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", False))
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", False))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", False))
    JTM_CHANNEL_ID = int(os.environ.get("JTM_CHANNEL_ID", False))
    JTM_CHANNEL_USERNAME = os.environ.get("JTM_CHANNEL_USERNAME", None)
    FBAN_GROUP = int(os.environ.get("FBAN_GROUP", False))
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    TAG_FEATURE = os.environ.get("TAG_FEATURE", "DISABLE")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ASSISTANT_LOG = bool(os.environ.get("ASSISTANT_LOG", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/GbeshMod/modified"
      )
    ALIVE_IMAGE = os.environ.get(
        "ALIVE_IMAGE", "https://telegra.ph/file/24f412762232e8656177a.jpg"
      )
    ASSISTANT_IMG = os.environ.get(
        "ASSISTANT_IMG", "https://telegra.ph/file/66b907a1ccd4ca09f6177.jpg"
      )
    CUSTOM_ALIVE_TEXT = os.environ.get(
        "ALIVE_TEXT", "✮ MY BOT IS RUNNING SUCCESSFULLY ✮"
      )
    CUSTOM_ALIVE_EMOJI = os.environ.get(
      "CUSTOM_ALIVE_EMOJI", "➲"
      )
    NO_OF_BUTTONS_DISPLAY_IN_CMD = int(os.environ.get("NO_OF_BUTTONS_DISPLAY_IN_CMD", "10"))

    NO_OF_COLUMS_DISPLAY_IN_CMD = int(os.environ.get("NO_OF_COLUMS_DISPLAY_IN_CMD", "2"))

    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "⚝")
    BOT_NICK_NAME = os.environ.get("BOT_NICK_NAME")

else:
    if os.path.exists("config.py"):
        from config import Development as Config
        
        # REQUIRED
        TOKEN = TG_BOT_TOKEN
        BOT_TOKEN = TG_BOT_TOKEN
        TG_BOT_TOKEN_BF_HER = TG_BOT_TOKEN
        
        BOT_USERNAME = TG_BOT_USERNAME
        TG_BOT_USER_NAME_BF_HER = TG_BOT_USERNAME
        
        TG_API_ID = APP_ID
        TG_API_HASH = API_HASH
        
        BOT_N_N = BOT_NICK_NAME
        botnickname = BOT_NICK_NAME
        TELEGRAPH_SHORT_NAME = BOT_NICK_NAME
        
        USR_TOKEN = USR_TOKEN_UPTOBOX
        TIMEZONE = TZ
        OWNER_NAME = ALIVE_NAME8
        
        ALIVE_PIC = ALIVE_IMAGE
        ALIVE_LOGO = ALIVE_IMAGE
        ALIVE_PHOTO = ALIVE_IMAGE
        ALIVE_PHOTTO = ALIVE_IMAGE
        
        ASSISTANT_LOGO = ASSISTANT_IMG
        ASSISTANT_START_PIC = ASSISTANT_IMG
        
        PM_PERMIT_GROUP_ID = PRIVATE_GROUP_ID
        CUSTOM_PMPERMIT_TEXT = CUSTOM_PMPERMIT
        PRIVATE_GROUP_BOT_API_ID = PM_LOGGR_BOT_API_ID
        
        TEMP_DIR = TEMP_DOWNLOAD_DIRECTORY
        TMP_DOWNLOAD_DIRECTORY = TRASH_DOWNLOAD_DIRECTORY
        
        LYDIA_API = LYDIA_API_KEY
        AI_API_KEY = LYDIA_API_KEY
        
        ALIVE_TEXT = CUSTOM_ALIVE_TEXT