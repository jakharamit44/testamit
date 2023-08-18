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

    API_HASH = os.environ.get("API_HASH", "ad762fe0516f367115ba651d929cf429")

    BOT_TOKEN = os.environ.get(

        "BOT_TOKEN", "6511699844:AAFEF1kACN7F9aaIB7HiuJ6ETk9LceXji30")

    OWNER_ID = int(os.environ.get("OWNER_ID", "5702180952"))

    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)

    CHAT_ID = [int(x) for x in os.environ.get(

        "CHAT_ID", "-1001587677801").split()]

    SESSION_STRING = os.environ.get("SESSION_STRING", "BQEOqKoAD9v3tANx-2GzCt0dGrXzOxtcc4eml2ecbFfcGtCu7r_WKkkUn4nwJXqG0aKalXSHnHoxQSBL0y3WBkk78pOKoBbe80x156Js7KIAAdl6yB0OMyRVj-2R-x8ZUkQvFCtCXolWV_AOvvgKG6NV7fwo23_OAONRBhSWkiRZzyVHBSMlmN79aFkVKxOC054sFZYuTVB90Z4jfy4mYBhU9kS2Av5bjvrHXH0b8OtwTClGgUE96dPQGSMWOf0ok73pq62l1_VYy9J5NzKNj5FygyX4Np46zG2kIbfE_RQ-cEmNY7K01jLHUH_ZiUzU7mAh7oZteKfogXLjmHoQ1txp5a8rgQAAAAFT4GBYAA")

    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://baba:baba@cluster0.etssakc.mongodb.net/?retryWrites=true&w=majority")

    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "telegram")

class Script(object):

    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message I'm Auto Request Accept Bot")

    ACCEPT_MESSAGE = os.environ.get(

        "ACCEPT_MESSAGE", "Your request to join channel has been approved!/n/n Send /start to know more")
