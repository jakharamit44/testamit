import os

from dotenv import load_dotenv

load_dotenv()

def is_enabled(value, default):

    if value.lower() in ["true", "yes", "1", "enable", "y"]:

        return True

    elif value.lower() in ["false", "no", "0", "disable", "n"]:

        return False

    else:

        return default

class Config(object):

    API_ID = int(os.environ.get("API_ID", "17737898"))

    API_HASH = os.environ.get("API_HASH", "ad762fe0516f367115ba651d929cf429)

    BOT_TOKEN = os.environ.get(

        "BOT_TOKEN", "bot token")

    OWNER_ID = int(os.environ.get("OWNER_ID", "owener id"))

    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)

    CHAT_ID = [int(x) for x in os.environ.get(

        "CHAT_ID", "Chat id").split()]

    SESSION_STRING = os.environ.get("SESSION_STRING", "string account")

    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://baba:baba@cluster0.etssakc.mongodb.net/?retryWrites=true&w=majority")

    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "telegram")

class Script(object):

    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message I'm Auto Request Accept Bot")

    ACCEPT_MESSAGE = os.environ.get(

        "ACCEPT_MESSAGE", "You have been accepted to the channel. By @")
