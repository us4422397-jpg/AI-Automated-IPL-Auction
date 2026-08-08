from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
import redis.asyncio as redis
from app.config import get_settings

settings = get_settings()

async def get_redis_client():
    client = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
    try:
        yield client
    finally:
        await client.close()

