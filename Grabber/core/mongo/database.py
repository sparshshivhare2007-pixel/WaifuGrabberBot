# Grabber/core/mongo/database.py

import motor.motor_asyncio
import os
from typing import Optional

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.waifus_db = None
        self.user_waifus = None
        self.settings_db = None
        self.is_connected = False
        
    async def connect(self):
        """Connect to MongoDB"""
        try:
            # Get MongoDB URI from environment variable or use default
            MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
            MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "waifu_bot")
            
            # For MongoDB Atlas (cloud)
            # MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/database")
            
            print(f"🔄 Connecting to MongoDB: {MONGO_URI}")
            
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                MONGO_URI,
                serverSelectionTimeoutMS=30000,
                connectTimeoutMS=30000
            )
            
            # Test connection
            await self.client.admin.command('ping')
            
            self.db = self.client[MONGO_DB_NAME]
            self.waifus_db = self.db["waifus"]
            self.user_waifus = self.db["user_waifus"]
            self.settings_db = self.db["settings"]
            
            self.is_connected = True
            print(f"✅ Connected to MongoDB: {MONGO_DB_NAME}")
            return True
            
        except Exception as e:
            print(f"❌ MongoDB connection failed: {e}")
            self.is_connected = False
            return False
    
    async def disconnect(self):
        """Disconnect from MongoDB"""
        if self.client:
            self.client.close()
            self.is_connected = False
            print("✅ Disconnected from MongoDB")

# Create a single instance
database = Database()

# Auto-connect function (call this when bot starts)
async def init_db():
    await database.connect()
