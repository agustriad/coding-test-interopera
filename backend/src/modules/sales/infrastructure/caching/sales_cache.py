# src\modules\sales\infrastructure\caching\sales_cache.py

from src.core.cache import cache
from src.core.constants.cache_attribute import CacheKeyName, CacheTTL

class SalesCache:
    @staticmethod
    async def get_list():
        cache_list_data = await cache.get(CacheKeyName.SALES_LIST_DATA)
        if cache_list_data:
            return cache_list_data
        
        return None
    
    @staticmethod
    async def get_top_3():
        cache_top_data = await cache.get(CacheKeyName.SALES_TOP_DATA)
        if cache_top_data:
            return cache_top_data
            
        else:
            return None
        
    @staticmethod
    async def set_data(data):
        await cache.set(CacheKeyName.SALES_LIST_DATA, data, CacheTTL.FIVE_MINUTES)

    @staticmethod
    async def set_data_top(data):
        await cache.set(CacheKeyName.SALES_TOP_DATA, data, CacheTTL.TEN_MINUTES)
