# src\modules\sales\infrastructure\repositories\sales_repo_impl.py

from src.core.utils.files.json import read_json, write_json
from typing import List, Optional
from src.core.utils.sorted import sorted_data
from src.modules.sales.infrastructure.caching.sales_cache import SalesCache
from src.modules.sales.domain.entities.sales_entity import SalesEntity
from src.modules.sales.domain.repositories.sales_repository import SalesRepository

class SalesRepoImpl(SalesRepository):
    
    def __init__(self, data_path: str):
        self.data_path = data_path

    
    async def get_list(self) -> List[SalesEntity]:
        cache = await SalesCache.get_list()
        if cache:
            return cache
        # return SalesCache.get_list()

        data = read_json(self.data_path)
        if data is None:
            return None
        
        data = data["salesReps"]

        for item in data:
            item["total_deal"] = sum(deal["value"] for deal in item.get("deals", [])) | 0

        data = sorted_data(data=data, key_name="name", reverse=False)

        await SalesCache.set_data(data)

        return data
    
    async def get_detail(self, sales_id: int) -> Optional[SalesEntity]:
        sales = await self.get_list()
        
        # filter by id
        get_by_id = next((item for item in sales if item["id"] == sales_id), None)

        return get_by_id
    
    async def get_top_sales(self):
        cache_top_3 = await SalesCache.get_top_3()
        if cache_top_3:
            return cache_top_3
        else:
            sales = await self.get_list()
            data_sort = sorted_data(data=sales, key_name="total_deal", reverse=True)
            top_3 = data_sort[:3]
            SalesCache.set_data_top(top_3)
            return top_3
 
        