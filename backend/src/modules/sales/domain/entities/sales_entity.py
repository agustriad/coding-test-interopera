# src\modules\sales\domain\entities\sales_entity.py

from typing import List, Optional
from pydantic import BaseModel

class DealDTO(BaseModel):
    client: str
    value: int
    status: str

class ClientDTO(BaseModel):
    name: str
    industry: str
    contact: str

class SalesEntity(BaseModel):
    id: int
    name: str
    role: str
    region: str
    skills: List[str]
    deals: List[DealDTO]
    clients: List[ClientDTO]
    total_deal: int