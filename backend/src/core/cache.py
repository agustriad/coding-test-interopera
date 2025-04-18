import json
import redis
from src.core.config import settings
from src.core.constants.cache_attribute import CacheTTL

class Cache:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True
        )
    
    async def get(self, key):
        data = self.redis_client.get(key)
        if data is not None:
            return json.loads(data)
        return None
    
    async def set(self, key, value, ttl=CacheTTL.FIVE_MINUTES):
        self.redis_client.setex(key, int(ttl) ,json.dumps(value))

    async def delete(self, key):
        self.redis_client.delete(key)

    async def disconnect(self):
        self.redis_client.close()
        print("Redis connection closed.")

    async def connect(self):
        print("Redis connection established.")

cache = Cache()