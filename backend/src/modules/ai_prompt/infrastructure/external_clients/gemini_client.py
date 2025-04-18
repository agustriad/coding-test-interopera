# modules/ai_prompt/infrastructure/external_clients/gemini_client.py

import base64
from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO
from src.modules.ai_prompt.config import PromptEnv
from src.modules.ai_prompt.utils.constants.mode_generate import ModeGenerator

class GeminiClient:

    def __init__(self, api_key=PromptEnv.GEMINI_APIKEY):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)


    async def send_prompt(self, content: str):

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=content,
        )

        return response.text
