import asyncio
import importlib
from pyrogram import idle
from Grabber.modules import ALL_MODULES
from Grabber.core.mongo import init_mongo  # ✅ MongoDB import
import logging

# --------------------------- LOGGING --------------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

loop = asyncio.get_event_loop()

async def sumit_boot():
    # ✅ CONNECT TO MONGODB FIRST
    LOGGER.info("🔄 Connecting to MongoDB...")
    if not await init_mongo():
        LOGGER.error("❌ MongoDB connection failed! Bot will not work properly.")
        return
    
    LOGGER.info("✅ MongoDB connected successfully!")
    
    # ✅ LOAD ALL MODULES
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Grabber.modules." + all_module)
            LOGGER.info(f"✅ Loaded module: {all_module}")
        except Exception as e:
            LOGGER.error(f"❌ Failed to load module {all_module}: {e}")
    
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
