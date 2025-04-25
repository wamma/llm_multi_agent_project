# agents/llm_adapter.py
from openai import AsyncOpenAI
import os


# provider registry
_PROVIDER: dict[str, type] = {}

def register_provider(prefix: str, wrapper_cls: type):
    _PROVIDER[prefix] = wrapper_cls

class LLMAdapter:
    def __init__(self, model_name: str):
        # model_name 예시: "openai:gpt-3.5-turbo"
        prefix, _, real_name = model_name.partition(":")
        Wrapper = _PROVIDER.get(prefix)
        if not Wrapper:
            raise ValueError(f"Unsupported provider: {prefix}")
        self.engine = Wrapper(real_name)

    async def generate(self, prompt: str) -> str:
        return await self.engine.generate(prompt)