from enum import IntEnum, StrEnum, Enum

class CacheKeyNamePrompt(StrEnum):
    PROMPT_REQ_COLLECTION:str = "PROMPT_REQ_COLLECTION"
    PROMPT_RES_COLLECTION:str = "PROMPT_RES_COLLECTION"

class CacheTTLPrompt(IntEnum):
    THIRTY_MINUTES: int = 60 * 30