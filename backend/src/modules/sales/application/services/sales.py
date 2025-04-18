# src\modules\sales\application\services\sales.py

from typing import List, Optional
from src.modules.sales.domain.entities.sales_entity import SalesEntity
from src.modules.sales.domain.repositories.sales_repository import SalesRepository

# service sales : get_list
class SalesService:

    def __init__(self, repository=SalesRepository):
        self.repository = repository

    async def get_sales_list(self) -> List[SalesEntity]:
        data = await self.repository.get_list()
        return data
    
    async def get_sales_detail(self, sales_id: int) -> Optional[SalesEntity]:
        return await self.repository.get_detail(sales_id)
    
    # get top 3 sales
    async def get_top_sales(self) -> List[SalesEntity]:
        return await self.repository.get_top_sales()

