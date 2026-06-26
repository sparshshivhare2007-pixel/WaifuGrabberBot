from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB
import os

# --------------------------- MongoDB Client --------------------------- #

class MongoDB:
    def __init__(self):
        self.client = None
        self.database = None
        self.waifus_db = None
        self.user_waifus = None
        self.settings_db = None
        self.is_connected = False
    
    async def connect(self):
        """Connect to MongoDB"""
        try:
            MONGO_URI = MONGO_DB if MONGO_DB else "mongodb://localhost:27017"
            
            print(f"🔄 Connecting to MongoDB Atlas...")
            
            self.client = AsyncIOMotorClient(
                MONGO_URI,
                serverSelectionTimeoutMS=30000,
                connectTimeoutMS=30000
            )
            
            # Test connection
            await self.client.admin.command('ping')
            
            self.database = self.client.waifu_grabbers
            self.waifus_db = self.database.waifus
            self.user_waifus = self.database.user_waifus
            self.settings_db = self.database.settings
            
            self.is_connected = True
            print(f"✅ MongoDB Atlas connected successfully!")
            print(f"   Database: waifu_grabbers")
            return True
            
        except Exception as e:
            print(f"❌ MongoDB connection failed: {e}")
            self.is_connected = False
            return False

# Create instance
mongo_db = MongoDB()

# Backward compatibility
mongo = None
database = None

async def init_mongo():
    """Initialize MongoDB connection"""
    global mongo, database
    await mongo_db.connect()
    if mongo_db.is_connected:
        mongo = mongo_db.client
        database = mongo_db.database
    return mongo_db.is_connected
