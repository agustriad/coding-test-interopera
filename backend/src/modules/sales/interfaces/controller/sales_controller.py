# src\modules\sales\interfaces\controller\sales_controller.py

from typing import List
from src.modules.sales.domain.entities.sales_entity import SalesEntity
from src.modules.sales.application.services.sales import SalesService

class SalesController:

    def __init__(self, service: SalesService):
        self.service = service

    async def get_sales_list(self) -> List[SalesEntity]:
        res =  await self.service.get_sales_list()
        return res
    
    async def get_sales_detail(self, sales_id: int) -> SalesEntity:
        res = await self.service.get_sales_detail(sales_id)
        return res
    
    async def get_top_sales(self) -> List[SalesEntity]:
        res = await self.service.get_top_sales()
        return res;