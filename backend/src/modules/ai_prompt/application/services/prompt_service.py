from typing import List, Optional
from src.modules.ai_prompt.application.dto.request_prompt_dto import GetDetailPromptDTO,DeletePromptDTO,PostPromptDTO
from src.modules.ai_prompt.domain.repositories.prompt_repository import PromptRepository
from src.modules.ai_prompt.domain.entities.prompt_entity import PromptEntity, GetListEntity, GetDetailEntity
from src.core.utils.uuid import generate_uuid4

class PromptService:
    def __init__(self, repository: PromptRepository):
        self.repository = repository

    async def store_prompt(self, prompt: PostPromptDTO) -> GetDetailPromptDTO:
        get_uuid = generate_uuid4()
        data = PromptEntity(id=get_uuid, content=prompt.content, type=prompt.type)
        return await self.repository.store_prompt(data)
    
    async def get_prompt_list(self) -> List[GetListEntity]:
        return await self.repository.get_prompt_list()
    
    async def get_prompt_detail(self, prompt_id:str) -> Optional[GetDetailEntity]:
        return await self.repository.get_prompt_detail(prompt_id)
    
    async def delete_prompt(self, prompt_id:str) -> bool:
        return await self.repository.delete_prompt(prompt_id)
