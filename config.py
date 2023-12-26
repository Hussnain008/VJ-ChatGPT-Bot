import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "23381586"))
API_HASH = environ.get("API_HASH", "b2319ac63b04e8f88abe36306b60bc58")
BOT_TOKEN = environ.get("BOT_TOKEN", "6822692189:AAHydoCSkWBaswJfDR00wLYO0Z6PHQrHzbg")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002065049156"))
ADMINS = int(environ.get("ADMINS", "6510235517"))
DB_URI = environ.get("DB_URI", "mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
