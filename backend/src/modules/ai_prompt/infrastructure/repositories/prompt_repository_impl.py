import json

from src.modules.ai_prompt.domain.entities.prompt_entity import GetListEntity, GetDetailEntity, PromptEntity
from src.modules.ai_prompt.domain.repositories.prompt_repository import PromptRepository
from src.modules.ai_prompt.infrastructure.external_clients.gemini_client import GeminiClient

from typing import List, Optional
from src.core.utils.uuid import generate_uuid4
from src.core.cache import cache
from src.modules.ai_prompt.utils.constants.cache_attribute import CacheTTLPrompt, CacheKeyNamePrompt
from src.core.utils.datetime import current_date
from src.modules.ai_prompt.infrastructure.caching.prompt_cache import PromptCache


class PromptRepositoryImpl(PromptRepository):
    def __init__(self, client: None):
        self.client = client or GeminiClient()

    async def store_prompt(self, prompt: PromptEntity) -> GetDetailEntity:
        promp_id = generate_uuid4()
        
        cache_content = await PromptCache.get_prompt(prompt.content[:30])
        if cache_content:
            return cache_content
        
        response = await self.client.send_prompt(prompt.content)

        entity = GetDetailEntity(id=promp_id, content=prompt.content, type=prompt.type, response=response, datetime=current_date())
        json_data = {
            "id": entity.id,
            "content": entity.content,
            "type": entity.type,
            "response": entity.response,
            "datetime": entity.datetime
        }

        await PromptCache.set_prompt(entity.content[:30], json_data)
        return json_data
    
    async def delete_prompt(self, prompt_id: str) -> bool:
        if prompt_id in cache:
            del cache[prompt_id]
            return True
        
        return False

    # not used
    async def get_prompt_list(self) -> Optional[List[GetListEntity]]:
        return None
    
    # not used
    async def get_prompt_detail(self, prompt_id):
        pass
