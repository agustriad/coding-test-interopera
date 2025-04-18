from typing import List, Optional
from src.modules.ai_prompt.domain.entities.prompt_entity import PromptEntity, GetListEntity, GetDetailEntity
from src.modules.ai_prompt.application.dto.request_prompt_dto import PostPromptDTO
from src.modules.ai_prompt.application.services.prompt_service import PromptService

class PromptController:
    def __init__(self, service: PromptService):
        self.service = service

    async def store_prompt(self, prompt: PostPromptDTO):
        return await self.service.store_prompt(prompt)
    
    async def get_prompt_list(self) -> List[GetListEntity]:
        return await self.service.get_prompt_list()
    
    async def get_prompt_detail(self, prompt_id: str) -> Optional[GetDetailEntity]:
        return await self.service.get_prompt_detail(prompt_id)
    
    async def delete_prompt(self, prompt_id: str) -> bool:
        return await self.service.delete_prompt(prompt_id)