import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "7236453")
    API_HASH = environ.get("API_HASH", "33010a70e94f80e55145980072cce969")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7219591797:AAFmTbsDAWYRApdvCChnA6SDBb3bYWln7xo") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://videshi:videshi@videshi.wtffv.mongodb.net/?retryWrites=true&w=majority&appName=videshi")
    DATABASE_NAME = environ.get("DATABASE_NAME", "videshiii")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002447703798'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
