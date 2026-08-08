import redis.asyncio as redis
import json
from typing import Optional, Any
from fastapi.encoders import jsonable_encoder

class CacheService:
    def __init__(self, redis_client: redis.Redis):
        self.client = redis_client

    async def get(self, key: str) -> Optional[Any]:
        data = await self.client.get(key)
        if data:
            return json.loads(data)
        return None

    async def set(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        serialized = json.dumps(jsonable_encoder(value))
        await self.client.setex(key, ttl_seconds, serialized)

    async def delete(self, key: str) -> None:
        await self.client.delete(key)
