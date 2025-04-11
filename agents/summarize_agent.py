from agents.llm_adapter import LLMAdapter

class SummarizeAgent:
    def __init__(self):
        self.default_model = "openai:gpt-3.5-turbo"

    async def run(self, context: dict) -> str:
        text = context.get("input", "")
        model_name = context.get("llm_model", self.default_model)
        adapter = LLMAdapter(model_name)
        prompt = f"다음 내용을 한 문장으로 요약해줘:\n\n{text}"
        return await adapter.generate(prompt)