from agents.llm_adapter import LLMAdapter

class TranslateAgent:
    def __init__(self):
        self.default_model = "openai:gpt-3.5-turbo"

    async def run(self, context: dict) -> str:
        text = context.get("input")
        target_lang = context.get("target_lang", "en")
        model_name = context.get("llm_model", self.default_model)

        prompt = f"Translate the following to {target_lang}:\n{text}"
        adapter = LLMAdapter(model_name)
        return await adapter.generate(prompt)