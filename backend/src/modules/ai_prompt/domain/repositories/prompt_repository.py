from abc import ABC, abstractmethod
from src.modules.ai_prompt.domain.entities.prompt_entity import PromptEntity, GetDetailEntity,GetListEntity

class PromptRepository(ABC):
    @abstractmethod
    async def store_prompt(self, prompt: PromptEntity) -> GetDetailEntity:
        pass

    @abstractmethod
    async def get_prompt_list(self, prompt: PromptEntity) -> GetListEntity:
        pass

    @abstractmethod
    async def get_prompt_detail(self, prompt_id: str) -> GetDetailEntity:
        pass

    @abstractmethod
    async def delete_prompt(self, prompt_id: str) -> PromptEntity:
        pass
