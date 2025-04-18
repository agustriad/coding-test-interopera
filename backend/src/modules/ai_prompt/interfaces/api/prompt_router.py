from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from src.core.exceptions import InternalServerErrorException, NotFoundException, BadRequestException
from src.modules.ai_prompt.domain.entities.prompt_entity import PromptEntity
from src.modules.ai_prompt.application.dto.request_prompt_dto import PostPromptDTO
from src.modules.ai_prompt.infrastructure.external_clients.gemini_client import GeminiClient
from src.modules.ai_prompt.infrastructure.repositories.prompt_repository_impl import PromptRepositoryImpl
from src.modules.ai_prompt.application.services.prompt_service import PromptService
from src.modules.ai_prompt.interfaces.controller.prompt_controller import PromptController


# inject repo, service, controller
repository = PromptRepositoryImpl(client=GeminiClient())
service = PromptService(repository=repository)
controller = PromptController(service=service)

prompt_router = APIRouter()

@prompt_router.post("/")
async def store_prompt(prompt: PostPromptDTO):
    try:
        data = await controller.store_prompt(prompt)
        return {"data": data}
    except Exception as e:
        print(str(e))
        raise InternalServerErrorException("Something went wrong while generating text")
    


