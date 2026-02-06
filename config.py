from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "16490688"))
API_HASH = getenv("API_HASH", "ad958ab159ed1125afb5fcdc3875b120")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "7252249791"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84@ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot")
MUST_JOIN = getenv("MUST_JOIN", "MUSIC_BOT_WORLD")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/520y6h.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "MUSIC_BOT_TEAM")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "MUSIC_BOT_WORLD")
