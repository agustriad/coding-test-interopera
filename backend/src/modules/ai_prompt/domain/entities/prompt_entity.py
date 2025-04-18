# from dataclasses import dataclass
# from src.modules.ai_prompt.utils.constants.mode_generate import ModeGenerator
# from src.core.utils.datetime import current_date

# # @dataclass
# class PromptEntity:
#     def __init__(self, id=str, text=str, type=str, model=ModeGenerator, timestamp=current_date):
#         self.id = id
#         self.text = text
#         self.type = type
#         self.model = model
#         self.timestamp = timestamp
    
#     def __repr__(self):
#         return f"Prompt(id={self.id}, text={self.text}, type={self.type}, model={self.model}, timestamp={self.timestamp})"

#     # text: str
#     # mode: str

import html
import uuid
from pydantic import BaseModel, Field, field_validator
from src.core.utils.datetime import current_date
from dataclasses import dataclass

@dataclass
class GetListEntity:
    def __init__(self, id=str, label=str, datetime=current_date):
        self.id = id
        self.label = label
        self.datetime = datetime
    
    def __repr__(self):
        return f"Prompt(id={self.id}, label={self.label}, datetime={self.datetime})"
    
@dataclass
class GetDetailEntity:
    def __init__(self, id=str, content=str, type=str, response=str, datetime=current_date):
        self.id = id
        self.content = content
        self.datetime = datetime
        self.type = type
        self.response = response
    
    def __repr__(self):
        return f"Prompt(id={self.id}, content={self.content}, type={self.type}, response={self.response}, datetime={self.datetime})"

class PromptEntity(BaseModel):
    id:str = Field(..., example="id_prompt", min_length=3, type=uuid.uuid4)
    content: str = Field(...,example="What is the meaning of life?", min_length=3)
    type: str = Field(..., example="text or image", min_length=3)
    
    @field_validator("content")
    @classmethod
    def escape_and_validator(cls, value: str) -> str:
        return html.escape(value)