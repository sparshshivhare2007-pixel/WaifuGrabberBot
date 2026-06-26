from os import getenv

API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7641508639").split()))
SUDO_IDS = list(map(int, getenv("SUDO_IDS", "7641508639").split()))
MONGO_DB = getenv("MONGO_DB", "")
GEMINI_KEY = getenv("GEMINI_KEY", "")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DevsHubChat")
