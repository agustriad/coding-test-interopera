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

class SalesDTO(BaseModel):
    id: int
    name: str
    role: str
    region: str
    skills: List[str]
    deals: List[DealDTO]
    clients: List[ClientDTO]
    total_deal: int

class ResponseDto(BaseModel):
    data: Optional[List[SalesDTO]]
    