from openai import AsyncOpenAI
import os


class OpenAIWrapper:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model_name.replace("openai:", ""),
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

class LLMAdapter:
    def __init__(self, model_name: str):
        if model_name.startswith("openai"):
            self.engine = OpenAIWrapper(model_name)
        else:
            raise ValueError(f"Unsupported model provider: {model_name}")

    async def generate(self, prompt: str) -> str:
        return await self.engine.generate(prompt)