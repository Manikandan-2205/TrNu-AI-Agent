from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import logging

log = logging.getLogger(__name__)

# Replace with environment variable in production
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)

# Database instance
db = client.ai_service_desk

async def ping_db():
    try:
        await client.admin.command('ping')
        return {"status": "success", "message": "Connected to MongoDB"}
    except ConnectionFailure as e:
        return {"status": "error", "message": str(e)}
