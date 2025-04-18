import os
from dotenv import load_dotenv

load_dotenv()

class PromptEnv:
    GEMINI_URL: str = os.getenv("GEMINI_URL","")
    GEMINI_APIKEY: str = os.getenv("GEMINI_APIKEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "")
    