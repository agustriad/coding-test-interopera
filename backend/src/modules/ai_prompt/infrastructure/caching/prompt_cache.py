# src\modules\sales\infrastructure\caching\sales_cache.py

from src.core.cache import cache
from src.core.constants.cache_attribute import CacheKeyName, CacheTTL

class PromptCache:
    @staticmethod
    async def get_prompt(key:str):
        cache_prompt_content = await cache.get(f"{CacheKeyName.PROMPT_REQ}{key}")
        if cache_prompt_content:
            return cache_prompt_content
        
        return None
        
    @staticmethod
    async def set_prompt(key:str,data):
        await cache.set(f"{CacheKeyName.PROMPT_REQ}{key}", data, CacheTTL.THIRTY_MINUTES)
