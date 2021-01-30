import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "b3f161e3-6dfb-4d05-8c07-35f873a0a8d8")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1491444696:AAGA9frENUfhUZcRgPGQlHqj5_vHzHxy-Qw")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 2882240))
    API_HASH = os.environ.get("API_HASH", 9fdd5d0301d5ac2172a693d085af1a8c))
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1216142595").split())
    # Banned Unwanted Members..
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/bd3ef3778728490e16fe1.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
