import html
from pydantic import BaseModel, Field, field_validator
from ai_prompt.utils.constants.mode_generate import ModeGenerate

class PostPromptDTO(BaseModel):
    content: str = Field(...,example="What is the meaning of life?", min_length=3)
    type: str = Field(..., example="text or image", min_length=3)
    model: ModeGenerate = Field(..., example="gemini or meta", min_length=3)
    
    @field_validator("text")
    @classmethod
    def escape_and_validator(cls, value: str) -> str:
        return html.escape(value)
    
class GetDetailPromptDTO(BaseModel):
    id: str = Field(..., example="id_prompt", min_length=3)

class DeletePromptDTO(BaseModel):
    id: str = Field(..., example="id_prompt", min_length=3)
    
    

