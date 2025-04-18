from enum import IntEnum, StrEnum, Enum

class CacheKeyName(StrEnum):
    SALES_LIST_DATA = "SALES_LIST_DATA"
    SALES_SORT_DATA = "SALES_SORT_DATA"
    SALES_TOP_DATA = "SALES_TOP_DATA"
    PROMPT_REQ = "PROMPT_REQ"
    PROMPT_RES = "PROMPT_RES"

class CacheTTL(IntEnum):
    FIVE_MINUTES: int = 60 * 5
    TEN_MINUTES: int = 60 * 10
    THIRTY_MINUTES: int = 60 * 30