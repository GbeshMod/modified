import os


from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if not ENV:
    from local_config import Development as Config
elif ENV:
    class Config(object):
        LOGGER = True
        APP_ID = int(os.environ.get("APP_ID", 6))
        API_HASH = os.environ.get("API_HASH", None)
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        DB_URI = os.environ.get("DATABASE_URL", None)
        TRASH_DOWNLOAD_DIRECTORY = os.environ.get(
            "TRASH_DOWNLOAD_DIRECTORY", "./trash/"
        )
        TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", './download/')
        TEMP_DIR = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
        LOGGER = True
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        # Here for later purposes
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
        LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
        TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
        # Send .get_id in any channel to fill this value.
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
        PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", -100))
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
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
        PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", None))
        NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
        SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
        ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
        WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())
        ALIVE_TEXT = os.environ.get("ALIVE_TEXT", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        STRING_SESSIONS = os.environ.get("STRING_SESSIONS", None)
        VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
        GPLINKS_API_KEY = os.environ.get("GPLINKS_API_KEY", None)
        SUPERHERO_API_KEY = os.environ.get("SUPERHERO_API_KEY", None)
        FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY", None)
        WOLFRAM_API = os.environ.get("WOLFRAM_API", None)
        USR_TOKEN_UPTOBOX = os.environ.get("USR_TOKEN_UPTOBOX", None)
        HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        SUB_TO_MSG_ASSISTANT = os.environ.get("SUB_TO_MSG_ASSISTANT", False)
        AUTO_SPELL_FIX = os.environ.get("AUTO_SPELL_FIX", False)
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        COUNTRY = str(os.environ.get("COUNTRY", ""))
        LOCATION = os.environ.get("LOCATION", None)
        DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
        WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", None)
        WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
        WEATHER_DEFLANG = os.environ.get("WEATHER_DEFLANG", "EN")
        TZ = os.environ.get("TZ", None)
        TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
        TIME_API_KEY = os.environ.get("TIME_API_KEY", None)

        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Modified")
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        DEEP_API_KEY = os.environ.get("DEEP_API_KEY", None)
        CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
        WALL_API = os.environ.get("WALL_API", None)
        DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
        NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS_TOKEN", None)
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        PRIVATE_GROUP_BOT_API_ID = int(
            os.environ.get("PRIVATE_GROUP_BOT_API_ID", False)
        )
        DISABLE_MARKDOWN = os.environ.get("DISABLE_MARKDOWN", False)
        LOAD_OTHER_PLUGINS = os.environ.get("LOAD_OTHER_PLUGINS", False)
        LOAD_OTHER_PLUGINS_CHNNL = os.environ.get("LOAD_OTHER_PLUGINS_CHNNL", "@deadplugins")
        MAX_MESSAGE_SIZE_LIMIT = 4095
        UB_BLACK_LIST_CHAT = set(
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        )
        MAX_ANTI_FLOOD_MESSAGES = 10
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
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
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
        TESSDATA_PREFIX = os.environ.get(
            "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
        )
        GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/usr/bin/google-chrome"
        )
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TRASH_DOWNLOAD_DIRECTORY)
            t_file = open(TRASH_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
        G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
        G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
        if G_PHOTOS_AUTH_TOKEN_ID:
          G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        MONGO_URI = os.environ.get("MONGO_URI", None)
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
        NO_OF_BUTTONS_DISPLAY_IN_CMD = int(os.environ.get("NO_OF_BUTTONS_DISPLAY_IN_CMD", 10))

        NO_OF_COLUMS_DISPLAY_IN_CMD = int(os.environ.get("NO_OF_COLUMS_DISPLAY_IN_CMD", 2))

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

