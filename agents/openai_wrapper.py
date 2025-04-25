# agents/openai_wrapper.py
from openai import AsyncOpenAI
import os
from .llm_adapter import register_provider

class OpenAIWrapper:
    def __init__(self, model_name: str):
        # real_name: "gpt-3.5-turbo" 등
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_name = model_name

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

# “openai:” 접두어 붙이면 이 클래스가 쓰이도록 등록
register_provider("openai", OpenAIWrapper)
