from var import Var
from modified.Configs import Config
from modified.utils import modified_cmd
from modified.utils import admin_cmd, mod_version


simpmusic = simpdef.simpmusic 
simpmusicvideo = simpdef.simpmusicvideo
idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
BOT_N_N = Config.BOT_NICK_NAME
currentversion = mod_version


if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"🛠 SHOWING {BOT_N_N} STATS 🛠 \n"
    f"VERSION ➠ {currentversion} \n"
    f"DATABASE ➠  {dbstats} \n"
    f"SUDO ➠ {amiusingsudo} \n"
    f"LOG-CHAT  ➠ {logchat} \n"
    f"HEROKU  ➠ {riplife} \n"
    f"G-DRIVE  ➠ {wearenoob}"
)
