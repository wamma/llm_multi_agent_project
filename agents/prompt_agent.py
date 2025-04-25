# agents/prompt_agent.py
from .llm_adapter import LLMAdapter

class PromptAgent:
    def __init__(self, template: str, default_model: str = "openai:gpt-3.5-turbo"):
        self.template = template
        self.default_model = default_model

    async def run(self, context: dict) -> str:
        # context에 llm_model 키가 없으면 default_model 사용
        model = context.get("llm_model", self.default_model)
        # {input}, {target_lang} 등을 context로 채워 넣음
        prompt = self.template.format(**context)
        return await LLMAdapter(model).generate(prompt)
