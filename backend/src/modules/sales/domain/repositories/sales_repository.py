# src\modules\sales\domain\repositories\sales_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from src.modules.sales.domain.entities.sales_entity import SalesEntity

# for abstract logic
class SalesRepository(ABC):
    @abstractmethod
    async def get_list(self) -> List[SalesEntity]:
        pass

    @abstractmethod
    async def get_detail(self, sales_id: int) -> Optional[SalesEntity]:
        pass

    @abstractmethod
    async def get_top_sales(self) -> List[SalesEntity]:
        pass
