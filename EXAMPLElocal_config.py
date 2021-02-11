from modified.Configs import Config

class Development(Config):
    LOGGER = True


    API_HASH = ""
    APP_ID = 
    GITHUB_ACCESS_TOKEN = ""
    HEROKU_API_KEY = ""
    PLUGIN_CHANNEL = 
    PRIVATE_GROUP_ID = 
    STRING_SESSION = ""
    TG_BOT_TOKEN = ""
    TG_BOT_USER_NAME = ""
    
    

    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    
    # Get one from https://timezonedb.com/register
    TIME_API_KEY = ""

    # OpenWeather Map API Key for .weather command
    # Get from https://openweathermap.org/
    OPEN_WEATHER_MAP_APPID = ""
    WEATHER_DEFCITY = ""
    WEATHER_DEFLANG = ""


    # Coffeehouse chatbot api key, get one from  https://coffeehouse.intellivoid.net/
    LYDIA_API_KEY = ""

    # Get one from https://wall.alphacoders.com/api.php
    WALL_API = ""

    #Get from https://www.remove.bg/ ☚  
    REM_BG_API_KEY = ""

    # Get from https://ocr.space/ocrapi
    OCR_SPACE_API_KEY = ""

    # for google photo https://j.mp/39lWQQm
    # Google Drive Credentials 
    # Get from https://console.cloud.google.com
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""
    G_DRIVE_AUTH_TOKEN_DATA = ""
    TEMP_DOWNLOAD_DIRECTORY = ""

    # You have to have your own unique two values for API_KEY and API_SECRET
    # Obtain yours from https://www.last.fm/api/account/create for Last.fm
    LASTFM_API = ""
    LASTFM_SECRET = ""
    LASTFM_USERNAME = ""
    LASTFM_PASSWORD = ""


    # Wolfram api
    # Get an API KEY from products.wolframalpha.com/api/
    WOLFRAM_API = ""

    # Genius lyrics get this value from https://genius.com/developers both has
    # same values
    # Client Access Token from https://genius.com/api-clients
    GENIUS_CLIENT_ID = ""
    GENIUS_ACCESS_TOKEN = ""
    GENIUS_CLIENT_SECRET = ""

    # API for direct link uptobox, https://docs.uptobox.com/#how-to-find-my-api-token
    USR_TOKEN_UPTOBOX = ""
    #https://uptobox.com/affiliate?aff_id=13511425
    
    
    
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = ""
    IBM_WATSON_CRED_PASSWORD = ""

    # Deepai value can get from https://deepai.org/
    DEEP_API_KEY = ""

    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
     SCREEN_SHOT_LAYER_ACCESS_KEY = ""

    # Need to get an API key from https://rapidapi.com/api-sports/api/api-football-beta
    FOOTBALL_API_KEY = ""

    # Need to get an API key from https://gplinks.in
    GPLINKS_API_KEY = ""

    # Need to get an API key from https://virustotal.com
    VIRUSTOTAL_API_KEY = ""


# class Production(Config):
#     LOGGER = True
